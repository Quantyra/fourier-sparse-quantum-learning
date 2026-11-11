# Review of P010 manuscript v0.3.0

**Source SHA-256 (as supplied):** `9730a332f889842bf984999d1dd21c52a110a4ef7a9b079e7d6616e0a886a7ee`
I did not recompute this hash because executing commands was excluded. This review applies to the text pasted above, and I have not confirmed that the text matches the hash.

**Scope.** I reviewed every changed hunk of the v0.2.0→v0.3.0 diff. These are the abstract, Theorem 1 resources, version history, Lemma 7 (shared-batch search) with its processing-cost paragraph, and all of §"All resource costs". I read them against the unchanged lemmas they rely on: the estimates and certificate lemmas, Lemma 4 (fit), Lemmas 8–9 (bias/majority), Propositions 10–11 (safety/progress) and the success proof. I re-derived the unchanged lemmas only where they connect to the changes. I did not fetch or validate any links. Line numbers come from the diff hunk headers and are approximate (±1).

---

## Answers to the named questions

**(1) Frozen children with correlated estimates: valid.**
- **Identity.** At depth j, every child is a j-bit prefix. So one triple law (x, y ∈ F₂ʲ, z ∈ F₂ⁿ⁻ʲ) gives an unbiased estimate of E_u for all children at once, by eq. (bucket).
- **Hoeffding bound.** Summands are ±1, so the bound is 2exp(−2Nt²/4) = 2exp(−Nτ⁴/32) at t = τ²/4.
- **Constants.** N ≥ 32τ⁻⁴L₀, and L₀ = ⌈log₂(4nP/β)⌉ ≥ ln(4nP/β). This gives β/(2nP) per child, β/n over |C_j| ≤ 2P children, and β over n depths.
- **Conditioning.** C_j and H are fixed by the past, and the rows are fresh i.i.d. The union bound needs no independence between children, and the manuscript correctly says so.
- **Early termination.** Setting unreached-depth failure to false, then taking expectations of the conditional bounds, is a correct way to handle stopping.
- **Overflow.** On accuracy at depth j, every retained child has E_u ≥ τ²/2. The buckets are disjoint with total energy ‖H‖² = 1, so at most 2/τ² ≤ P are retained. Overflow therefore implies an accuracy failure at that depth.
- **Empty frontier.** An empty frontier on the good event implies no |Ĥ(s)| ≥ τ, because every heavy ancestor has E_u ≥ τ² and estimate ≥ 3τ²/4.
- **Caps.**
  - Random bits: Σⱼ(n+j) = (3n²+n)/2, times N.
  - Evaluations: 2nN.
  - Constant: N = 8192k⁴⌈log₂(4096nk²)⌉ matches τ = 1/(4k), P = 64k², β = ρ = 1/16.

**(2) Interface preserved: yes.**
- The conclusion matches the old interface: an output of at most P indices on every tape, and coverage of all τ-heavy indices with probability ≥ 1−ρ conditional on any fixed H.
- H is Boolean on every tape (sign-majority, ties → +1). Parseval alone bounds the bucket count, so H need not be sparse.
- Proposition 11's staged union bound still applies the search failure conditional on H.
- The success proof's indicator/supermartingale argument (E[2^{−I_t} | F_{t−1}] ≤ 3/4) never conditions on future safety.
- The certification batch remains fresh with respect to the search coins.

**(3) Charging: yes.**
- **Main per-trial terms:**
  - Evaluations: 2nN · C_H, with C_H = Õ(nk + k³), giving Õ(n²k⁵ + nk⁷).
  - Explicit child parities: nPN(n+h) = Õ(n²k⁶).
  - Random bits and input assembly: Õ(n²k⁴).
  - Threshold comparisons: O(nP(d+h)²).
- **Evaluator cost.** C_H is valid on every tape because:
  - the distinct-index guard caps H at ≤ k indices;
  - weights are stored as multiplicity × weight per group (g sums of ≤ k numbers with B + log m bits);
  - the weight positive factor D_e/(mR) is correct, since w_s = D_e/N_s.
- **Other work.** Certification (q_c·P·(n + b_a)), estimate and residual evaluation, Gram formation, Booleanity (k² XOR keys plus sort) and validation are all itemised and fall below the dominant terms.

**(4) Fraction-free/Cramer bound: holds on all tapes.**
- **Entry and minor bounds.** Gram and right-side entries are ≤ q_c on every tape, and |U| ≤ k is enforced before fitting. So every minor, including column-replaced ones, is ≤ k!·q_c^k, giving b_a = O(k log(kq_c)).
- **Sylvester step.** The identity M_pp·M_ij − M_ip·M_pj = d·det(2-bordered) is correct, since the left side equals d²·det(2×2 Schur block). It makes each Bareiss division exact.
- **Pivoting and singularity.**
  - Pivot swaps track the sign.
  - "No nonzero pivot remaining in the column" correctly yields det = 0. This covers singular Gram matrices (→ FAIL) and zero numerators (→ coefficient 0).
  - The Gram determinant is ≥ 0 (positive semidefinite), so D > 0 when it is nonsingular.
- **Cost.** One determinant costs O(k³·b_a²) = Õ(k⁵), so k+1 determinants cost Õ(k⁶) time with Õ(k³) reused space.
- **Precision.** Precision resets with each original-label refit.

**(5) Totals: confirmed.**
- **Time.** The per-trial maximum is Õ(n²k⁶ + nk⁷), and multiplying by T = O(log k) is absorbed. The copy count (eq. copies) is untouched because search uses only H.
- **Live space:**
  - prefixes: O(nk²);
  - search counters: Õ(k²);
  - certificate accumulators: P·Õ(k) = Õ(k³);
  - determinant and weights: Õ(k³);
  - label rows: Õ(nk);
  - k² keyed products: Õ(nk² + k³).
- **Space total.** These sum to Õ(nk² + k³).

**(6) Attribution, novelty and practical-performance boundaries: accurate.**
- Bareiss is cited only for the method, and the needed identity is derived in the text.
- Version history explicitly disclaims a new search principle and any practical runtime claim.
- Ye remains described as having the smaller sample bound.

---

## Findings

### Blocking
None.

### Non-blocking (should fix before freeze)

**N1 — Orphan heading** (`main.tex:67`).
`\paragraph{Revision scope.}` is immediately followed by `\paragraph{Version history.}`, so an empty run-in heading is rendered.
*Fix:* delete line 67.

**N2 — Ambiguous matrix symbol in the Sylvester identity** (`main.tex:≈370`).
In `d\det A[B bordered …]`, the symbol A is undefined here. A_U elsewhere is the ±1 design matrix, not the matrix being eliminated. The same section also uses A_s for fit numerators, and Lemma 7 uses A_u for accumulators.
*Fix:* write `\det G[\cdot]`, where G is the Gram matrix or its column-replaced variant being eliminated.

**N3 — Symbol reuse in adjacent paragraphs** (`main.tex:≈193, ≈368, ≈379`).
- B is the pivot block at ≈368 and the weight bit length at ≈379. It is also the safety-failure event in the success proof and the Bernstein bound in the estimates lemma.
- d is the parameter bit length at ≈193 and the pivot determinant at ≈368.
- h is the counter width at ≈193 and also E Q_i in Lemma 8.

None of these causes a mathematical error, but together they make the cost section harder to audit.
*Fix:* rename locally, for example B → B_w (weight bits), pivot block → K, d → d_τ, h → h_c.

**N4 — Unquantified parameter-arithmetic term** (`main.tex:≈197`).
"plus polynomial parameter-arithmetic cost" is weaker than the Õ claim needs.
*Fix:* add "for the instantiated τ = 1/(4k) and β = ρ, computing L₀, N and the integer threshold 3τ²N/4 costs polylog(nk)."

### Optional exposition

- **O1.** In Lemma 7's proof, state explicitly that "overflow at depth j implies some child's estimate at depth j is inaccurate." It currently follows only implicitly from the cap paragraph.
- **O2.** The "Apart from the stored evaluator" space claim (≈197) should also exclude the evaluation workspace (Õ(n + gB) bits). This is still within Õ(nk² + k³).
- **O3.** The bounds are conservative, as the manuscript says:
  - one augmented Bareiss pass would give Õ(k⁵) per fit;
  - k long divisions cost Õ(k⁴), not Õ(k⁵);
  - child parities could be updated incrementally.

  No change is needed unless the author wants tighter exponents.
- **O4.** In version history, consider calling batch sharing across same-level prefix tests "a standard implementation device." This further anticipates novelty objections.

---

## Verdict: **GO WITH NOTES**

I found no mathematical or resource-accounting errors in the changes.
- Lemma 7 is valid with correlated shared-batch estimates, early termination and overflow.
- The search interface used by the progress proof is unchanged.
- The fraction-free bound holds on every tape.
- The bounds Õ(n²k⁶ + nk⁷) time, O(k log²(2k)) copies and Õ(nk² + k³) space follow.

N1–N4 are editorial and notational fixes that I recommend before freezing.
