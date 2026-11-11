# Fourier-sparse quantum learning

Version **0.4.0 is published and verified**, November 10, 2026 Hawaii (November 11 UTC): [version DOI 10.5281/zenodo.24129424](https://doi.org/10.5281/zenodo.24129424), [all-version DOI](https://doi.org/10.5281/zenodo.24118802), [release and PDF](https://github.com/Quantyra/fourier-sparse-quantum-learning/releases/tag/v0.4.0). Pruned hash-prefix search and local character correction give complete classical bit time tilde-O(n^2 k^3+n k^5+k^7), retaining O(k log^2(2k)) supplied examples, exact recovery with success >37/50 and tilde-O(nk^2+k^3) live bits. Actual Grok/Claude/AGY [reviews and final-source checks](reviews/v0.4.0/DISPOSITION.md) completed, with feedback dispositioned. All 88 archive files and the release PDF match the frozen tag; [post-release receipt](publication/zenodo-v0.4.0-verification.json). The fifteen-page PDF has 21 embedded fonts, 33 passing rational checks and a byte-identical clean rebuild. AI reviews are not human peer review or formal certification; no practical-runtime or exhaustive novelty claim is added.

Version **0.3.0 is published and verified**, November 10, 2026 Hawaii (November 11 UTC): [version DOI 10.5281/zenodo.24126516](https://doi.org/10.5281/zenodo.24126516), [all-version DOI](https://doi.org/10.5281/zenodo.24118802), [release and PDF](https://github.com/Quantyra/fourier-sparse-quantum-learning/releases/tag/v0.3.0). Shared-batch search sharpens classical bit time to tilde-O(n^2 k^6+n k^7), retaining O(k log^2(2k)) supplied examples, exact recovery with success >37/50 and tilde-O(nk^2+k^3) live bits. Actual Grok/Claude/AGY [focused reviews and final-source checks](reviews/v0.3.0/DISPOSITION.md) completed. All 71 archive files and the release PDF match the frozen tag; [post-release receipt](publication/zenodo-v0.3.0-verification.json). This thirteen-page revision has 21 embedded fonts, 22 passing rational checks and a byte-identical clean rebuild. AI reviews are not human peer review or formal certification; practical runtime and exhaustive novelty remain unassessed.

Version **0.2.0** includes the improved O(k log^2(2k)) sample bound. Grok, Claude and AGY completed [full reviews and final-source rechecks](reviews/v0.2.0/DISPOSITION.md), with feedback dispositioned. Published November 10, 2026 (Hawaii): [version DOI 10.5281/zenodo.24122694](https://doi.org/10.5281/zenodo.24122694), [all-version DOI](https://doi.org/10.5281/zenodo.24118802), [release and PDF](https://github.com/Quantyra/fourier-sparse-quantum-learning/releases/tag/v0.2.0). Every one of 54 archived files and the release PDF match the tag; see the [post-release receipt](publication/zenodo-v0.2.0-verification.json). Version 0.1.0 and its [review history](reviews/DISPOSITION.md) remain preserved. AI reviews are not independent human peer review or formal certification.

**Polynomial-Time Exact Learning of Fourier-Sparse Boolean Functions from Nearly Linear Quantum Samples**

Daniel Fredriksen · Quantyra Inc. · [ORCID 0009-0002-9123-7435](https://orcid.org/0009-0002-9123-7435)

[Read the manuscript (PDF)](manuscript/main.pdf) · [LaTeX source](manuscript/main.tex) · [Internal review](REVIEW.md) · [Publication status](publication/README.md)

Previous manuscript version **0.1.0**, published November 10, 2026. [Version DOI: 10.5281/zenodo.24118803](https://doi.org/10.5281/zenodo.24118803) ? [All-version DOI](https://doi.org/10.5281/zenodo.24118802) ? [Frozen release and PDF](https://github.com/Quantyra/fourier-sparse-quantum-learning/releases/tag/v0.1.0). Every archived file and the release PDF were verified against the exact tag; see the [post-release receipt](publication/zenodo-verification.json).

The main theorem exactly recovers every Boolean function with at most k nonzero Fourier coefficients using O(k log^2(2k)) independent supplied uniform quantum examples, with success at least 2/3 and fixed-polynomial total computation and working space in n and k. Each copy is measured separately. No target membership queries or state-preparation inverse is supplied.

Fresh residual-label estimates make a sign-majority of sampled parities explicitly evaluable. Classical Fourier search on that known function produces candidate indices; fresh original-target certification and exact refitting contract missing Fourier energy. Constant-confidence proposals can fail without destroying certified progress. A capped adaptive progress count gives the improved sample bound. The complete trajectory, unsuccessful trials and rational bit costs are included.

This complements [Ye's smaller sample bound](https://arxiv.org/abs/2610.17648v1) with a polynomial computational guarantee. Earlier efficient learners and standard ingredients are attributed. No claim of exhaustive novelty, optimal logarithmic factors, noise robustness, practical runtime, general quantum simulation or a BPP/BQP resolution is made.

The analysis is **AI-assisted**, with internal checks and version-specific Grok, Claude and AGY model review records. No independent peer review or formal certification is claimed. This repository contains a theorem and document verification tools, not an implementation or benchmark of the complete learning algorithm. The [verification scope](verification/README.md) separates document checks from mathematics.

## Build and check

Requirements: Python 3.10 or newer, Tectonic 0.17.0, and PyMuPDF 1.28.2. For the package checker also install the pinned PyYAML and jsonschema versions in [requirements](tools/requirements.txt). Citation validation caches the official CFF 1.2.0 schema on its first run.

```text
python tools/build.py --tectonic /path/to/tectonic --render
python tools/check_constants.py
python tools/check_package.py
```

The build uses a fixed SOURCE_DATE_EPOCH. It writes ignored local output under `.build/` and the PDF/build receipt in the archive. Rendering is for actual visual inspection; it does not automatically mark pages reviewed. Package verification must be repeated if any included file changes. No tool creates a release, sends a message, enables Zenodo, or runs the learner.

## License and disclosure

The manuscript and archive are licensed under [CC BY 4.0](LICENSE). OpenAI Codex assisted derivation, literature comparison, drafting and internal checking. Separate model reviews were obtained through Grok, Claude and AGY (configured with Gemini). The author remains responsible for the claims. See [CITATION.cff](CITATION.cff) for citation metadata; no DOI placeholder is used.
