# Focused Revision Review Report

**Manuscript Title:** *Polynomial-Time Exact Learning of Fourier-Sparse Boolean Functions from Nearly Linear Quantum Samples*  
**Author:** Daniel Fredriksen (Quantyra Inc.)  
**Baseline Commit:** `69dfe76e30a0e80ae82265031f5e5b408a3d9342`  
**Revised `manuscript/main.tex` SHA-256:** `91aadd7a185ad4c8b365350018703ecb8a3fe7c0dfaa7593fa08ec8533b6e804`  
**Review Type:** Focused baseline-to-revision diff review  

---

## 1. Verdict

### **GO** (Unconditional for Preprint Release)

The revision directly addresses and resolves the findings from the initial review. The core sample and resource bounds ($O(k \log^3(2k))$ quantum copies, bit-time $\widetilde{O}(n^2 k^7 + n k^9)$, live space $\widetilde{O}(n k^2 + k^3)$) remain identical. The text modifications are strictly clarificatory and foundational, introducing zero new mathematical blockers or regressions.

---

## 2. Audit of Targeted Diff Modifications

### A. ADDED Matrix Chernoff Tail Simplification (Lemma 4)
* **Diff Lines 71–89:** The proof now details the scalar simplification connecting Tropp's operator tail bounds (Corollary 5.2) to the concrete scalar exponential bound:
  - Upper tail exponent $h(\delta) = (1+\delta)\ln(1+\delta) - \delta \ge \delta^2/3$, verified by integrating $\ln(1+t) \ge t - t^2/2$ on $[0, \delta]$.
  - Lower tail exponent $g(\delta) = \delta + (1-\delta)\ln(1-\delta) \ge \delta^2/2$, verified by integrating $-\ln(1-t) \ge t$.
  - Summing the two tails yields $p \exp(-q\delta^2/(2p)) + p \exp(-q\delta^2/(3p)) \le 2p \exp(-q\delta^2/(3p))$.
  - The sample budget $q_c \ge 300(k+1)\ln\frac{2(k+1)}{\beta} \ge 300p\ln\frac{2p}{\beta}$ (with $p = |S_0| \le k+1$) is explicitly justified because both $p$ and $\ln(2p/\beta)$ increase monotonically with $p$.
* **Assessment:** The derivation is fully closed and mathematically rigorous.

### B. Explicit Flag-Zero Discard and Distinct-Count Cap (Step 2 & Section 6)
* **Diff Lines 141–142, 153–154, 162–163:** Step 2 now states:
  - *"Discard every flag-zero outcome."*
  - *"Abort if more than $k$ distinct indices occur among these $gm$ grouped indices."*
  - Section 6 clarifies that *"each retained flag-one outcome belongs to $S$; discarded flag-zero outcomes are not counted."*
  - Binomial flag-sufficiency probability is explicitly verified: $gm/4 = 36kg \ge g \ge \log_2(1/\beta) \ge \ln(1/\beta) \implies \exp(-gm/4) \le \beta$.
* **Assessment:** This removes any operational ambiguity: flag-zero measurements are immediately dropped, and the distinct-count cap applies solely to the retained flag-one pool. Because Hadamard measurement of $|\psi_f\rangle$ yields flag 1 only on indices $s \in S$, and $|S| \le k$, this cap never fires on valid quantum states.

### C. Same-Batch Refit Specification (Step 4 & Lemma 4)
* **Diff Line 144–145:** Step 4 now explicitly reads:
  - *"Refit the target labels $f(X_\ell)$ from this same certification batch exactly on the updated archive $U$; abort on singularity or $\norm a_2^2>2$."*
* **Assessment:** This confirms the exact data reused for the refit (the $q_c$ target labels $(X_\ell, f(X_\ell))$ from the certification batch) and the matrix operated on (the updated archive $U^+$). By Lemma 4, the single empirical Gram event on the full support $S_0$ bounds all submatrices simultaneously, ensuring this refit is non-singular and contractive without extra labels or circular conditioning.

---

## 3. Resolution of Initial AGY Review Notes

Both notes identified in the initial review have been directly incorporated and resolved:

1. **Resolution of Note 1 (Bias Bound Partition Accounting):**  
   * *Initial finding:* The transition to $\norm{h-f}_2^2 \le 36\varepsilon^2 e^2$ relied on the fact that $S_{\text{pass}}$ and $S_{\text{fail}}$ partition $S$, with error bounds bounded by $\max\{9/4, 34.8\} \le 36$.  
   * *Revision:* Lines 129–130 now explicitly state: *"The passing and failing sets partition $S$, so Parseval bounds the total squared error by $36|S|\Delta^2 \le 36\varepsilon^2e^2$."*  
   * *Status:* **RESOLVED.**

2. **Resolution of Note 2 (Centered Bound and Scalar Bernstein Details):**  
   * *Initial finding:* The scalar centered bound $(\sqrt{2k}+1)e \le 3\sqrt{k}e$ and Bernstein denominator warranted explicit display.  
   * *Revision:* Lines 58–63 now state $\norm{r}_\infty \le \sqrt{2k}e$, $|\widehat{r}(s)| \le e$, resulting in centered bound $(\sqrt{2k}+1)e \le 3\sqrt{k}e$. The revision displays the scalar denominator $\sigma^2 + Bt/3 \le e^2(1+\varepsilon) \le 2e^2$, cites Tropp Theorem 6.1(ii), and proves union bound convergence $2(P+1)e^{-L_0} = \beta/2$ using $L_0 = \ln(4(P+1)/\beta)$.  
   * *Status:* **RESOLVED.**

---

## 4. Additional Diff Improvements

* **Ye Literature Framing (Line 23):** Softened to accurately state that Ye (arXiv:2610.17648v1) proves a sample guarantee without asserting a fixed polynomial computation bound, avoiding any unverified claim of a computational lower bound for Ye's algorithm.
* **Granularity Derivation (Line 32):** Explicitly derives $|c_s| \ge 2/s_0 \ge 1/k$ from GOSSW Theorem 8.1.
* **Notation Cleanup:** Replaced candidate set symbol $D$ with $\mathcal{D}$ to prevent confusion with rational denominator $D$.
* **Disclosure (Line 178):** Accurately reflects multi-model review history (Grok, Claude, AGY configured with Gemini).

---

## 5. Blocker Assessment

**No blockers remain.** All identified notes are resolved, the added proofs are correct, and all resource and error bounds hold. The manuscript is recommended for publication without reservation.
