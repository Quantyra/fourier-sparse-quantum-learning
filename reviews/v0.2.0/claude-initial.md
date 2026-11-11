# Adversarial audit: manuscript v0.2.0, "Polynomial-Time Exact Learning of Fourier-Sparse Boolean Functions from Nearly Linear Quantum Samples"

**Verdict: GO WITH NOTES.** I found no blocking mathematical error. The new mechanism holds: constant-confidence proposals, fresh high-confidence certification, and capped adaptive progress via a supermartingale-style count. The constants close with margin. The notes below concern a citation dependency, the promise-violation scope, notation, and presentation.

**Limits of this audit.** I worked only from the packet. I did not verify the SHA-256, fetch any source, or check the primary-source comparison. Ye (arXiv:2610.17648, Oct 2026) is after my knowledge horizon. Statements about Ye and the Caro et al. Corollary 10 pinpoint are unverified here. The ACLPW bounds O(k^{3/2}log²k) and Ω(k log k) match my recollection. The Tropp numbering (Cor. 5.2 for Chernoff, Thm 6.1 with parts (i)–(iii) for Bernstein) matches my recollection, but I did not check page pinpoints. I make no novelty inference.

---

## 1. Worked checks

**Fourier sampling.** After H^{⊗(n+1)}, the amplitude of (s,1) is 2^{-1/2}·2^{-n}Σ_x f(x)χ_s(x) = c_s/√2. The amplitude of (s,0) is 2^{-1/2}δ_{s,0}. So Pr[flag=1] = ½ and s|flag=1 ~ c_s². ✓

The selection "first gm flag-one outcomes" depends only on flags. Conditional on any flag pattern with ≥gm ones, those indices are i.i.d. c_s². ✓

The Chernoff bound with μ=2gm and δ=½ gives exp(−gm/4). Since g≥13 and m=144k, this is far below ρ. ✓

**Lemma 1 (fresh residual estimates).**
- B=(√2+1)√k·e ≤ 3√k·e and t=εe/√k, so Bt/3 = εe². The denominator is ≤ 2e² and the tail is 2exp(−qε²/4k). ✓
- For v: Var(r²) ≤ ‖r‖∞²e² ≤ 2ke⁴. At t=e²/2 the denominator is 2(3k+k/2)e⁴ = 7ke⁴, giving exp(−q/28k). ✓
- The budget gives qε²/4k ≥ 8L₀ and q/28k ≥ (32/28)L₀ ≥ L₀. The union bound is ≤ 2(P+1)e^{−L₀} = β/2. ✓
- At e=0 everything is exact. ✓

**Lemma 2 (certification).** For s∉U, â(s)=0, so E z_s = c_s.
- For a null s: z² ≤ ε²e²/k < 2ε²e²/k ≤ threshold. The inequality is strict because e>0.
- For |c_s| > 4εe/√k: |z_s| > 3εe/√k > √6·εe/√k ≥ √threshold, since √6 ≈ 2.449. ✓
- At e=0 we have z≡0 and the threshold is 0, so the strict ">" admits nothing. ✓

Additional observation: v=0 forces every r(X_ℓ)=0, hence every z_s=0. So the certificate admits nothing whenever v=0, even off the good event. This is a useful robustness fact worth stating.

**Lemma 3 (Gram).**
- φ' = −ln(1−δ) ≥ δ gives ≥ δ²/2.
- The upper exponent is ≥ δ²/2 − δ³/6 ≥ δ²/3 for δ ≤ 1. ✓
- At δ=1/10, 2p·e^{−q/300p} ≤ β ⇔ q ≥ 300p ln(2p/β). ✓
- Normal equations: labels equal A_U c_U + A_V c_V exactly, so ‖a_U−c_U‖ ≤ (10/9)(1/10)√W = √W/9. ✓
- ‖f−a‖² ≤ (1+1/81)W. ✓
- ‖a‖ ≤ √(1−W) + √W/9 ≤ √(82/81) by Cauchy–Schwarz. ✓
- Adaptivity is correct: the event concerns only the fixed S₀ Gram matrix, so it covers every U⁺ ⊆ S selected from the same rows.

**Lemma 4 (capped search).**
- Hoeffding on ±1 summands gives 2exp(−Nτ⁴/32) ≤ β/(2nP), over ≤ 2nP test slots. ✓
- Retained buckets have E ≥ τ²/2, and H Boolean gives ΣĤ²=1. So at most 2/τ² ≤ P are retained.
- With τ=1/(4k), P = ⌈64k²⌉ = 64k², which matches (eq:parameters). ✓
- Parseval for H holds on every tape because H is a sign-majority. This is what makes the cap meaningful on bad histories.

**Lemma 5 (bias and variance).**
- t = 4ε√(v/k) ∈ [2√2Δ, 2√6Δ] and 2√6 ≈ 4.90 < 5. ✓
- On a pass: |c/c̃| ≤ 1 + 1/(2√2) ≈ 1.354 < 3/2, and the coefficient error is ≤ 1.5Δ. On a fail: |c| < 6Δ.
- The squared bias is ≤ 36kΔ² = 36ε²e². ✓
- The second moment is ≤ (9/4)|S|. ✓

**Lemma 6 (majority).**
- m=144k gives Var ≤ 1/64. Chebyshev at ½ gives 1/16.
- Majority error ≤ 2^g·16^{−g/2} = 2^{−g}.
- 4(4‖h−f‖² + 2^{−g}) = 16·36ε²e² + 4·2^{−g}. ✓
- First term with ε²=ρ/2^18 and e² < 2W: 1152ρW/262144 = ρW/227.6 ≤ ρW/128. ✓
- Second term: 4·2^{−g} ≤ ρ/(128k²) ≤ ρW/128, using W ≥ 1/k². ✓
- Markov at W/64. ✓
- Parameters: ε² = 2^{−22} = ρ/2^{18} exactly, and g=13 at k=1 (8192 = 2^{13}). ✓

**Proposition 9 (contraction).**
- An omitted true s has |Ĥ(s)| < 1/4k ≤ |c_s|/4, so c_s² ≤ (16/9)(Ĥ(s)−c_s)². Summing gives ≤ (16/9)(W/64) = W/36. ✓
- Non-admitted proposed true indices contribute ≤ k·16γ²e²/k = e²/64 ≤ (82/81)W/64.
- Total: 0.02778 + 0.01582 = 0.0436 < 0.0625. ✓
- Probability ≥ 1 − (ρ/2 + ρ + ρ + ρ) − 2β ≥ 3/4 − 1/800. ✓

**Main proof (progress count).**
- E[2^{−I_t}|F_{t−1}] = 1 − ½Pr(I_t=1|·) ≤ 3/4. The tower property gives (3/4)^T without independence. ✓
- Markov: Pr(Z_T<ℓ) ≤ 2^{ℓ−1}(3/4)^T actually suffices; the stated 2^ℓ is valid but loose.
- 2(3/4)^8 = 6561/32768 ≈ 0.2002 < ¼. ✓
- 16^ℓ = (2^ℓ)^4 ≥ 16k⁴, so W < 1/(16k⁴) < 1/k² ≤ min positive W. ✓
- Success ≥ 1 − 0.01 − 0.25 = 0.74; the true value is ≈ 0.79. ✓

**Validation.** d has ≤ 2k terms and ‖d‖∞=2, so 4 ≤ 2k‖d‖₂² = 2k·4·Pr[≠], giving Pr ≥ 1/(2k). Then (1−1/2k)^{2k ln 100} ≤ 1/100. ✓ The check a²≡1 really forces a to be {±1}-valued.

---

## 2. The audited mechanisms

**Arbitrary-proposal safety.** This is correct. L depends only on data that precede the certification batch, and |L| ≤ P is enforced by construction: the search cap, or ∅. Lemma 2 therefore applies to any L. C uses the *old* residual and G is subset-uniform, so the shared batch is legitimate. The union of C^c and G^c is charged at 2β per trial with no independence assumption. W is monotone because nothing is deleted.

**Shared-batch Gram and certification.** Correct as argued above. One point to state explicitly: C's event is indexed by the realized L, which is F-measurable before the batch. This is what Lemma 1's "conditional on any history fixing a, 𝒟" covers.

**Conditional probabilities and dummy indicators.** Correct, and the proof does not condition on future safety.
- I_t is F_t-measurable.
- "Safety failure occurred earlier" is F_{t−1}-measurable.
- On valid histories with W>0, Proposition 9 supplies the ½ bound directly.
- On B, the dummy ones carry no correctness claim, and B is charged separately.
- Global aborts occur only on C^c ∪ G^c, and are therefore after a safety failure. Hence "unused indicators are one" is harmless.

**Termination by granularity.** This is exact and uses no observed quantity: no W, and no stopping on v=0. There is one dependency: every constant (τ=1/4k, W ≥ 1/k², the 2^{−g} budget, ℓ) relies on |c_s| ≥ 1/k. See Note 1.

**Every-tape costs.** The copy count is deterministic: T(q_e+4gm+q_c) + ⌈2k ln100⌉ regardless of flags, failed searches, or empty L. Time and space caps are input-determined:
- the distinct-index guard caps grouped indices at ≤ k;
- the archive is capped at k before the fit;
- b_a comes from Hadamard on integer Gram entries ≤ q_c, independent of correctness;
- weights are only formed for nonzero estimates;
- the search cap is P.

The Õ(n²k⁷ + nk⁹) bound follows from O(nk⁶log) H-evaluations per round, each costing O(nk) for parities plus Õ(k³) for g group sums of k weights with Õ(k²) bits. Certification at Õ(nk³ + k⁴) and refits at Õ(k⁴) are dominated. Space: P·n prefixes, P·Õ(k) accumulators, and Õ(k³) weight storage give Õ(nk² + k³). ✓

**Retained lemmas and access.**
- f is touched only through supplied copies.
- KM-style queries go only to the stored H.
- No inverse state preparation and no collective measurement are used.
- No step implicitly evaluates f at chosen points; Booleanity uses the convolution of a and validation uses fresh labels.

---

## 3. Endpoints and adversarial cases

**k=1.** ℓ=1, T=8, β=1/1600, P=64, τ=¼, m=144, g=13. f=±χ_s; one successful trial suffices and the rest preserve W=0. Validation uses 10 labels with disagreement ≥ ½. ✓

Worked copy count at k=1, using ln:
- q_e = ⌈2^{27}·ln128⌉ ≈ 6.51×10⁸
- 4gm = 7,488
- q_c = max(32768·ln416000 ≈ 423,960, 600·ln6400 ≈ 5,258) = 423,960
- Total ≈ 8·6.52×10⁸ ≈ **5.2×10⁹ copies**, or ≈ 7.5×10⁹ under the ⌈log₂⌉ convention.

This is consistent with the "asymptotic only" disclaimer, but readers should see it (Note 3).

**W=0.** Absorbing on safety: residual ≡ 0, c̃_s = â(s) = c_s exactly, cutoff 0, nothing certified, refit exact. Lemmas 5–6 correctly require W>0 and are not invoked. Initial W=1, so W=0 never occurs at the start.

**Wrong or inaccurate hypotheses (H).** Fully covered by arbitrary-proposal safety. A bad estimator batch, v=0 in the estimator, a garbage H, a search FAIL, or <gm flags all yield at most a wasted trial.

**Wrong k (promise violation).** This case is not covered and is not flagged. The caps still hold because they are input-determined. But the validation soundness argument assumes the target is k-sparse. Counterexample: f = χ_s flipped at one point has sparsity about 2^n. The fit on {s} is exactly χ_s unless the flipped point is sampled, so it passes Booleanity and validation with probability ≈ 1 − O(copies/2^n) and returns a wrong answer silently (Note 2).

**Aborts.** On valid histories, |U|>k, singularity and ‖a‖²>2 are impossible on C∩G, so aborts are inside the 1/100 budget. The ‖a‖²>2 guard is never needed for correctness and only bounds bad tapes; say so.

---

## 4. Unsupported or unverifiable claims

1. **Ye comparison.** "Theorem 1.1 … does not state a fixed polynomial computation bound" and "Algorithms 1–2 … solve over the candidate dictionary" are negative claims about one version. This review cannot verify them. Keep "v1" in the claim and in the abstract sentence "complements … by supplying a fixed polynomial computational guarantee." The abstract currently reads more strongly than the body's hedge.
2. **Caro et al. Corollary 10** (O(k⁴log(k²/δ))): unverified here.
3. **GOSSW Thm 8.1 as ⌊log₂s⌋−1 granularity:** not checked against the source. Supporting evidence: the floor 2/s₀ is attained by AND on j bits (s₀=2^j, minimum coefficient 2^{1−j}), and sparsities 2 and 3 are impossible for Boolean f, so the claimed consequence is at least consistent with small cases.
4. **"Removing a logarithm from the previous version":** v0.1 is not in the packet, so the comparison is unverified. The v0.2 bound O(k log²(2k)) is verified above.
5. **AI-review disclosure.** This report is another AI model review. Do not count it toward "independent peer review."

---

## 5. Clarifications (non-blocking)

1. **Granularity sensitivity.** State that only |c_s| ≥ 1/k is used and that the cited theorem gives 2/k. Note that a weaker floor of 1/(2k), as from ⌈log s⌉-granularity, would only rescale τ, P and g, and would not change the asymptotics. This makes the proof robust to a pinpoint dispute.
2. **Promise scope.** Add one sentence saying that if |S| > k the resource caps still hold but neither correctness nor detection is claimed, and that the validation bound assumes a k-sparse target.
3. **Explicit constants.** Give the k=1 copy figure or a closed-form leading constant. Note that ε^{−2} = 2^{22} in q_e dominates; this is where loosened constants cost most.
4. **Parameter instantiation table.** List each lemma invocation with its substituted parameters:
   - Lemma 1 (estimator): β←ρ, P←k, ε←ε
   - Lemma 1 (certifier): β←β, P←64k², ε←γ
   - Lemma 6: β←ρ
   - Lemma 4: β←ρ

   Lemma 6's generic "β" currently collides with the global β.
5. **Notation collisions.**
   - e (Euler) vs e = ‖f−a‖, e.g. "e^{−L₀}" and "e^{−δ}"
   - ℓ (summation index) vs ℓ = ⌈log₂2k⌉
   - P (list cap) vs P_U
   - t (deviation, cutoff and trial index)
   - "4\,2^{-g}" renders like "42^{−g}"; use 4·2^{−g}
6. **S₀ = S∪{0}** is unexplained. It is harmless but unnecessary. Explain it, or drop it and use k in place of k+1.
7. **Lemma 4.** State explicitly that the union bound runs over ≤ 2nP *test slots*, since the number of tests is adaptive. Specify the multiplicative Chernoff form used for the flag count.
8. **Ordering.** (eq:ctilde) uses q_e before (eq:batches) defines it.
9. **Lemma 1.** On valid tapes r is supported on S, so ≤ k terms rather than 2k. Mention that 2k is kept for bad tapes.
10. **Markov.** 2^{ℓ−1} suffices; optional tightening.
11. **Safety remark.** Add the v=0 ⇒ "no admissions" observation from Section 1 as an explicit remark.

---

## 6. Verdict justification

Every inequality I checked closes with explicit slack:
- contraction 0.0436 < 0.0625
- majority term ρW/227.6 vs ρW/128
- progress tail 0.200 < 0.25
- success 0.74 > 2/3

The four requested mechanisms are sound. The proof does not condition on future safety. Failed proposals are charged in both copies and time. The shared batch is handled by a subset-uniform event. Termination is exact via granularity with no data-dependent stopping.

The remaining risks are external dependencies (the GOSSW pinpoint, the Ye negative claim, the Caro pinpoint), the unstated promise-violation behavior, and presentation. None of these invalidates Theorem 1 as stated. **GO WITH NOTES.**
