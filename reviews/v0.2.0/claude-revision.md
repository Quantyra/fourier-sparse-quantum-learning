# Focused final-source recheck: manuscript v0.2.0

**Final source SHA-256 (as supplied, not computed here):** `a826eda138c3cbe0dee0a12a53470a559429e0d1b40f97afd62356666f2429d6`

I checked the diff against my initial review and read the complete final source. I did not hash the files, fetch any sources, or rely on other models' conclusions. This is a focused recheck, not a new full audit.

**Verdict: GO WITH NOTES**

## Diff items checked

**1. Ye version pin (abstract and §1): correct, and resolves my unsupported-claim item 1.**
- Both the abstract and the prior-work paragraph now scope the claim to the cited version.
- Residual nit: the §7 sentence "does not improve Ye's logarithmic sample factor~\cite{Ye}" is still unversioned. This is harmless because the bibitem pins v1.

**2. Zero sampled variance remark (Lemma 2 proof): correct.**
- v = q⁻¹Σr(X_ℓ)² = 0 forces every observed r(X_ℓ) = 0, so every z_s = 0.
- The test z_s² > 0 is strict, so nothing is admitted.
- This holds on every tape, with or without the accuracy event, and matches the remark I suggested.

**3. Exact pointwise Fourier inversion (Lemma 3): correct.**
- f = Σ_{s∈S} c_s χ_s holds at every point as a finite identity, so y = A_U c_U + A_V c_V exactly with V = S∖U.
- This is inversion, not a "pointwise Parseval" claim, and the proof uses it correctly.

**4. Parameter instantiation sentence (§5): correct, and resolves my clarification 4.**
- Estimator: (k, ε, ρ). Certifier: (P, γ, β). Lemmas 4 and 6 are instantiated with ρ.
- These match q_e, q_c, the choice 2^g ≥ 512k²/ρ, and ε² = ρ/2¹⁸ exactly.
- Minor: §4 still says "with probability at least 1−β" for (eq:uniformtrue) before the instantiation is stated. A forward reference would help but is not required.

**5. W = 0 with out-of-S proposals (Proposition 8): correct as stated.**
- At W = 0 the old fit is f, so the residual is identically zero.
- Lemma 1's event therefore holds surely, so C cannot fail. Every candidate in L∖U is rejected by item 2, including indices outside S.
- H need not equal f, and L need not be contained in S; the proof does not assume either.
- Only G can fail. G is needed solely for nonsingularity: any nonsingular least-squares fit on U = S reproduces f exactly. A failure of G is charged within 2Tβ.

**6. Promise and validation scope (§7): correct, and resolves my Note 2.**
- The resource caps depend only on the input (n, k): the distinct-index guard at k, the archive cap at k, a fixed number of trials, and fixed batch sizes.
- They therefore hold under a promise violation, as claimed.
- The validation bound is now explicitly restricted to targets of sparsity at most k, consistent with my near-parity counterexample.

**7. Typography: fixed.** "4·2^{−g}" is now unambiguous.

The diff changes no algorithm step, constant, probability argument or resource bound. The success chain I verified in the initial review (0.0436 < 1/16, 2(3/4)⁸ ≈ 0.200, success ≥ 0.74) is unaffected.

## Self-check of my initial report against the flagged premises

- **First-trial success at k = 1.** I wrote "one successful trial suffices." That means W reaches 0 after the first trial that achieves contraction. It is not an unconditional first-trial success. Each trial contracts only with conditional probability ≥ 3/4 − 2β, and the guarantee comes from T = 8 trials with tail ≈ 0.200. My statement should be read in that sense.
- **Parseval.** I used Parseval for the Boolean H, ΣĤ² = ‖H‖₂² = 1, which is a global identity. No pointwise claim was made or needed.
- **Primary-source verification.** I did not directly verify any source. GOSSW, Tropp, Caro and Ye pinpoints remain unverified by me, as stated in the initial report.
- **Integer multiplication cost.** The Õ(nk + k³) per-query cost for H needs only schoolbook arithmetic. Each group sum adds ≤ k signed weights of Õ(k²) bits, each scaled by a multiplicity of O(log k) bits, and g = O(log k). No fast multiplication is assumed. This matches the source's explicit "schoolbook" wording.
- **W = 0.** My initial statement "c̃_s = â(s) = c_s" is correct for every s: â(s) = c_s on U = S and 0 = c_s off S. It does not imply H = f, and I did not claim that it does.

## Remaining non-blocking notes (not addressed by this diff)

1. **Granularity robustness.** Every constant depends on |c_s| ≥ 1/k from the GOSSW pinpoint. The source gives the stronger 2/s₀. A one-line remark that a weaker floor of 1/(2k) would only rescale τ, P and g would hedge against a pinpoint dispute.
2. **Explicit constants.** At k = 1 the run uses about 5.2×10⁹ copies with natural logs, dominated by ε⁻² = 2²². The "asymptotic only" disclaimer covers this, but a stated figure would inform readers.
3. **Notation collisions remain.**
   - e: Euler's number vs. the residual norm, as in e^{−L₀} and e^{−δ}.
   - ℓ: summation index vs. ⌈log₂ 2k⌉.
   - P: list cap vs. the projection P_U.
   - t: deviation, cutoff magnitude and trial index.
4. **S₀ = S ∪ {0}** is still unexplained. It is harmless.
5. **Markov step.** 2^{ℓ−1} suffices in place of 2^ℓ; this is optional tightening.

None of these affects the correctness of Theorem 1 as stated.
