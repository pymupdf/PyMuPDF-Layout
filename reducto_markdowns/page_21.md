Now I present the constrained optimization procedure to compute the sharp lower bound under MTR. I pay particular attention to the special case where \( a_{k+1}-a_{k}=\delta \) for each integer \( k \) at the optimum. In this case, the lower bound reduces to

\[
\operatorname{sup} \sum \max \left(F_{1}\left(y+(k+1) \delta\right)-F_{0}\left(y+k \delta\right), 0\right),
\]

and computation of (B.1) poses a simple one-dimensional optimization problem.
Let

\[
V(\delta)=\sup _{0 \leq y \leq \delta} \sum_{k=-\infty}^{\infty} \max \left(F_{1}\left(y+(k+1) \delta\right)-F_{0}\left(y+k \delta\right), 0\right),
\]
and
\[
V_{K}(\delta)=\max _{y \in\left\{y^{*}+k \delta\right\}_{k=-\infty}^{\infty}} \sum_{k=-K}^{K} \max \left(F_{1}\left(y+(k+1) \delta\right)-F_{0}\left(y+k \delta\right), 0\right),
\]
where \( y^{*} \in \arg \max \sum_{k=-\infty}^{\infty} \max \left(F_{1}\left(y+(k+1) \delta\right)-F_{0}\left(y+k \delta\right), 0\right) \) and \( K \) is a nonnegative integer.

Step 1. Compute \( V(\delta) \).

Step 2. To further reduce computational costs, set \( K \) to be a nonnegative integer satisfying \( \left|V(\delta)-V_{K}(\delta)\right|< \) \( \varepsilon \) for small \( \varepsilon>0 .^{24} \)

Step 3. For \( J=K \), solve the following optimization problem:

\[
\operatorname{sup}_{\left\{a_{k}\right\}_{k=-J}^{J} \in \mathcal{S}_{\delta}^{J, K}(\widehat{y})} \sum_{k=-J}^{\max }\left\{F_{1}\left(a_{k+1}\right)-F_{0}\left(a_{k}\right), 0\right\},
\]
where
\[
\mathcal{S}_{\delta}^{J, K}(y)=\left\{\left\{a_{k}\right\}_{k=-J}^{J} ; a_{J} \leq y+K \delta, a_{-J} \geq y-K \delta, 0 \leq a_{k+1}-a_{k} \leq \delta,\right.
\]
\[
\delta<a_{k+2}-a_{k} \text { for each integer } k\right\},
\]
\[
\widehat{y}=\underset{y \in\left\{y^{*}+k \delta\right\}_{k=-\infty}^{\infty} k=-K}{\arg \max } \sum_{k=-K}^{K} \max \left(F_{1}\left(y+(k+1) \delta\right)-F_{0}\left(y+k \delta\right), 0\right) .
\]

Step 4. Repeat Step 3 for \( J=K+1, \ldots, 2 K .^{25} \)

It is not straightforward to solve the problem (B.2) numerically in Step 3; the function \( \max \{x,0\} \) is non-differentiable. Furthermore in practice, marginal distribution functions are often estimated in a complicated

\( { }^{24} \mathrm{I} \) put \( \varepsilon=10^{-5} \) for the implementation in Section 4 and Section 5.

\( { }^{25} \) By Lemma B.1, I considered \( J=K, K+1, \ldots, 2 K \) for the sequence \( \left\{a_{k}\right\}_{k=-J}^{J} \) and compared the values of local maxima achieved by \( \left\{a_{k}\right\}_{k=-J}^{J} \) with \( V_{K}(\delta) \)

74

=