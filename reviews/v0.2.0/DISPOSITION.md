# Version 0.2.0 review dispositions

COMPLETE: all three providers returned complete full-source reviews and focused final-source checks. Final verdicts are recorded in [the manifest](manifest.json); all applicable findings are dispositioned and no unresolved blocking finding remains. Clearance is tied to the final source below, not inherited from v0.1.0.

This record is the authoring coordinator's disposition of actual AI reports. It is not independent human peer review or formal certification. Original reports are retained verbatim, including reviewer errors. A report's confident language is not itself evidence of correctness. The coordinator supplied source identities and checked the exact input/output records; reviewers did not independently compute file hashes or fetch primary papers.

## Implemented clarifications

- Scope the Ye comparison explicitly to its cited version; retain the smaller sample bound and the distinction between a sample theorem and a computational guarantee. The unchanged primary-source evidence in [SOURCES.md](../../SOURCES.md) is reused, rather than claimed as a new reviewer source audit.
- State that sparsity at most k is an input promise. Resource caps still apply if it is violated, but correctness and detection are not guaranteed; validation's soundness bound assumes the promised target class.
- State the proposal/certification instantiations of the generic lemma parameters. Constants, sample counts, confidence allocations and algorithm steps are unchanged.
- Explain exact pointwise Fourier inversion in the same-batch fit proof. This is not a pointwise Parseval assertion.
- Explain that sampled variance zero forces all certificate correlations to vanish, and that at zero missing energy the proposal can still contain false indices. Certification, not an assumed support property of the nonlinear hypothesis, rejects them.
- Replace the potentially ambiguous product 4 times 2 to the minus g by an explicit multiplication dot.

These changes are bound to the exact initial-to-final diff in [the revision packet](revision-packet.txt). The strengthened sample theorem and its probability/resource proof are unchanged by the review clarifications.

## Claude findings

The full review and focused revision both return GO WITH NOTES. The reviewer checks arbitrary-proposal safety, shared-batch refitting, the adaptive indicator proof, all costs and endpoints. Implemented findings are listed above. Remaining suggestions are non-blocking: a sharper Markov constant, a tighter granularity floor, extra sample-count examples, alternative notation and removal of a harmless extra Gram coordinate. We retain the proved conservative constants and explicit asymptotic-only disclaimer. The actual required 1/k granularity consequence was checked against the retained primary source; no altered theorem is introduced merely to hedge an already checked pinpoint. The k=1 and zero-residual cases remain covered without an unsupported deterministic first-trial guarantee.

The report's local elimination estimate with exponent four is not adopted under schoolbook integer multiplication; a conservative polynomial bound with exponent five remains below the manuscript's much larger total envelope. Its approximately 0.79 figure is a stronger lower bound from the displayed tail estimate, not the true success probability. Some reviewer lemma numbers use separate counters, whereas the manuscript shares its theorem counter; the actual LaTeX labels and PDF numbering are correct. No claim of new primary-source verification, novelty certification or peer review is taken from the report.

## AGY findings and report corrections

The first invocation returned an empty response after its packet read was denied. It is preserved as an excluded operational attempt, not a review. A retry allowed only the exact packet read and returned a complete GO WITH NOTES report. Its suggested exact-label decomposition motivated the Fourier-inversion clarification; the displayed denominator calculation already states both individual and product bit lengths.

Several initial report assertions were incorrect: it claimed that zero missing energy makes the proposal cutoff fail, that k=1 forces first-trial success, used the wrong sign for a negative Bernstein exponent, described pointwise Parseval, assigned incorrect equation/lemma numbers and claimed direct source verification. The [clarification exchange](agy-clarification.md) retracts these assertions. That exchange itself still incorrectly inferred that the search list lies in the true support at zero missing energy. The final-source packet explicitly rejects this inference, and the [final review](agy-revision.md) correctly explains why nonlinear hypotheses can propose extra frequencies and zero residual certificates reject them. Cosmetic line/equation numbering errors in the reports are not promoted to manuscript defects.

The final AGY verdict is GO on the exact revised source. This is an actual AGY request configured with Gemini 3.8 Flash High; its returned JSON does not independently attest the serving model. Claims of independence or primary-paper verification in the original report are not adopted. Schoolbook elimination costs are treated conservatively as above. None of these report corrections requires weakening the theorem.

## Internal changed-proof audit

The coordinator checked the actual proof obligations: proposals precede fresh safety rows; the true-support Gram event covers every adaptively chosen true subset; zero fitted entries remain in the permanent archive; failed proposals are paid and cannot increase missing energy on safety; first-failure probability is at most 1/100; proof-only dummy indicators have conditional success at least 1/2 without conditioning on future safety; their exponential moment bounds the shortage of contractions; granularity forces exact recovery; and all tape-dependent aborts respect finite time/space caps. Eighteen rational budget checks and document checks support this audit but are not a machine proof or a learner experiment.

## Grok findings

The full-source report returns GO WITH NOTES and checks the shared-batch, arbitrary-proposal, indicator, granularity and every-tape arguments. The source already expressly uses a staged union bound; no change was necessary for that note. Its norm inequality follows directly from Cauchy--Schwarz, and g>=13, m>=144 gives exp(-gm/4)<=exp(-468)<1/16. Optional tightening of Markov and leading constants is not needed for the stated theorem. The source already charges later Gram failures after exact recovery.

The report's generic majority parameter beta must be instantiated as proposal rho, as the final source now states explicitly. Its statement that a wrong hypothesis leaves the archive unchanged is too strong: a poor proposal can still supply true indices that are admitted; the actual guarantee is true-only nondecreasing archive inclusion and nonincreasing missing energy. No stronger assertion is adopted. Fresh rows give conditional safety uniformly over proposals; the proof uses conditional bounds, not independence of the resulting proposal-dependent events. A fixed expression is a total copy cap, since a global abort can consume fewer copies. No optimality claim for the chosen number of attempts is made. These are report qualifications, not gaps in the source. The focused final-source recheck is retained separately.

## Final boundary

Three initial reviews plus three focused final-source checks, with an additional AGY correction exchange, are actual provider outputs. AI agreement, document builds and eighteen arithmetic checks are not independent human peer review, formal certification, a learner experiment or proof of publication priority. Internal review and accepted clarifications support publication within the explicitly stated analytic boundary. Old v0.1.0 reports and the excluded empty attempt are retained. No source change follows the final-source review packet.

Final source SHA-256: `a826eda138c3cbe0dee0a12a53470a559429e0d1b40f97afd62356666f2429d6`.
