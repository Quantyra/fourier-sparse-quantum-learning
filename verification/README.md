# Verification scope

This directory records document builds, exact constant arithmetic, visual inspection and package identity. These checks do not run the complete learner, establish its success probability experimentally, prove the theorem mechanically or constitute independent peer review.

- `build.json`: compiler/version, source/PDF hashes, diagnostics and extracted page lengths.
- `constants.json`: eighteen exact rational arithmetic checks for the displayed proof budgets.
- `visual.json`: actual internal inspection of every page, bound to the PDF hash.
- `package.json`: exact archive inventory, metadata checks, citation validation and PDF font check.

The initial internal analytic review is in [REVIEW.md](../REVIEW.md). Actual Grok, Claude and AGY reports, focused revision checks and finding dispositions are in [current dispositions](../reviews/v0.2.0/DISPOSITION.md); [the current manifest](../reviews/v0.2.0/manifest.json) binds inputs and reports to the revised source. Package checks verify those recorded identities, not the mathematical content of model reports. The source/transfer assessment is in [SOURCES.md](../SOURCES.md). Build logs and rendered pages are reproducible local files under ignored `.build/`; they are not claimed to be archived here.

The previous version's build, constants, visual and package receipts are retained byte-for-byte under `history/v0.1.0/`. Root-level review records describe v0.1.0; they are not evidence of reviewing v0.2.0. Current package checks require each requested provider to have covered the current source hash.
