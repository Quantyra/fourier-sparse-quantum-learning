# P010 v0.3.0 final-source verification

**Source hash (as supplied, not recomputed):** `aa73155e2bee2ce85f27eff07785f601ae29fbc535dff0e25ed0cc5b3fadd565`

**Verdict: GO WITH NOTES.** I found no blocking issues.

## Rechecked items

**1. Conditional coverage under frozen-child sharing (Lemma `lem:search`).**
- At each depth, the children `C_j` and `H` are fixed before the batch is drawn.
- Each child's row summands are i.i.d. in [−1,1], so Hoeffding applies per child. Correlation across children is irrelevant under a union bound.
- The constants check out. τ⁻⁴·32·L₀ with L₀ ≥ ln(4nP/β) gives 2e^{−L₀} ≤ β/(2nP). Summing over ≤2P children gives β/n per depth, then β across depths via conditional expectation. No conditioning on future batches is needed.
- The numbers instantiate correctly: N = 8192k⁴⌈log₂(4096nk²)⌉, since 4·64k²·16 = 4096k².

**2. No FAIL on accurate batches.** On simultaneous accuracy, retained buckets have energy ≥ τ²/2 and are disjoint, so at most 2/τ² ≤ P survive. The new sentence "overflow ⇒ inaccurate estimate at that depth" is correct. An empty frontier cannot drop a τ-heavy index, because its ancestors have energy ≥ τ² and pass the 3τ²/4 threshold.

**3. Progress interface.** The success proof uses only coverage at confidence ρ and the ≤P output cap. Search failure is one of the four ρ-events (1 − 4ρ = 3/4), and search FAIL maps to L = ∅ without touching the archive. The revised closing sentence states this accurately.

**4. Singular Gram vs. zero numerator.**
- A zero Gram determinant gives FAIL (a global abort for a nonempty fit). On G this cannot happen for U ⊆ S.
- A zero column-replacement determinant gives a zero coefficient. The index is retained in U and removed only at output.
- "No nonzero pivot ⇒ determinant zero" applies uniformly to both matrices, and the consequence is correctly split.
- The bordered-minor identity is Sylvester's (Desnanot–Jacobi) form and is correct as stated with M, K, Δ, D_uv.

**5. Cheap comparisons vs. certificate arithmetic.**
- Search threshold tests are O(nP(d_τ+h_c)²), which is polylog per child. Parameter arithmetic is polylog(2nk).
- Certification is P·q_c·n = Õ(nk³) for parities. Accumulation and squaring of Õ(k)-bit values over P candidates is Õ(k⁴).
- The text keeps these separate and pays Õ(nk³+k⁴), which is correct.

**6. Time bound Õ(n²k⁶+nk⁷).**

| Cost | Calculation | Result |
|---|---|---|
| Evaluations | 2nN · Õ(nk+k³) | Õ(n²k⁵+nk⁷) |
| Child-parity scans | nPN(n+h_c) | Õ(n²k⁶) |
| Randomness | — | Õ(n²k⁴) |
| Hypothesis weights | — | Õ(k⁵) |
| Refit | — | Õ(k⁶) |
| Booleanity | — | Õ(nk²+k⁴) |

Multiplying by T = O(log k) preserves the bound. All retained statements support it.

**7. Copies.** T(q_e+4gm+q_c)+O(k) with T, g = O(log k) and q_e, q_c, m = O(k log k) / O(k) gives O(k log²(2k)). Search uses no target copies.

**8. Live space Õ(nk²+k³).** The components are:
- prefixes nP = O(nk²)
- weights k·B_w = Õ(k³)
- evaluator workspace g·Õ(k²)
- certificate accumulators P·Õ(k) = Õ(k³)
- determinant workspace Õ(k³)
- label rows Õ(nk)
- keyed products k²(n+Õ(k))

All fit the envelope. Adding evaluator workspace to the search space statement is consistent with this.

## Nonblocking findings

1. **Notation collision: Δ.** Δ = det K (costs section) reuses Δ := εe/√k from `eq:uniformtrue`. This partly undercuts the "separate local notation" goal. Consider Δ_K or δ_K.
2. **Undefined symbol and collisions in the cost sections.**
   - S_uv (Schur-complement entry) is not defined, and S is the support set.
   - D (fit denominator) sits near D_uv.
   - N_s (estimate numerators) sits near the sample count N.

   All are locally disambiguable.
3. **Ambiguous β in the sharing paragraph.** "β=ρ=1/16" refers to the lemma's generic β, not the global β = 1/(200T). A parenthetical such as "(the lemma's failure argument)" would avoid misreading.

## Scope and limits

This was a static reading of the supplied diff and full source only. I executed nothing, edited nothing, fetched nothing, and did not verify the hash or any external citations (Tropp, GOSSW Theorem 8.1, Ye, Caro, Bareiss). Arithmetic constants were checked by hand. This is not a machine-checked proof.
