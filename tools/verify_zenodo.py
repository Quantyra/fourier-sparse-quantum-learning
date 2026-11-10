"""Read-only verification of a published Zenodo record against a local Git tag.

Downloads public artifacts and writes an ignored local receipt. Does not publish,
edit a record, create a release, or claim mathematical certification.
"""
import argparse
import hashlib
import io
import json
from pathlib import Path
import subprocess
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
REPO = 'Quantyra/fourier-sparse-quantum-learning'


def fetch(url):
    request = urllib.request.Request(url, headers={'User-Agent': 'manuscript-archive-verifier/1.0'})
    with urllib.request.urlopen(request, timeout=90) as response:
        return response.read()


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('record_id', type=int)
    parser.add_argument('tag')
    args = parser.parse_args()
    require(not args.tag.startswith('-'), 'Expected a tag, not a Git option')
    record = json.loads(fetch(f'https://zenodo.org/api/records/{args.record_id}'))
    metadata = record['metadata']
    expected_metadata = json.loads(git('show', args.tag + ':.zenodo.json'))
    require(metadata['title'] == expected_metadata['title'], 'Zenodo title mismatch')
    require(metadata['version'] == expected_metadata['version'], 'Zenodo version mismatch')
    require(metadata['creators'] == expected_metadata['creators'], 'Zenodo author/ORCID mismatch')
    require(metadata['resource_type']['type'] == 'publication', 'Expected a publication')
    require(metadata['resource_type']['subtype'] == 'preprint', 'Expected a preprint')
    require(metadata['license']['id'].lower() == 'cc-by-4.0', 'Zenodo license mismatch')
    require(metadata['access_right'] == 'open', 'Expected an open record')
    version_doi = record['doi']
    concept_doi = record['conceptdoi']
    require(version_doi != concept_doi, 'Version and concept DOI must remain distinct')
    for doi in (version_doi, concept_doi):
        with urllib.request.urlopen('https://doi.org/' + doi, timeout=60) as response:
            require(response.status == 200, 'DOI did not resolve')
    archives = [f for f in record['files'] if f['key'].endswith('.zip')]
    require(len(archives) == 1, 'Expected exactly one GitHub source ZIP')
    archive = archives[0]
    data = fetch(archive['links']['self'])
    require(len(data) == archive['size'], 'Archive size mismatch')
    algorithm, expected_checksum = archive['checksum'].split(':', 1)
    require(hashlib.new(algorithm, data).hexdigest() == expected_checksum, 'Archive checksum mismatch')
    with zipfile.ZipFile(io.BytesIO(data)) as zipped:
        members = [i for i in zipped.infolist() if not i.is_dir()]
        roots = {i.filename.split('/', 1)[0] for i in members}
        require(len(roots) == 1, 'Unexpected ZIP root structure')
        actual = {i.filename.split('/', 1)[1]: zipped.read(i) for i in members}
    names = git('ls-tree', '-r', '--name-only', args.tag).decode('utf-8').splitlines()
    require(set(actual) == set(names), 'Archive file inventory differs from tag')
    hashes = {}
    for name in names:
        require(actual[name] == git('show', args.tag + ':' + name), 'Archived bytes differ: ' + name)
        hashes[name] = hashlib.sha256(actual[name]).hexdigest()
    release = json.loads(subprocess.check_output(
        ['gh', 'api', f'repos/{REPO}/releases/tags/{args.tag}'], cwd=ROOT))
    require(not release['draft'], 'GitHub release is still a draft')
    pdf_assets = [a for a in release['assets'] if a['name'].endswith('.pdf')]
    require(len(pdf_assets) == 1, 'Expected exactly one release PDF')
    require(fetch(pdf_assets[0]['browser_download_url']) == actual['manuscript/main.pdf'],
            'Release PDF differs from archived PDF')
    receipt = {
        'scope': 'Public archive/metadata identity; not mathematical certification',
        'result': 'PASS', 'repository': 'https://github.com/' + REPO,
        'tag': args.tag, 'commit': git('rev-list', '-n', '1', args.tag).decode().strip(),
        'record_id': args.record_id, 'record_url': f'https://zenodo.org/records/{args.record_id}',
        'version_doi': version_doi, 'concept_doi': concept_doi,
        'release_url': release['html_url'], 'published_at': release['published_at'],
        'archive_bytes': len(data), 'archive_checksum': archive['checksum'],
        'archive_sha256': hashlib.sha256(data).hexdigest(),
        'all_files_match_tag': True, 'files_sha256': hashes,
        'release_pdf_matches_archive': True,
    }
    output = ROOT / '.build' / f'zenodo-{args.record_id}-verification.json'
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps({k: v for k, v in receipt.items() if k != 'files_sha256'}))


if __name__ == '__main__':
    main()
