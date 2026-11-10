# Focused Revision Check (baseline 69dfe76 → revised main.tex 91aadd7a…)

## Verdict: **GO WITH NOTES**

**No blocker remains.** The changes fix my F1 (distinct-index abort scope) and F7 (refit wording). They supply the missing computations from F4 and F5, and they reword F2 to a statement about what Ye's paper states rather than what its method cannot do. I found no new mathematical error in the changed text.

## Checks of the changed mathematics

**Granularity (§2).** The revision uses $2^{1-\lfloor\log_2 s_0\rfloor}\ge2^{1-\log_2 s_0}=2/s_0\ge1/k$, since $s_0\le k$. ✓ This now uses the floor form, which is stronger than the ceiling form I noted. I did not verify the source statement myself (see Limits). Even under the ceiling form, the conclusion $|c_s|>1/s_0$ would still hold, as noted in my initial review.

**Lemma 2 (Bernstein).**
- Centered bound: $(\sqrt{2k}+1)e\le(\sqrt2+1)\sqrt k\,e\le3\sqrt k\,e$. ✓
- Coefficient denominator: $e^2+3\sqrt k\,e\cdot\varepsilon e/(3\sqrt k)=e^2(1+\varepsilon)\le2e^2$. The exponent is $q\varepsilon^2/(4k)$. ✓
- Variance-estimate denominator: $2\big(3ke^4+3ke^2\cdot\tfrac{e^2}{2}/3\big)=7ke^4$. With $t^2=e^4/4$ this gives $q/(28k)$. ✓
- Union bound: $P$ coefficient terms are each $\le2e^{-8L_0}\le2e^{-L_0}$, and the one variance term is $\le2e^{-L_0}$. The total is $\le2(P+1)\cdot\beta/(4(P+1))=\beta/2$. ✓

**Lemma 4 (Chernoff).**
- Summands are PSD with $\lambda_{\max}=p$ and expected sum $qI_p$, so the exponent $\mu/R=q/p$ is correct. ✓
- $\tfrac{d}{d\delta}[\delta+(1-\delta)\ln(1-\delta)]=-\ln(1-\delta)\ge\delta$. Integrating gives $\ge\delta^2/2$. ✓
- $\tfrac{d}{d\delta}[(1+\delta)\ln(1+\delta)-\delta]=\ln(1+\delta)\ge\delta-\delta^2/2$. Integrating gives $\delta^2/2-\delta^3/6\ge\delta^2/3$ for $\delta\le1$. ✓
- The lower tail $pe^{-q\delta^2/(2p)}$ is at most $pe^{-q\delta^2/(3p)}$, so summing the two tails gives the stated bound. ✓
- Restricting to $\delta<1$ is harmless at $\delta=1/10$.
- Monotonicity of $300p\ln(2p/\beta)$ in $p$: both factors are positive and increasing because $\beta<1$. ✓
- Renaming $v(X)$ to $\phi(X)$ removes the clash with the statistic $v$. ✓

**Lemma 6 (Hoeffding).** For range 2, $2\exp(-2Nt^2/4)=2\exp(-Nt^2/2)$. At $t=\tau^2/4$ this is $2\exp(-N\tau^4/32)$. ✓ The abort now explicitly returns FAIL. ✓

**Lemma 7.** The pass and fail sets partition $S$, so the total squared error is $36|S|\Delta^2\le36\varepsilon^2e^2$. ✓

**Proposition 10 (flags).**
- $gm/4=144kg/4=36kg\ge g$. ✓
- $2^g\ge512k^2/\beta>1/\beta$, so $g\ge\log_2(1/\beta)\ge\ln(1/\beta)$. ✓
- So $e^{-gm/4}\le\beta$. ✓

## Checks of algorithm and access changes

- **Step 2 (F1).** Flag-zero outcomes, which are always $s=0$, are now discarded, and the cap counts only the $gm$ grouped indices. The $k=1$, $f=\chi_a$ spurious-FAIL reading is eliminated. The §6 sentence now matches, so the cap never fires on ideal inputs. ✓
- **Step 4 (F7).** The refit now uses $f(X_\ell)$ from the same certification batch on the updated archive. This matches Proposition 10's use of the full-support Gram event. ✓
- **Abort rules.** "Every abort below returns FAIL" makes the abort rules uniform. The resource and every-tape argument is unaffected. ✓
- **Access model (F9).** The new sentence saying that after measurement the data are uniform labeled examples plus Fourier samples with law $c_s^2$ is accurate. ✓
- **Undefined jargon (F8).** The "clipping defect" sentence is removed. The replacement sentence is accurate and makes no new claim. ✓
- **Recurrence and resources.** The unchanged sample counts, recurrence, success bound and resource theorem are consistent with the edits: no parameter changed.

## Claims and attribution

**Ye.** The text now says Theorem 1.1 "does not state" a polynomial computation bound and that "we do not assert a computational lower bound." This is the appropriate form, and it resolves the wording problem in F2.

*Note:* the abstract (unchanged) still says the work "complements the smaller sample bound of Ye by supplying a fixed polynomial computational guarantee." I read that as consistent with the new §1 wording, since it claims only that this paper supplies such a guarantee. For uniformity, consider "a stated fixed polynomial computational guarantee."

**Disclosure.**
- The ambiguous funding sentence is removed, which is acceptable. A positive statement would be clearer if one is true.
- The new provenance sentence ("separate model reviews through Grok, Claude and AGY") is a factual claim about review history that I cannot verify. It should not be read as an endorsement. The paper's following sentence already disclaims peer review and certification, which is adequate.

## Items not addressed (non-blocking, informational)

- **F6, partly addressed.** $P$ is still used for both the estimator list size and $64k^2$, though "list-size argument $k$" now disambiguates. $N$ is still overloaded.
- **F10.** There is no remark about the very large constants (about $2\times10^{10}$ copies at $k=1$).
- **F12.** $S_0=S\cup\{0\}$ is still unexplained. It is harmless.

## Limits of verification

- I did not access GOSSW, Tropp or Ye. The coordinator's source notes are relayed claims, not evidence I could inspect:
  - the GOSSW Theorem 8.1 floor form on p. 21;
  - Tropp Theorem 6.1(ii) being the $\sigma^2+Rt/3$ form, and Corollary 5.2's factors;
  - Ye's Theorem 1.1 and Algorithms 1–2 content.
- Ye postdates my knowledge cutoff.
- The changed derivations above are internally correct regardless of these pinpoints, because each is now displayed in full.
- I checked only the diff against my earlier full audit. My conclusions rest on hand derivation, not on agreement with any other model's review.