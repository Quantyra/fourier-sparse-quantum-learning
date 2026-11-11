# Verification scope

This directory records document builds, exact constant arithmetic, visual inspection and package identity. These checks do not run the complete learner, establish its success probability experimentally, prove the theorem mechanically or constitute independent peer review.

- `build.json`: compiler/version, source/PDF hashes, diagnostics and extracted page lengths.
- `constants.json`: twenty-two exact rational arithmetic checks for the displayed proof budgets, including the shared-search sample and union-bound factors.
- `visual.json`: actual internal inspection of every page, bound to the PDF hash.
- `package.json`: exact archive inventory, metadata checks, citation validation and PDF font check.

The initial internal analytic review is in [REVIEW.md](../REVIEW.md). Version 0.3.0 has separate actual Grok, Claude and AGY reports, focused final-source checks and finding dispositions under `reviews/v0.3.0/`; its manifest binds inputs and reports to the revised source. Package checks verify those recorded identities, not the mathematical content of model reports. The source/transfer assessment is in [SOURCES.md](../SOURCES.md). Build logs and rendered pages are reproducible local files under ignored `.build/`; they are not claimed to be archived here.

Previous build, constants, visual and package receipts are retained byte-for-byte under `history/v0.1.0/` and `history/v0.2.0/`. Root-level review records describe v0.1.0, and `reviews/v0.2.0/` retains that version's reviews. Current package checks require each requested provider to have covered the current source hash.
