# Historical internal manuscript review

This file retains the initial v0.1.0 analytic review. Version 0.2.0 has [separate reports and dispositions](reviews/v0.2.0/DISPOSITION.md); its artifact identities are recorded in the current verification directory. The historical proof and resource statements below are not the revised theorem's review record.

This record covers initial prepared commit `69dfe76e30a0e80ae82265031f5e5b408a3d9342`; its artifact identities and release hold are historical. The author subsequently authorized publication after actual provider reviews. See [current cross-provider dispositions](reviews/DISPOSITION.md), [current artifact receipts](verification/README.md) and [publication status](publication/README.md) for the revised candidate.

Candidate: version 0.1.0, November 10, 2026. Reviewer: the same OpenAI Codex assistant that assisted the derivation and manuscript preparation. These are separately documented review lenses, **not independent reviewers, independent peer review, or formal certification**. The review covers the complete manuscript, not only the main theorem statement.

Preparation decision: **GO WITH NOTES; the mathematical manuscript and artifact checks are complete.** Release decision: **HOLD for the author's requested Zenodo connection and subsequent release direction**, with no remaining blocking scientific or artifact finding identified internally. No release is authorized or executed by this record. Exact final source/PDF identities and completed checks are recorded below.

## Mathematical and adversarial lens

Outcome: no unresolved blocking analytic finding at the stated imported-result interfaces.

1. **Freshness and hidden support.** Conditional on the past, both the residual and true support are fixed. A simultaneous estimator event is over at most k true frequencies in the analysis, not all ambient frequencies. Estimates exist before new Fourier samples, even though only sampled coordinates are evaluated. The displayed mean and second-moment calculations therefore retain conditional independence. No support oracle is used.
2. **Reciprocal cutoff.** On the estimator event the cutoff lies between 2 sqrt(2) Delta and 2 sqrt(6) Delta. Passing estimates have the correct sign and ratio below 3/2. Failing coefficients have magnitude below 6 Delta. This pays squared bias 36 epsilon^2 e^2 and second moment at most 9k/4. Zero estimates never enter a reciprocal.
3. **Majority conversion.** Outside the input set of measure at most 4 times squared bias, the conditional mean has sign margin at least 1/2. Independent groups give a pointwise majority-error bound 2^(-g); integrating uses only bounded Boolean output. Independence across inputs is not assumed. Markov's 1/beta cost is charged through the estimator accuracy.
4. **Original-energy contraction.** Search omissions cost at most (16/9)||H-f||_2^2. Fresh certification uses f-a, not f-H, so residual sparsity is preserved. The rejected proposed mass is at most alpha^2 W/64. Their sum is strictly below W/16 without an overshoot, degree or flatness assumption.
5. **Adaptive refit.** The Gram event is for one fixed true-support matrix, not the empirically chosen archive. On it every admitted subset has inverse norm at most 10/9 and cross-block norm at most 1/10, giving alpha^2=82/81. Certification and refitting may use the same rows; their failure events are union-bounded, not declared independent.
6. **Whole trajectory and endpoints.** Initialization has W=1. Positive W is at least 1/k^2. T fixed rounds force W=0, and exact refitting recovers f. Sparsity one, constants, empty archives, early W=0, sign ties, false candidates and singular systems are specified. A first-failure bound gives success above 0.94. Fresh final validation is an additional false-acceptance guard, not an event that needs to be subtracted from correct-output success.
7. **Retained obstructions.** H includes fresh observed parities beyond the old archive. It is not a scalar function of the old fit. The proof neither propagates an unbounded projected cube nor assumes all missing energy is visible in a fixed small seed-sum frontier. None of those stronger premises is required here.

## Access, complexity and exact arithmetic lens

Outcome: GO WITH NOTES. This is an analytic resource proof, not executed learner software.

- All target access is a charged fresh label or Fourier measurement. Classical search evaluates the stored H at chosen inputs, using its own charged random bits. Its O(log n) confidence factor does not consume additional target copies.
- The complete copy budget is T(q_e+4gm+q_c) plus validation. q_e=O(k log^2 k), not O(k log k); T yields O(k log^3 k). The 1/beta loss and failed Fourier flags are included.
- Exact least squares on sign rows resets a common denominator of O(k log(kq_c)) bits every round. Multiplying at most k nonzero estimator numerators gives polynomial-bit inverse weights. Their signs can be evaluated by integer sums; there is no constant-time real-number assumption or recursive composition of old hypothesis circuits.
- Capped prefix search takes O(nk^6 log(nk/beta)) H evaluations per round. Evaluation costs tilde-O(nk+k^3), giving the conservative tilde-O(n^2 k^7+n k^9) total bit bound. Estimation, certificate accumulation, fraction-free fitting, random input generation and final convolution fit below it.
- Live storage includes P candidate vectors, both label batches, rational accumulators, the fitted coefficients, sampled frequencies, multiplicities and precomputed integer weights. It is tilde-O(nk^2+k^3); no P-by-P Gram matrix is stored.
- The cap and abort rules apply on bad tapes too. Constants and exponents are large. No practical-runtime, noisy-input, state-preparation-cost or complete implementation claim is supported.

## Source, attribution and claims lens

Outcome: GO WITH NOTES; exhaustive priority remains unestablished. [SOURCES.md](SOURCES.md) records source versions, named transfer questions and search limitations. The corrected 2021 exact-learning paper, Ye's smaller sample result, Caro et al.'s efficient exact learner, granularity, Fourier search and matrix concentration are attributed. The first draft's phrase “matching-in-scale lower bound” was removed because the cited upper and lower bounds differ polynomially. The contribution is simultaneous resource efficiency; it is not the first result on either resource alone.

The title, abstract, theorem, algorithm, cost proof, README and citation/Zenodo metadata must state the same exact noiseless supplied-example scope. No claim resolves AA, BPP/BQP, optimal sample complexity, noise robustness or publication priority. The archive excludes private planning notes and prior abandoned routes. Their preservation in the original research record does not make them dependencies of this proof.

## Artifact and reproducibility lens

Outcome: PASS. The first local TeX build identified two overfull paragraphs, which were rephrased without changing the theorem. A second build retained one warning, resolved by displaying the probability bound. The final log has no layout, reference or missing-glyph diagnostics. Fontconfig emitted its environment notice, but the PDF's 21 fonts are all embedded and every page was visually checked.

Operational findings retained: one Windows command-line probe lost inner quoting, and an inspection probe encountered the console's Unicode encoding limit. A cffconvert dependency installation failed before installation on this embedded Python; citation validation instead uses the official CFF 1.2.0 schema and an isolated jsonschema installation. The package checker initially missed a PDF disclosure because of a ligature and then matched its own forbidden-reference literal. Unicode normalization and a precise pattern corrected those checks without weakening the disclosure or privacy requirements. The older Git executable required its compatible branch-initialization command; a Markdown hard-break was changed to a blank paragraph to pass whitespace checking. None is mathematical evidence or a learner execution.

The local build uses Tectonic 0.17.0 and PyMuPDF 1.28.2. Twelve exact rational checks pass. All ten final pages were actually inspected with no visible defect. Source SHA-256: `26d4d6a33e829577919fb70481b7c15d069839af96063502a3e913c077494718`. PDF SHA-256: `2178e4d485d6da2f9aa42346eef92b116905188d51ab2b75ae01e19f77f7e782`. A clean index export rebuilt the byte-identical PDF and passed the same package checks. These identities are also in the build, visual and package receipts.

The package checker validates citation schema, author/ORCID/title/version/license/preprint consistency, absence of an unissued manuscript DOI, exact source/PDF/constant/visual correspondence, local links, font embedding and private-path/credential exclusion. Final record-only changes require a refreshed inventory and clean-export package check; unchanged TeX/PDF do not require another mathematical or visual claim. No learner experiment or formal build was performed.

## Complete claim map and disposition

| Claim | Manuscript support | Review outcome |
| --- | --- | --- |
| Every-target exact list with success at least 2/3 | Lemmas 2--7, Proposition 8, Section 5 trajectory and granularity | GO internally |
| O(k log^3(2k)) supplied examples, no target membership queries | Explicit four-step algorithm, equation (22), Sections 3 and 6 | GO internally |
| Fixed polynomial total bit time/live space on every tape | Section 6 denominators, capped search, fitting and abort accounting | GO WITH NOTES: conservative asymptotic costs; no implementation |
| Difference from prior work | Section 1 and SOURCES.md | GO WITH NOTES: priority not certified |
| Artifact and metadata correspondence | Build/constant/visual/package receipts and clean export | PASS for recorded source/PDF |
| Independent peer review or formal certification | No such evidence | NOT CLAIMED; this internal review does not substitute for either |

No mathematical statement was strengthened during manuscript preparation. The original general bound and evidence boundary remain. The preparation milestone is ready for a public repository and the author's Zenodo setup; no DOI, journal submission, automatic successor research or formalization job follows.
