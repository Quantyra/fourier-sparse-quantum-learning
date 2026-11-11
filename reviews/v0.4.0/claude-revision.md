# P010 v0.4.0: focused final-source check

**Source SHA-256 (as supplied, not recomputed):** `f82d438e4989f90d8334701c62bade11e8b87cdf9ec849a991e3b214e67b07c7`

**Scope:** I read the complete final LaTeX and the exact initial-to-final diff. I made no edits, ran no commands, used no delegation and accessed no external sources. I used the source assessment only as context and did not fetch or validate any reference. This is an AI review of an informal analytic theorem. It is not human peer review, formal certification or a learner benchmark.

## Blocking-issue checks

**Dependent hashes.** The two identities in `eq:bucket` average over the full label-parameter space ($u\in\F_2^j$ or $\F_2^t$). This gives the indicator $B_js=v$ without assuming rank, without coset representatives and for infeasible labels too. The collision probability $\Pr[Ba=Bs]=2^{-t}$ for $a\ne s$ needs only that the rows are independent and uniform, so it holds even when $t>n$.
*No issue.*

**Pruning.** The Hoeffding bound for $[-1,1]$ summands at deviation $\tau^2/4$ is $2e^{-N\tau^4/32}$. With the stated $N$, this is $2e^{-L_0}\le\eta/(8tP)$.
- A union bound over at most $2P$ labels per level and $t$ levels gives $\eta/4$.
- Heavy prefixes have energy at least $\tau^2$, so on the accuracy event they survive.
- Survivors have energy at least $\tau^2/2$, so there are at most $2/\tau^2\le P$ of them and overflow cannot occur.
- The staged conditioning (later levels' tests are chosen only after the current batch completes) is handled correctly.

*No issue.*

**Heavy-only tail isolation.** Markov gives $\Pr[T_s>\tau^2/1024]\le1024/(2^t\tau^2)$. A union bound over at most $\tau^{-2}$ heavy coefficients gives $1024/(2^t\tau^4)$. The choice $t=\lceil\log_2(4096/(\eta\tau^4))\rceil$ makes this at most $\eta/4$.
- The new distinct-heavy-label sentence is correct: a collision with another heavy $s'$ forces $T_s\ge\tau^2>\tau^2/1024$.
- Light buckets are correctly left unconstrained, because certification absorbs any extra proposals they produce.

*No issue.*

**Shifted-sign correction with correlated projections.**
- Markov on $r_s$ at the two uniform points $y$ and $y+e_i$ gives at most $32T_s/\tau^2\le1/32$. Mean-zero residuals are correctly not assumed.
- Each empirical projection is a mean of $M$ terms in $\pm1$ with mean $\mathcal P_v(\cdot)$. Hoeffding at $\tau/4$ gives $2e^{-M\tau^2/32}\le2e^{-7}\le1/64$.
- Because the two projections share rows, a union bound (not independence) gives $1/32$, so a vote is wrong with probability at most $1/16$.
- On the good event each estimate is within $\tau/2$ of $d_s\chi_s$ with $|d_s|\ge\tau$. Both signs are therefore correct and nonzero, and their product is $\chi_s(e_i)$. This covers negative coefficients and $s=0$.

The revised wording ("each empirical projection … ; their failure union is at most $1/32$") now states this correctly. *No issue.*

**Fresh repetition independence.** The $J$ repetitions use fresh $(y,u)$. They are therefore independent conditional on $H$, $B$ and the pruning transcript, for a fixed label and coordinate.
- The majority bound is $2^J(1/16)^{\lceil J/2\rceil}\le2^{-J}\le\eta/(4nP)$.
- A union bound over at most $nP$ heavy bits gives $\eta/4$, without needing cross-coordinate or cross-label independence.
- The three budgets total $3\eta/4$, and the proposition correctly cites search failure as $3\rho/4\le\rho$.

*No issue.*

**All-tape list caps.** Every tape stays within the stated caps:
- $|C_j|\le2P$ through the overflow $\FAIL$ rule.
- $|\mathcal C|\le P$.
- The $Bs_v=v$ filter makes the output indices distinct, giving at most $P$ outputs.
- Projection counters are bounded by $M$.
- Trial, batch and archive caps are explicit.

*No issue.*

**Full bit and space costs.** I rechecked each term:

| Cost component | Bound |
|---|---|
| Pruning evaluations, $tN\cdot\widetilde O(nk+k^3)$ | $\widetilde O(nk^5+k^7)$ |
| Correction evaluations, $nJM\cdot\widetilde O(nk+k^3)$ | $\widetilde O(n^2k^3+nk^5)$ |
| Pruning label-parity scans, $tN\cdot P$ | $\widetilde O(k^6)$ |
| Correction label-parity scans, $nJM\cdot P$ | $\widetilde O(nk^4)$ |
| Pruning hash-vector formation | $\widetilde O(nk^4)$ |
| Correction hash-vector formation | $\widetilde O(n^2k^2)$ |
| Live space, $P(n+t+h_s)$ | $\widetilde O(nk^2)$ |
| Random bits | $\widetilde O(nk^4+n^2)$ |

All of these lie within `eq:resources`. The separate two-product evaluation display, which repeats $nk^5$, is redundant but correct, and was retained intentionally. *No issue.*

## Precise changes

1. **Datta attribution in the introduction.** It now matches the Section 3 attribution (hashed isolation and local character correction, Lemma 8 and Claims 12–15). It does not overclaim a runtime transfer. **Correct.**
2. **Distinct-heavy-label justification.** The added sentence is valid and closes the previously implicit step. **Correct.**
3. **Each-projection versus union wording.** The text now separates the per-projection bound ($1/64$) from the union bound ($1/32$), and the arithmetic matches. **Correct.**
4. **Hashed-search confidence terminology.** The proposition now names Lemma `lem:search` with failure $3\rho/4$. Section 6 now correctly attributes the $\log n$ to the repetition count $J$, whose evaluations are of $H$, so it does not enter the copy count. **Correct.**

No algorithm, constant, theorem statement or probability interface changed in the diff.

## Findings by severity

- **Blocking:** none.
- **Major:** none.
- **Minor or editorial (optional, non-blocking):**
  - $M=\lceil224\tau^{-2}\rceil$ is looser than needed. This is intentionally retained.
  - The duplicated $nk^5$ term in the evaluation-cost display is intentionally retained.

## Verdict: **GO**
