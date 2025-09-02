Now I present the constrained optimization procedure to compute the sharp lower bound under MTR. I pay particular attention to the special case where  $a_{k+1} - a_k = \delta$  for each integer k at the optimum. In this case, the lower bound reduces to

$$\sup_{0 \le y \le \delta} \sum_{k=-\infty}^{\infty} \max \left( F_1 \left( y + \left( k+1 \right) \delta \right) - F_0 \left( y + k \delta \right), 0 \right), \tag{B.1}$$

and computation of  $(B.1)$  poses a simple one-dimensional optimization problem.

 $\text{Let}$ 

$$V\left(\delta\right) = \sup_{0 \le y \le \delta} \sum_{k=-\infty}^{\infty} \max\left(F_1\left(y + (k+1)\,\delta\right) - F_0\left(y + k\delta\right), 0\right),$$

and

$$V_{K}(\delta) = \max_{y \in \{y^{*} + k\delta\}_{k=-\infty}^{\infty}} \sum_{k=-K}^{K} \max(F_{1}(y + (k+1)\delta) - F_{0}(y + k\delta), 0),$$

where  $y^* \in \underset{0 \le y \le \delta}{\arg \max} \sum_{k=-\infty}^{\infty} \max \left( F_1 \left( y + (k+1) \, \delta \right) - F_0 \left( y + k \delta \right), 0 \right)$  and  $K$  is a nonnegative integer.

**Step 1.** Compute  $V(\delta)$ .

**Step 2.** To further reduce computational costs, set K to be a nonnegative integer satisfying  $|V(\delta) - V_K(\delta)| <$  $\varepsilon$  for small  $\varepsilon > 0.$ <sup>24</sup>

**Step 3.** For  $J = K$ , solve the following optimization problem:

$$\sup_{\{a_k\}_{k=-J}^{J} \in \mathcal{S}_{\delta}^{J,K}(\widehat{y})} \sum_{k=-J}^{J} \max\left\{F_1\left(a_{k+1}\right) - F_0\left(a_k\right), 0\right\},\tag{B.2}$$

where

 $\equiv$ 

$$\mathcal{S}^{J,K}_{\delta}(y) = \left\{ \begin{array}{l} \left\{ a_{k} \right\}_{k=-J}^{J}; a_{J} \le y + K\delta, a_{-J} \ge y - K\delta, \ 0 \le a_{k+1} - a_{k} \le \delta, \\ \delta < a_{k+2} - a_{k} \text{ for each integer } k \end{array} \right\}, \\ \widehat{y} = \underset{y \in \{y^{*} + k\delta\}_{k=-\infty}^{\infty}}{\arg\max} \sum_{k=-K}^{K} \max\left(F_{1}\left(y + (k+1)\,\delta\right) - F_{0}\left(y + k\delta\right), 0\right).$$

**Step 4.** Repeat Step 3 for  $J = K + 1, ..., 2K^{25}$ 

It is not straightforward to solve the problem (B.2) numerically in Step 3; the function  $\max\{x,0\}$  is nondifferentiable. Furthermore in practice, marginal distribution functions are often estimated in a complicated

<sup>&</sup>lt;sup>24</sup>I put  $\varepsilon = 10^{-5}$  for the implementation in Section 4 and Section 5.

<sup>&</sup>lt;sup>25</sup>By Lemma B.1, I considered  $J = K, K + 1, \ldots, 2K$  for the sequence  $\{a_k\}_{k=-J}^J$  and compared the values of local maxima achieved by  $\{a_k\}_{k=-J}^J$  with  $V_K(\delta)$