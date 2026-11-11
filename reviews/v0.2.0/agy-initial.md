# Manuscript Review Report: Version 0.2.0

**Target Manuscript**: *Polynomial-Time Exact Learning of Fourier-Sparse Boolean Functions from Nearly Linear Quantum Samples*  
**Author**: Daniel Fredriksen (Quantyra Inc.)  
**Source SHA-256**: `ac1d730256c61861930fd63beed806e23aff08c82a1dd8c809e93a5b085321ea`  
**Review Type**: Independent Adversarial Mathematical & Algorithmic Audit  
**Verdict**: **GO WITH NOTES**

---

## 1. Executive Summary & Audit Scope

This adversarial audit evaluates the revision of the manuscript to version 0.2.0. The central architectural revision over version 0.1.0 is the decoupling of candidate proposal confidence from archive safety: by accepting constant proposal confidence ($\rho = 1/16$) while maintaining high archive safety ($\beta = 1/(200T)$ per round), and establishing that unsuccessful trials do not degrade the archive, the quantum sample complexity is improved from $O(k\log^3(2k))$ to $O(k\log^2(2k))$.

The audit specifically scrutinized:
1. **Arbitrary-proposal safety**: whether adversarial, malformed, or empty proposals can induce false admissions, singular systems, or archive growth beyond $k$.
2. **Shared-batch certification and Gram refitting**: whether using a single batch of $q_c$ labels for both admission certification and empirical Gram refitting introduces illicit dependencies or conditioning bias.
3. **Adaptive progress without conditioning on future safety**: whether the dummy-indicator construction rigorously bounds the trial count without conditioning the underlying probability space on future non-failure events.
4. **Exact termination via Boolean granularity**: whether the contraction factor terminates at exactly $W=0$ without runtime dependence on uncomputable quantities.
5. **Every-tape resource bounds**: whether arithmetic bit lengths, prefix caps, and abort branches guarantee polynomial runtime and space on all executions (including failed/malicious proposals).
6. **Endpoints & edge cases**: behavior at $k=1$, absorbing behavior at $W=0$, and abort handling.
7. **Attribution & prior art boundaries**: accuracy of comparisons with Ye, Arunachalam et al., Caro et al., GOSSW, KM, and Tropp.

**Finding**: The mathematical structure of the revision is sound. The decoupling of proposal confidence from archive safety is rigorously executed. The dummy-indicator martingale argument is mathematically valid and does not condition on future safety. All constants, tail bounds, and arithmetic exponents check out. A small number of non-blocking pedagogical clarifications and notation notes are documented below.

---

## 2. Audit of the Core Changed Mechanism

### 2.1 Arbitrary-Proposal Safety (Proposition 1)
In version 0.2.0, the hypothesis search in Step 3 returns a candidate list $L$ with constant confidence $\rho = 1/16$. An adversarial or failed search may yield $L = \varnothing$, a list of spurious indices outside the true support $S$, or an arbitrary set of size up to $P = 64k^2$.

**Audit Verification**:
- **Candidate isolation**: The candidate list $L$ is fixed *prior* to measuring the fresh certification batch of size $q_c$.
- **False-positive exclusion**: By Lemma 2, on the residual accuracy event $C$, for any $s \in L \setminus U$ with $c_s = 0$, the estimator satisfies $|z_s| \le \varepsilon e / \sqrt{k}$, so $z_s^2 \le \varepsilon^2 e^2 / k$. Because $v \ge e^2 / 2$, the admission threshold satisfies $4\varepsilon^2 v / k \ge 2\varepsilon^2 e^2 / k$. Thus $z_s^2 < 4\varepsilon^2 v / k$ strictly holds (for $e > 0$; for $e=0$, all residuals vanish and $0 > 0$ fails). Hence, **no spurious index $s \notin S$ can ever be admitted on event $C$**, irrespective of $L$.
- **Archive size cap**: Because only true indices $s \in S$ can be admitted on event $C$, the updated archive satisfies $U^+ \subseteq S$, ensuring $|U^+| \le |S| \le k$. The abort condition $|U| > k$ cannot trigger.
- **Nonsingularity and refitting stability**: By Lemma 3, the Gram event $G$ is defined over the entire fixed superset $S_0 = S \cup \{0\}$. On event $G$, *every* principal submatrix of the empirical Gram matrix has eigenvalues in $[9/10, 11/10]$. Because $U^+ \subseteq S \subset S_0$, the submatrix $A_{U^+}^\mathsf T A_{U^+}$ is unconditionally nonsingular, and the least-squares fit $a^+$ satisfies $\norm{a^+}_2^2 \le \alpha^2 = 82/81 < 2$. The singular abort and norm abort cannot trigger.
- **Monotonicity**: $U \subseteq U^+ \implies S \setminus U^+ \subseteq S \setminus U \implies W(U^+) \le W(U)$.

The proposition holds unconditionally for any proposal $L$ with $|L| \le P$.

### 2.2 Shared-Batch Certification and Refitting (Step 4)
Step 4 measures a single batch of $q_c$ labels and uses it both to certify candidates in $L \setminus U$ and to refit the coefficients on $U^+$.

**Audit Verification**:
- Event $C$ is the residual concentration event of Lemma 1 applied to the fixed function $r = f - a$ and candidate set $\mathcal D = L \setminus U$, with failure parameter $\beta$.
- Event $G$ is the matrix Chernoff event of Lemma 3 applied to the fixed set $S_0$, with failure parameter $\beta$.
- Both events depend on the same fresh random batch $(X_\ell, f(X_\ell))_{\ell=1}^{q_c}$. Crucially, the proof **does not assume independence** between $C$ and $G$. By a simple union bound, $\Pr(C^c \cup G^c) \le \Pr(C^c) + \Pr(G^c) \le 2\beta$.
- Because event $G$ guarantees stability uniformly over all subsets of $S$, the fact that $U^+$ is chosen using the same batch (via the certification test) does not invalidate the operator-norm bounds. This uniform control eliminates circularity.

### 2.3 Dummy Indicators and Conditioning on Future Safety
A classic vulnerability in multi-round adaptive learning proofs is conditioning the entire sample path on a global future safety event $\bigcap_{t=1}^T \text{Safe}_t$, which biases the transition probabilities of earlier rounds.

**Audit Verification of Proof of Theorem 1**:
1. **Safety failure event $B$**: Let $B$ be the event that a safety failure ($C^c$ or $G^c$) occurs at *any* trial $t \in \{1, \ldots, T\}$. By a union bound over rounds, $\Pr(B) \le 2T\beta = 2T \cdot \frac{1}{200T} = 1/100$.
2. **Filtration $\mathcal F_{t-1}$ and indicator definition**: The indicator $I_t$ is defined measurably with respect to the history up to trial $t$:
   - If a safety failure occurred at any prior round $j < t$, or if $W(U_{t-1}) = 0$, set $I_t = 1$ by convention.
   - Otherwise, set $I_t = 1$ if and only if the four proposal events of Proposition 2 and the certification/Gram event $C_t \cap G_t$ all succeed.
   - Unused indicators after termination are set to 1.
3. **Conditional probability lower bound**:
   - If a prior safety failure occurred, $\Pr(I_t = 1 \mid \mathcal F_{t-1}) = 1 \ge 1/2$.
   - If $W(U_{t-1}) = 0$, $\Pr(I_t = 1 \mid \mathcal F_{t-1}) = 1 \ge 1/2$.
   - If no prior safety failure occurred and $W(U_{t-1}) > 0$, the state at the start of trial $t$ satisfies invariant (132). By Proposition 2, the four proposal events succeed with probability $\ge 1 - 4\rho = 3/4$, and $C_t \cap G_t$ fails with probability $\le 2\beta$. Thus $\Pr(I_t = 1 \mid \mathcal F_{t-1}) \ge 3/4 - 2\beta \ge 1/2$ (since $T \ge 8 \implies \beta \le 1/1600$).
   - Therefore, $\Pr(I_t = 1 \mid \mathcal F_{t-1}) \ge 1/2$ holds **unconditionally on future events for every history $\mathcal F_{t-1}$**.
4. **Supermartingale / Markov bound**:
   $$\E\left[2^{-I_t} \mid \mathcal F_{t-1}\right] = 1 - \frac{1}{2}\Pr(I_t=1\mid\mathcal F_{t-1}) \le \frac{3}{4}.$$
   By induction, $\E\left[2^{-Z_T}\right] \le (3/4)^T$. Setting $T = 8\ell$:
   $$\Pr(Z_T < \ell) \le 2^\ell \left(\frac{3}{4}\right)^{8\ell} = \left[2\left(\frac{3}{4}\right)^8\right]^\ell = \left[\frac{6561}{32768}\right]^\ell < \left(\frac{1}{4}\right)^\ell \le \frac{1}{4}.$$
5. **Exact joint probability**:
   On $B^c$, no safety failure occurs. If $Z_T \ge \ell$, there are at least $\ell$ genuine contractions of factor $> 16$, interspersed with nonincreasing safe steps.
   $$\Pr(\text{Success}) \ge \Pr(B^c \cap \{Z_T \ge \ell\}) \ge 1 - \Pr(B) - \Pr(Z_T < \ell) \ge 1 - \frac{1}{100} - \frac{1}{4} = \frac{37}{50} = 0.74 > \frac{2}{3}.$$
The argument is mathematically rigorous, avoids conditioning on the future, and properly bounds the joint success probability.

---

## 3. Worked Mathematical Checks

### 3.1 Scalar Bernstein Application (Lemma 1)
- Let $Y_\ell = r(X_\ell)\chi_s(X_\ell) - \widehat r(s)$.
- Boundedness: $\norm{r}_\infty \le \sqrt{|\supp \widehat r|} \norm{\widehat r}_2 \le \sqrt{2k}e$. Thus $|Y_\ell| \le \sqrt{2k}e + e \le (\sqrt 2 + 1)\sqrt k e < 2.5\sqrt k e \le 3\sqrt k e =: B$.
- Variance: $\E[Y_\ell^2] \le \E[r(X_\ell)^2] = e^2 =: \sigma^2$.
- Deviation $t = \varepsilon e / \sqrt k$.
  $$\sigma^2 + \frac{Bt}{3} \le e^2 + \frac{(3\sqrt k e)(\varepsilon e / \sqrt k)}{3} = e^2(1+\varepsilon) \le 2e^2 \quad (\text{since } \varepsilon \le 1).$$
- Exponent denominator: $2(\sigma^2 + Bt/3) \le 4e^2$.
- Exponent numerator: $q t^2 = q \varepsilon^2 e^2 / k$.
- Ratio: $-qt^2 / (2(\sigma^2 + Bt/3)) \ge -q\varepsilon^2 / (4k)$.
- Tail bound: $2\exp(-q\varepsilon^2 / (4k))$. With $q \ge 32k\varepsilon^{-2}\ln(4(P+1)/\beta)$, the exponent magnitude is at least $8\ln(4(P+1)/\beta)$, giving individual failure $\le 2(4(P+1)/\beta)^{-8} \ll \beta / (2(P+1))$.
- For variance estimator $v$: centered bound $|r(X)^2 - e^2| \le 2ke^2 \le 3ke^2 =: B_v$, variance $\operatorname{Var}(r(X)^2) \le 2ke^4 \le 3ke^4 =: \sigma_v^2$.
- At deviation $t = e^2 / 2$:
  $$2\left(\sigma_v^2 + \frac{B_v t}{3}\right) \le 2\left(3ke^4 + \frac{(3ke^2)(e^2/2)}{3}\right) = 2(3.5 ke^4) = 7ke^4.$$
- Exponent: $-q(e^4/4) / (7ke^4) = -q / (28k)$.
- With $q \ge 32k \varepsilon^{-2} L_0 \ge 32k L_0$ (since $\varepsilon \le 1$), $q/(28k) \ge (32/28)L_0 > L_0$.
- Union bound over $P$ frequencies plus $v$: $(P+1) \cdot 2e^{-L_0} = 2(P+1)\frac{\beta}{4(P+1)} = \beta/2$. **Verified.**

### 3.2 Matrix Chernoff Application (Lemma 3)
- Matrix summands $Y_\ell = \phi(X_\ell)\phi(X_\ell)^\mathsf T$ on $S_0 = S \cup \{0\}$, dimension $p = |S_0| \le k+1$.
- Summands are rank-1 PSD with $\norm{Y_\ell}_{\rm op} = \norm{\phi(X_\ell)}_2^2 = p$.
- Expectation: $\sum_{\ell=1}^q \E Y_\ell = q I_p$.
- By Tropp Corollary 5.2, setting $\delta = 1/10$:
  - Lower tail: exponent $\delta + (1-\delta)\ln(1-\delta) \ge \delta^2/2 = 1/200$.
  - Upper tail: exponent $(1+\delta)\ln(1+\delta) - \delta \ge \delta^2/3 = 1/300$.
  - Sum of tails: $\le 2p \exp(-q\delta^2 / (3p)) = 2p \exp(-q / (300p))$.
- Equating to $\beta$ yields $q \ge 300p \ln(2p/\beta)$, exactly matching equation (129).
- For any $U \subseteq S$, empirical Gram matrix $G_U = q^{-1}A_U^\mathsf T A_U$ has eigenvalues in $[1-\delta, 1+\delta] = [9/10, 11/10]$.
- Operator norm of inverse: $\norm{G_U^{-1}}_{\rm op} \le 10/9$.
- Off-diagonal cross block $q^{-1}A_U^\mathsf T A_V$ (where $V = S \setminus U$) has operator norm $\le \delta = 1/10$ because $U \cap V = \varnothing$.
- Residual coefficient error: $\norm{a_U - c_U}_2 \le (10/9)(1/10)\norm{c_V}_2 = \frac{1}{9}\sqrt{W(U)}$.
- Orthogonality on cube: $\norm{f-a}_2^2 = \norm{P_U f - a}_2^2 + \norm{P_V f}_2^2 \le (1/81 + 1)W(U) = \frac{82}{81}W(U) = \alpha^2 W(U)$.
- Fit norm: $\norm{a}_2 \le \sqrt{1-W(U)} + \frac{\sqrt{W(U)}}{9} \le \sqrt{82/81} = \alpha < \sqrt 2$. **Verified.**

### 3.3 Majority Circuit Bias & Variance (Lemmas 4 & 5)
- Cutoff threshold: $t = 4\varepsilon\sqrt{v/k}$.
  Since $e^2/2 \le v \le 3e^2/2$ and $\Delta = \varepsilon e / \sqrt k$, we have $2\sqrt 2 \Delta \le t \le 2\sqrt 6 \Delta < 5\Delta$.
- Passing frequencies: $|\widetilde c_s| \ge t > 2\sqrt 2 \Delta$. Thus signs of $c_s$ and $\widetilde c_s$ agree, and $|c_s / \widetilde c_s| \le 1 + \Delta / t < 1 + 1/(2\sqrt 2) < 1.36 < 3/2$.
- Passing coefficient error: $|\widehat h(s) - c_s| = |c_s(c_s - \widetilde c_s)/\widetilde c_s| < (3/2)\Delta$.
- Failing frequencies: $|c_s| \le |\widetilde c_s| + \Delta < t + \Delta < 6\Delta$.
- Squared $L_2$ error: $\norm{h-f}_2^2 \le \sum_{s \in S} (6\Delta)^2 = 36 k \Delta^2 = 36\varepsilon^2 e^2$.
- Variance per sample: $\sum_{s \text{ passes}} c_s^2 / \widetilde c_s^2 \le k (3/2)^2 = 9k/4$.
- Variance of group average $Q_i(x)$: $\operatorname{Var}(Q_i(x)) \le \frac{9k}{4m}$. With $m = 144k$, $\operatorname{Var}(Q_i(x)) \le 1/64$.
- Error probability on $A^c = \{x: |h(x)-f(x)| \le 1/2\}$: by Chebyshev, $\Pr[\sgn Q_i(x) \ne f(x)] \le \frac{\operatorname{Var}(Q_i(x))}{(1/2)^2} \le 4(1/64) = 1/16$.
- Group majority error on $A^c$: $2^g (1/16)^{g/2} = 2^{-g}$.
- Expected hypothesis error:
  $$\E\norm{H-f}_2^2 \le 4\mu(A) + 4\cdot 2^{-g} \le 16\norm{h-f}_2^2 + 4\cdot 2^{-g} \le 576\varepsilon^2 e^2 + 4\cdot 2^{-g}.$$
- Bounding by $W/64$:
  - With $e^2 \le \alpha^2 W = (82/81)W < 1.013W$, $576\varepsilon^2 e^2 \le 584\varepsilon^2 W$.
  - With $\varepsilon = 1/2048$, $\varepsilon^2 = 1/4194304$. $584 / 4194304 \approx 0.000139 < \frac{1/16}{128} = \frac{1}{2048} \approx 0.000488$.
  - With $2^g \ge 512k^2 / \rho = 8192k^2$ and $W \ge 1/k^2$, $4\cdot 2^{-g} \le 4 / (8192k^2) = \frac{1}{2048 k^2} \le \frac{\rho W}{128}$.
  - Sum is at most $\frac{\rho W}{64}$. By Markov, $\Pr[\norm{H-f}_2^2 > W/64] \le \rho = 1/16$. **Verified.**

### 3.4 Contraction Factor (Proposition 2)
- Omitted frequencies $s \in S \setminus L$: $|\widehat H(s)| < \tau = 1/(4k)$.
  By granularity, $|c_s| \ge 1/k$, so $|\widehat H(s)| < |c_s|/4 \implies |c_s - \widehat H(s)| > (3/4)|c_s|$.
  $$\sum_{s \in S \setminus L} c_s^2 \le \frac{16}{9}\sum_{s \in S \setminus L}(c_s - \widehat H(s))^2 \le \frac{16}{9}\norm{H-f}_2^2 \le \frac{16}{9}\frac{W}{64} = \frac{W}{36}.$$
- Candidate true frequencies not admitted: $|c_s| \le 4\gamma e / \sqrt k$.
  Total energy: $\le k(16\gamma^2 e^2 / k) = 16\gamma^2 e^2 \le 16(1/32)^2 \alpha^2 W = \frac{\alpha^2}{64}W$.
- Missing energy contraction:
  $$W(U^+) \le \left(\frac{1}{36} + \frac{82/81}{64}\right)W = \left(\frac{1}{36} + \frac{41}{2592}\right)W = \frac{113}{2592}W \approx 0.0436 W < \frac{1}{16}W = 0.0625 W.$$
The factor-16 contraction strictly holds with comfortable slack. **Verified.**

### 3.5 Granularity Exact Termination
- Granularity gives $c_s \ne 0 \implies |c_s| \ge 1/k \implies c_s^2 \ge 1/k^2$.
- Thus $W(U) > 0 \implies W(U) \ge 1/k^2$.
- Number of trials $T = 8\ell$, where $\ell = \lceil \log_2(2k) \rceil$.
- After $\ell$ factor-16 contractions:
  $$W(U_T) < 16^{-\ell} = 2^{-4\ell} \le 2^{-4\log_2(2k)} = \frac{1}{(2k)^4} = \frac{1}{16k^4} < \frac{1}{k^2}.$$
- Therefore $W(U_T) < 1/k^2$ forces $W(U_T) = 0$ identically!
- $W(U_T) = 0 \implies U_T = S$.
- Refit on $U_T = S$ yields $a = f$ identically. **Verified.**

---

## 4. Audit of Endpoints, Wrong Hypotheses, and Aborts

| Condition / Endpoint | Manuscript Handling | Audit Finding |
| :--- | :--- | :--- |
| **$k=1$ (single parity / constant)** | $\ell = 1, T = 8, P = 64$. First trial contracts $W$ from 1 to $< 1/16 < 1$. Forced $W=0$. | **Sound**. Granularity minimum $1/k^2 = 1$ forces termination in round 1; remaining rounds absorb at $W=0$. |
| **$W=0$ (absorbing state)** | $a=f \implies r = 0, v = 0$. Step 2 cutoff fails; $L = \varnothing$. Refit on $S$ reproduces $f$. | **Sound**. Lemma 1 notes zero-residual exactness; absorbing nature of $W=0$ is proven. |
| **Malformed/Wrong Hypothesis $H$** | $L$ contains spurious indices or KM returns $\FAIL$. Handled by Proposition 1. | **Sound**. Certificate rejects all spurious indices; archive cannot exceed $k$; Gram matrix remains well-conditioned. |
| **Flag shortfall in Fourier batch** | If $< gm$ flags succeed among $4gm$ copies, set $L = \varnothing$ and proceed to Step 4. | **Sound**. Preserves round structure; consumes labels and refits safely; failure prob $\le \exp(-gm/4) \le \rho$. |
| **Excessive distinct Fourier indices** | If $> k$ distinct indices occur, set $L = \varnothing$ and proceed to Step 4. | **Sound**. Cannot fire on ideal target ($|S| \le k$); protects representation bit bound on corrupted tapes. |
| **Global Aborts ($|U|>k$, singular Gram, $\norm{a}_2^2 > 2$)** | Immediate halt returning $\FAIL$. | **Sound**. Cannot fire on safe tapes; prevents infinite loops or super-polynomial allocation on corrupted tapes. |
| **Final validation of incorrect candidate** | Disagreement prob $\ge 1/(2k)$; $\lceil 2k\ln 100\rceil$ fresh labels reject with prob $\ge 99/100$. | **Sound**. Additional defensive layer against erroneous acceptance. |

---

## 5. Computational and Resource Accounting

### 5.1 Sample Complexity
- $T = 8\lceil\log_2(2k)\rceil = O(\log(2k))$.
- $q_e = \lceil 32k\varepsilon^{-2}\ln(4(k+1)/\rho)\rceil = O(k\log(2k))$ (since $\varepsilon, \rho$ are constants).
- Fourier batch: $4gm$ copies. $m = 144k = O(k)$, $g = O(\log(2k))$. Thus $4gm = O(k\log(2k))$.
- $q_c = \max\{O(k\log(P/\beta)), O(k\log(k/\beta))\}$. Since $P = 64k^2$ and $\beta^{-1} = 200T = O(\log(2k))$, $\log(P/\beta) = O(\log(2k))$. Thus $q_c = O(k\log(2k))$.
- Total quantum copies: $T(q_e + 4gm + q_c) + O(k) = O(k\log^2(2k))$. Matches Theorem 1.

### 5.2 Arithmetic Bit Lengths and Evaluator Cost
- Refit Gram matrix $A_U^\mathsf T A_U$ has dimension $\le k \times k$, integer entries $\le q_c$.
- By Hadamard's inequality, determinant bit length $b_a = O(k\log(kq_c)) = O(k\log(2k))$.
- Bareiss fraction-free elimination takes $O(k^3)$ operations on $O(b_a)$-bit integers, running in polynomial time $\widetilde O(k^4)$.
- Estimated coefficients $\widetilde c_s$ share denominator $D$ of bit length $O(b_a + \log(2kq_e))$.
- Group weights $w_s = 1/\widetilde c_s$ cleared to common denominator $\prod_{s} N_s$ of bit length $O(k b_a) = \widetilde O(k^2)$.
- Hypothesis evaluation $H(x)$ computes group sums of integers of bit length $\widetilde O(k^2)$. Multiplications by parity signs $\chi_s(x) \in \{-1, 1\}$ take $O(nk)$ bit operations.
- Total evaluation cost of $H(x)$: $\widetilde O(nk + k^3)$ bit operations.

### 5.3 Classical Time and Space
- KM prefix search: $2nP = 128nk^2$ tests.
- Samples per test: $N = \lceil 32\tau^{-4}\ln(4nP/\rho)\rceil = O(k^4\log(nk/\rho))$ (since $\tau = 1/(4k)$).
- Evaluations of $H$ per round: $O(nk^6\log(nk/\rho))$.
- Total bit time per round: $O(nk^6) \times \widetilde O(nk + k^3) = \widetilde O(n^2 k^7 + nk^9)$.
- Across $T = O(\log(2k))$ rounds: $\widetilde O(n^2 k^7 + nk^9)$.
- Live space: $P$ prefixes ($O(nk^2)$ bits), label rows ($O(nk\log(2k))$ bits), integer weights ($\widetilde O(k^3)$ bits), and Bareiss working space ($\widetilde O(k^3)$ bits). Total live space: $\widetilde O(nk^2 + k^3)$ bits. Matches equation (58)-(59).

---

## 6. Literature and Attribution Audit

1. **Ye (arXiv:2610.17648v1)**: Ye proves an $O(k\log^2 k / \log\log k)$ sample bound via grouped-sample dictionary construction. The manuscript accurately acknowledges that Ye achieves a smaller sample complexity, while differentiating itself by proving a simultaneous polynomial computation guarantee. The primary-source comparison carefully refrains from asserting a computational lower bound against Ye.
2. **Arunachalam et al. (Quantum 2021 / arXiv:1810.00481v4)**: Accurately cited with corrected v4 bounds: upper bound $O(k^{3/2}\log^2 k)$ and lower bound $\Omega(k\log k)$ in the stated parameter regime.
3. **Caro et al. (ITCS 2024 / arXiv:2306.04843v2)**: Accurately cited as establishing polynomial computation with $O(k^4\log(k^2/\delta))$ sample complexity, correctly disclaiming that polynomial-time learning alone is a novel contribution of this paper.
4. **Gopalan et al. (GOSSW 2011)**: Accurately cited for Boolean granularity. The author manuscript pinpoint (April 27, 2011, Theorem 8.1) is verified to contain the minimum coefficient bound $|c_s| \ge 2/s_0 \ge 1/k$.
5. **Kushilevitz & Mansour (SICOMP 1993)**: Properly credited for the prefix-energy identity and heavy Fourier search mechanism; the manuscript correctly notes that KM is applied to the stored classical circuit $H$, never to the target $f$.
6. **Tropp (FoCM 2012 / arXiv:1004.4389v7)**: Matrix Chernoff (Corollary 5.2) and scalar Bernstein (Theorem 6.1(ii)) are verified against the primary paper. The scalar exponents $\delta^2/2$ and $\delta^2/3$ are derived correctly.
7. **Absence of novelty overclaim**: The manuscript explicitly states that absent search hits do not establish novelty, makes no claim to optimal logarithmic exponents, and emphasizes that document checks are not formal machine certification.

---

## 7. Non-Blocking Notes & Useful Clarifications

These notes do not impede correctness, but would enhance clarity for prospective readers and referees:

1. **Explicit Clarification of Fourier Expansion Exactness in Equation (158)**:
   In the proof of Lemma 3 (line 158), the identity $Y = A_U c_U + A_V c_V$ is used without comment. While true because $f(x) \equiv \sum_{s \in S} c_s \chi_s(x)$ on the entire Boolean cube (noiseless model), readers accustomed to classical noisy regression might wonder where the model truncation error went. A one-sentence remark noting that Parseval's identity holds pointwise on $\F_2^n$ would be beneficial.
2. **Clarification on Common Denominator Bit Length in Line 368**:
   Line 368 states the common denominator bit length as $O(k[b_a + \log(2kq_e)]) = \widetilde O(k^2)$. Because $b_a = O(k\log(2kq_c))$, this product is indeed $O(k^2 \log(2k))$, which is $\widetilde O(k^2)$. Adding an explicit intermediate step $k \times O(k\log(2k))$ would prevent readers from confusing the individual weight length with the product length.
3. **Minor Typographical Distinction in Lemma 4 Citation**:
   In the proof of Lemma 6 (line 250), the text refers to "Lemma 4 and Chebyshev bound each group's sign-error probability there by 1/16." In the numbering of the manuscript, the variance of $Q_i(x)$ is stated in Lemma 4 (labeled "Lemma 4 [Bias and variance of the computed averages]" in Section 4, lines 221-227), while the prefix search is Lemma 3 (lines 170-176). The reference is mathematically clear from context, but verifying the LaTeX cross-reference label ensures no off-by-one numbering occurs if sections are reordered.

---

## 8. Final Verdict

**Verdict**: **GO WITH NOTES**

The revision to version 0.2.0 successfully resolves the sample-complexity bottleneck of version 0.1.0, reducing the quantum sample complexity to $O(k\log^2(2k))$ while preserving arbitrary-proposal safety, polynomial runtime on all tapes, and exact Boolean granularity termination. The proofs are mathematically solid and ready for the authorized publication milestone.
