The internal argument for the exact \(k\)-sparse theorem closes. I found no demonstrated false step in the contraction, sample bound, adaptive refit, rational bit growth, or fixed polynomial resource caps. The result is still conditional on three load-bearing external inequalities that this packet does not contain.

# Review: exact learning of \(k\)-Fourier-sparse Boolean functions

**Verdict: GO WITH NOTES** (preprint). No demonstrated blocker in the proof as written. Acceptance of the theorem still depends on Gopalan–O’Donnell–Servedio–Shpilka–Wimmer granularity and on Tropp’s scalar Bernstein and matrix Chernoff forms being at least as strong as the inequalities used below. Literature comparisons are author assertions, not lemmas in the proof.

## Findings

### 1. Load-bearing external inequalities are not proved here
**Severity:** unverified external dependency (not an internal contradiction).  
**Where:** granularity (1); Lemma 1 (Bernstein exponents \(4k\) and \(28k\)); Lemma 3 (displayed matrix Chernoff bound).  

The \(1/k\) floor is used twice in an essential way: positive missing energy satisfies \(W\ge 1/k^2\), which absorbs the \(4\cdot 2^{-g}\) majority term, and \(\tau=1/(4k)\le |c_s|/4\), which gives the omitted-mass factor \(16/9\). The manuscript only paraphrases the source: for sparsity \(s_0>1\), nonzero coefficients are integer multiples of \(2^{1-\lfloor\log_2 s_0\rfloor}\). From that paraphrase the \(1/k\) bound does follow, because
\[
2^{1-\lfloor\log_2 s_0\rfloor}=2/2^{\lfloor\log_2 s_0\rfloor}\ge 2/s_0\ge 2/k
\]
whenever \(1<s_0\le k\), and a one-sparse Boolean function is a signed parity (\(|c|=1\)). A ceiling in place of the floor would still be strictly stronger than \(1/k\). I cannot check Theorem 8.1 itself.

The Gram sample size is numerically tight against the inequality printed in the proof. With \(\delta=1/10\), \(R=p\le k+1\) and
\[
q\ge 300(k+1)\ln\frac{2(k+1)}{\beta},
\]
one gets \(2p\exp(-q\delta^2/(3p))\le\beta\) with equality at \(p=k+1\). A worse constant in the cited corollary would make \(q_c\) too small. Bernstein is not in that position: see the slack calculation below.

**Smallest repair:** quote the three invoked statements verbatim (hypothesis, range of \(\delta\), and the exact exponential) and add the five-line substitutions that produce \(4k\), \(28k\), and \(300(k+1)\). If a quoted constant is weaker, increase only that sample-size leading factor; the \(O(k\log^3(2k))\) shape and the later contraction arithmetic do not change.

### 2. Concentration algebra is asserted rather than written
**Severity:** missing explanation, low. The stated exponents match the usual scalar Bernstein form
\[
\Pr(|\mathrm{sum}|\ge t)\le 2\exp\Bigl(-\frac{t^2/2}{\sigma^2+Mt/3}\Bigr)
\]
and the usual Hoeffding form for variables in \([-1,1]\).  

Coefficient side: variance proxy \(\le e^2\), centered bound \(\le 3\sqrt{k}\,e\) (since \(\|r\|_\infty\le\sqrt{3k}\,e\) and \(|\widehat r|\le e\), and \(\sqrt{3k}+1\le 3\sqrt{k}\) for every integer \(k\ge 1\)), deviation \(\varepsilon e/\sqrt{k}\), and \(\varepsilon\le 1\), give exactly \(2\exp(-q\varepsilon^2/(4k))\). Energy side: \(\mathrm{Var}(r^2)\le 3ke^4\), \(|r^2-e^2|\le 3ke^2\), deviation \(e^2/2\), give exactly \(2\exp(-q/(28k))\). Prefix tests: range length \(2\), deviation \(\tau^2/4\), give \(2\exp(-N\tau^4/32)\).  

With \(q\ge 32k\varepsilon^{-2}\ln(4(P+1)/\beta)\) the coefficient exponent is \(8\ln(4(P+1)/\beta)\), about eight times what a union bound over \(P+1\) events needs. The same \(q\) makes the energy failure negligible because the real \(\varepsilon^{-2}\) is at least \(512^2\), not \(1\). Hoeffding is tight: \(2nP\) tests times \(\beta/(2nP)\) equals \(\beta\). The adaptive-test union bound is valid (each test is charged conditional on the past; at most \(2nP\) tests occur before the cap).

**Smallest repair:** paste those three substitutions into the proofs. No sample-size change is required for the printed exponents.

### 3. A few abort branches are named but not tied to \(\FAIL\)
**Severity:** missing explanation, low.  
**Where:** algorithm steps 2 and 4 (“abort” on more than \(k\) distinct indices, \(|U|>k\), singularity, or \(\|a\|_2^2>2\)), versus step 3 and the flag test, which say `return FAIL`.  

The cost section says every tape hits an explicit rule and stops. On the good event none of these aborts fire: Fourier hits lie in \(S\), certification admits nothing outside \(S\), and the full-support Gram event gives a nonsingular fit with \(\|a\|_2^2\le 82/81<2\).

**Smallest repair:** write `return FAIL` on each abort.

### 4. No demonstrated mistake in the contraction or the rational-cost reset
Checked and not a defect: fresh-batch conditioning; uniform control on the fixed true support rather than on adaptively chosen sample indices; reciprocal bias; majority exceptional set; same-batch Gram refit; \(W=0\); denominator reset. Details are in the next section. I tried to break the boundary case \(|c_s|=1/k\), \(W=1/k^2\), \(v=3e^2/2\), and estimate error exactly \(\Delta\). The pass/fail split and the strict inequality \((1/36+\alpha^2/64)<1/16\) still hold.

## Checks that support the core argument

**Access.** Hadamarding every qubit of (1) gives amplitude \(c_s/\sqrt{2}\) on \((s,1)\). The flag is \(1\) with probability \(1/2\), and the conditional index law is \(c_s^2\). Taking the first \(gm\) successes among \(4gm\) copies, given at least \(gm\) flags, preserves that law. A binomial lower tail below half the mean is at most \(\exp(-gm/4)\). For these parameters that is far below \(\beta\).

**Residual estimators (Lemma 1) and certification (Lemma 2).** On \(e^2/2\le v\le 3e^2/2\) and \(|z_s-c_s|\le\Delta=\varepsilon e/\sqrt{k}\): if \(c_s=0\), then \(z_s^2\le\varepsilon^2 e^2/k\) while the threshold is at least \(2\varepsilon^2 e^2/k\); if \(|c_s|>4\Delta\), then \(|z_s|>3\Delta\) while \(\sqrt{\mathrm{threshold}}\le\sqrt{6}\,\Delta<3\Delta\). False admissions are impossible on this event, and every sufficiently large true coefficient is kept. The list \(L\) is fixed before the certificate batch. The analysis event for the hypothesis batch is accuracy of \(v\) and of \(\widetilde c_s\) for every \(s\in S\), with \(|S|\le k\). It is not a union over the cube. Weights are computed only on indices that actually appear; the expectation over Fourier measure may still sum over the whole pass set inside \(S\).

**Bias (Lemma 4).** Cutoff \(t=4\varepsilon\sqrt{v/k}\) satisfies \(2\sqrt{2}\,\Delta\le t\le 2\sqrt{6}\,\Delta<5\Delta\). On a pass, \(|c/\widetilde c|\le 1+\Delta/t\le 1+1/(2\sqrt{2})<3/2\) and the signs agree, so the coefficient error is \(<3\Delta/2\). On a failure, \(|c|<6\Delta\). At most \(k\) frequencies, and failures dominate passes, so \(\|h-f\|_2^2\le 36\varepsilon^2 e^2\). The second moment of one weighted sample is \(\sum c_s^2/\widetilde c_s^2<9k/4\), hence \(\mathrm{Var}(Q_i(x))\le 9k/(4m)\). The choice \(m=144k\) makes this \(1/64\).

**Majority (Lemma 5).** Outside a set \(A\) of measure at most \(4\|h-f\|_2^2\), the margin is \(1/2\), so Chebyshev gives sign-error at most \(1/16\). For odd \(g\), a crude binomial bound is \(2^g(1/16)^{g/2}=2^{-g}\). No independence across inputs is used. Boolean range \(4\) gives
\[
\mathbb{E}\|H-f\|_2^2\le 576\varepsilon^2 e^2+4\cdot 2^{-g}.
\]
Parameters: \(R=\lceil\beta^{-1/2}\rceil\), \(\varepsilon=1/(512R)\), so \(\varepsilon^2\le\beta/262144\), and \(2^g\ge 512k^2/\beta\). Then, using \(e^2\le\alpha^2 W\) and \(\alpha^2<2\),
\[
1152/262144=9/2048<16/2048=1/128,
\]
so the bias term is \(<\beta W/128\). Granularity gives \(4\cdot 2^{-g}\le\beta W/128\). Markov at level \(W/64\) costs at most \(\beta\). The first term is in fact only about \(0.29\) of \(\beta W/128\) if one uses \(\alpha^2=82/81\) instead of \(2\). Signs are taken before the majority, so large rational averages do not enlarge \(A\).

**One Gram event (Lemma 3).** \(\|q^{-1}A_{S_0}^\top A_{S_0}-I\|_{\mathrm{op}}\le 1/10\) controls every principal block and every off-diagonal block of every \(U\subseteq S\), with no subset union bound. Hence
\[
\|a_U-c_U\|_2\le(10/9)(1/10)\sqrt{W}=\sqrt{W}/9,
\]
and orthogonality yields \(\|f-a\|_2^2\le(1+1/81)W\). Cauchy–Schwarz gives \(\|a\|_2\le\sqrt{82/81}\). The empty fit is \(0\). If \(U=S\), then \(c_V=0\), so the fit is exactly \(f\), not merely close. Choosing \(U\) from this same batch is legitimate because the event is defined on the full unknown support before the subset is selected. The algorithm inverts only the columns it kept.

**Contraction.** On the good search event, a missed true frequency has \(|\widehat H(s)|<\tau\le|c_s|/4\), so
\[
\sum_{s\in S\setminus L}c_s^2\le(16/9)\|H-f\|_2^2\le W/36.
\]
True frequencies that are proposed but rejected contribute at most \(16\gamma^2 e^2=e^2/64\le\alpha^2 W/64\) because \(\gamma=1/32\). Therefore
\[
\frac1{36}+\frac{\alpha^2}{64}=\frac{226}{5184}<\frac{324}{5184}=\frac1{16}.
\]
So \(W(U^+)<W/16\) whenever \(W>0\). If \(W=0\), the invariant forces \(a=f\), the certificate residual is identically zero, nothing new is admitted, and the Gram event refits \(f\) exactly. A bad majority does not by itself abort this case; charging it inside the \(6\beta\) is only loose. Six conditional failures, first-failure over \(T\) rounds, and \(\beta=1/(100(T+1))\) give failure \(<0.06\), so success \(>0.94>2/3\). Then \(T=\lceil\log_2(2k)\rceil\) yields \(W<16^{-T}\le 1/(16k^4)<1/k^2\), so granularity forces \(W=0\).

**Search interface.** The prefix identity (4) is proved and uses chosen inputs to the stored \(H\) only. Retained buckets have true energy at least \(\tau^2/2\), so at most \(2/\tau^2\) survive at one depth. Here \(\tau=1/(4k)\) and \(P=\lceil 4/\tau^2\rceil=64k^2\). Classical samples per test depend on \(\ln(nP/\beta)\); those evaluations are of \(H\) and do not add quantum copies. Replacing each \(\ln z\) by \(\lceil\log_2 z\rceil\) only increases counts.

**Resources, including bad tapes.** \(T,\beta^{-1},\varepsilon^{-2},g=O(\log(2k))\), \(q_e=O(k\log^2(2k))\), \(q_c=O(k\log(2k))\), and \(gm=O(k\log(2k))\). The copy sum \(T(q_e+4gm+q_c)+O(k)\) is \(O(k\log^3(2k))\). The \(n\)-dependence of search confidence is classical. Quantum work is \(O(n)\) gates per copy.

Each refit is a fresh integer \(k\times k\) system with entries at most \(q_c\), not a composition with the previous hypothesis. Hadamard gives numerator/denominator length \(b_a=O(k\log(2kq_c))\) on every nonsingular tape. Inverse weights use a product of at most \(k\) numerators, hence \(\widetilde O(k^2)\) bits, including on tapes where a cutoff weight is large: the rational representation is capped by Cramer/Hadamard size, not by the statistical magnitude. Zero estimates are not inverted. Sign of a group sum ignores positive common factors and \(1/m\). Per evaluation, schoolbook cost is \(\widetilde O(nk+k^3)\). With \(O(nk^2)\) prefix tests and \(O(k^4\log(nk/\beta))\) samples each, \(T\) rounds give \(\widetilde O(n^2k^7+nk^9)\) bit operations. Live storage of \(O(k^2)\) prefixes, \(O(k^2)\) streamed counters, \(k\) weights, and the current \(k\times k\) Gram is \(\widetilde O(nk^2+k^3)\). Rounds, batch sizes, prefix caps, and integer lengths are data-independent, so the caps hold on every measurement and random tape.

**Final check.** Distinct \(\{\pm1\}\)-valued functions with sparsity at most \(k\) disagree with probability at least \(1/(2k)\), because a difference has at most \(2k\) Fourier terms and infinity norm \(2\), so Cauchy–Schwarz yields \(\|d\|_2^2\ge 2/k\). Thus \(\lceil 2k\ln 100\rceil\) fresh labels accept a wrong Boolean candidate with probability at most \(1/100\). On the good event the last fit equals \(f\) exactly, the convolution test \(a^2=1\) passes, and validation matches every label. Validation is not what produces the \(0.94\).

**Small-\(k\) and log losses.** For \(k=1\), \(T=1\), \(\beta=1/200\), \(W<1/16<1\), and \(\tau=1/4=|c|/4\) for a parity. Ceiling in \(T\) only helps the energy drop. \(\log_2\) versus \(\ln\) multiplies some classical and validation counts by at most \(1/\ln 2\), which the \(O\) and \(\widetilde O\) notation absorbs. Search contributes no quantum \(n\)-factor. The hidden leading factor on \(q_e\) is enormous (order \(10^8\)–\(10^9\) before logarithms) because \(\varepsilon\sim\sqrt{\beta}/512\) and \(m=144k\), \(\tau^{-4}=(4k)^4\). That is compatible with the stated asymptotic claim; the manuscript already says the exponents are loose and not a practical runtime.

## Claims, attribution, and what was not verified

The proof’s own description of the mechanism matches the argument: residual-relative weights from a fresh label batch, an explicitly evaluable sign-majority, Kushilevitz–Mansour search only against that stored hypothesis, then a separate batch certifying candidates to the original target. Keeping the residual \(f-a\), rather than \(f-H\), is necessary in the proof because \(H\) is an arbitrary Boolean function of degree up to \(n\).

Access-model wording is consistent with the algorithm: supplied copies only, separate measurements, no membership queries to \(f\), no state-preparation inverse, and no claim about BPP versus BQP. Chosen-input access is correctly limited to \(H\).

Disclosure (author affiliation, Codex assistance, no funding claim, no peer review, CC BY 4.0, bounds not practical) is specific enough for a preprint. Internal checking mentioned in the last section is not independent evidence.

I do not treat the author source-comparison notes as evidence. From this packet alone I cannot verify:

- Ye’s sample bound, or the assertion that Ye’s dictionary has no fixed polynomial decoding;
- the Arunachalam–Chakraborty–Lee–Paraashar–de Wolf \(O(k^{3/2}\log^2 k)\) upper bound and the stated range of the \(\Omega(k\log k)\) lower bound;
- Caro et al., Corollary 10, including \(O(k^4\log(k^2/\delta))\) copies and polynomial time;
- the exact statements of Gopalan et al. Theorem 8.1 and Tropp Theorem 6.1(ii) and Corollary 5.2;
- novelty. The manuscript itself does not claim publication priority. “Complements Ye” and “neither polynomial time alone nor near-linear samples alone” are comparative sentences whose premises sit outside the proof.

Standard Fourier facts used as identities (Parseval, the prefix-energy formula, orthonormality of characters, exactness of a full-support least-squares fit) are derived or immediate in the text. The search lemma is self-contained; the Kushilevitz–Mansour citation is attribution, not a hidden black box.

No code was run, no cited source was opened, and no other project file was read.

## Blocker

No demonstrated blocker remains in the internal chain from the stated Bernstein, Chernoff, and \(1/k\) granularity inequalities through contraction, exact arithmetic, and the resource bounds. The Gram constant is the sensitive citation: it has no slack. Bernstein, Hoeffding, and the \(226/5184\) versus \(1/16\) contraction do have slack. If the three external inequalities hold as used, the theorem’s asymptotic claim stands. If the matrix-Chernoff or granularity constant is weaker than printed, the repair is a larger explicit leading factor in \(q_c\) or in \(g\) and \(T\), not a change of architecture.