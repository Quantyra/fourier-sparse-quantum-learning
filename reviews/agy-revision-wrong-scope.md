# Final Manuscript Review Report

**Manuscript Title:** *Polynomial-Time Exact Learning of Fourier-Sparse Boolean Functions from Nearly Linear Quantum Samples*  
**Author:** Daniel Fredriksen (Quantyra Inc.)  
**Baseline Commit:** `69dfe76e30a0e80ae82265031f5e5b408a3d9342`  
**Review Scope:** Adversarial AI audit, single-packet offline verification (`packet.txt`)  

---

## 1. Verdict

### **GO WITH NOTES** (Preprint Ready)

The proof rigorously demonstrates exact representation recovery for every $k$-Fourier-sparse Boolean function $f: \mathbb{F}_2^n \to \{-1, 1\}$ using $O(k \log^3(2k))$ uniform quantum examples, with classical bit-time $\widetilde{O}(n^2 k^7 + n k^9)$ and live working space $\widetilde{O}(n k^2 + k^3)$. No fatal mathematical flaws, circularities, or ungrounded leaps exist. The core argument is sound, constructive, and completely specified.

---

## 2. Findings and Precise Technical Notes

* **Finding 1 (Low / Minor Clarification) — Partition Convexity in Lemma 6 (Bias Bound)**  
  * **Location:** Lemma 6, lines 207 and 218–219 ($\norm{h-f}_2^2 \le 36\varepsilon^2 e^2$).  
  * **Analysis:** Frequencies in $S$ partition into passing ($k_1$) and failing ($k_2$) subsets ($k_1 + k_2 = |S| \le k$). Passing frequencies incur squared error at most $\frac{9}{4}\Delta^2$. Failing frequencies satisfy $|c_s| \le t + \Delta \le (2\sqrt{6}+1)\Delta \approx 5.899\Delta < 6\Delta$, contributing at most $(2\sqrt{6}+1)^2\Delta^2 \le 34.8\Delta^2$. Because $\max\{9/4, 34.8\} < 36$, any partition satisfies:
    $$\sum_{s \in S_{\text{pass}}} \left(\frac{c_s^2}{\widetilde c_s}-c_s\right)^2 + \sum_{s \in S_{\text{fail}}} c_s^2 \le 34.8 k \Delta^2 < 36 k \Delta^2 = 36\varepsilon^2 e^2.$$  
  * **Repair:** Add a brief parenthetical noting that $\max\{9/4, (2\sqrt{6}+1)^2\} \le 36$ bounds the combined sum over all $|S| \le k$ terms.

* **Finding 2 (Low / Precision Clarification) — Centered Bound in Lemma 2**  
  * **Location:** Lemma 2, line 106 ($|r(X)\chi_s(X) - \mathbb{E}[r(X)\chi_s(X)]| \le 3\sqrt{k}e$).  
  * **Analysis:** Because $|\operatorname{supp}(\widehat r)| \le 2k$, $\norm{r}_\infty \le \sqrt{2k}e$. By the triangle inequality, the centered deviation is at most $(\sqrt{2k}+1)e = (\sqrt{2} + 1/\sqrt{k})\sqrt{k}e \le (\sqrt{2}+1)\sqrt{k}e \approx 2.414\sqrt{k}e \le 3\sqrt{k}e$ for all $k \ge 1$.  
  * **Repair:** Explicitly state that $k \ge 1$ gives $(\sqrt{2k}+1)e \le 3\sqrt{k}e$.

* **Finding 3 (Informational / Implementation) — Integer Sample Count Ceiling**  
  * **Location:** Section 5, line 260.  
  * **Analysis:** Replacing $\ln z$ by $\lceil\log_2 z\rceil$ strictly increases sample counts ($\log_2 z \approx 1.44 \ln z > \ln z$ for $z > 1$), preserving all concentration tail bounds while ensuring deterministic integer sizing without floating-point errors.  
  * **Repair:** None required; the design is mathematically sound.

---

## 3. Audit of Core Mathematical Arguments and Constants

1. **Granularity & Absorption:** By Gopalan et al. (GOSSW 2011, Theorem 8.1), non-zero Fourier coefficients satisfy $|c_s| \ge 1/k$ for all $k \ge 1$ (including $k=1$ parities). Thus, positive residual energy satisfies $W(U) \ge 1/k^2$. The geometric contraction guarantees $W(U_T) < 16^{-T} \le \frac{1}{16k^4} < \frac{1}{k^2}$, which forces $W(U_T) = 0$ exactly, avoiding asymptotic residual tails.
2. **Adaptive Refitting via Full-Support Matrix Chernoff (Lemma 4):** A fresh batch of $q_c \ge 300(k+1)\ln\frac{2(k+1)}{\beta}$ labels guarantees that the empirical Gram matrix on the fixed support $S_0 = S \cup \{0\}$ satisfies $\norm{q_c^{-1}A_{S_0}^\mathsf{T}A_{S_0} - I_{|S_0|}}_{\text{op}} \le 1/10$ with probability $\ge 1-\beta$. Because this event is defined on $S_0$ prior to subset selection, it holds uniformly for all submatrices $U \subseteq S$. The data-dependent archive $U^+$ selected from this batch is therefore rigorously controlled without requiring a union bound over $2^k$ subsets.
3. **Contraction Calculation (Proposition 8):** Frequencies omitted from search have energy at most $\frac{16}{9}\norm{H-f}_2^2 \le \frac{16}{9}(W/64) = W/36$. Frequencies passing search but rejected by certificate have energy at most $16\gamma^2 e^2 \le 16(1/32)^2 \alpha^2 W = \frac{41}{2592}W$ (where $\alpha^2 = 82/81$). The total contraction:
   $$W(U^+) \le \left(\frac{1}{36} + \frac{41}{2592}\right)W = \frac{113}{2592}W \approx 0.0436 W < \frac{W}{16} = 0.0625 W.$$
4. **Majority Exceptional-Set Integration (Lemma 7):** On bad points $A = \{x : |h(x)-f(x)| > 1/2\}$ (measure $\le 4\norm{h-f}_2^2$), error is capped at 4 because outputs are Boolean. On good points, Chebyshev gives group sign-error $\le 1/16$, and majority failure is $\le 2^{-g}$. Integrating yields $\mathbb{E}\norm{H-f}_2^2 \le 576\varepsilon^2 e^2 + 4 \cdot 2^{-g} \le \frac{\beta W}{64}$, yielding success by Markov.
5. **Exact Arithmetic & Polynomial Trajectory:** Determinant numerators and denominators have bit-length $b_a = O(k\log(kq_c)) = \widetilde{O}(k)$ by Hadamard's bound. Clearing denominators across at most $k$ inverse weights requires a product of bit-length $\widetilde{O}(k^2)$. Evaluating $H(x)$ takes $\widetilde{O}(nk + k^3)$ bit operations. Over $O(nk^6\log(nk/\beta))$ evaluations across $T$ rounds, the total bit-time is $\widetilde{O}(n^2 k^7 + n k^9)$ and live space is $\widetilde{O}(nk^2 + k^3)$ on every tape.

---

## 4. Scope, Access Model, and Literature Boundaries

* **Target Access:** Exclusively uniform quantum examples $|\psi_f\rangle$. Target evaluations/queries are never made. Kushilevitz–Mansour prefix search queries the known, stored circuit $H$, never $f$.
* **Attribution:** The text clearly delineates prior work: Ye ($O(k\log^2 k/\log\log k)$ sample bound, non-constructive decoding), Caro et al. ($O(k^4\log(k^2/\delta))$ polynomial-time learner), ACLPW ($\Omega(k\log k)$ lower bound), GOSSW, KM, and Tropp. The claim is strictly the simultaneous near-linear sample and fixed-polynomial runtime guarantee.
* **Review Boundary:** Conducted strictly from `packet.txt` without external file browsing or online queries. Tool disclosure (OpenAI Codex) is appropriately stated.

---

## 5. Blocker Assessment

**No blockers remain.** All checks, probability bounds, and arithmetic constraints hold. The manuscript is mathematically complete and recommended for preprint dissemination.
