Now I present the constrained optimization procedure to compute the sharp lower bound under MTR. I pay particular attention to the special case where ak+1 − ak = δ for each integer k at the optimum. In this case, the lower bound reduces to

sup Σ max (F1 (y+ (k + 1) 6) – Fo (y + kб),0), (B.1)

and computation of (B.1) poses a simple one-dimensional optimization problem.

Let

V (8) = sup Σ max (Fi (y+(k+1) 8) − Fo (y + kɗ),0),
0≤y≤ k=-∞

and

K
VK (8) max Σ max (Fi (y+(k+1) 8) — Fo (y + kd), 0),
yЄ{y*+k6}=-∞ k=-K

where y* € arg maxΣx=-∞ max (F₁ (y + (k + 1) 8) − Fo (y + kd),0) and K is a nonnegative integer.

Step 1. Compute V (δ) .

Step 2. To further reduce computational costs, set K to be a nonnegative integer satisfying |V (δ) − VK (δ)| < ε for small ε > 0. 24

Step 3. For J = K , solve the following optimization problem:

sup max {F1 (ak+1) - Fo (ak), 0}, (B.2)
{ak}=-ES (ŷ) k=-J

where

SJK (y) {ak}j;aj≤y+K8, α_¸ ≥ y − K8, 0 ≤ ak+1 − ak ≤ 8, 8<ak+2 ak for each integer k K ŷ = arg max Σ max (Fi (y + (k + 1) 6) — Fo (y + kб), 0). yЄ{y*+kd}∞ k=-K

Step 4. Repeat Step 3 for J = K+1,..., 2K.25

It is not straightforward to solve the problem (B.2) numerically in Step 3; the function max{x, 0} is non differentiable. Furthermore in practice, marginal distribution functions are often estimated in a complicated

24 I put ε = 10−5 for the implementation in Section 4 and Section 5.

25 By Lemma B.1, I considered J = K, K+1,..., 2K for the sequence {ak}}/_ k=-J and compared the values of local maxima achieved by {a}-- with VK (6)

74