"""Validate the manuscript archive; no publication or learner execution."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import urllib.request
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
local_deps = ROOT / '.build' / 'check-deps'
if local_deps.is_dir():
    sys.path.insert(0, str(local_deps))
import pymupdf
import yaml
from jsonschema import Draft7Validator


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', help='Write a new inventory after all checks pass')
    args = parser.parse_args()
    files = sorted(p for p in ROOT.rglob('*') if p.is_file() and not any(
        part in {'.git', '.build', '__pycache__', '.venv'} for part in p.relative_to(ROOT).parts))
    receipt_path = ROOT / 'verification/package.json'
    files = [p for p in files if p != receipt_path]
    require(len(files) >= 16, 'Incomplete archive')
    cff_text = (ROOT / 'CITATION.cff').read_text(encoding='utf-8')
    cff = yaml.safe_load(cff_text)
    schema_path = ROOT / '.build/cff-1.2.0-schema.json'
    schema_path.parent.mkdir(exist_ok=True)
    if not schema_path.exists():
        with urllib.request.urlopen('https://raw.githubusercontent.com/citation-file-format/citation-file-format/1.2.0/schema.json', timeout=30) as response:
            schema_path.write_bytes(response.read())
    schema = json.loads(schema_path.read_text(encoding='utf-8'))
    require(sha(schema_path) == '0b8d22140da702d766df318dcff3a91af2f39521298dcf36d76315fd99cc169b', 'Unexpected CFF schema bytes')
    Draft7Validator.check_schema(schema)
    Draft7Validator(schema).validate(cff)
    zenodo = json.loads((ROOT / '.zenodo.json').read_text(encoding='utf-8'))
    require(cff['preferred-citation']['title'] == zenodo['title'], 'Title mismatch')
    require(cff['version'] == zenodo['version'] == '0.1.0', 'Version mismatch')
    require(zenodo['upload_type'] == 'publication' and zenodo['publication_type'] == 'preprint', 'Wrong archive type')
    require(cff['license'] == zenodo['license'] == 'CC-BY-4.0', 'License mismatch')
    require(zenodo['creators'] == [{'name': 'Fredriksen, Daniel', 'affiliation': 'Quantyra Inc.', 'orcid': '0009-0002-9123-7435'}], 'Author mismatch')
    require(cff['authors'][0]['orcid'].endswith(zenodo['creators'][0]['orcid']), 'ORCID mismatch')
    require('doi' not in zenodo, 'Do not force an existing DOI into future GitHub archiving')
    published_path = ROOT / 'publication/zenodo-verification.json'
    if published_path.exists():
        published = json.loads(published_path.read_text(encoding='utf-8'))
        require(published['result'] == 'PASS' and published['all_files_match_tag']
                and published['release_pdf_matches_archive'], 'Unverified publication receipt')
        require(cff.get('doi') == cff['preferred-citation'].get('doi') == published['version_doi'],
                'Citation DOI differs from verified version DOI')
    else:
        require('doi' not in cff and 'doi' not in cff['preferred-citation'], 'Unissued manuscript DOI')
    build = json.loads((ROOT / 'verification/build.json').read_text(encoding='utf-8'))
    constants = json.loads((ROOT / 'verification/constants.json').read_text(encoding='utf-8'))
    visual = json.loads((ROOT / 'verification/visual.json').read_text(encoding='utf-8'))
    source_hash = sha(ROOT / 'manuscript/main.tex')
    pdf_hash = sha(ROOT / 'manuscript/main.pdf')
    require(build['source_sha256'] == constants['source_sha256'] == source_hash, 'Stale source check')
    require(build['pdf_sha256'] == visual['pdf_sha256'] == pdf_hash, 'Stale PDF check')
    require(constants['script_sha256'] == sha(ROOT / 'tools/check_constants.py'), 'Stale arithmetic script')
    require(constants['result'] == 'PASS' and all(constants['checks'].values()), 'Arithmetic checks failed')
    require(build['final_log_diagnostics'] == [], 'TeX diagnostics remain')
    doc = pymupdf.open(ROOT / 'manuscript/main.pdf')
    require(doc.metadata['title'] == zenodo['title'], 'PDF title mismatch')
    require(len(doc) == build['pages'], 'Page count mismatch')
    require(visual['pages_inspected'] == list(range(1, len(doc) + 1)), 'Incomplete visual inspection')
    require(visual['result'] == 'PASS', 'Visual findings unresolved')
    font_ids = sorted({font[0] for page in doc for font in page.get_fonts(full=True)})
    require(font_ids and all(doc.extract_font(x)[3] for x in font_ids), 'Unembedded font')
    text = unicodedata.normalize('NFKC', ' '.join(p.get_text() for p in doc))
    text = re.sub(r'(?<=\w)-\n(?=\w)', '', text)
    text = re.sub(r'\s+', ' ', text)
    for phrase in ('independent peer review or formal certification', 'OpenAI Codex', 'supplied quantum examples'):
        require(phrase in text, f'Missing PDF statement: {phrase}')
    for p in files:
        if p.suffix.lower() in {'.pdf', '.png'}:
            continue
        content = p.read_text(encoding='utf-8')
        require(not re.search(r'[A-Za-z]:[\\/](?:Users|Windows)[\\/]', content), f'Private machine path in {p.name}')
        require(not re.search(r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,}', content), f'Possible credential in {p.name}')
        require(not re.search(r'Quantyra-(?:Quantum-)?Planning[/\\]', content), f'Private planning reference in {p.name}')
        if p.suffix == '.md':
            for target in re.findall(r'\]\(([^)]+)\)', content):
                if target.startswith(('http:', 'https:', '#', 'mailto:')):
                    continue
                path = target.split('#', 1)[0]
                require((p.parent / path).exists(), f'Broken local link in {p.name}: {target}')
    inventory = {p.relative_to(ROOT).as_posix(): sha(p) for p in files}
    result = {'scope': 'Artifact/metadata identity only; not proof certification', 'result': 'PASS',
              'pages': len(doc), 'embedded_fonts': len(font_ids), 'files': inventory,
              'citation_schema': 'Official CFF 1.2.0 via jsonschema 4.25.1',
              'citation_schema_sha256': sha(schema_path),
              'pdf_sha256': pdf_hash, 'source_sha256': source_hash}
    if args.write:
        receipt_path.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8', newline='\n')
    else:
        retained = json.loads(receipt_path.read_text(encoding='utf-8'))
        require(retained == result, 'Package changed since inventory; inspect changes before --write')
    print(json.dumps({'package': 'PASS', 'files': len(inventory), 'pages': len(doc), 'fonts': len(font_ids)}))


if __name__ == '__main__':
    main()
