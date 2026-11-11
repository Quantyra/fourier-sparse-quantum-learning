# Discrepancy Audit and Corrected Review

**Document**: Version 0.2.0 (`fourier-sparse-quantum-learning`)  
**Source SHA-256**: `ac1d730256c61861930fd63beed806e23aff08c82a1dd8c809e93a5b085321ea`  
**Reviewer**: AGY (AI Provider Review; internal audit of supplied packet only)  
**Corrected Verdict**: **GO**

---

### Audit of Report Discrepancies

#### 1. Absorbing State at $W=0$
* **Report Error**: The prior report stated that at $W=0$, the hypothesis cutoff fails and $L = \varnothing$.
* **Correction**: In the source (eq. 197–200), $\widetilde c_s = \widehat a(s) + q_e^{-1}\sum_\ell (f(X_\ell)-a(X_\ell))\chi_s(X_\ell)$. When $W=0$, $U=S$ and the fit satisfies $a \equiv f$ (Lemma 4). Thus the residual $f-a$ is identically zero, so $\widetilde c_s = c_s$ and $v = 0$. For any true frequency $s \in S$, $c_s \ne 0$, so $\widetilde c_s^2 > 0 = 16\varepsilon^2 v / k$. Nonzero true coefficients **pass** the hypothesis cutoff. The function $H$ is well-formed, and classical search returns true candidates ($L \subseteq S$).
* The actual mechanism that maintains absorption is in Step 4:
  1. $L \setminus U = L \setminus S = \varnothing$.
  2. For any candidate, certification residuals $z_s = q_c^{-1}\sum_\ell(f-a)\chi_s \equiv 0$ and $v \equiv 0$. The threshold test $z_s^2 > 4\varepsilon^2 v / k \iff 0 > 0$ strictly rejects (Lemma 3), admitting no elements.
  3. Thus $U^+ = U = S$. On the Gram event $G$ (Lemma 4), refitting reproduces $a^+ = f$.
  4. The safety budget for all remaining trials is bounded by the initial union bound $\Pr(B) \le 2T\beta = 1/100$, confirming $W=0$ is absorbing on $B^c$.
* **Manuscript Impact**: **No defect**. The manuscript is mathematically correct.

#### 2. $k=1$ Endpoint Trajectory
* **Report Error**: The prior report claimed termination occurs deterministically in round 1.
* **Correction**: While $k=1 \implies \ell = 1$ and $T = 8\ell = 8$, round 1 progress is conditional on good proposal events and safety, succeeding with probability $\ge 1/2$. The manuscript executes all $T=8$ trials unconditionally (line 278). The trajectory guarantee follows from the dummy-indicator martingale:
  $$\Pr(Z_8 \ge 1) \ge 1 - 2(3/4)^8 = 1 - \frac{6561}{32768} \approx 0.7998 > \frac{3}{4}.$$
  On $B^c$, obtaining $Z_8 \ge 1$ guarantees at least one factor-16 contraction, driving $W < 1/16 < 1/k^2 = 1$. Boolean granularity then forces $W=0$, which absorbs for the remaining trials.
* **Manuscript Impact**: **No defect**. The manuscript's fixed-$T$ guarantee is correct.

#### 3. Scalar Bernstein Exponent Inequality
* **Report Error**: The prior check wrote $-qt^2 / (2(\sigma^2 + Bt/3)) \ge -q\varepsilon^2 / (4k)$.
* **Correction**: Since $2(\sigma^2 + Bt/3) \le 4e^2$, dividing by the denominator reverses the inequality for the negative exponent:
  $$-\frac{qt^2}{2(\sigma^2 + Bt/3)} \le -\frac{q(\varepsilon^2 e^2 / k)}{4e^2} = -\frac{q\varepsilon^2}{4k}.$$
  Taking exponentials gives the tail upper bound $2\exp(-q\varepsilon^2/(4k))$. The manuscript (lines 107–111) states this direction correctly.
* **Manuscript Impact**: **No defect**. The error was purely a sign slip in the report's worked check.

#### 4. Source-Verification Boundary & Review Identity
* **Report Error**: The prior report claimed external primary papers were "verified" and styled itself an "Independent" audit.
* **Correction**: This review is an automated AI provider review (AGY / Gemini), not independent human peer review or formal machine certification. Furthermore, it operated under a strict read-only boundary over the supplied packet (`initial-packet.txt`). The primary-source comparison table in the packet was audited as supplied evidence; no external databases or original PDFs were fetched.
* **Manuscript Impact**: **No defect**. The manuscript's disclosures (lines 385–389) accurately reflect this exact status.

#### 5. Fourier Expansion vs. "Pointwise Parseval"
* **Report Error**: The prior report suggested noting that "Parseval holds pointwise" to justify $Y = A_U c_U + A_V c_V$.
* **Correction**: Parseval's identity is an $L^2$ norm equality ($\sum c_s^2 = \E f^2$), not a pointwise relation. Pointwise equality is **Fourier inversion**: because $f$ is a Boolean function on $\F_2^n$, $f(x) = \sum_{s \in S} c_s \chi_s(x)$ holds for every $x \in \F_2^n$. Evaluating this identity at the sample rows $X_\ell$ gives $Y = A_U c_U + A_V c_V$ exactly, with zero model truncation error.
* **Manuscript Impact**: **No defect**. The manuscript's algebra is exact; the suggested note was based on flawed terminology and is retracted.

#### 6. Lemma and Proposition Numbering
* **Report Error**: The prior report claimed the source had numbering mismatches.
* **Correction**: In the source preamble, `\newtheorem{lemma}[theorem]{Lemma}` and `\newtheorem{proposition}[theorem]{Proposition}` inherit the `theorem` counter. The true document numbering is:
  * Theorem 1 (Main Theorem)
  * Lemmas 2, 3, 4, 5, 6, 7 (Estimates, Certificate, Gram fit, Search, Bias/Variance, Majority)
  * Propositions 8, 9 (Safety, Contraction)
  LaTeX cross-references (e.g., `Lemma~\ref{lem:bias}` in Lemma 7's proof compiling to "Lemma 6") match the compiled PDF.
* **Manuscript Impact**: **No defect**. The report's independent numbering scheme caused the apparent mismatch.

#### 7. Bareiss Elimination Runtime Accounting
* **Report Error**: The report assigned a specific $\widetilde O(k^4)$ bit cost to Bareiss elimination without specifying integer multiplication bit complexity.
* **Correction**: Bareiss elimination performs $O(k^3)$ ring operations on integers of bit length $O(b_a) = O(k\log(2kq_c))$. With schoolbook multiplication, this requires $\widetilde O(k^5)$ bit operations; with quasi-linear multiplication, $\widetilde O(k^4)$. The manuscript (lines 361, 373–374) claims only that exact elimination runs in polynomial bit time and is strictly dominated by the search envelope $\widetilde O(n^2 k^7 + nk^9)$.
* **Manuscript Impact**: **No defect**. The manuscript's claim is mathematically conservative and correct.

---

### Final Disposition

None of the 7 audited discrepancies correspond to defects, gaps, or vulnerabilities in manuscript version 0.2.0; all 7 were errors, overstatements, or improper notations introduced by the initial review report. 

* **Mathematical Validity**: Intact across all lemmas, tail bounds, adaptive refits, and dummy-indicator progress.
* **Remaining Blockers**: None.
* **Corrected Verdict**: **GO**. The manuscript is mathematically sound and approved for the authorized release.
