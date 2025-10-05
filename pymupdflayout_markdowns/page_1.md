10 

be formulated for the general SINR regime as follows: 

**==> formula intentionally omitted <==**

Note that the numerator and denominator in (12) are posynomials and minimizing a ratio between two posynomials is referred to be a truly non-convex NP hard intractable problem known as complimentary GP. However, this problem can be transformed into GP by letting the denominator K f (p) = p n,k,l h n,k,l + σ <sup>[2]</sup> + I n,l = <sup>[�]</sup> <sup>[L]</sup> l=1 � k=1 <sup>[u]</sup> <sup>[n,k,l]</sup> <sup>[(][p][)][ and approximating the denominator][ f]</sup> <sup>[(][p][)]</sup> with a monomial using the arithmetic/geometric mean inequality as follows: 

s n,k,l u n,k,l (p) 

**==> formula intentionally omitted <==**

where s n,k,l = <sup>[u]</sup> <sup>[n,k,l]</sup> f (p 0 <sup>[(][p]</sup> ) <sup>[0]</sup> <sup>[)]</sup> <sup>[. Thus, the problem can be solved by extending the single condensation]</sup> method presented in [14] for multi-cell scenario. The details of centralized scheme A are presented in Algorithm 2. 

## _B. Centralized Scheme A: Complexity Analysis_ 

The initial allocation phase has a complexity of O(KN <sup>[2]</sup> ) which is the same as Algorithm 1. Next, we perform a one dimensional search for the user in cell l with maximum incremental throughput at subcarrier n. The process is repeated for each subcarrier and cell. Thus, the com- putational complexity of this step is O(KNL). Since, the process continues until convergence, (i.e., M iterations), the complexity of this step can be written as O(KNLM). Finally, the total complexity of subcarrier allocation phase is O(KN <sup>[2]</sup> + NKLM). 

The complexity of Phase II is difficult to determine, however, it can be measured in terms of the degree of difficulty (DoD) that in turn relies on the number of constraints and variables associated with the GP [15]. Since we are dealing with LK power constraints and LKN power variables, the total computational complexity of centralized scheme A is O(KN <sup>[2]</sup> + NKLM) + DoD(LKN). Apparently it seems that implementing centralized GP/successive GP based schemes may not 

March 19, 2018 DRAFT 

