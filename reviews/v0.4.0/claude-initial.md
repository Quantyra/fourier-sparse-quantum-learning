# Focused review: P010 manuscript v0.4.0, hashed decoder and learner integration

**Source SHA-256 (as supplied, not recomputed):** `0f18f0b7e26495d2bf98dcf4d1f4a1fca5f8c219ca8e6de87e7ea5b6250a9476`

**Scope.** I reviewed by hand the complete v0.4.0 LaTeX and the v0.3.0→v0.4.0 diff you supplied. That covers Lemma `lem:search` and its proof, the "Complete processing and storage" paragraph, the specialization in §`sec:costs`, and how the lemma is used in Propositions `prop:safety` and `prop:contraction` and the main success proof. I did not edit files, run commands, delegate or fetch anything. In particular, I did not fetch Datta et al., KM or any other reference, so the attribution checks below only test internal consistency. This is an informal analytic check, not formal certification or a benchmark. Line numbers are approximate, counted from the diff hunk headers; labels and paragraph names are the reliable anchors.

---

## Verification of the requested checks

### (1) Bucket and projection identities: verified

- **First identity.** Write $H(x+w)=\sum_r d_r\chi_r(x)\chi_r(w)$ with $w=B_j^{\mathsf T}u$.
  - Averaging over $x$ forces $r=s$.
  - Then $\E_u(-1)^{u\cdot(B_js+v)}=[B_js=v]$, because $s\cdot B_j^{\mathsf T}u=u\cdot B_js$.
- **Second identity.** The same calculation with $y$ fixed gives it.
- **Dependent rows and $t>n$.** No rank or inverse is used anywhere.
- **Infeasible labels.** Both sides are $0$. Such labels are pruned on the accuracy event, since $0<3\tau^2/4-\tau^2/4$.

I found no counterexample for rank-deficient $B$ or for $t>n$. The case $t>n$ does occur here, since $t\approx24+4\log_2k$ while $n$ can be as small as $\log_2k$.

### (2) Frozen-prefix coverage and overflow: verified

- **Hoeffding bound.** Summands lie in $[-1,1]$, so the bound is $2\exp(-2N(\tau^2/4)^2/4)=2\exp(-N\tau^4/32)$.
  - $N\ge32\tau^{-4}L_0$ and $L_0\ge\log_2(\cdot)\ge\ln(\cdot)$ give $\le\eta/(8tP)$.
  - Summing over $2P$ labels and $t$ levels gives $\eta/4$, uniformly in $B$.
- **Freezing.** Each $C_j$ is frozen before its batch, and the next level's children are chosen only after the batch. So conditioning on "past, $B$" is legitimate.
- **Coverage and overflow.** On accuracy:
  - heavy prefixes have $E\ge\tau^2$ and survive;
  - survivors have $E\ge\tau^2/2$;
  - disjointness gives at most $2/\tau^2\le P$ survivors, so there is no overflow.
- **No full-bucket enumeration.** At most $2P$ labels are tested per level. The returned list has at most $P$ entries on every non-FAIL tape.

### (3) Heavy-only collision and Markov tail: verified

- **Collision probability.** For $a\ne s$, $\Pr[B(a+s)=0]=2^{-t}$ because rows are independent and uniform. This holds for any $n,t$.
- **Tail bound.** $\E T_s\le2^{-t}$. Markov at $\tau^2/1024$, a union over at most $\tau^{-2}$ heavy indices, and $2^t\ge4096/(\eta\tau^4)$ give $\le\eta/4$.
- **Distinct labels.** Two heavy indices sharing a label would force $T_s\ge\tau^2$, which the good event excludes.
- **Light buckets.** These are unconstrained. Their decoded indices are filtered only by $Bs_v=v$. They count against the cap of $P$ and are handled by certification.

### (4) Shifted-sign recovery: verified

- **Residual error.** Markov on $r_s$ at $y$ and at $y+e_i$ (each uniform) gives $\le32T_s/\tau^2\le1/32$.
- **Sampling error.** Hoeffding per projection gives $2e^{-7}\le1/64$. The union over the two correlated, shared-row estimates is $\le1/32$.
- **Sign correctness.** The total error is below $\tau/2<|d_s|$. So both signs are correct, and $\sgn(0)$ is never reached for a heavy label.
- **Bit extraction.** The product of the two signs is $\chi_s(e_i)$. This is correct for negative $d_s$ and for $s=0$.
- **Majority over repetitions.** Repetitions use fresh $y,u$, so they are independent given $(H,B,\text{transcript})$. The transcript only fixes $\mathcal C$.
  - $\binom{J}{\lceil J/2\rceil}(1/16)^{\lceil J/2\rceil}\le2^J4^{-J}=2^{-J}\le\eta/(4nP)$.
  - The union over at most $n\tau^{-2}\le nP$ heavy bits gives $\eta/4$.
- **Distinct output.** The final check $Bs_v=v$ makes outputs distinct and never removes a correctly decoded heavy index.

### (5) List cap, failure budget and substitution: verified

- **Failure.** The total is $3\eta/4=3\rho/4\le\rho$.
- **Cap.** The cap of $P$ holds on every tape, which is what `prop:safety` needs, and $q_c$ is already sized for $P$.
- **Progress.** `prop:contraction` uses only "every $|\widehat H(s)|\ge1/(4k)$ is listed". Extras are harmless under safety, and the staged union $1-4\rho$ is unchanged.

### (6) Resources: verified

**Evaluations.** $tN=\widetilde O(k^4)$ and $nJM=\widetilde O(nk^2)$. With $C_H=\widetilde O(nk+k^3)$ these cost $\widetilde O(nk^5+k^7)$ and $\widetilde O(n^2k^3+nk^5)$ respectively.

**Other per-trial search costs:**

| Item | Calculation | Cost |
|---|---|---|
| Pruning input/hash formation | $tN\cdot nt$ | $\widetilde O(nk^4)$ |
| Pruning label parity | $tN\cdot2P(t+h_s)$ | $\widetilde O(k^6)$ |
| Correction input/hash formation | $nJM\cdot nt$ | $\widetilde O(n^2k^2)$ |
| Correction label parity | $nJM\cdot P(t+h_s)$ | $\widetilde O(nk^4)$ |
| Votes | $nJPh_s$ | $\widetilde O(nk^2)$ |
| Final hash checks | $Pnt$ | $\widetilde O(nk^2)$ |

**Random bits.** The pruning term $N\sum_j(n+j)$ matches `eq:hashrandom`. The total is $\widetilde O(nk^4+n^2)$ per trial and also after the factor $T$.

**Live space.**
- Hash rows: $nt$.
- Labels and counters: $P(t+h_s)$.
- Decoded indices: $nP$.
- This gives $\widetilde O(nk^2)$, inside $\widetilde O(nk^2+k^3)$.
- `M ≥ P` holds generally, since $\lceil224\tau^{-2}\rceil\ge\lceil4\tau^{-2}\rceil$.

**Unchanged costs.** The fit $\widetilde O(k^6)$, certification $\widetilde O(nk^3+k^4)$, weights $\widetilde O(k^5)$ and Booleanity $\widetilde O(nk^2+k^4)$ all fit the new bound, and the factor $T$ costs only a logarithm.

**Specialized constants.** I re-derived all five: $t$ with argument $2^{24}k^4$, $L_0$ with argument $16384tk^2$, $N=8192k^4L_0$, $M=3584k^2$, and $2^J\ge4096nk^2$.

### (7) Attribution and limits: acceptable, with one consistency note (N1)

The scope and limitations section correctly disclaims practical runtime, sample optimality and novelty of the search principle. I cannot confirm the content of Datta et al. Lemma 8 and Claims 12–15 or the LIPIcs 364 bibliographic data.

---

## Findings by severity

**Blockers:** none.

**Major:** none.

**Minor**

- **N1. Attribution consistency (§1 "Prior work and comparison", ~line 62).** The ingredient list names "classical Fourier search~\cite{KM}" but omits Datta et al., which §4 credits for hashed isolation and local correction.
  - *Minimal fix:* "…and classical Fourier search~\cite{KM} with hashed isolation and local character correction~\cite{Datta} as attributed ingredients."
  - *Optional:* random linear bucketing with shifted-evaluation bit recovery is also standard in the sparse Walsh–Hadamard and sparse FFT literature. A one-clause "standard technique" acknowledgement would lower priority risk. No specific citation is required.
- **N2. Stale terminology.**
  - In `prop:contraction`, "Use failure budget $\rho$ in the proposal estimates, majority lemma and prefix search." *Fix:* "…and hashed search (Lemma~\ref{lem:search}, failure at most $3\rho/4$)."
  - In §`sec:costs`, before eq:copies ~line 405: "prefix-search confidence" should become "search confidence ($J$)".

**Cosmetic / optional exposition**

- **N3 (~line 458).** In $\widetilde O(nk^5+k^7+n^2k^3+nk^5)$ the $nk^5$ term is duplicated. *Fix:* $\widetilde O(n^2k^3+nk^5+k^7)$.
- **N4 (Recover paragraph, ~line 224).** "either empirical projection errs … with probability at most $2\exp(\cdot)\le1/64$" reads as a bound on the union. *Fix:* "each empirical projection errs … with probability at most …; their union is at most $1/32$."
- **N5 (Isolate paragraph, ~line 209).** Add the one-line reason for distinct heavy labels: "a shared label would give $T_s\ge d_{s'}^2\ge\tau^2$."
- **N6 (optional).** $2e^{-7}\approx0.0018$ against $1/64$ leaves slack, so $M$ could be smaller. This is harmless and is consistent with the "deliberately loose" disclaimer.

---

## Verdict: **GO WITH NOTES**

I attempted counterexamples for:
- rank-deficient $B$ and $t>n$;
- infeasible and empty labels;
- light-bucket false proposals;
- correlated shared-row projections;
- negative and constant characters;
- dependence between pruning and correction;
- the list cap on FAIL and non-FAIL tapes;
- cost or storage terms that might exceed the bound.

None of them holds. The bound $\widetilde O(n^2k^3+nk^5+k^7)$ time and $\widetilde O(nk^2+k^3)$ space follows as stated. N1–N2 are recommended before publication. N3–N6 are optional.
