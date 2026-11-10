# Adversarial Review: "Polynomial-Time Exact Learning of Fourier-Sparse Boolean Functions from Nearly Linear Quantum Samples" (v0.1.0)

**Baseline:** 69dfe76e30a0e80ae82265031f5e5b408a3d9342
**Scope:** I worked only from the supplied packet. I did not read other files, run code or use external sources. All arithmetic below was done by hand. This is an AI review, not human peer review or formal certification.

---

## 1. Verdict

**GO WITH NOTES** for a preprint.

I re-derived every inequality on the path to Theorem 1 and found no demonstrated mathematical error. All constants close, several with large slack. Every abort path is bounded, and the resource claims follow from the stated parameters.

The remaining issues are of three kinds:
- **One wording ambiguity.** The distinct-index abort rule, read literally, can make the algorithm fail spuriously.
- **Some missing displayed computations.** These are explanation gaps, not errors.
- **Attribution claims I cannot verify.** These are listed in §4. The most consequential is the negative claim about the computational cost of Ye's construction, which the novelty statement depends on.

---

## 2. Findings

Severity scale: **Blocker**, **Major**, **Moderate**, **Minor**, **Info**.
Type: **[M]** demonstrated mistake, **[E]** missing explanation, **[X]** unverified external-source claim, **[W]** wording or scope.

### F1. Distinct-index abort scope is ambiguous and, read literally, causes spurious FAIL. Moderate [W]/[M-conditional]

**Location:** §5, step 2: "Fourier-measure $4gm$ new copies. If fewer than $gm$ flags succeed, return FAIL. Split the first $gm$ successful indices into $g$ groups. Abort if more than $k$ distinct indices occur."

**Reasoning:** By the paper's own amplitude calculation, a flag-0 outcome has amplitude $2^{-n-1/2}\sum_x\chi_s(x)=\delta_{s,0}/\sqrt2$. So every flag-0 measurement returns $s=0$.

Suppose the distinct count is taken over all $4gm$ outcomes, or over all successful-plus-failed indices. Take $k=1$ and $f=\chi_a$ with $a\ne0$. Then indices $\{0,a\}$ appear with probability essentially one, the cap of $k=1$ is exceeded, and the algorithm always returns FAIL.

§6 says "The distinct-count cap never fires on valid ideal quantum examples, since a Fourier measurement only returns an element of $S$." That sentence is true only if the cap is applied to the $gm$ grouped flag-1 indices.

**Smallest repair:** Change the rule to "Abort if more than $k$ distinct indices occur among the $gm$ grouped indices." Make the §6 sentence match.

### F2. Negative claim about Ye's computational cost is load-bearing and unverified. Moderate [X]/[W]

**Location:** §1: "Its explicit dictionary construction does not provide the fixed polynomial computation asserted here." The abstract says "complements … by supplying a fixed polynomial computational guarantee." The author notes say "The inverse-weight averages in its coverage proof use unknown coefficients."

**Reasoning:** The claimed contribution is near-linear copies and polynomial computation simultaneously. That novelty rests on Ye (arXiv:2610.17648v1) not already giving a polynomial-time decoder.

Two problems:
- The statement asserts a property of another paper's construction. That is stronger than saying the other paper does not state such a bound.
- Ye v1 is dated after my knowledge cutoff, so I cannot check either version of the claim.

If Ye's decoding is in fact polynomial, or becomes polynomial with a routine argument, the contribution reduces to an alternative proof with a worse log factor.

**Smallest repair:** Reword to something like: "As we read v1, Ye does not state a polynomial bound on the computation of its dictionary decoding; its coverage argument uses inverse weights depending on unknown coefficients." Keep the explicit non-priority disclaimer.

### F3. Granularity transcription is unverified, but the conclusion is robust. Minor [X]/[E]

**Location:** §2, around eq. (3): "that theorem makes every coefficient an integer multiple of $2^{1-\lfloor\log_2 s_0\rfloor}$."

**Reasoning:** I cannot confirm the theorem number (8.1) or the floor-versus-ceiling form in GOSSW. However, (3) follows from either form:
- With a ceiling, $2^{1-\lceil\log_2 s_0\rceil}>2^{1-(\log_2 s_0+1)}=1/s_0\ge1/k$.
- With a floor, the bound is $\ge 2/s_0$.
- $s_0=1$ is a signed parity with $|c|=1$.
- $s_0=0$ is impossible for a Boolean $f$.

The proof is not robust to a weaker form such as "multiple of $2^{-\lceil\log_2 s_0\rceil}$". That form only gives $|c_s|>1/(2k)$, which would break $\tau=1/(4k)\le|c_s|/4$, $W\ge1/k^2$, and $T$. All of these would need a factor-2 adjustment.

**Smallest repair:** Add one sentence deriving $|c_s|\ge1/s_0$ from the cited form. State which version (journal or author manuscript) the theorem number refers to.

### F4. Concentration pinpoints are unverified; the inequalities used are standard and correct. Minor [X]/[E]

**Location:** Lemma 2 cites "[Tropp, Theorem 6.1(ii), scalar case]". Lemma 4 cites "[Tropp, Corollary 5.2]".

**Reasoning:** My recollection is that Corollary 5.2 is the matrix Chernoff bound, but I have not checked the text. I also cannot confirm which displayed form "(ii)" designates. If (ii) is a regime-split or subexponential form, its constants differ from the ones used.

Regardless of pinpoint, the standard scalar Bernstein bound $2\exp\!\big(-\tfrac{qt^2/2}{\sigma^2+Lt/3}\big)$ reproduces the paper's exponents exactly (see §3.1). The usual simplifications of the Chernoff bound give $2p\,e^{-q\delta^2/(3p)}$ (see §3.4).

**Smallest repair:** Cite the "bounded-case Bernstein inequality" by its displayed form rather than "(ii)". Display the one-line computation $\sigma^2+Lt/3\le e^2(1+\varepsilon)\le2e^2$.

### F5. Undisplayed arithmetic in several lemmas. Minor [E]

All of the following check out (see §3), but none is shown in the manuscript:
- Lemma 2: the union-bound arithmetic, i.e. why $q\ge32k\varepsilon^{-2}\ln(4(P+1)/\beta)$ dominates both $\exp(-q\varepsilon^2/4k)$ and $\exp(-q/28k)$.
- Proposition 10: $\exp(-gm/4)\le\beta$.
- Lemma 4: that $300p\ln(2p/\beta)$ is increasing in $p$, which justifies replacing $p$ by $k+1$.

**Repair:** Add one line each.

### F6. Overloaded symbols impede auditing. Minor [W]

| Symbol | Meanings in the manuscript |
|---|---|
| $P$ | generic list bound in Lemma 2; search cap $\lceil4/\tau^2\rceil$; global parameter $64k^2$; set to $k$ for the estimator batch ("using $P=k$" while (16) sets $P=64k^2$) |
| $v$ | empirical residual second moment; analysis row $v(X)$ in Lemma 4 |
| $D$ | frequency set in Lemma 2; common denominator in §6 |
| $N$ | search sample count; integer numerators $N_s$ |
| $q$ | generic in Lemmas 2–4; $q_e$ in (8) |

**Repair:** Rename, for example $P_{\rm est}=k$ and $P_{\rm cand}=64k^2$, $\hat v$ for the statistic, $\mathcal D$ for the frequency set.

### F7. Step 4 refit wording. Minor [W]

**Location:** Step 4: "Refit the original labels exactly on $U$."

This should say: the target labels $f(X_\ell)$ of the same certification batch, fitted on the updated archive $U^+$. Proposition 10's proof relies on exactly this, so the algorithm text should state it.

### F8. Undefined jargon in §7. Minor [W]

"…nor a large clipping defect. These distinctions explain how the computed operation avoids stronger stability assumptions…"

"Clipping defect" is not defined anywhere in the manuscript. The sentence reads as a residue of drafting.

**Repair:** Delete it, or define the term and the stability assumptions being contrasted.

### F9. Access-model observation the paper could state. Info [W]

Every copy is measured individually, either in the computational basis or after $H^{\otimes(n+1)}$. The algorithm therefore uses only:
- classical uniform labeled examples, and
- classical Fourier samples $s\sim c_s^2$ (after flag post-selection).

Stating this explicitly would sharpen the access-model comparison in §7 and pre-empt confusion with collective-measurement results.

### F10. Constants are astronomically large. Info

For $k=1$ the algorithm consumes about $2.08\times10^{10}$ copies (worked in §3.8). A single Fourier sample would suffice in that case. The paper disclaims practicality, so this is not an error. A one-line remark would prevent misreading of "nearly linear."

### F11. Disclosure wording. Minor [W]

- "No external funding is asserted in this manuscript" is evasive. If true, say "No external funding was received."
- "The accompanying review record identifies the checks" refers to a document not in this packet, so I could not assess it.
- The OpenAI Codex disclosure is clear and appropriate.

### F12. $S_0=S\cup\{0\}$ in Lemma 4 is unnecessary. Info

Adding the zero frequency is harmless; it costs one dimension. Either explain why it is there or drop it.

---

## 3. Checks supporting the core argument

### 3.1 Lemma 2: residual Bernstein constants

**Coefficient estimates.**
- $r=f-a$ has at most $2k$ Fourier terms, so $\|r\|_\infty\le\sqrt{2k}\,e\le\sqrt{3k}\,e$.
- $Y=r(X)\chi_s(X)$ has $\operatorname{Var}Y\le\E r^2=e^2$.
- $|Y-\widehat r(s)|\le(\sqrt3+1)\sqrt k\,e\le 2.74\sqrt k\,e\le3\sqrt k\,e$.
- With $t=\varepsilon e/\sqrt k$: $\sigma^2+Lt/3\le e^2+\varepsilon e^2\le2e^2$. The exponent is $q\,(\varepsilon^2e^2/k)/2\,/\,(2e^2)=q\varepsilon^2/(4k)$. ✓

**Second-moment estimate.**
- $0\le r^2\le3ke^2$, so $|r^2-e^2|\le3ke^2$.
- $\operatorname{Var}(r^2)\le\|r\|_\infty^2e^2\le3ke^4$.
- With $t=e^2/2$: the exponent is $(e^4/8)/(3ke^4+ke^4/2)=1/(28k)$, times $q$. ✓

**Union bound.** With $q\ge32k\varepsilon^{-2}L_0$ and $L_0=\ln(4(P+1)/\beta)$:
- $q\varepsilon^2/4k\ge8L_0$.
- $q/28k\ge(32/28)\varepsilon^{-2}L_0\ge L_0$.

So the total failure is $\le2(P+1)\cdot\beta/(4(P+1))=\beta/2$. That is a factor-2 slack on the overall bound, and the coefficient terms alone have far more. ✓

**Conditioning.** The conclusion holds conditional on any history fixing $a,D$ because the batch is fresh. If $e=0$, everything is exact. ✓

### 3.2 Uniform fixed-true-support event versus adaptive candidates

The estimator event (10) is a union over the deterministic set $S$ with $|S|\le k$. It is used only at indices returned by Fourier sampling, which are drawn after the estimator batch is fixed.

Flag-1 outcomes lie in $S$ with probability one. So every evaluated $\widetilde c_s$ is covered, with no union over adaptively chosen or exponentially many indices.

Candidates from search, which may lie outside $S$, are never scored with $\widetilde c$. They are scored by the separate fresh certification batch with $D=L$, $|L|\le64k^2$, and $L$ is fixed before that batch. ✓ This is the correct separation.

### 3.3 Lemma 3: certification thresholds

For $s\notin U$, $\widehat r(s)=c_s$. On the event:
- **$c_s=0$:** $z_s^2\le\varepsilon^2e^2/k<2\varepsilon^2e^2/k\le4\varepsilon^2v/k$. Not admitted. When $e=0$, $0>0$ is false, so it is also not admitted. ✓
- **$|c_s|>4\varepsilon e/\sqrt k$:** $|z_s|>3\varepsilon e/\sqrt k>\sqrt6\,\varepsilon e/\sqrt k\ge\sqrt{4\varepsilon^2v/k}$. Admitted. ✓

### 3.4 Lemma 4: Gram event and adaptive refit on the same batch

- $X_\ell=v(X_\ell)v(X_\ell)^\top\succeq0$, $\lambda_{\max}=p$, $\mu_{\min}=\mu_{\max}=q$.
- The standard Chernoff simplifications ($e^{-\delta^2/2}$ lower, $e^{-\delta^2/3}$ upper, $\delta\le1$) give $\le2p\,e^{-q\delta^2/(3p)}$.
- At $\delta=1/10$, it suffices that $q\ge300p\ln(2p/\beta)$, which is increasing in $p$. ✓

On $\|G-I\|\le1/10$, for any $U\subseteq S$ with $V=S\setminus U$:
- $\|G_{UU}^{-1}\|\le10/9$.
- $G_{UV}$ is an off-diagonal block of $G-I$, so $\|G_{UV}\|\le1/10$.
- Noiseless labels give $f(X)=A_Uc_U+A_Vc_V$ exactly, hence $a_U-c_U=G_{UU}^{-1}G_{UV}c_V$.
- So $\|P_Uf-a\|\le\sqrt W/9$ and $\|f-a\|^2=W+\|c_U-a_U\|^2\le\tfrac{82}{81}W$.
- $\|a\|\le\sqrt{1-W}+\sqrt W/9\le\sqrt{1+1/81}$ by Cauchy–Schwarz. ✓

The event depends only on the fixed $S_0$. It therefore covers every $U\subseteq S$ simultaneously, including a $U$ selected from the same batch, provided certification also succeeded so that $U\subseteq S$. The union of the certification and Gram events on one batch is handled correctly. ✓

### 3.5 Lemma 6: prefix energy search

- $\E_xH(x,z)\chi_u(x)=\sum_v\widehat H(u,v)\chi_v(z)$. Squaring and averaging over $z$ gives $E_u$, and the product form with a shared $z$ is exact. ✓
- Summands are in $\{-1,1\}$. Hoeffding at $\tau^2/4$ gives $2e^{-N\tau^4/32}$. ✓
- Per-test failure is $\le\beta/(2nP)$. There are $\le2nP$ adaptively chosen tests, each with fresh samples conditional on the past. Total $\le\beta$. ✓
- Survival: if $|\widehat H(s)|\ge\tau$, every ancestor has $E_u\ge\tau^2$, so its estimate is $\ge3\tau^2/4$.
- Retained buckets have $E_u\ge\tau^2/2$, and disjoint buckets at a depth sum to 1, so at most $2/\tau^2<P$ are retained. The cap never fires on the good event. ✓
- Random bits: $2j+(n-j)\le2n$ per sample. ✓

### 3.6 Lemmas 7–8: reciprocal bias, variance and majority

**Cutoff.** $t=4\varepsilon\sqrt{v/k}\in[2\sqrt2\Delta,\,2\sqrt6\Delta]\approx[2.83\Delta,\,4.90\Delta]$. ✓
- $W>0$ forces $e\ge\sqrt W>0$, so $t>0$ and $\Delta/t$ is defined. ✓
- **Pass:** $|c_s/\widetilde c_s|\le1+1/(2\sqrt2)\approx1.354<3/2$, and signs agree since $|\widetilde c_s|\ge t>\Delta$. ✓
- **Fail:** $|c_s|<t+\Delta\le5.90\Delta<6\Delta$. This includes $\widetilde c_s=0$. ✓

**Bias and variance.**
- Coefficient error: $\le1.5\Delta$ on a pass and $<6\Delta$ on a fail, so $\|h-f\|^2\le k\cdot36\Delta^2=36\varepsilon^2e^2$. ✓
- Second moment of one weighted sample: $\sum_{\text{pass}}c_s^2/\widetilde c_s^2\le9k/4$, uniformly in $x$. With $m=144k$, $\operatorname{Var}Q_i(x)\le1/64$. ✓

**Majority.**
- Off $A=\{|h-f|>1/2\}$: a group sign error requires $|Q_i-h|\ge1/2$. This covers the tie rule $\operatorname{sgn}0=1$ when $f=-1$. Chebyshev gives $\le1/16$. ✓
- Majority error: $\le2^g(1/16)^{(g+1)/2}\le2^{-g}$. ✓
- $\mu(A)\le4\|h-f\|^2$ by Markov. ✓
- Fubini over $x$ and the groups needs no cross-$x$ independence: $\E\|H-f\|^2=4\Pr_{x,\text{groups}}[H\ne f]\le16\|h-f\|^2+4\cdot2^{-g}$. ✓

**Constants.**
- $\varepsilon=1/(512R)$ with $R^2\ge1/\beta$ gives $\varepsilon^2\le\beta/262144$.
- Then $576\varepsilon^2e^2\le576\cdot\tfrac{82}{81}\cdot\beta W/262144\approx0.00222\,\beta W\le\beta W/128$.
- $4\cdot2^{-g}\le\beta/(128k^2)\le\beta W/128$, using $W\ge1/k^2$.
- Markov at $W/64$ gives probability $\le\beta$. ✓

### 3.7 Proposition 10: contraction and the W=0 case

**Omitted from $L$.** Then $|\widehat H(s)|<1/(4k)\le|c_s|/4$, so $c_s^2\le\tfrac{16}{9}(c_s-\widehat H(s))^2$. Summing gives $\le\tfrac{16}{9}\cdot W/64=W/36$. ✓

**In $L$ but not admitted.** Each has $|c_s|\le4\gamma e/\sqrt k$. Summing over at most $k$ such terms gives $\le16\gamma^2e^2=e^2/64\le\alpha^2W/64$. ✓

**Total.** $(1/36+82/5184)W\approx0.0436\,W<0.0625\,W$. ✓

**$W=0$.** The invariant forces $a=f$, so $e=0$ and $v=0$. Every $z_s$ is 0 and nothing is admitted; on the Gram event the refit is exact. The flags and search aborts can still fire. They are charged within $6\beta$, which is correct because the round count is fixed. ✓

**Flags.** $\Pr[\mathrm{Bin}(4gm,1/2)<gm]\le e^{-gm/4}$, and $gm/4\ge36gk\gg\ln(1/\beta)$. Selecting the first $gm$ successes uses only flag values, so those indices are i.i.d. $c_s^2$. ✓

**Over rounds.**
- First-failure union bound: $6T\beta=6T/(100(T+1))<0.06$. ✓
- $16^{-T}\le(2k)^{-4}<1/k^2$, so granularity forces $W=0$ and $U=S$. The final refit is $f$, and the Booleanity and validation checks pass surely. ✓
- **Final validation.** For distinct Boolean functions of sparsity at most $k$, $\|d\|_\infty=2\le\sqrt{2k}\|d\|_2$, so they disagree on at least a $1/(2k)$ fraction of inputs. Then $(1-1/2k)^{2k\ln100}\le1/100$. With the $\lceil\log_2\rceil$ convention this is $14k$ labels, which is still enough. ✓

### 3.8 Worked constants for k=1 (with the ⌈log₂⌉ convention)

| Quantity | Value |
|---|---|
| $T$ | 1 |
| $\beta$ | 1/200 |
| $R$ | 15 |
| $\varepsilon$ | 1/7680, so $\varepsilon^2=1.695\times10^{-8}\le\beta/262144=1.907\times10^{-8}$ ✓ |
| $g$ | 17 ($2^{17}=131072\ge102400$, odd ✓) |
| $m$ | 144 |
| $\tau$ | 1/4 |
| $P$ | 64 |
| $q_e$ | $32\cdot7680^2\cdot\lceil\log_2 1600\rceil=32\cdot58{,}982{,}400\cdot11\approx2.076\times10^{10}$ |
| $4gm$ | 9792 |
| $q_c$ | $\max(32768\cdot16,\;600\cdot10)=524{,}288$ |
| Validation | 14 |

The contraction $1\to<1/16<1/k^2$ completes in one round. Asymptotically:
- $\varepsilon^{-2}=\Theta(\log k)$, $q_e=\Theta(k\log^2k)$, $q_c=\Theta(k\log k)$, $4gm=\Theta(k\log k)$.
- Over $T=\Theta(\log k)$ rounds the total is $\Theta(k\log^3(2k))$. ✓

### 3.9 Exact arithmetic, bit-time, space and randomness

**Denominators.**
- The Gram matrix and right-hand side are integer with entries $\le q_c$. Hadamard's bound gives $b_a=O(k\log(kq_c))=O(k\log k)$ on every nonsingular tape. ✓
- $\widetilde c_s$ has denominator $q_e\cdot\mathrm{Det}$ and numerator $b_a+O(\log kq_e)$ bits. ✓
- Integer weights $\mathrm{sgn}(N_s)\prod_{t\ne s}|N_t|$ (with $D$ in the numerators) have $\widetilde O(k^2)$ bits. ✓
- No hypothesis is nested across rounds, and the refit resets the bit bound. ✓

**Time.**
- One evaluation of $H$: $O(nk)$ for parities, plus $g$ group sums of $\le k$ terms of $\widetilde O(k^2)$ bits, giving $\widetilde O(nk+k^3)$. ✓
- Evaluations per round: $2N\cdot2nP=\widetilde O(nk^6)$.
- Product over $T$ rounds: $\widetilde O(n^2k^7+nk^9)$. ✓
- Other costs are dominated: Bareiss elimination $\widetilde O(k^5)$, certification $\widetilde O(nk^3+k^4)$, convolution $\widetilde O(k^4+nk^2)$.

**Space.**
- Retained prefixes or candidates: $O(nk^2)$.
- Label rows: $\widetilde O(nk)$.
- Residual rationals: $\widetilde O(k^2)$.
- Weights: $\widetilde O(k^3)$.
- $O(k^2)$ accumulators of $\widetilde O(k)$ bits: $\widetilde O(k^3)$.
- Bareiss matrix: $\widetilde O(k^3)$.
- Total $\widetilde O(nk^2+k^3)$. ✓

**Randomness.** Only the search uses classical random bits: $\le2n$ per sample, $\widetilde O(n^2k^6)$ in total. These are covered by the bit-time bound (suggestion in F4/F5: state this separately).

**Every tape.** All of the following are capped independently of correctness: batch sizes, $T$, $\le2nP$ tests, $\le k$ distinct sampled indices, $|L|\le P$, $|U|\le k$ before refit, and fit bit-length. Singular systems, zero estimates, ties and overflow all have explicit rules. ✓ (Subject to F1 wording.)

### 3.10 Counterexample attempts (none succeeded)

1. **$f=\chi_a$, $k=1$.** Passes, except under the literal reading in F1.
2. **Bent function, $k=2^n$.** $|c_s|=2^{-n/2}=1/\sqrt k\ge1/k$. The parameters still apply, and copy usage stays $O(k\log^3k)$ in $k$.
3. **Search returns up to $64k^2$ spurious non-$S$ indices** because $H$ has a dense spectrum. All are rejected on the certification event, which unions over $L$.
4. **An index outside $S$ needs $\widetilde c$.** Impossible: flag-1 samples lie in $S$.
5. **Adaptively chosen archive refit on the same rows.** Covered by the full-$S_0$ Gram event.
6. **Small $W\approx1/k^2$ with a single missing coefficient.** $|c|=\sqrt W\gg5\Delta\approx5\varepsilon\sqrt W/\sqrt k$, so it passes the cutoff, and $H$'s error budget $\beta/(512k^2)$ is below $W/64$.
7. **$v=0$ while $e>0$.** Excluded on the event, since $v\ge e^2/2$.
8. **Estimate of zero.** Never divided; it is treated as a fail, which is covered by the $6\Delta$ bound.

---

## 4. Claims, literature boundaries and what I could not verify

| Claim | Status |
|---|---|
| ACLPW: $O(k^{3/2}\log^2k)$ upper, $\Omega(k\log k)$ lower bound | Consistent with my recollection of the published paper. Not checked against "corrected v4" text. |
| Ye (arXiv:2610.17648v1): $O(k\log^2k/\log\log k)$, grouped dictionary, and no fixed-polynomial computation | **Unverifiable**: postdates my knowledge cutoff. The computational claim is load-bearing for novelty (F2). |
| Caro et al., Corollary 10: efficient exact learner with $O(k^4\log(k^2/\delta))$ copies | Unverified pinpoint and bound. |
| GOSSW Theorem 8.1 granularity form | Unverified pinpoint and floor form. The conclusion (3) is robust to the ceiling form (F3). |
| KM attribution of the prefix-energy search | Appropriate. The manuscript proves the needed version itself, so nothing depends on the citation. |
| Tropp Corollary 5.2 / Theorem 6.1(ii) | Pinpoints unverified. The inequalities as used are correct (F4). |
| "No primary theorem with the same joint guarantee" (author notes) | A search-absence statement, appropriately disclaimed. Not evidence of novelty, and I make no literature claim either way. |
| Internal AI review record | Not supplied, not assessed. |

**Scope and wording.**
- Access model: copies are supplied, there are no membership queries, no inverse preparation circuit, and measurements are single-copy. This is stated clearly and is consistent with the algorithm.
- The non-claims ("not first efficient", "not optimal logs", "no practical runtime", "no BPP/BQP implication") are appropriate.
- The title and abstract do not overclaim, apart from the Ye comparison (F2).

---

## 5. Does any blocker remain?

**No mathematical blocker.** The proof of the exact-learning theorem, with $O(k\log^3(2k))$ copies, success $\ge0.94$, and the stated bit-time and space caps on every tape, checks out step by step.

Before posting, I recommend:
- **F1:** a one-phrase fix so the algorithm as written cannot spuriously fail.
- **F2:** a rewording of the novelty sentence, which depends on an external claim I cannot verify.

F3–F8 and F11 are small clarity or citation repairs.