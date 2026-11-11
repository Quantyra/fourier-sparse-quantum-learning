# Mathematical and Resource Review: Manuscript v0.4.0 (P010)

- **Source SHA-256:** `0f18f0b7e26495d2bf98dcf4d1f4a1fca5f8c219ca8e6de87e7ea5b6250a9476` *(as supplied in packet; not recomputed)*
- **Scope:** Focused mathematical, algorithmic, and resource analysis of the revised decoder (pruned hash-prefix search and local coordinate correction) in manuscript v0.4.0 and its end-to-end integration with the quantum example learner.
- **Review Basis:** Evaluated solely against the complete revised LaTeX source, exact v0.3.0 $\to$ v0.4.0 diff, and source assessment provided in the review packet. In accordance with instructions, no external network requests were made and no reference pages are claimed to have been fetched.
- **Overall Verdict:** **GO WITH NOTES**

---

## 1. Executive Summary

Manuscript v0.4.0 replaces the $n$-depth Kushilevitz–Mansour classical search on the known Boolean hypothesis $H$ with a two-phase hashed recovery scheme:
1. **Depth-$t$ Hash-Prefix Pruning:** Tests prefixes of a random linear hash $B \in \mathbb{F}_2^{t \times n}$ up to depth $t = O(\log k)$ using frozen batches of size $|C_j| \le 2P$.
2. **Local Coordinate Bit Correction:** Recovers the $n$ individual coordinate bits of surviving heavy characters via majority voting over $J = O(\log(nk))$ repetitions of sign-projected evaluations.

This architectural change reduces the classical bit time from $\widetilde O(n^2 k^6 + n k^7)$ (v0.3.0) to $\widetilde O(n^2 k^3 + n k^5 + k^7)$, while strictly preserving the near-linear quantum sample complexity $O(k \log^2(2k))$, the archive safety invariant, constant conditional progress per trial ($\ge 1/2$), live space $\widetilde O(n k^2 + k^3)$, and deterministic resource bounds on all tapes.

All 7 required check areas have been thoroughly examined and stress-tested. The mathematical arguments are sound, the failure budgets close with slack ($3\rho/4 \le \rho$), and no blocking errors were found.

---

## 2. Detailed Checklist Evaluation

### (1) Bucket and Projection Identities (Lines 74–82, 426–434)
- **Mathematical Form:**
  $$E_{j,v} = \sum_{s: B_j s = v} d_s^2 = \mathbb{E}_{x,u} \left[ H(x) H(x + B_j^{\mathsf T} u) (-1)^{v \cdot u} \right]$$
  $$\mathcal{P}_v(y) = \sum_{s: B s = v} d_s \chi_s(y) = \mathbb{E}_u \left[ H(y + B^{\mathsf T} u) (-1)^{v \cdot u} \right]$$
- **Verification:**
  - Expanding $H$ into its Fourier representation $\sum_s d_s \chi_s$ and taking the expectation over uniform $x \in \mathbb{F}_2^n$ yields $\mathbb{E}_x [(-1)^{(s+s') \cdot x}] = \delta_{s,s'}$, which eliminates all cross terms identically without any rank assumption on $B_j$.
  - Taking the expectation over uniform $u \in \mathbb{F}_2^j$ yields $\mathbb{E}_u [(-1)^{(B_j s + v) \cdot u}] = \mathbf{1}_{\{B_j s = v\}}$.
  - For $y \in \mathbb{F}_2^n$ and uniform $u \in \mathbb{F}_2^t$, $\mathbb{E}_u [(-1)^{(B s + v) \cdot u}] = \mathbf{1}_{\{B s = v\}}$, directly recovering $\sum_{s: B s = v} d_s \chi_s(y)$.
- **Dependent Rows, Infeasible Labels, and $t > n$:**
  - Because expectation over $u$ is taken over the entire affine space $\mathbb{F}_2^j$ (or $\mathbb{F}_2^t$), the character orthogonality relation $\mathbb{E}_u [(-1)^{w \cdot u}] = \mathbf{1}_{\{w = 0\}}$ holds for *any* vector $w = B_j s + v \in \mathbb{F}_2^j$, regardless of whether the rows of $B_j$ are linearly dependent, whether $t > n$, or whether $v \notin \operatorname{image}(B_j)$.
  - If $v$ is infeasible, the sum is empty ($0$), and the identity correctly evaluates to $0$.
  - No matrix inversion, Gaussian elimination, or coset representation is used.

### (2) Frozen-Prefix Coverage and Overflow Protection (Lines 105–116, 435–446)
- **Batch Freezing:** At each depth $j \in \{1, \dots, t\}$, the candidate frontier $C_j$ freezes both children of retained labels ($|C_j| \le 2P$).
- **Hoeffding Bounds:**
  - Each summand $Y_{v} = H(x) H(x + B_j^{\mathsf T} u) (-1)^{v \cdot u} \in \{-1, +1\} \subset [-1, 1]$.
  - At deviation $\tau^2/4$, Hoeffding's bound gives:
    $$\Pr[|A_v/N - E_{j,v}| > \tau^2/4 \mid \text{past}, B] \le 2 \exp(-N \tau^4 / 32) \le \frac{\eta}{8 t P}$$
    since $N = \lceil 32 \tau^{-4} L_0 \rceil$ with $L_0 \ge \ln(16 t P / \eta)$.
  - Union bound over at most $2P$ frozen children: $\le \eta / (4t)$ per depth. Summed over $t$ depths, the total conditional probability of any reached estimate erring by $>\tau^2/4$ is at most $\eta/4$.
- **Heavy Survival & Overflow Invariant:**
  - If $|d_s| \ge \tau$, then $E_{j, B_j s} \ge d_s^2 \ge \tau^2$. On accuracy, $A_v/N \ge \tau^2 - \tau^2/4 = 3\tau^2/4$, so every ancestor survives.
  - Any retained label satisfies $E_{j,v} \ge 3\tau^2/4 - \tau^2/4 = \tau^2/2$. Disjoint buckets sum to total energy $\le \sum_s d_s^2 = 1$, bounding the number of survivors by $2/\tau^2 \le P$.
  - Overflow is mathematically impossible on the accuracy event; therefore, aborting on overflow incurs no false negative on good tapes.
  - Across all $t$ depths, at most $2tP$ labels are evaluated, avoiding any exponential $2^t$ enumeration.

### (3) Heavy-Only Collision and Markov Isolation (Lines 117–127, 448–457)
- **Noise Formulation:** For heavy $s$ ($|d_s| \ge \tau$), $T_s(B) = \sum_{a \ne s: Ba = Bs} d_a^2$.
- **Pairwise Collision Law:**
  - For any fixed $a \ne s$, $a - s \ne 0$. For independent uniform rows $b_k \in \mathbb{F}_2^n$, $\Pr[b_k \cdot (a - s) = 0] = 1/2$. Across $t$ independent rows, $\Pr[Ba = Bs] = 2^{-t}$, holding unconditionally for any $n$ and $t$.
  - Linearity of expectation gives $\mathbb{E}_B [T_s] \le 2^{-t} \sum_{a \ne s} d_a^2 \le 2^{-t}$.
- **Heavy Tail Bound:**
  - By Markov's inequality: $\Pr_B [T_s > \tau^2/1024] \le 1024 \cdot 2^{-t} / \tau^2$.
  - Since $\sum_s d_s^2 = 1$, there are at most $\tau^{-2}$ heavy coefficients. Union bounding over all heavy $s$:
    $$\Pr_B [\exists s: |d_s| \ge \tau, T_s > \tau^2/1024] \le \frac{1024}{2^t \tau^4} \le \frac{\eta}{4}$$
    which holds because $t = \lceil \log_2(4096 / (\eta \tau^4)) \rceil$.
- **Role of False Proposals:** On this event, heavy coefficients have distinct full hashes ($T_s \le \tau^2/1024 < \tau^2 \le d_{s'}^2$ prohibits collision between heavy characters). Buckets with no heavy character are permitted to collide or generate arbitrary proposals because original-target certification in Step 4 screens all proposals against $f$.

### (4) Shifted-Sign Coordinate Recovery (Lines 129–159, 460–486)
- **Decomposition:** For surviving heavy label $v = Bs$, $\mathcal{P}_v(y) = d_s \chi_s(y) + r_s(y)$ with $\|r_s\|_2^2 = T_s \le \tau^2/1024$.
- **Residual Fluctuation:** Both $y$ and $y + e_i$ are marginally uniform in $\mathbb{F}_2^n$. By Chebyshev/Markov:
  $$\Pr_y [|r_s(y)| > \tau/4 \text{ or } |r_s(y + e_i)| > \tau/4] \le \frac{32 T_s}{\tau^2} \le \frac{32}{1024} = \frac{1}{32}$$
- **Empirical Projection Error:** For fixed $y$, Hoeffding at deviation $\tau/4$ gives:
  $$\Pr[|\text{empirical} - \mathcal{P}_v| > \tau/4 \mid y] \le 2 \exp(-M \tau^2 / 32) \le 2 e^{-7} \le 1/64$$
  since $M = \lceil 224 \tau^{-2} \rceil$ and $224/32 = 7$. Union bound over $y$ and $y + e_i$: $\le 1/32$.
- **Sign Product:** Outside failure ($p \le 1/32 + 1/32 = 1/16$), both projections are within $\tau/2$ of $d_s \chi_s$. Since $|d_s| \ge \tau > \tau/2$, both signs are exact:
  $$\operatorname{sign}(\mathcal{P}_v(y)) \operatorname{sign}(\mathcal{P}_v(y + e_i)) = \operatorname{sign}(d_s)^2 \chi_s(y) \chi_s(y + e_i) = 1 \cdot \chi_s(e_i) = (-1)^{s_i}$$
  - Since $\operatorname{sign}(d_s)^2 = 1$, this holds identically for $d_s < 0$ and $d_s > 0$.
  - For the constant character $s = 0$, $s_i = 0$, $(-1)^0 = 1$, which decodes correctly.
- **Majority Vote and Independence:**
  - The $J$ repetitions draw fresh uniform $y$ and $u_1, \dots, u_M$, making them conditionally i.i.d. given $H, B$, and the pruning transcript.
  - For odd $J$, a wrong majority requires $\ge \lceil J/2 \rceil$ vote errors. The probability is at most:
    $$2^J (1/16)^{\lceil J/2 \rceil} \le 2^J \cdot 4^{-(J+1)} \le 2^{-J} \le \frac{\eta}{4 n P}$$
    since $2^J \ge 4nP/\eta$.
  - A union bound over at most $n P$ bits (for the $\le P$ heavy characters) yields total failure $\le \eta/4$. No independence across coordinates or labels is assumed.
  - Final consistency check $B s_v = v$ guarantees surviving indices from distinct labels are strictly distinct.

### (5) Exact List Cap, Failure Budget, and Learner Integration (Lines 580–630)
- **Output Size Cap:** Pruning caps $|\mathcal{C}| \le P$. Each label yields at most one decoded candidate $s_v$. Retained candidates satisfy $B s_v = v$, so distinct labels produce distinct indices. Output size is always $\le P = 64 k^2$.
- **Failure Budget:** Lemma~\ref{lem:search} failure is at most $\eta/4 + \eta/4 + \eta/4 = 3\eta/4$. In the learner, $\eta = \rho = 1/16$, so search failure is $\le 3\rho/4 < \rho$.
- **Staged Union Bound:**
  - Estimator batch error: $\le \rho$
  - Fourier flag count failure: $\le \rho$
  - Hypothesis accuracy (Lemma~\ref{lem:majority}): $\le \rho$
  - Heavy recovery search (Lemma~\ref{lem:search}): $\le 3\rho/4 \le \rho$
  - Simultaneous proposal success probability: $\ge 1 - 4\rho = 3/4$.
- **Contraction & Safety:** On proposal success, omitted heavy energy is $\le W/36$ and unadmitted candidate energy is $\le \alpha^2 W / 64$, ensuring $W(U^+) < W(U)/16$. Intersecting with certification/Gram safety $C \cap G$ (failure $\le 2\beta$) gives safe contraction probability $\ge 3/4 - 2\beta \ge 1/2$. All existing adaptive progress arguments (Proposition~\ref{prop:safety}, Proposition~\ref{prop:contraction}, Theorem~\ref{thm:main}) remain valid without modification.

### (6) Complete Classical Resource Accounting (Lines 161–179, 491–509, 698–718)
- **Parameter Values:** $\tau = 1/(4k)$, $P = 64k^2$, $\eta = \rho = 1/16$, $t = O(\log k)$, $L_0 = O(\log k)$, $N = \widetilde O(k^4)$, $M = O(k^2)$, $J = O(\log(nk))$.
- **Hypothesis Evaluations:**
  - Pruning: $2tN = O(t k^4 \log k) = \widetilde O(k^4)$ calls.
  - Coordinate Recovery: $2nJM = O(n \log(nk) k^2) = \widetilde O(nk^2)$ calls.
  - Each $H$ evaluation takes $\widetilde O(nk + k^3)$ bit operations.
  - Evaluation bit time:
    $$\widetilde O(k^4) \cdot \widetilde O(nk + k^3) + \widetilde O(nk^2) \cdot \widetilde O(nk + k^3) = \widetilde O(nk^5 + k^7 + n^2 k^3 + nk^5) = \widetilde O(n^2 k^3 + nk^5 + k^7)$$
- **Non-Evaluation Classical Processing:**
  - Pruning matrix-vector $B_j^{\mathsf T} u$ and $x$ XOR: $t N \cdot O(nt) = \widetilde O(nk^4)$.
  - Pruning label parities: $t N \cdot 2P(t + h_s) = \widetilde O(k^6)$.
  - Correction matrix-vector $B^{\mathsf T} u$ and $y$ XOR: $n J M \cdot O(nt) = \widetilde O(n^2 k^2)$.
  - Correction label parities: $n J M \cdot P(t + \log M) = \widetilde O(nk^4)$.
  - Vote handling and final $B s_v = v$ hash checks: $n J P \log J + P \cdot O(nt) = \widetilde O(nk^2)$.
  - All non-evaluation terms are strictly dominated by $\widetilde O(n^2 k^3 + nk^5 + k^7)$.
- **Other Learner Costs:** Gram formation $\widetilde O(nk^2 + k^3)$, Bareiss exact refitting $\widetilde O(k^6)$, candidate certification $\widetilde O(nk^3 + k^4)$, and final Booleanity $\widetilde O(nk^2 + k^4)$ all fit within $\widetilde O(n^2 k^3 + nk^5 + k^7)$. Multiplying by $T = O(\log k)$ trials preserves the asymptotic bound.
- **Random Bits (Exact Formula):**
  $$nt + N [tn + t(t+1)/2] + nJ(n + Mt) = \widetilde O(nk^4 + n^2)$$
  Every bit is generated and discarded row-by-row.
- **Live Space:** Hash $O(n \log k)$ bits, counters and accumulators $O(k^2 \log k)$ bits, decoded candidates $O(nk^2)$ bits, Gram determinant workspace $\widetilde O(k^3)$ bits. Total space: $\widetilde O(nk^2 + k^3)$.
- **Tape Determinism:** All sample batches, loop iterations, candidate list sizes, and integer counter widths are bounded a priori. Unsuccessful proposals, singular matrices, or overflows terminate cleanly within these deterministic resource envelopes.

### (7) Attribution and Stated Limits (Lines 230–246, 720–769, 808–813)
- **Attribution:**
  - Prefix-energy search: Kushilevitz–Mansour (KM).
  - Hashed isolation and local character correction: Datta et al. (STACS 2026, Lemma 8 and Claims 12–15).
  - Boolean granularity: Gopalan et al. (GOSSW).
  - Matrix Chernoff and scalar Bernstein bounds: Tropp.
  - Fraction-free Gaussian elimination: Bareiss.
  - Quantum sample benchmarks: Ye ($O(k \log^2 k / \log \log k)$ sample bound), ACLPW ($O(k^{3/2} \log^2 k)$), Caro et al. ($O(k^4 \log(k^2/\delta))$ efficient exact learner).
- **Stated Limitations:**
  - No practical running time or tight constants claimed.
  - Does not improve Ye's logarithmic factor or match the $\Omega(k \log k)$ lower bound.
  - Assumes noiseless supplied quantum examples and target sparsity promise $\le k$.
  - Does not imply a classical simulation of quantum computation or resolve BPP vs. BQP.
  - Acknowledges internal AI-assisted derivation and review; explicitly notes that document builds and automated checks do not constitute formal machine-checked certification or independent human peer review.

---

## 3. Findings and Observations

### Genuine Blockers
*None.* The mathematical derivations, resource bounds, and failure probabilities are rigorous and complete.

### Minor / Advisory Notes

1. **Infeasible Hash Label Handling (Expositional Note — Source line 433 vs. 460):**
   - *Observation:* Line 433 notes that bucket identities hold for infeasible labels $v \notin \operatorname{image}(B)$ (where the true energy is identically $0$). On rare random fluctuations, an infeasible label could survive pruning into $\mathcal{C}$.
   - *Resolution in Text:* Line 460 specifies: *"Finally discard $s_v$ if $Bs_v \ne v$, and return the remaining indices."* Because an infeasible label has no preimage under $B$, whatever decoded candidate $s_v$ is proposed will necessarily satisfy $B s_v \ne v$ and be discarded with certainty. This is fully sound; no change is required.

2. **Evaluation Cost Summation (Editorial Note — Source line 705–707):**
   - *Observation:* The evaluation cost is listed as $\widetilde O(nk^5 + k^7 + n^2 k^3 + nk^5)$. The term $nk^5$ appears twice, corresponding to the two separate products $2tN \times nk$ and $2nJM \times k^3$.
   - *Resolution in Text:* Line 712 correctly consolidates all terms into $\widetilde O(n^2 k^3 + nk^5 + k^7)$. The explicit breakdown is mathematically transparent and harmless.

3. **Verification of $M \ge P$ Condition (Source line 509):**
   - *Observation:* Line 509 notes that decoded-bit storage scans fit the correction bound because $M \ge P$.
   - *Confirmation:* $P = 64k^2$ and $M = 3584k^2$; since $3584 \ge 64$, $M \ge P$ holds strictly for all $k \ge 1$ with a factor of $56$ slack.

---

## 4. Final Disposition

The v0.4.0 decoder modification is mathematically valid, correctly integrated, and establishes the claimed $\widetilde O(n^2 k^3 + n k^5 + k^7)$ classical bit-time complexity without weakening any previously established guarantees.

**Final Verdict: GO WITH NOTES**
