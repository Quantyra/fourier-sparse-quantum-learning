**GO WITH NOTES.** The hashed decoder and its learner substitution are mathematically consistent with the stated cap, failure budget, sample bound, live space, and \(\widetilde O(n^2k^3+nk^5+k^7)\) bit time. No blocker and no required formula change.

Source SHA-256 (as supplied, not recomputed): `0f18f0b7e26495d2bf98dcf4d1f4a1fca5f8c219ca8e6de87e7ea5b6250a9476`

Scope: informal analytic review of the v0.4.0 pruned-hash decoder (Lemma `lem:search`) and its use in archive safety, contraction, samples, exact arithmetic, and resource caps. Not a formal certificate, not an implementation benchmark, and not a re-fetch of the cited pages.

## Blockers

None.

## Required revisions

None.

## Notes (optional exposition)

1. In “Recover original coordinate bits,” the sentence “either empirical projection errs by more than \(\tau/4\) with probability at most \(2e^{-7}\le 1/64\)” is ambiguous. The next sentence is the one the budget uses: the two-estimate union is at most \(1/32\). That union is valid because each marginal is at most \(2\exp(-M\tau^2/32)\le 2e^{-7}\le 1/64\). Minimal wording change: replace “either” by “each.”

2. In “Complete processing and storage,” the generic correction display is \(O(nJM(C_H+\cdots))\) while each correction row evaluates \(H\) twice. The factor \(2\) sits inside \(O(\cdot)\). The instantiated count \(2tN+2nJM\) is the one used for the theorem. Minimal display change: write \(2C_H\) in that generic correction bound.

3. Proposition `prop:contraction` still says “prefix search,” and the copy-count paragraph still says “prefix-search confidence.” Both statements remain true for this hash-prefix procedure, and neither log-\(n\) term enters the quantum-copy count. Optional alignment: say “hashed search.”

## Checked claims

**(1) Bucket and projection identities.** Equation `eq:bucket` is the standard character average. Expanding \(H\) and averaging \(x\) kills cross terms; averaging \(u\in\mathbb F_2^j\) (respectively \(\mathbb F_2^t\)) inserts the indicator \(B_js=v\) (respectively \(Bs=v\)). The average is over the full label space, so it does not need full rank, an inverse, or a coset representative. Dependent rows, \(t>n\), and infeasible \(v\) give energy or projection \(0\) on both sides. Collision probabilities stay \(2^{-t}\) for \(a\neq s\), including \(t>n\), because the \(t\) rows are independent and each nontrivial linear form is unbiased.

**(2) Frozen prefixes, coverage, overflow.** Counters are frozen before each depth batch and updated only after the batch, so Hoeffding applies conditional on \(B\) and the past. Summands lie in \([-1,1]\), and
\[
2\exp(-N\tau^4/32)\le 2e^{-L_0}\le\eta/(8tP)
\]
because \(L_0=\lceil\log_2(16tP/\eta)\rceil\ge\ln(16tP/\eta)\). At most \(2P\) labels are tested at a depth, so one depth contributes at most \(\eta/(4t)\), and \(t\) depths contribute at most \(\eta/4\). Unreached depths are counted as non-failures. On that event every heavy prefix has energy at least \(\tau^2\) and survives the inclusive threshold \(3\tau^2/4\); every retained bucket has energy at least \(\tau^2/2\). Same-depth buckets are disjoint and have total energy \(1\), so at most \(2/\tau^2\le P=\lceil 4/\tau^2\rceil\) survive. Overflow and a missed heavy index are both inside the inaccurate-estimate event. Only those \(O(P)\) children are tested; there is no \(2^t\)-label loop. The empty frontier cannot drop a heavy index on this event.

**(3) Heavy-only isolation.** Linearity gives \(\mathbb E_B T_s\le 2^{-t}\) despite dependent collisions. At most \(\tau^{-2}\) frequencies have magnitude at least \(\tau\). Markov plus that union is at most \(1024/(2^t\tau^4)\). The choice \(2^t\ge 4096/(\eta\tau^4)\) makes this at most \(\eta/4\). On the complement, heavy labels are distinct because another heavy mass is at least \(\tau^2>\tau^2/1024\). Light buckets are allowed to propose anything. Those proposals remain inside the output cap and are not given an isolation claim.

**(4) Shifted-sign recovery.** For a good hash, a surviving heavy label, and \(T_s\le\tau^2/1024\),
\[
\Pr_y[|r_s(y)|>\tau/4\text{ or }|r_s(y+e_i)|>\tau/4]\le 32T_s/\tau^2\le 1/32.
\]
Translation invariance gives the same second moment at \(y+e_i\); the residual need not be centered. The two empirical means share the \(M\) vectors \(u\) but are separate bounded averages, so Hoeffding is marginal and the union is at most \(1/32\). Thus a vote is wrong with probability at most \(1/16\). Off that event both estimates lie within \(\tau/2\) of \(d_s\chi_s\), hence keep its sign, including when the sum is nonzero. The sign product equals \(\chi_s(e_i)=(-1)^{s_i}\) because \(\operatorname{sgn}(d_s)^2=1\). Negative coefficients and the constant character are covered. A positive majority correctly writes bit \(0\); \(J\) odd avoids a tie. The \(J\) repetitions are independent given \(H\), \(B\), and the pruning transcript. For odd \(J\),
\[
2^J(1/16)^{\lceil J/2\rceil}=2^{-J-2}\le 2^{-J}\le\eta/(4nP).
\]
A union over at most \(nP\) heavy bits costs at most \(\eta/4\). Coordinates and labels may be dependent. The final check \(Bs_v=v\) keeps a correctly decoded heavy index and forces distinct outputs. Prune, hash, and correction add to at most \(3\eta/4\), with no correctness claim on the bad event. The argument is conditional on any history that fixes \(H\) before these coins. All queries are to \(H\).

**(5) Cap and learner substitution.** Non-failure output has size at most \(P\). Failure is mapped to \(L=\varnothing\), which is still a list of size at most \(P\). Specialized parameters match the lemma: \(\tau=1/(4k)\), \(P=64k^2\), \(t=\lceil\log_2(2^{24}k^4)\rceil\), \(L_0=\lceil\log_2(16384\,tk^2)\rceil\), \(N=8192k^4L_0\), \(M=3584k^2\), and \(2^J\ge 4096nk^2\). Search failure is at most \(3\rho/4\le\rho\) after \(H\) is fixed. Proposition `prop:contraction` may therefore keep charging one \(\rho\) in the existing four-event bound \(1-4\rho=3/4\). Safety (Proposition `prop:safety`) still applies to every list of size at most \(P\): light-bucket extras use the same fresh original-target test, false indices are rejected on the certificate event, and extra true admissions only decrease missing energy. The omitted-mass estimate \((16/9)\lVert H-f\rVert_2^2\le W/36\) still follows from \(|\widehat H(s)|<1/(4k)\le|c_s|/4\). No new all-search success event is required. Quantum copies stay \(O(k\log^2(2k))\); \(J\)’s \(\log(nk)\) multiplies evaluations of \(H\) only.

**(6) Resources.** One evaluation of \(H\) is \(\widetilde O(nk+k^3)\) at the stated weight length \(\widetilde O(k^2)\). Multiplying by \(2tN+2nJM\) produces \(\widetilde O(nk^5+k^7+n^2k^3)\). Separate charges close: pruning matrix-vector work \(\widetilde O(nk^4)\), pruning parity \(\widetilde O(k^6)\), correction matrix-vector work \(\widetilde O(n^2k^2)\), correction parity \(\widetilde O(nk^4)\), vote and hash checks inside those bounds, and \(M=3584k^2\ge P=64k^2\). Equation `eq:hashrandom` is the exact bit count of \(B\), the depth-\(j\) pairs, and the fresh correction strings, totaling \(\widetilde O(nk^4+n^2)\) over \(T\) trials, discarded row by row. Refits remain \(\widetilde O(k^6)\) per trial by the existing fraction-free bound, including singular and aborted tapes; \(T\) unsuccessful trials remain inside the tilde bound. Certification, grouping, inverse weights, Booleanity, and final validation are lower order. No \(P\)-column fit is formed after archive overflow. Live space stays \(\widetilde O(nk^2+k^3)\): hash rows \(O(n\log(2k))\), at most \(P\) decoded indices, logarithmic counters, \(\widetilde O(k)\)-bit certificate accumulators, and the reused \(\widetilde O(k^3)\) determinant workspace. Projection counters are integers of magnitude at most \(M\). No sample table is stored.

**(7) Attribution and limits.** The search proof is self-contained and does not import a runtime or all-survivor theorem. Kushilevitz–Mansour is used as the prefix-energy source; Datta et al. are named for hashed isolation and local correction. This review did not fetch those pages, so the specific pointer to Lemma 8 and Claims 12–15 is not reconfirmed here. It is not load-bearing. The text does not claim a new Fourier-search principle, a practical runtime, a better sample bound than the cited Ye version, noise robustness, or behavior past the sparsity promise. Dense \(H\), promise failure, and the noiseless supplied-example model are stated in the scope section.
