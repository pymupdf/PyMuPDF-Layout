10

be formulated for the general SINR regime as follows:

L KN σ² + In,l αn,k,l
minimize log2 ΠΠΠ
Pn,k,l l=1 k=1 n=1 Pn,k,lhn,k,l +σ² + In,l. (12)
N
subject to Σan,k,lPn,k,l Pk,max, VE, VI
n=1

Note that the numerator and denominator in (12) are posynomials and minimizing a ratio between two posynomials is referred to be a truly non-convex NP hard intractable problem known as complimentary GP. However, this problem can be transformed into GP by letting the denominator f(p) = Pn,k,lhn,k,l +0² + In‚l = k=1 K Un,k,l(p) and approximating the denominator f(p) with a monomial using the arithmetic/geometric mean inequality as follows:

L K L K Sn,k,l
ΣΣ Unk;1(P) ≥ ÍÍÎÌ (Unk.1(P)\ (13)
Sn,k,l
l=1 k=1 l=1 k=1

where Sn,k,l= Un,k,l (PO) Thus, the problem can be solved by extending the single condensation f(po) method presented in [14] for multi-cell scenario. The details of centralized scheme A are presented in Algorithm 2.

B. Centralized Scheme A: Complexity Analysis

The initial allocation phase has a complexity of O(KN 2 ) which is the same as Algorithm 1. Next, we perform a one dimensional search for the user in cell l with maximum incremental throughput at subcarrier n. The process is repeated for each subcarrier and cell. Thus, the com putational complexity of this step is O(KNL ). Since, the process continues until convergence, (i.e., M iterations), the complexity of this step can be written as O(KNLM ). Finally, the total complexity of subcarrier allocation phase is O(KN 2 + NKLM ).

The complexity of Phase II is difficult to determine, however, it can be measured in terms of the degree of difficulty (DoD) that in turn relies on the number of constraints and variables associated with the GP [15]. Since we are dealing with LK power constraints and LKN power variables, the total computational complexity of centralized scheme A is O(KN 2 + NKLM ) + DoD(LKN ). Apparently it seems that implementing centralized GP/successive GP based schemes may not

March 19, 2018

DRAFT