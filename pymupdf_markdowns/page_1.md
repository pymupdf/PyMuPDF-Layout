be formulated for the general SINR regime as follows:



K
�


k=1



N
�


n=1



10


(12)



� α n,k,l



minimize log 2
p n,k,l



L
�


l=1



σ [2] + I n,l
� p n,k,l h n,k,l + σ [2] + I n,l



subject to



N
� α n,k,l p n,k,l ≤ P k,max, ∀k, ∀l


n=1



Note that the numerator and denominator in (12) are posynomials and minimizing a ratio between


two posynomials is referred to be a truly non-convex NP hard intractable problem known as


complimentary GP. However, this problem can be transformed into GP by letting the denominator


K
f (p) = p n,k,l h n,k,l + σ [2] + I n,l = [�] [L] l=1 � k=1 [u] [n,k,l] [(][p][)][ and approximating the denominator][ f] [(][p][)]


with a monomial using the arithmetic/geometric mean inequality as follows:



L
�


l=1



K
� u n,k,l (p) ≥


k=1



L
�


l=1



K
�


k=1



u n,k,l (p)


s

� n,k,l



s n,k,l
(13)
�



where s n,k,l = [u] [n,k,l] f (p 0 [(][p] ) [0] [)] [. Thus, the problem can be solved by extending the single condensation]


method presented in [14] for multi-cell scenario. The details of centralized scheme A are


presented in Algorithm 2.


_B. Centralized Scheme A: Complexity Analysis_


The initial allocation phase has a complexity of O(KN [2] ) which is the same as Algorithm 1.


Next, we perform a one dimensional search for the user in cell l with maximum incremental


throughput at subcarrier n. The process is repeated for each subcarrier and cell. Thus, the com

putational complexity of this step is O(KNL). Since, the process continues until convergence,


(i.e., M iterations), the complexity of this step can be written as O(KNLM). Finally, the total


complexity of subcarrier allocation phase is O(KN [2] + NKLM).

The complexity of Phase II is difficult to determine, however, it can be measured in terms of the

degree of difficulty (DoD) that in turn relies on the number of constraints and variables associated


with the GP [15]. Since we are dealing with LK power constraints and LKN power variables, the


total computational complexity of centralized scheme A is O(KN [2] + NKLM) + DoD(LKN).


Apparently it seems that implementing centralized GP/successive GP based schemes may not


March 19, 2018 DRAFT


