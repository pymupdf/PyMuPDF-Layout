

Now I present the constrained optimization procedure to compute the sharp lower bound under MTR. I pay particular attention to the special case where a<sub>k+1</sub> − a<sub>k</sub> = δ for each integer k at the optimum. In this case, the lower bound reduces to

$$\sup_{0≤y≤δ} \sum_{k=-∞}^{∞} \max (F_1 (y + (k + 1) δ) − F_0 (y + kδ) , 0) ,\quad (B.1)$$

and computation of (B.1) poses a simple one-dimensional optimization problem.

Let

$$V (δ) = \sup_{0≤y≤δ} \sum_{k=-∞}^{∞} \max (F_1 (y + (k + 1) δ) − F_0 (y + kδ) , 0) ,$$

and

$$V_K (δ) = \max_{y∈\{y^*+kδ\}_{k=-∞}^{∞}} \sum_{k=-K}^{K} \max (F_1 (y + (k + 1) δ) − F_0 (y + kδ) , 0) ,$$

where y<sup>*</sup> ∈ arg max<sub>0≤y≤δ</sub> ∑<sub>k=-∞</sub><sup>∞</sup> max (F<sub>1</sub> (y + (k + 1) δ) − F<sub>0</sub> (y + kδ) , 0) and K is a nonnegative integer.

**Step 1.** Compute V (δ) .

**Step 2.** To further reduce computational costs, set K to be a nonnegative integer satisfying |V (δ) − V<sub>K</sub> (δ)| < ε for small ε > 0.<sup>24</sup>

**Step 3.** For J = K, solve the following optimization problem:

$$\sup_{\{a_k\}_{k=-J}^{J} ∈S_δ^{J,K}(ȳ)} \sum_{k=-J}^{J} \max \{F_1 (a_{k+1}) − F_0 (a_k) , 0\} ,\quad (B.2)$$

where

$$S_δ^{J,K} (y) = \left\{ \{a_k\}_{k=-J}^{J} : a_J ≤ y + Kδ, a_{-J} ≥ y − Kδ, 0 ≤ a_{k+1} − a_k ≤ δ, \atop δ < a_{k+2} − a_k \text{ for each integer } k \right\} ,$$

$$ȳ = \arg \max_{y∈\{y^*+kδ\}_{k=-∞}^{∞}} \sum_{k=-K}^{K} \max (F_1 (y + (k + 1) δ) − F_0 (y + kδ) , 0) .$$

**Step 4.** Repeat Step 3 for J = K + 1, . . . , 2K.<sup>25</sup>

It is not straightforward to solve the problem (B.2) numerically in Step 3; the function max{x, 0} is non-differentiable. Furthermore in practice, marginal distribution functions are often estimated in a complicated

<sup>24</sup>I put ε = 10<sup>−5</sup> for the implementation in Section 4 and Section 5.
<sup>25</sup>By Lemma B.1, I considered J = K, K + 1, . . . , 2K for the sequence {a<sub>k</sub>}<sub>k=-J</sub><sup>J</sup> and compared the values of local maxima achieved by {a<sub>k</sub>}<sub>k=-J</sub><sup>J</sup> with V<sub>K</sub> (δ)

74
