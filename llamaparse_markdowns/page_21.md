
Now I present the constrained optimization procedure to compute the sharp lower bound under MTR. I pay particular attention to the special case where \(a_{k+1} - a_k = \delta\) for each integer \(k\) at the optimum. In this case, the lower bound reduces to

$$
\sup_{0 \leq y \leq \delta} \sum_{k=-\infty}^{\infty} \max \bigl(F_1(y + (k+1)\delta) - F_0(y + k\delta), 0 \bigr), \tag{B.1}
$$

and computation of (B.1) poses a simple one-dimensional optimization problem.

Let

$$
V(\delta) = \sup_{0 \leq y \leq \delta} \sum_{k=-\infty}^{\infty} \max \bigl(F_1(y + (k+1)\delta) - F_0(y + k\delta), 0 \bigr),
$$

and

$$
V_K(\delta) = \max_{y \in \{y^* + k\delta\}_{k=-\infty}^\infty} \sum_{k=-K}^K \max \bigl(F_1(y + (k+1)\delta) - F_0(y + k\delta), 0 \bigr),
$$

where 
$$
y^* \in \arg\max_{0 \leq y \leq \delta} \sum_{k=-\infty}^\infty \max \bigl(F_1(y + (k+1)\delta) - F_0(y + k\delta), 0 \bigr)
$$ 
and \(K\) is a nonnegative integer.

**Step 1.** Compute \(V(\delta)\).

**Step 2.** To further reduce computational costs, set \(K\) to be a nonnegative integer satisfying \(|V(\delta) - V_K(\delta)| < \varepsilon\) for small \(\varepsilon > 0\).[^24]

**Step 3.** For \(J = K\), solve the following optimization problem:

$$
\sup_{\{a_k\}_{k=-J}^J \in \mathcal{S}_{\delta}^{J,K}(\hat{y})} \sum_{k=-J}^J \max \{ F_1(a_{k+1}) - F_0(a_k), 0 \}, \tag{B.2}
$$

where

$$
\mathcal{S}_{\delta}^{J,K}(y) = \left\{ \{a_k\}_{k=-J}^J ; a_J \leq y + K\delta, \quad a_{-J} \geq y - K\delta, \quad 0 \leq a_{k+1} - a_k \leq \delta, \quad \delta < a_{k+2} - a_k \text{ for each integer } k \right\},
$$

and

$$
\hat{y} = \arg\max_{y \in \{y^* + k\delta\}_{k=-\infty}^\infty} \sum_{k=-K}^K \max \bigl(F_1(y + (k+1)\delta) - F_0(y + k\delta), 0 \bigr).
$$

**Step 4.** Repeat Step 3 for \(J = K+1, \ldots, 2K\).[^25]

It is not straightforward to solve the problem (B.2) numerically in Step 3; the function \(\max\{x, 0\}\) is non-differentiable. Furthermore, in practice, marginal distribution functions are often estimated in a complicated

[^24]: I put \(\varepsilon = 10^{-5}\) for the implementation in Section 4 and Section 5.  
[^25]: By Lemma B.1, I considered \(J = K, K+1, \ldots, 2K\) for the sequence \(\{a_k\}_{k=-J}^J\) and compared the values of local maxima achieved by \(\{a_k\}_{k=-J}^J\) with \(V_K(\delta)\).
