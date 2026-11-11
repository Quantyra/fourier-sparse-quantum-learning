Local workstation file links were replaced with links to the archived input packet; substantive review text is unchanged.

### Source SHA-256 and Review Scope

* **Source SHA-256**: `9730a332f889842bf984999d1dd21c52a110a4ef7a9b079e7d6616e0a886a7ee`
* **Scope Reviewed**:
  * **Packet**: [`packet.txt`](initial-packet.txt)
  * **Manuscript**: Version 0.3.0 changes against v0.2.0 and complete source integration context.
  * **Core Sections**: Section 1 (main result, access model, contribution), Section 3 ([`lem:search`](initial-packet.txt) shared-batch heavy-spectrum search, bucket identity, Hoeffding bound, prefix sharing), Section 4 (hypothesis construction, cutoff, majority), Section 5 ([`prop:safety`](initial-packet.txt), [`prop:contraction`](initial-packet.txt), [`thm:main`](initial-packet.txt) proof, resource budgeting), Section 6 ([`sec:costs`](initial-packet.txt), fraction-free Bareiss elimination, intermediate determinant precision, live space, failure tape termination), Section 7 (limitations, verification status, disclosures), and references.

---

### Evaluation of Named Questions

#### 1. Freezing child tests, conditional Hoeffding, and union bounds under shared correlated triples
* **Conditional Hoeffding validity**: At depth $j$, freezing the set of candidate children $C_j$ (with $|C_j| \le 2P$) conditionally on the past history fixes both $C_j$ and $H$. For any individual child $u \in C_j$, the $N$ triples $(x_r, y_r, z_r)_{r=1}^N$ are independent across rows $r$. The summand $H(x_r, z_r)H(y_r, z_r)\chi_u(x_r+y_r)$ is bounded in $[-1, 1]$ (interval length 2) with mean $E_u$. Hoeffding’s two-sided inequality yields deviation bound $2\exp(-N t^2 / 2)$. At deviation $t = \tau^2/4$, this exponent is $-N\tau^4/32 \le -L_0 \le -\ln(4nP/\beta)$, bounding individual child failure by $\beta/(2nP)$.
* **Correlated estimates**: Children tested in the same batch share $(x_r, y_r, z_r)$, making child estimators $A_u/N$ mutually correlated. However, the union bound over $u \in C_j$ ($\sum_{u \in C_j} \beta/(2nP) \le 2P \cdot \beta/(2nP) = \beta/n$) requires no independence whatsoever among estimators.
* **Early termination**: If at any depth $j$ no child passes the energy threshold, $C_{j+1} = \emptyset$ and the algorithm terminates immediately returning $\emptyset$. The convention defining failure as false at unreached depths correctly maintains $\Pr[F_j \mid \mathcal{H}_{j-1}] \le \beta/n$ unconditionally. On the good accuracy event, every ancestor of an index with $|\widehat{H}(s)| \ge \tau$ has $E_u \ge \tau^2$, so $A_u/N \ge 3\tau^2/4$; thus an ancestor is never discarded, and early termination cannot occur if a heavy coefficient exists.
* **Good-event overflow**: On the accuracy event, every retained child satisfies $E_u \ge \tau^2/2$. Because distinct prefixes of length $j$ define disjoint cylinders in $\mathbb{F}_2^n$, Parseval gives $\sum_{u \in C_j, \text{retained}} E_u \le \sum_{u \in \mathbb{F}_2^j} E_u = 1$. The number of retained children cannot exceed $1/(\tau^2/2) = 2/\tau^2 \le P$. Thus, the capacity cap $|C_j| \le 2P$ and the retention cap $\le P$ never abort on the good event.

#### 2. Search interface preservation, exact recovery, and adaptive progress
* **Search interface compatibility**: [`lem:search`](initial-packet.txt) preserves the exact contract required by [`prop:contraction`](initial-packet.txt): it accepts black-box evaluation of deterministic $H$, rational threshold $\tau = 1/(4k)$, list cap $P = 64k^2$, and failure budget $\rho = 1/16$. It returns at most $P$ candidates or $\FAIL$, and with probability at least $1-\rho$, contains every $s$ with $|\widehat{H}(s)| \ge \tau$.
* **No Fourier sparsity assumed for $H$**: The search proof and correctness rely strictly on the bucket energy identity $E_u = \sum_v \widehat{H}(u, v)^2$ and $\norm{H}_2^2 = 1$. $H$ is permitted to have full degree $n$ and an exponentially dense Fourier spectrum; its evaluation cost remains polynomial ($\widetilde O(nk + k^3)$).
* **No conditioning on future safety**: The adaptive progress martingale construction in [`thm:main`](initial-packet.txt) tracks progress indicators $I_t$ conditionally on past filtration $\mathcal{F}_{t-1}$. Safety failure $B$ is bounded by a separate union bound ($2T\beta \le 1/100$) over first-failure times without conditioning on future trial safety.

#### 3. Accounting of $H$ evaluations, parities, randomness, and exact comparisons
* **Evaluations of $H$**: Evaluated only $2N$ times per depth batch across $n$ depths, totaling $2nN = \widetilde O(nk^4)$ evaluations per trial. At $\widetilde O(nk + k^3)$ bit ops per evaluation, the trial evaluation cost is $\widetilde O(n^2k^5 + nk^7)$.
* **Child parities**: Inner products $u \cdot (x+y)$ of length $j \le n$ are computed for each child and row: $n \cdot N \cdot (2P) \cdot n = \widetilde O(n^2 k^6)$ bit operations. Counter additions of $\pm 1$ require $O(\log N)$ bits each.
* **Randomness generation**: Drawing triples $(x, y, z)$ takes $j + j + (n-j) = n+j$ random bits per row. Over $n$ depths, $\sum_{j=1}^n (n+j) = (3n^2+n)/2$ bits per row, totaling $N(3n^2+n)/2 = \widetilde O(n^2k^4)$ bits per trial, generated and discarded row by row.
* **Comparisons**: Threshold checks $4A_u \ge 3\tau^2 N$ and certificate tests $z_s^2 > 4\gamma^2 v/k$ are cleared of rational denominators and evaluated as exact integer cross-products of bit length $\widetilde O(k)$, costing $\widetilde O(nk^2)$ across all tests.

#### 4. Fraction-free / Bareiss Cramer fit on singular and bad tapes
* **Bordered minors and division exactness**: The fraction-free update identity $M_{pp}M_{ij} - M_{ip}M_{pj} = d \det A[B \text{ bordered by } p,i \text{ and } p,j]$ follows from Sylvester's determinant theorem. Division by the previous pivot $d = \det B$ is exact over $\mathbb{Z}$. Every stored entry during elimination is an exact minor of the original Gram matrix of order $\le k$.
* **Size of intermediate integers**: Because entries of $A_U^\top A_U$ and $A_U^\top y$ are bounded in $[-q_c, q_c]$, Hadamard's bound limits any order-$m$ minor ($m \le k$) to $k! q_c^k$. Intermediate integers and temporary multiplication products have length $O(b_a) = O(k \log(2kq_c)) = \widetilde O(k)$ bits.
* **Singular and unsuccessful tapes**: If column pivots vanish, Bareiss elimination terminates with determinant 0 and returns $\FAIL$. No division by zero occurs. The dimension cap $|U| \le k$ is enforced prior to forming the Gram system, preventing $P \times P$ expansion. Sequential computation of $k+1$ determinants reuses working memory, bounding determinant space to $O(k^2 b_a) = \widetilde O(k^3)$ bits. Each refit uses original labels $f(X_j)$, resetting precision so denominators do not compound across trials.

#### 5. Preservation of copy complexity and space bounds under $\widetilde O(n^2k^6 + nk^7)$ runtime
* **Sample complexity**: Lemma 4 classical search queries only the synthetic hypothesis $H$ and consumes zero quantum copies. The copy count is determined strictly by $T$ trials of $q_e + 4gm + q_c$ plus validation, retaining $O(k \log^2(2k))$ copies.
* **Bit time**: Evaluator sharing lowers $H$ evaluation cost from $\widetilde O(n^2k^7 + nk^9)$ to $\widetilde O(n^2k^5 + nk^7)$, leaving explicit child parities at $\widetilde O(n^2k^6)$ and refits at $\widetilde O(k^6)$. The total classical bit time is $\widetilde O(n^2k^6 + nk^7)$.
* **Live space**: Search rows are discarded after updating counters; search requires $O(nP + P\log N) = \widetilde O(nk^2)$ bits. Group weights require $\widetilde O(k^3)$ bits, certificate accumulators require $P \cdot \widetilde O(k) = \widetilde O(k^3)$ bits, and Bareiss elimination reuses an $\widetilde O(k^3)$-bit workspace. Total live space is strictly preserved at $\widetilde O(nk^2 + k^3)$ bits.

#### 6. Attribution, novelty, and practical-performance boundaries
* **Attributions**: Bareiss (1968, fraction-free elimination), Kushilevitz–Mansour (1993, heavy Fourier search), Tropp (2012, matrix Chernoff & Bernstein), Gopalan et al. (GOSSW 2011, Boolean granularity), Arunachalam et al. (ACLPW 2021), and Caro et al. (2024) are accurately cited with appropriate interfaces.
* **Comparison with Ye (2026)**: The manuscript explicitly acknowledges that Ye's sample bound $O(k \log^2 k / \log\log k)$ is smaller than the $O(k \log^2(2k))$ bound proved here, clarifying that Ye's theorem establishes sample complexity without an asserted fixed-polynomial runtime bound.
* **Boundaries**: The text explicitly disclaims practical running times, optimal logarithmic factors, quantum state-preparation costs, BPP/BQP implications, or general classical simulation.

---

### Findings by Severity

#### Blocking Findings
* **None**. All mathematical derivations, probability bounds, resource scalings, and algorithmic mechanisms are sound.

#### Minor / Editorial Findings

1. **Duplicate Paragraph Heading**
   * **Location**: [`packet.txt` lines 254–255](initial-packet.txt) (also visible in diff lines 39–41).
   * **Issue**: The text contains two consecutive paragraph commands:
     ```latex
     \paragraph{Revision scope.}
     \paragraph{Version history.}
     Version~0.1.0 used $O(k\log^3(2k))$ copies...
     ```
   * **Reasoning**: In v0.2.0 the header was `\paragraph{Revision scope.}`. In v0.3.0, `\paragraph{Version history.}` was added without removing `\paragraph{Revision scope.}`, resulting in an empty orphan paragraph header in the compiled document.
   * **Minimal Correction**:
     ```diff
     --- a/main.tex
     +++ b/main.tex
     @@ -254,2 +254,1 @@
     -\paragraph{Revision scope.}
      \paragraph{Version history.}
     ```

2. **Clarification of Boundary Random Bits at $j=n$**
   * **Location**: [`lem:search`](initial-packet.txt) & [`packet.txt` line 377](initial-packet.txt).
   * **Issue**: At depth $j=n$, the suffix $z \in \mathbb{F}_2^{n-j}$ is 0-bit (empty), so the row requires $n + j = 2n$ bits for $x, y$. The formula $\sum_{j=1}^n (n+j) = (3n^2+n)/2$ is exact, but noting $(n-j=0 \text{ when } j=n)$ clarifies the edge case for readers verifying the suffix distribution.
   * **Minimal Correction**: None required; purely expository.

---

### Final Verdict

**GO WITH NOTES**

The v0.3.0 changes are mathematically rigorous, algorithmically complete, and properly bounded. The sharpening of classical bit time to $\widetilde O(n^2k^6 + nk^7)$ through depth-shared evaluations correctly charges all child parities and arithmetic without compromising sample complexity, live space, or proof architecture. The only recommended edit is removing the duplicate `\paragraph{Revision scope.}` header before final release.
