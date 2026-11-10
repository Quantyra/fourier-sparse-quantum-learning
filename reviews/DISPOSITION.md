# Cross-provider review and finding dispositions

Date: November 10, 2026. Coordinator: OpenAI Codex, acting within the author's request to obtain Grok, Claude and AGY reviews, implement appropriate feedback, and publish via Zenodo after readiness. Status: COMPLETE; no unresolved blocking finding. Final artifact readiness is recorded separately in publication/README.md.

The initial packet pins public commit `69dfe76e30a0e80ae82265031f5e5b408a3d9342`. It contains the full manuscript and author source-comparison notes. Earlier review reports and verdicts were withheld; the manuscript itself discloses prior internal checking, so this is not a claim of fully blind peer review. Each provider was asked for a complete adversarial proof/resource/claims review. External browsing, commands, edits and delegation were not requested. See [the exact packet](initial-packet.txt) and [input identities](inputs.json).

These are separate AI reviews, not human peer review, formal certification, a proof of correctness, or exhaustive novelty validation. Source comparisons remain explicitly bounded. Findings are checked on their mathematical merits; agreement does not override a demonstrated error.

| Reviewer | Actual review status | Model identity | Scope/limitation |
| --- | --- | --- | --- |
| AGY | GO WITH NOTES, completed | Configured Gemini 3.8 Flash (High); the response does not independently attest the serving model | Complete offline packet review; no external citation fetch, implementation or formal verification |
| Claude | GO WITH NOTES, completed after recovery | Returned `claude-opus-5-5` | Complete supplied-packet review with tools disabled; initial failed/empty attempts remain excluded |
| Grok | GO WITH NOTES, completed after recovery | Returned `grok-4.7`; usage identifies `grok-4.7-build` | Complete supplied-packet review with tools disabled; the earlier timeout is excluded |

## Findings

| ID | Finding | Disposition |
| --- | --- | --- |
| AGY-1, low | Make the pass/fail partition explicit in the bias proof | ACCEPTED. The revised proof states that the sets partition S and bounds the sum by 36 times the support size times Delta squared. No bound or assumption changes. |
| AGY-2, low | Show the centered scalar Bernstein bound explicitly | ACCEPTED. The revised proof uses the at-most-2k support and the coefficient bound to obtain (sqrt(2k)+1)e <= 3 sqrt(k)e. No constant changes. |
| AGY-3, informational | Integer rounding of sample counts is sound | NO CHANGE. The existing exact integer convention is retained. |
| Claude F1, moderate | Distinct-count abort could be read as including failed flags; a nonzero parity then spuriously fails | ACCEPTED. Step 2 now discards flag-zero outcomes and applies the cap only to the first gm successful grouped indices. The resource explanation matches. This makes the intended sampled-data contract unambiguous. |
| Claude F2, moderate | Negative claim about Ye's computational cost needs qualification and primary-source checking | ACCEPTED. The comparison now states what Ye's Theorem 1.1 guarantees and what Algorithms 1--2 explicitly do, without claiming a computational lower bound. The exact source was rechecked; see SOURCES.md. |
| Claude F3, minor | Granularity pinpoint and consequence should be explicit | ACCEPTED clarification. The primary author manuscript confirms Theorem 8.1 and the floor form. The manuscript now names that version and derives the coefficient floor explicitly. No constant changes. |
| Claude F4, minor | Bernstein pinpoint and denominator arithmetic should be checked | PINPOINT CONFIRMED; arithmetic added. Tropp v7 Theorem 6.1(ii) is exactly the needed bounded-case fraction; part (iii) is the split form. The correct citation remains. |
| Claude F5, minor | Show concentration union, Gram-budget and flag-tail arithmetic | ACCEPTED. Added the three short calculations without changing parameters. |
| Claude F6, minor | Overloaded local symbols | PARTLY ACCEPTED. The frequency set is now calligraphic D, the Gram row is phi, and the estimator's list-size argument is stated without apparently redefining global P. Standard local q, denominator D, and numerator subscripts are retained. |
| Claude F7, minor | Clarify which labels and archive are refitted | ACCEPTED. Step 4 names original target labels from the same fresh certification batch and the updated archive. |
| Claude F8, minor | Undefined clipping-defect jargon | ACCEPTED. Removed the undefined term and tightened the scope paragraph. |
| Claude F9, informational | State classical access after measurement | ACCEPTED. Added the uniform-label/successful-Fourier-sample description. |
| Claude F10, informational | Extremely loose constants, even for k=1 | RETAIN existing asymptotic/non-practical boundary. The general construction is deliberately unoptimized; no practical implementation is claimed. No extra quantitative performance claim is introduced. |
| Claude F11, minor | Funding wording and review-record availability | REMOVED the awkward funding sentence rather than inventing a factual no-funding declaration. Initial review records were intentionally withheld from the model packet; the public archive supplies them with exact scopes. |
| Claude F12, informational | Extra zero column in the analysis-only Gram event | RETAIN. It is harmless, fully charged by k+1, never forces zero into the archive, and does not supply an algorithmic input. No improvement is claimed from removing it. |


| Grok 1, external dependency | Verify exact granularity, Bernstein and Chernoff interfaces | VERIFIED by the coordinator against the named primary versions in SOURCES.md. Added the applied PSD/norm/expectation hypotheses, exact Chernoff factors and their scalar simplification. The printed sample constants suffice. These source checks are separate from the offline model review. |
| Grok 2, low | Show coefficient, energy and prefix concentration substitutions | ACCEPTED. The revised proofs explicitly display each substitution and the estimator union budget. Sample counts are unchanged. |
| Grok 3, low | Tie every abort to FAIL | ACCEPTED. A single algorithm convention covers every abort, and the search proof explicitly returns FAIL. |
| Grok 4, informational | No internal defect found in contraction or rational reset | NO NEW CLAIM. Retain the proof and its analytic, unformalized status. |

Coordinator check of the report: Section F of AGY's report writes the second moment expression as an equality for the variance. That expression is an upper bound on the variance; subtracting the squared mean gives the variance itself. The manuscript already uses the correct inequality, so this report typo is not incorporated. The original report is retained as returned. Its statement that every detail was verified is the reviewer's assessment, not a machine certificate or independent citation verification.

No theorem statement, sample bound, runtime exponent, access assumption or success probability changed. The distinct-index clarification removes an ambiguous literal reading of the algorithm; it does not introduce a new learner or a stronger guarantee. Focused final-diff checks are recorded separately from the full initial reviews.

## Operational attempts and revision scope

Authentication failure, empty response, local storage exhaustion and the first Grok timeout were retained as failed/incomplete attempts, never as mathematical reviews. Working space was restored by the author. Streamed Grok and Claude recovery returned substantive reports. The initial packet and all accepted reports remain hash-bound.

AGY's first revision launch rejected an effort/model mismatch without reviewing. Its next continuation returned another baseline-oriented report and repeated already-resolved findings instead of checking the new diff. That report is preserved as [wrong-scope output](agy-revision-wrong-scope.md), excluded from revision clearance. The follow-up names the exact revision file to avoid the resumed conversation's old working-directory ambiguity. Its description of Ye as having non-constructive decoding is not adopted: Ye has explicit recovery algorithms; the scoped comparison is about the stated polynomial computation guarantee.

Grok's focused response contains the aside `32/28<1`, which is false (32/28=8/7>1). The preceding displayed inequality in that same response and the manuscript are correct; no manuscript change follows. Reviewer lemma numbering sometimes differs from the actual manuscript, so these dispositions refer to named lemmas. Claude's optional abstract wording and extra constant/zero-column notes do not identify an error; retain the accurate abstract, existing non-practical limitation, paid k+1 column budget and disambiguated local notation. Do not invent a funding declaration.

## Final revision checks

The [exact revision packet](revision-packet.txt) contains the complete baseline-to-final-source diff and names the revised source SHA-256. Each reviewer continued its own initial conversation. [Grok](grok-revision.md) returned GO, [Claude](claude-revision.md) returned GO WITH NOTES, and [AGY](agy-revision.md) returned GO after the wrong-scope attempt was corrected. The accepted AGY response prints the exact revised source hash and checks the new Chernoff calculation, flag-zero discard and same-batch refit. No reviewer saw another reviewer's verdict as evidence.

All applicable findings are resolved or explicitly dispositioned above; no blocking finding remains. These are focused revision checks, not three new complete proof audits. AGY's strong recommendation is preserved as its wording, not adopted as an unconditional correctness certificate. None of the models independently verified the external primary sources; the coordinator's named source checks are in SOURCES.md. Original complete reports: [Grok](grok-initial.md), [Claude](claude-initial.md), [AGY](agy-initial.md).

Final source SHA-256: `91aadd7a185ad4c8b365350018703ecb8a3fe7c0dfaa7593fa08ec8533b6e804`. [Manifest](manifest.json) records actual model labels, packet/report identities, terminal completion and invocation duration. The revised manuscript builds without diagnostics; all twelve exact arithmetic checks and actual inspection of ten PDF pages pass. Clean-export and final archive identity checks belong to publication readiness, not mathematics.
