# Fourier-sparse quantum learning

**Polynomial-Time Exact Learning of Fourier-Sparse Boolean Functions from Nearly Linear Quantum Samples**

Daniel Fredriksen · Quantyra Inc. · [ORCID 0009-0002-9123-7435](https://orcid.org/0009-0002-9123-7435)

[Read the manuscript (PDF)](manuscript/main.pdf) · [LaTeX source](manuscript/main.tex) · [Internal review](REVIEW.md) · [Publication status](publication/README.md)

Manuscript version **0.1.0**. The manuscript and internal review package are prepared for Zenodo connection. No release or Zenodo DOI has been issued for this manuscript.

The main theorem exactly recovers every Boolean function with at most k nonzero Fourier coefficients using O(k log^3(2k)) independent supplied uniform quantum examples, with success at least 2/3 and fixed-polynomial total computation and working space in n and k. Each copy is measured separately. No target membership queries or state-preparation inverse is supplied.

Fresh residual-label estimates make a sign-majority of sampled parities explicitly evaluable. Classical Fourier search on that known function produces candidate indices; fresh original-target certification and exact refitting contract missing Fourier energy. The complete trajectory and rational bit costs are included in the manuscript.

This complements [Ye's smaller sample bound](https://arxiv.org/abs/2610.17648v1) with a polynomial computational guarantee. Earlier efficient learners and standard ingredients are attributed. No claim of exhaustive novelty, optimal logarithmic factors, noise robustness, practical runtime, general quantum simulation or a BPP/BQP resolution is made.

The analysis and review are **internal and AI-assisted**. No independent peer review or formal certification is claimed. This repository contains a theorem and document verification tools, not an implementation or benchmark of the complete learning algorithm. The [verification scope](verification/README.md) separates document checks from mathematics.

## Build and check

Requirements: Python 3.10 or newer, Tectonic 0.17.0, and PyMuPDF 1.28.2. For the package checker also install the pinned PyYAML and jsonschema versions in [requirements](tools/requirements.txt). Citation validation caches the official CFF 1.2.0 schema on its first run.

```text
python tools/build.py --tectonic /path/to/tectonic --render
python tools/check_constants.py
python tools/check_package.py
```

The build uses a fixed SOURCE_DATE_EPOCH. It writes ignored local output under `.build/` and the PDF/build receipt in the archive. Rendering is for actual visual inspection; it does not automatically mark pages reviewed. Package verification must be repeated if any included file changes. No tool creates a release, sends a message, enables Zenodo, or runs the learner.

## License and disclosure

The manuscript and archive are licensed under [CC BY 4.0](LICENSE). OpenAI Codex assisted derivation, literature comparison, drafting and internal checking. The author remains responsible for the claims. No external funding is asserted. See [CITATION.cff](CITATION.cff) for citation metadata; no DOI placeholder is used.
