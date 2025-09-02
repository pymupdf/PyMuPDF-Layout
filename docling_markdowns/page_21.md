Now I present the constrained optimization procedure to compute the sharp lower bound under MTR. I pay particular attention to the special case where a k +1 -a k = δ for each integer k at the optimum. In this case, the lower bound reduces to

<!-- formula-not-decoded -->

and computation of (B.1) poses a simple one-dimensional optimization problem.

Let

<!-- formula-not-decoded -->

and

<!-- formula-not-decoded -->

where y ∗ ∈ arg max 0 ≤ y ≤ δ ∑ ∞ k = -∞ max( F 1 ( y +( k +1) δ ) -F 0 ( y + kδ ) , 0) and K is a nonnegative integer.

Step 1. Compute V ( δ ) .

Step 2. To further reduce computational costs, set K to be a nonnegative integer satisfying | V ( δ ) -V K ( δ ) | ε for small ε &gt; 0 . 24

&lt;

Step 3. For J = K , solve the following optimization problem:

<!-- formula-not-decoded -->

where

<!-- formula-not-decoded -->

Step 4. Repeat Step 3 for J = K +1 , . . . , 2 K. 25

It is not straightforward to solve the problem (B.2) numerically in Step 3; the function max { x, 0 } is nondifferentiable. Furthermore in practice, marginal distribution functions are often estimated in a complicated

24 I put ε = 10 -5 for the implementation in Section 4 and Section 5.

25 By Lemma B.1, I considered J = K, K +1 , . . . , 2 K for the sequence { a k } J k = -J and compared the values of local maxima achieved by { a k } J k = -J with V K ( δ )