# P010 v0.3.0 review disposition

Final source SHA-256: `aa73155e2bee2ce85f27eff07785f601ae29fbc535dff0e25ed0cc5b3fadd565`. **GO WITH NOTES for publication preparation**, subject to final artifact/clean-export checks. Three actual provider initial reviews and three focused final-source checks completed. Grok and Claude final verdicts: GO WITH NOTES. AGY final verdict: GO. No unresolved blocking finding remains.

## Scope and actual providers

The initial packet contains the complete revised source, exact v0.2.0 diff and source assessment. The final packet contains the complete final source, exact revision diff and named correction checks. Initial reviewers received no other reviewer verdict. Reports cover shared-batch conditional coverage, its adaptive-progress interface, full bit-time/live-space costs and attribution boundaries; they do not claim independent revalidation of every unchanged imported result. Earlier version-specific reviews remain historical evidence.

Grok configured grok-4.7 and returned grok-4.7-build metadata. Claude configured opus and returned claude-opus-5-5. AGY configured gemini-3.8-flash-high with high effort; returned JSON does not independently attest the serving model. Initial Grok/Claude effort was medium and their focused final check low. All actual attempts and their input/output hashes are in the manifest. These are AI reviews, not human peer review, formal certification or exhaustive novelty validation.

## Findings and decisions

| Finding | Disposition |
| --- | --- |
| Empty Revision scope heading before Version history (all initial reports) | Removed before the final packet. |
| Undefined matrix symbol in the bordered-minor formula (Claude N2) | Explicitly define M as the Gram or column-replaced matrix, K as the pivot block, and the bordered determinants. |
| Crowded local notation (Claude N3) | Use h_c for counters, d_tau for parameter widths, K for the pivot block and B_w for weight width. |
| Unquantified parameter arithmetic (Claude N4) | State polylog(2nk) arithmetic for the instantiated P, L_0, N and comparison factors. |
| Search-space statement omitted evaluator workspace (Claude O2) | Explicitly exclude both stored evaluator and its workspace from the small search-only expression, then include both in the complete bound. |
| Overflow/early termination reasoning (Claude O1) | Explicitly state that overflow at a reached depth implies an inaccurate estimate; retain heavy-ancestor coverage. |
| Suggested smaller arithmetic bounds or more aggressive parity sharing | Retain conservative proved upper bounds; no further optimization or stronger theorem is needed for this version. |
| Optional logarithm-base expansion and empty suffix at depth n | Existing definitions and displayed bounds already cover these cases; no constant or algorithm change required. |
| Final notes about local Delta/D/N/S notation and generic beta | Retained as nonblocking exposition: definitions are local, the determinant identity is derived, and Section 5 explicitly instantiates the search lemma's generic failure parameter as rho. No proof step uses the determinant Delta as the earlier estimation tolerance. |

## Reviewer errors retained rather than adopted

The initial Grok/AGY summaries could be read as aborting on any zero elimination determinant. The algorithm aborts only for a zero Gram determinant in a nonempty fit; a zero column-replacement determinant is a valid zero coefficient. The manuscript now says this explicitly, and all final reports distinguish the two cases.

AGY's initial comparison-cost summary understated certificate processing. The manuscript pays tilde-O(nk^3+k^4), not the cheaper search-comparison cost. Final reports explicitly check that distinction. AGY's final blanket phrase that certification and "other steps" fit that smaller envelope is not adopted: weight preparation costs tilde-O(k^5), and fitting tilde-O(k^6), both separately paid in the source and still below the theorem bound.

Several report lemma/proposition numbers are inaccurate. The coordinator checked manuscript labels and displayed statements; the search is Lemma 5 and the safety/progress propositions are 8 and 9. Review summaries are not replacements for the source. No report establishes that reference pages were fetched or that the supplied hash was independently recomputed. Public AGY reports replace workstation file links with links to their archived packets, with unchanged substantive text and raw-response hashes retained.

## Incomplete attempts and verification limits

An AGY version probe timed out before any review launch; the first batch wrapper eventually reported that startup exception even though the separately identified Grok and Claude reviews completed. One subsequent AGY launch rejected medium effort for its high-effort model and produced zero review turns. Both are excluded from clearance; the corrected high-effort run and final check completed. No authentication failure or empty report is counted as a review.

The authoring assistant separately checked the probability interface, all-tape integer precision, processing costs and exact output contract. Twenty-two rational constant checks and actual thirteen-page visual inspection support artifacts only. Clean-export and package receipts complete the operational gates. The sharper computation guarantee remains an informal analytic theorem; model agreement does not establish novelty, practicality, independent human acceptance or formal certification.
