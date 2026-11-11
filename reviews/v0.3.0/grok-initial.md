The designated source SHA-256 is `9730a332f889842bf984999d1dd21c52a110a4ef7a9b079e7d6616e0a886a7ee`. The digest was not recomputed; no commands, files, delegates, or external sources were used. The review covers the pasted v0.3.0 manuscript, including the search, progress, and cost integration against the unchanged learner.

**Verdict: GO WITH NOTES.** No blocking mathematical or resource error. The six named claims hold as written.

## Named questions

**(1) Frozen-batch Hoeffding.** Valid, including correlation, early exit, and overflow.

At depth \(j\), \(C_j\) and \(H\) are fixed before the \(N\) fresh rows. For each frozen child the summands are i.i.d. in \(\{-1,1\}\) and unbiased for \(E_u\). Hoeffding’s two-sided bound on an interval of length 2 is \(2\exp(-Nt^2/2)\). With \(t=\tau^2/4\) and
\[
N=\lceil 32\tau^{-4}L_0\rceil,\qquad L_0=\lceil\log_2(4nP/\beta)\rceil,
\]
one has \(N\tau^4/32\ge L_0\). Since \(\log_2 Z=\ln Z/\ln 2\ge\ln Z\), \(L_0\ge\ln(4nP/\beta)\), so each child fails with conditional probability at most \(\beta/(2nP)\). Correlation across children is irrelevant to this marginal bound. A union over \(|C_j|\le 2P\) is at most \(\beta/n\).

Unreached depths after `FAIL` or an empty frontier contribute indicator zero. The tower property gives unconditional depth-failure at most \(\beta/n\), hence at most \(\beta\) over \(n\) depths, without conditioning on future batches.

On simultaneous accuracy, every ancestor of a coefficient of magnitude at least \(\tau\) has energy at least \(\tau^2\) and is kept; every kept bucket has energy at least \(\tau^2/2\). Same-length prefixes are disjoint and total energy is 1, so at most \(2/\tau^2\le P=\lceil 4/\tau^2\rceil\) survive. The cap is “exceeds \(P\)”, so it does not fire on the good event, and an empty frontier cannot drop a heavy index. Algorithm `FAIL` or a missed heavy index is contained in the inaccurate-batch event.

**(2) Constant-confidence interface.** Preserved. Lemma (Shared-batch heavy-spectrum search) still returns at most \(P\) indices, or `FAIL`, and includes every \(|\widehat H|\ge\tau\), with conditional probability at least \(1-\rho\). Density of \(H\) is allowed: at most \(1/\tau^2\) coefficients can meet that threshold, and the bucket cap \(2/\tau^2\le P\) does not use sparsity of \(H\).

Proposition (Constant conditional progress) still charges four proposal failures by a staged union bound, at most \(4\rho=1/4\), then fresh \(C\cap G\) at most \(2\beta\). Safety is not assumed for the whole future. The indicators \(I_t\) are 1 by convention after a safety failure or after \(W=0\); otherwise the conditional success probability is at least \(3/4-2\beta\ge 1/2\). The supermartingale bound \(\Pr(Z_T<\ell)<1/4\) and \(\Pr(B)\le 1/100\) still give success greater than \(37/50>2/3\). A global abort still implies a safety failure. Changed list law does not enter the argument beyond this interface.

**(3) Charging.** Complete. Per trial the manuscript uses \(2nN\) evaluations of \(H\), not \(N\) per child. With \(N=8192k^4\lceil\log_2(4096nk^2)\rceil\), which matches \(\lceil 32\tau^{-4}L_0\rceil\) at \(\tau=1/(4k)\), \(P=64k^2\), and \(\rho=1/16\), those evaluations are \(\widetilde O(n^2k^5+nk^7)\). Child parities are a separate \(\widetilde O(n^2k^6)\) scan. Randomness \(TN(3n^2+n)/2=\widetilde O(n^2k^4)\) matches \(\sum_{j=1}^n(n+j)\). Threshold cross-multiples, prefix copies, residual and certificate arithmetic, the \(k+1\) determinants, and the final \(k^2\) convolution products are all inside \(\widetilde O(n^2k^6+nk^7)\) for \(n,k\ge 1\). The factor \(T=O(\log(2k))\) is absorbed by the stated tilde convention.

**(4) Fraction-free fit.** The bit bound holds on every tape. Gram and right-hand side entries are integers bounded by \(q_c\). Every minor of order at most \(k\) has magnitude at most \(k!\,q_c^k\), hence bit length \(b_a=O(k\log(2kq_c))=\widetilde O(k)\), whether or not the tape is singular or statistically good. The displayed Sylvester step
\[
M_{pp}M_{ij}-M_{ip}M_{pj}=d\cdot\det(\text{double border})
\]
is the correct one-step Bareiss identity, with empty pivot 1, so the division is exact while a pivot exists. A zero pivot returns `FAIL` on a nonempty fit. Products of two minors have \(O(b_a)\) bits. One determinant is \(O(k^3b_a^2)\) time and \(O(k^2b_a)\) bits; \(k+1\) sequential determinants, reusing workspace, are \(\widetilde O(k^6)\) time and \(\widetilde O(k^3)\) space. Refits use original labels, so denominators reset. Residual, estimate, certificate, norm, and Booleanity cross-products stay the same order of bits.

**(5) Global resources.** The new bit-time bound does not change the copy or space claims. Quantum copies remain
\[
T(q_e+4gm+q_c)+\lceil 2k\ln 100\rceil=O(k\log^2(2k)),
\]
because the extra \(\log(nk)\) search confidence is classical work on \(H\). Live space stays \(\widetilde O(nk^2+k^3)\): \(O(P)\) prefixes, \(O(\log N)\)-bit counters, \(\widetilde O(k)\)-bit certificate accumulators, group weights of total \(\widetilde O(k^3)\) bits, reused determinant workspace \(\widetilde O(k^3)\), and final \(k^2\) keyed products. Rows are discarded; there is no \(N\)-row table and no \(P\)-column fit. Caps apply on abort, singular, empty, and inaccurate tapes.

**(6) Boundaries.** Internally consistent. The manuscript attributes the smaller sample bound to the cited Ye version, polynomial-time exact learning with more copies to Caro et al., granularity to GOSSW, concentration to Tropp, prefix energy to Kushilevitz–Mansour, and integer-preserving elimination to Bareiss. It states the joint near-linear-copy plus polynomial-bit guarantee, and it explicitly declines a new search principle, a practical runtime, a logarithmic-factor optimum, a computational lower bound for Ye, and peer-review or machine-checked status. Citation contents were not re-fetched.

## Notes (non-blocking)

- After “Mechanism”, `\paragraph{Revision scope.}` is empty and is immediately followed by `\paragraph{Version history.}`. Delete the empty heading.
- In the search proof, the step \(L_0\ge\ln(4nP/\beta)\) is true but compressed. One line, \(\log_2 Z=\ln Z/\ln 2\ge\ln Z\), would stop a base-of-log misreading. No constant change is required.
- Partial-pivoting sign tracking is asserted from the Sylvester step rather than written as a full induction. The minor-size and Cramer bounds do not depend on expanding that bookkeeping.

No formula, sample count, or resource exponent needs correction.
