**GO WITH NOTES.** Supplied source SHA-256 (not recomputed): `f82d438e4989f90d8334701c62bade11e8b87cdf9ec849a991e3b214e67b07c7`.

**Scope.** AI reading of the supplied final `main.tex` and the four-hunk initial-to-final diff only. No edits, execution, delegation, or external lookup. Informal analytic check of the learning argument and resource caps. The loose `M` and the duplicated `nk^5` evaluation display are treated as intentional.

**Blocking / major.** None. No algorithm, constant, theorem statement, or probability interface in the diff changes the proof, and the v0.4.0 mechanisms below close as written.

**Checked mechanisms.**

- Dependent hash rows are allowed, including `t>n`. Bucket and projection identities are averages over the full label space. For `a≠s`, each independent uniform row collides with probability `1/2`, so `Pr[Ba=Bs]=2^{-t}` and `E[T_s]≤2^{-t}`.
- Heavy-only isolation is a Markov bound on `T_s`, union-bounded over at most `τ^{-2}` heavy frequencies, giving probability at most `η/4`. The new sentence is the right distinct-label reason: a second heavy `s'` in the bucket would put `T_s≥d_{s'}^2≥τ^2`, which is outside `T_s≤τ^2/1024`. Light buckets may propose anything.
- Shifted signs survive correlated projections. Residual Markov gives `Pr_y[|r_s(y)| or |r_s(y+e_i)| > τ/4]≤1/32`. The revised wording assigns `2exp(-Mτ^2/32)≤1/64` to each average; the same-`u` pair is then union-bounded by `1/32` without independence. On the complement, both estimates sit within `τ/2` of a term of magnitude at least `τ`, so the sign product is `χ_s(e_i)`, including negative and constant characters. A vote is wrong with probability at most `1/16`.
- The `J` repetitions are fresh given `H`, `B`, and the pruning transcript. The odd-`J` majority bound is at most `2^{-J}≤η/(4nP)`, and `nP` heavy bits cost at most `η/4`. Pruning, hash, and correction sum to `3η/4`.
- Every tape keeps `|C_j|≤2P`, stops at overflow, returns at most `P` indices, and drops hash mismatches. Distinct retained labels cannot decode to the same index. With `η=ρ`, search failure is at most `3ρ/4≤ρ`. Proposition 2 still spends a full `ρ` on that event inside `1-4ρ=3/4`.
- Instantiated parameters match the lemma: `τ=1/(4k)`, `P=64k^2=4/τ^2`, `t`, `L_0`, `N=8192k^4 L_0`, `M=3584k^2`, and `2^J≥4096nk^2`. The two-evaluation count `2tN+2nJM`, with one `H` evaluation `Õ(nk+k^3)`, is `Õ(nk^5+k^7+n^2k^3)`. Prefix and correction formation and parity scans fit the same envelope. Live space stays `Õ(nk^2+k^3)`: capped labels, logarithmic counters, no sample table, determinant workspace `Õ(k^3)`. The `log n` in `J` is classical `H` work and is outside the copy count.

**Diff wording.** Datta is named for hashed isolation and local character correction; the search proof remains self-contained. “Each” projection matches the following `1/32` union. The contraction proof names Lemma search and its `3ρ/4` failure, and the copy paragraph correctly attributes `log n` to `J`.

**Note (non-blocking, pre-existing, outside the diff).** In the residual-estimate proof, the written energy tail `2exp(-q/(28k))` does not match that proof’s own Bernstein form together with the loosened denominator `7ke^4`; that pair gives `q/(56k)`. The coefficient half is consistent. The infinity bound `‖r‖_∞≤√(2k)e` already stated in the same proof restores an energy exponent at least `3q/(56k)≥(12/7)L_0` for every `ε≤1`. Both theorem call sites are far inside that region (`ε=1/2048` and `γ=1/32`). The stated budgets and `1-β` uses remain valid.
