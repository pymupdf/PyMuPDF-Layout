6


III. BOUNDS ON THE NETWORK THROUGHPUT


_A. Lower Bound on the Optimal Network Throughput_


A LB for the optimum multi-cell network throughput can be computed by considering worst


case ICI. Observing the dependency of ICI on the subcarrier allocation and power allocation


variables, we assume that each user in each cell is transmitting on each subcarrier with its


maximum power. A simple LB for the average network throughput C taking the worst case ICI


into account can be written as follows:


̸



N
� αn,k,llog2


n=1


̸



K
�


k=1


̸



C(Al, Pl) ≥ [1]

L


̸



L
�


l=1


̸



1 + [p][n,k,l][h][n,k,l]
� σ [2] + ξn,l


̸



(8)
�


̸



where ξn,l = [�][L] j=1,j≠ l �Kk=1 [P][k,][max][g][n,k,jl][.]


A tighter LB can be derived by using Algorithm 1 where each subcarrier is allocated to the

̸



user that maximizes Qn,k,l where:


Qn,k,l = [p][n,k,l][h][n,k,l] (9)

ξn,l + σ [2]

̸



Thus, Qn,k,l is an SINR term for each user k at each subcarrier n in each cell l assuming worst

̸


̸



case interference. We collect these SINR terms into a vector qn,l = [qn,1,l, qn,2,l...., qn,K,l] and


are then used to compute the LB network throughput using (1).

̸


̸


̸



Note that if ξn,l = 0, than Qn,k,l becomes the marginal rate which is shown to be a near-optimal


criterion in single cell network scenarios without ICI [2]. Moreover, equal power allocation has

insignificant performance loss in high SINR regime compared to the optimal water-filling solution


[2], [4], thus power equalization is implemented in Algorithm 1. For the low SINR regime, we

can incorporate water-filling rather than equalization in a straightforward manner.


_B. Upper Bound on the Optimal Network Throughput_


Establishing an UB is significantly important in order to calibrate the performance of sub

optimal resource allocation schemes with respect to the optimal solution. The UB can be derived


March 19, 2018 DRAFT



̸



̸


