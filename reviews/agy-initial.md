# Substantive Mathematical Review Report

**Manuscript Title:** *Polynomial-Time Exact Learning of Fourier-Sparse Boolean Functions from Nearly Linear Quantum Samples*  
**Author:** Daniel Fredriksen (Quantyra Inc.)  
**Baseline Commit:** `69dfe76e30a0e80ae82265031f5e5b408a3d9342`  
**Review Mode:** Adversarial AI Mathematical & Algorithmic Audit (Internal, Offline, Single-Packet)  
**Date:** November 10, 2026  

---

## 1. Verdict

### **GO WITH NOTES** (Preprint Ready)

The manuscript presents a complete, mathematically coherent, and self-contained proof establishing that every $k$-Fourier-sparse Boolean function $f: \mathbb{F}_2^n \to \{-1, 1\}$ can be exactly reconstructed with probability at least $2/3$ using $O(k \log^3(2k))$ independent uniform quantum examples and fixed-polynomial classical bit-time $\widetilde{O}(n^2 k^7 + n k^9)$ and live working space $\widetilde{O}(n k^2 + k^3)$. 

No fatal mathematical flaws or unfillable gaps were identified. Every intermediate lemma, numerical constant, probability bound, rational denominator bit-length, and resource cap was explicitly tracked and verified. A few minor non-fatal pedagogical clarifications are noted below to maximize rigor and transparency.

---

## 2. Findings and Detailed Mathematical Assessment

### Finding 1 (Severity: Low / Pedagogical Clarification) — Partition Accounting in Lemma 6 (Bias Bound)
* **Location:** Lemma 6, lines 207 and 218–219.
* **Text:** $\norm{h-f}_2^2 \le 36\varepsilon^2 e^2$.
* **Analysis:** In the proof, Fourier frequencies in $S$ are partitioned into those that pass the cutoff ($S_{\text{pass}}$) and those that fail ($S_{\text{fail}}$). Let $k_1 = |S_{\text{pass}}|$ and $k_2 = |S_{\text{fail}}|$, with $k_1 + k_2 = |S| \le k$.
  - For $s \in S_{\text{pass}}$, the coefficient error is at most $\frac{3}{2}\Delta$, contributing at most $k_1 \cdot \frac{9}{4}\Delta^2$.
  - For $s \in S_{\text{fail}}$, $|c_s| \le t + \Delta \le (2\sqrt{6}+1)\Delta \approx 5.899\Delta < 6\Delta$, contributing at most $k_2 \cdot (2\sqrt{6}+1)^2 \Delta^2 \le 34.8 k_2 \Delta^2$.
  - Because $\frac{9}{4} \le (2\sqrt{6}+1)^2 < 34.8 < 36$, the convex combination across any partition $k_1 + k_2 \le k$ is bounded by:
    $$\sum_{s \in S_{\text{pass}}} \left(\frac{c_s^2}{\widetilde c_s}-c_s\right)^2 + \sum_{s \in S_{\text{fail}}} c_s^2 \le \max\left\{\frac{9}{4}, 34.8\right\} k \Delta^2 < 36 k \Delta^2 = 36 \varepsilon^2 e^2.$$
* **Proposed Repair:** Briefly note in line 219 that because $\max\{9/4, (2\sqrt{6}+1)^2\} \le 36$ and $|S_{\text{pass}}| + |S_{\text{fail}}| \le k$, the sum over all frequencies in $S$ is bounded by $36 k \Delta^2$.

---

### Finding 2 (Severity: Low / Precision Clarification) — Scalar Bernstein Centered Bound in Lemma 2
* **Location:** Lemma 2, line 106.
* **Text:** "Each $r(X)\chi_s(X)$ has variance at most $e^2$ and centered absolute bound at most $3\sqrt{k}e$."
* **Analysis:** $r$ is supported on at most $2k$ terms, so $\norm{r}_\infty \le \sqrt{2k} e$. Then $|r(X)\chi_s(X)| \le \sqrt{2k}e$ and $|\mathbb{E}[r(X)\chi_s(X)]| = |\widehat{r}(s)| \le e$. By the triangle inequality:
  $$|r(X)\chi_s(X) - \mathbb{E}[r(X)\chi_s(X)]| \le (\sqrt{2k} + 1) e = \left(\sqrt{2} + \frac{1}{\sqrt{k}}\right)\sqrt{k}e.$$
  For $k \ge 1$, $\sqrt{2} + 1/\sqrt{k} \le \sqrt{2} + 1 \approx 2.414 \le 3$.
* **Proposed Repair:** State explicitly that $(\sqrt{2k}+1)e \le 3\sqrt{k}e$ holds for all $k \ge 1$.

---

### Finding 3 (Severity: Informational / Notation) — Sample Count Rounding Convention
* **Location:** Section 5, line 260.
* **Text:** "replace each $\ln z$ in a sample count by $\lceil\log_2 z\rceil$."
* **Analysis:** Since $\log_2 z = \frac{\ln z}{\ln 2} \approx 1.4427 \ln z > \ln z$ for $z > 1$, replacing $\ln z$ by $\lceil\log_2 z\rceil$ strictly increases the sample counts, ensuring all concentration inequalities continue to hold while enabling exact integer thresholding without transcendental floating-point approximations.
* **Proposed Repair:** None required; the design is completely sound.

---

## 3. Substantive Mathematical Audit of the Core Argument

### A. Boolean Granularity and Support Size
* **Conditioning:** $f: \mathbb{F}_2^n \to \{-1, 1\}$ with $|S| \le k$ and $1 \le k \le 2^n$.
* **Minimum Non-zero Magnitude:** By Gopalan et al. (GOSSW 2011, Theorem 8.1), for sparsity $s_0 > 1$, every non-zero Fourier coefficient is an integer multiple of $2^{1 - \lfloor \log_2 s_0 \rfloor} \ge 2/s_0 \ge 2/k > 1/k$. For $s_0 = 1$, $f = \pm \chi_s$, so $|c_s| = 1 \ge 1/k$.
* **Lower Bound on Residual Energy:** If $W(U) = \sum_{s \in S \setminus U} c_s^2 > 0$, then $S \setminus U$ contains at least one frequency, implying $W(U) \ge \min_{s \in S} c_s^2 \ge 1/k^2$. This guarantees that whenever $W(U) < 1/k^2$, we must have $W(U) = 0$ exactly.

---

### B. Fresh Residual Estimation (Lemma 2)
* **Sample Count:** $q \ge 32 k \varepsilon^{-2} \ln \frac{4(P+1)}{\beta}$.
* **Coefficient Estimator:** $z_s = q^{-1} \sum_\ell r(X_\ell)\chi_s(X_\ell)$.
  - Variance $\sigma^2 \le e^2$, bound $B \le 3\sqrt{k}e$, deviation $\eta = \varepsilon e / \sqrt{k}$.
  - Bernstein denominator: $2\sigma^2 + \frac{2}{3}B\eta \le 2e^2 + 2\varepsilon e^2 \le 4e^2$ (since $\varepsilon \le 1$).
  - Exponent: $\frac{q \eta^2}{4e^2} = \frac{q \varepsilon^2}{4k} \ge 8 \ln \frac{4(P+1)}{\beta}$.
  - Two-sided tail: $2 \exp\left(-\frac{q\varepsilon^2}{4k}\right) \le \frac{\beta}{2(P+1)}$.
* **Variance Estimator:** $v = q^{-1}\sum_\ell r(X_\ell)^2$.
  - Centered bound $|r(X)^2 - e^2| \le 3k e^2$, variance $\operatorname{Var}(r(X)^2) \le 3k e^4$, deviation $\eta_v = e^2/2$.
  - Bernstein denominator: $2(3k e^4) + \frac{2}{3}(3k e^2)(e^2/2) = 7k e^4$.
  - Exponent: $\frac{q(e^4/4)}{7k e^4} = \frac{q}{28k} \ge \frac{32}{28}\varepsilon^{-2} \ln \frac{4(P+1)}{\beta} > \ln \frac{4(P+1)}{\beta}$.
  - Two-sided tail: $2 \exp\left(-\frac{q}{28k}\right) \le \frac{\beta}{2(P+1)}$.
* **Union Bound:** $(P \text{ coefficients}) + (1 \text{ variance}) = P+1$ events, total failure $\le (P+1) \cdot \frac{\beta}{2(P+1)} = \frac{\beta}{2} < \beta$. Exact for $e = 0$.

---

### C. Original-Coefficient Certification (Lemma 3)
* **Test Rule:** For $s \in L \setminus U$, admit if $z_s^2 > 4\varepsilon^2 v / k$.
* **Threshold Range:** Because $e^2/2 \le v \le 3e^2/2$, the threshold $T = 4\varepsilon^2 v / k$ satisfies:
  $$\frac{2\varepsilon^2 e^2}{k} \le T \le \frac{6\varepsilon^2 e^2}{k} \implies \sqrt{T} \in \left[\sqrt{2}\frac{\varepsilon e}{\sqrt{k}}, \sqrt{6}\frac{\varepsilon e}{\sqrt{k}}\right].$$
* **Soundness ($s \notin S$):** $c_s = 0$, so $|z_s| \le \frac{\varepsilon e}{\sqrt{k}} \implies z_s^2 \le \frac{\varepsilon^2 e^2}{k} < \frac{2\varepsilon^2 e^2}{k} \le T$. No false frequencies admitted.
* **Completeness ($s \in S \setminus U$ with $|c_s| > 4\varepsilon e/\sqrt{k}$):**
  $$|z_s| \ge |c_s| - |z_s - c_s| > \frac{4\varepsilon e}{\sqrt{k}} - \frac{\varepsilon e}{\sqrt{k}} = \frac{3\varepsilon e}{\sqrt{k}} \implies z_s^2 > \frac{9\varepsilon^2 e^2}{k} > \frac{6\varepsilon^2 e^2}{k} \ge T.$$
  Every heavy true frequency is admitted.

---

### D. Adaptive Refitting via Full-Support Matrix Chernoff (Lemma 4)
* **Full-Support Event:** Let $S_0 = S \cup \{0\}$, with $p = |S_0| \le k + 1$. Define $v(x) = (\chi_s(x))_{s \in S_0}$. Then $\mathbb{E}[v(X)v(X)^\mathsf{T}] = I_p$ and $\norm{v(X)}_2^2 = p$.
* **Matrix Chernoff (Tropp 2012, Corollary 5.2):** For $\delta = 1/10$ and $q \ge 300(k+1)\ln\frac{2(k+1)}{\beta}$:
  $$\Pr\left[\norm{q^{-1} A_{S_0}^\mathsf{T} A_{S_0} - I_p}_{\text{op}} > \frac{1}{10}\right] \le 2p \exp\left(-\frac{q(1/10)^2}{3p}\right) \le \beta.$$
* **Uniformity over all $U \subseteq S$:** Any principal submatrix and off-diagonal block satisfies:
  $$\norm{q^{-1} A_U^\mathsf{T} A_U - I_{|U|}}_{\text{op}} \le \frac{1}{10} \implies \norm{(q^{-1} A_U^\mathsf{T} A_U)^{-1}}_{\text{op}} \le \frac{1}{1 - 1/10} = \frac{10}{9},$$
  $$\norm{q^{-1} A_U^\mathsf{T} A_{S \setminus U}}_{\text{op}} \le \frac{1}{10}.$$
* **Normal Equations Bound:**
  $$\norm{a_U - c_U}_2 \le \norm{(q^{-1}A_U^\mathsf{T}A_U)^{-1}}_{\text{op}} \norm{q^{-1}A_U^\mathsf{T}A_V}_{\text{op}} \norm{c_V}_2 \le \frac{10}{9} \cdot \frac{1}{10} \sqrt{W(U)} = \frac{\sqrt{W(U)}}{9}.$$
* **Residual Contraction and Cauchy-Schwarz:**
  - $\norm{f-a}_2^2 = \norm{f - P_U f}_2^2 + \norm{P_U f - a}_2^2 \le W(U) + \frac{W(U)}{81} = \frac{82}{81} W(U) = \alpha^2 W(U)$.
  - By 2D Cauchy-Schwarz on $(1, 1/9)$ and $(\sqrt{1-W}, \sqrt{W})$:
    $$\norm{a}_2 \le \sqrt{1-W(U)} + \frac{\sqrt{W(U)}}{9} \le \sqrt{1 + \frac{1}{81}} = \alpha = \sqrt{\frac{82}{81}} < \sqrt{2} \implies \norm{a}_2^2 < 2.$$
* **Reusing the Batch:** Because the matrix concentration event is defined on the fixed unknown true support $S_0$, it holds simultaneously for all submatrices. The data-dependent selection of $U^+$ from this batch is therefore rigorously controlled without requiring a union bound over $2^k$ subsets.

---

### E. Heavy-Spectrum Classical Search on Stored $H$ (Lemma 5)
* **Bucket Parseval Identity:** For $u \in \mathbb{F}_2^j$:
  $$E_u = \sum_{v \in \mathbb{F}_2^{n-j}} \widehat{H}(u, v)^2 = \mathbb{E}_z \left(\mathbb{E}_x H(x, z)\chi_u(x)\right)^2 = \mathbb{E}_{z, x, y} H(x, z)H(y, z)\chi_u(x+y).$$
* **Hoeffding Bound:** Each summand is in $[-1, 1]$ (width 2). For $N = \lceil 32\tau^{-4} \ln \frac{4nP}{\beta}\rceil$ samples:
  $$\Pr[|\widetilde E_u - E_u| > \tau^2/4] \le 2 \exp\left(-\frac{2 N (\tau^2/4)^2}{4}\right) = 2 \exp\left(-\frac{N\tau^4}{32}\right) \le \frac{\beta}{2nP}.$$
* **Tree Invariants:** Total tests $\le 2nP$. Union bound over all tests gives total error $\le \beta$.
  - If $\widehat{H}(s)^2 \ge \tau^2$, every ancestor $u$ has $E_u \ge \tau^2$, so $\widetilde E_u \ge 3\tau^2/4$ and survives.
  - Every retained bucket has $E_u \ge \tau^2/2$. Disjoint buckets at depth $j$ sum to $\norm{H}_2^2 = 1$, so at most $2/\tau^2 \le P$ prefixes survive at any depth. The abort cap never fires on the good event.

---

### F. Queryable Hypothesis Construction and Majority Integration (Lemmas 6 and 7)
* **Uniform Estimation on True Support $S$:** Lemma 2 is applied to $D = S$ (size $|S| \le k$). This event holds with probability at least $1 - \beta$. Because Fourier measurements of $|\psi_f\rangle$ only yield frequencies in $S$, the algorithm only ever queries $\widetilde c_s$ for $s \in S$.
* **Cutoff Properties:** $t = 4\varepsilon\sqrt{v/k} \in [2\sqrt{2}\Delta, 2\sqrt{6}\Delta] \subset [2\sqrt{2}\Delta, 5\Delta]$.
  - If $s$ passes: $|c_s/\widetilde c_s| \le 1 + \Delta/t \le 1 + 1/(2\sqrt{2}) < 3/2$, and $\sgn(\widetilde c_s) = \sgn(c_s)$.
  - If $s$ fails: $|c_s| \le t + \Delta < 6\Delta$.
* **Variance of Group Average:** For $m = 144k$:
  $$\operatorname{Var}(Q_i(x)) = \frac{1}{m} \sum_{s \in S, \text{ passes}} \frac{c_s^2}{\widetilde c_s^2} \le \frac{1}{m} k \left(\frac{3}{2}\right)^2 = \frac{9k}{4m} = \frac{9k}{4(144k)} = \frac{1}{64}.$$
* **Majority Error Integration:**
  - Let $A = \{x : |h(x) - f(x)| > 1/2\}$. Measure $\mu(A) \le 4\norm{h-f}_2^2$.
  - Outside $A$, $|h(x)| \ge 1/2$ with correct sign. By Chebyshev, $\Pr[\sgn Q_i(x) \ne f(x)] \le \frac{1/64}{(1/2)^2} = \frac{1}{16}$.
  - Majority of $g$ independent groups has error $\le 2^g (1/16)^{g/2} = 2^{-g}$.
  - Integrating over $\mathbb{F}_2^n$:
    $$\mathbb{E}_{\text{groups}} \norm{H-f}_2^2 \le 4 \mu(A) + 4 \cdot 2^{-g} \le 16 \norm{h-f}_2^2 + 4 \cdot 2^{-g} \le 576 \varepsilon^2 e^2 + 4 \cdot 2^{-g}.$$
* **Markov Bound:**
  - $576 \varepsilon^2 e^2 \le 576 \left(\frac{\beta}{262144}\right) (2W) = \frac{9}{2048}\beta W \le \frac{\beta W}{128}$.
  - $4 \cdot 2^{-g} \le 4 \left(\frac{\beta}{512 k^2}\right) \le \frac{\beta W}{128}$ (since $W \ge 1/k^2$).
  - Thus $\mathbb{E}[\norm{H-f}_2^2] \le \frac{\beta W}{64} \implies \Pr\left[\norm{H-f}_2^2 > \frac{W}{64}\right] \le \beta$.

---

### G. Uniform Energy Contraction (Proposition 8)
* **Omitted from $L$:** $|\widehat H(s)| < \tau = \frac{1}{4k} \le \frac{|c_s|}{4} \implies c_s^2 \le \frac{16}{9}(c_s - \widehat H(s))^2$.
  $$\sum_{s \in S \setminus L} c_s^2 \le \frac{16}{9} \norm{H-f}_2^2 \le \frac{16}{9}\left(\frac{W}{64}\right) = \frac{W}{36}.$$
* **Proposed but Not Admitted:** $|c_s| \le 4\gamma e / \sqrt{k}$ with $\gamma = 1/32$.
  $$\sum_{s \in (S \cap L) \setminus U^+} c_s^2 \le k \left(\frac{4\gamma e}{\sqrt{k}}\right)^2 = 16 \gamma^2 e^2 \le 16\left(\frac{1}{1024}\right)\alpha^2 W = \frac{\alpha^2 W}{64}.$$
* **Total New Residual Energy:**
  $$W(U^+) \le \left(\frac{1}{36} + \frac{\alpha^2}{64}\right) W = \left(\frac{1}{36} + \frac{82}{81 \cdot 64}\right)W = \left(\frac{1}{36} + \frac{41}{2592}\right)W = \frac{113}{2592} W \approx 0.0436 W < \frac{W}{16} = 0.0625 W.$$
* **Round Convergence:** After $T = \lceil \log_2(2k) \rceil$ rounds, $W(U_T) < 16^{-T} \le \frac{1}{16k^4} < \frac{1}{k^2}$, forcing $W(U_T) = 0$ and $U_T = S$ identically.

---

### H. Exact Arithmetic and Finite Resource Bounds (Section 6)
* **Sample Count:** Total copies $= T(q_e + 4gm + q_c) + \lceil 2k\ln 100\rceil = O(k \log^3(2k))$.
* **Normal Equations Bit-Length:** Gram matrix $A_U^\mathsf{T} A_U$ has dimension $\le k \times k$, entries in $[-q_c, q_c]$. By Hadamard's bound, determinant bit-length is $b_a = O(k \log(2k q_c)) = \widetilde O(k)$.
* **Common Denominator for $H$:** Nonzero estimates $\widetilde c_s = N_s/D$ have bit-length $\widetilde O(k)$. The product $\Pi = \prod_{s \text{ passes}} |N_s|$ clearing denominators has bit-length at most $k \cdot \widetilde O(k) = \widetilde O(k^2)$.
* **Evaluation Cost of $H$:**
  - Evaluating parity $\chi_s(x)$ for $\le k$ distinct indices: $O(nk)$ bits.
  - Summing $\le k$ integers of bit-length $\widetilde O(k^2)$: $k \cdot \widetilde O(k^2) = \widetilde O(k^3)$ bits.
  - Group signs and majority over $g = O(\log k)$ groups: $\widetilde O(nk + k^3)$ bit operations per query to $H$.
* **Classical Bit-Time:**
  - Search tests per round: $2nP = O(nk^2)$.
  - Samples per test: $N = O(k^4 \log(nk/\beta))$.
  - Evaluations of $H$ per round: $O(nk^6 \log(nk/\beta))$.
  - Bit-time per round: $O(nk^6) \times \widetilde O(nk + k^3) = \widetilde O(n^2 k^7 + n k^9)$.
  - Charged over $T = O(\log k)$ rounds: $\widetilde O(n^2 k^7 + n k^9)$.
* **Live Space:** Prefix tree storage $O(nk^2)$, batch rows $\widetilde O(nk)$, weights and Gram matrix $\widetilde O(k^3)$, candidate accumulators $\widetilde O(k^3)$, giving $\widetilde O(nk^2 + k^3)$ live bits.

---

## 4. Claims, Scope, and Literature Boundaries

### Scope and Boundaries
1. **Access Model:** Independent uniform quantum examples $|\psi_f\rangle = 2^{-n/2}\sum_x |x\rangle|b_f(x)\rangle$. Each copy is measured individually (computational or Hadamard basis). No multi-copy coherent operations, no state-preparation oracle, and no queries to $f$ are used.
2. **Attribution and Novelty:**
   - **Ye (arXiv:2610.17648v1, Oct 2026):** Proves an $O(k \log^2 k / \log\log k)$ sample bound using grouped dictionaries, but does not give a polynomial decoding time. The manuscript explicitly acknowledges this smaller sample bound and positions its contribution strictly as supplying the polynomial computational guarantee.
   - **Caro et al. (ITCS 2024 / arXiv:2306.04843v2):** Efficient exact learner with $O(k^4 \log(k^2/\delta))$ copies. The manuscript correctly notes that polynomial-time learning alone is not novel.
   - **Arunachalam et al. (ACLPW 2021):** Benchmark bounds $O(k^{3/2}\log^2 k)$ and $\Omega(k\log k)$.
   - **Gopalan et al. (GOSSW 2011):** Boolean granularity $|c_s| \ge 1/k$.
   - **Tropp (2012):** Matrix Chernoff and scalar Bernstein bounds.
   - **Kushilevitz–Mansour (KM 1993):** Prefix-energy Fourier search applied strictly to the internally constructed hypothesis $H$, never to the unknown target $f$.
3. **Disclosure:** Discloses AI assistance (OpenAI Codex) and internal AI review in accordance with ethical standards.
4. **Limits of Offline Verification:** This review was conducted strictly from the contents of `packet.txt` without access to external web services, local build artifacts, or other repository files. The mathematical properties of external citations (GOSSW Theorem 8.1, Tropp Corollary 5.2) were audited against their known mathematical formulations recorded in the packet.

---

## 5. Blocker Assessment

**No blockers remain.** The theorem statement, analytic lemmas, probabilistic arguments, and explicit computational resource caps are sound, consistent, and ready for publication in preprint form.
