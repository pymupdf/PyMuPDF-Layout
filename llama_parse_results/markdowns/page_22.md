

6

# III. BOUNDS ON THE NETWORK THROUGHPUT

## A. Lower Bound on the Optimal Network Throughput

A LB for the optimum multi-cell network throughput can be computed by considering worst case ICI. Observing the dependency of ICI on the subcarrier allocation and power allocation variables, we assume that each user in each cell is transmitting on each subcarrier with its maximum power. A simple LB for the average network throughput C taking the worst case ICI into account can be written as follows:

$$C(A_l, P_l) \geq \frac{1}{L} \sum_{l=1}^{L} \sum_{k=1}^{K} \sum_{n=1}^{N} \alpha_{n,k,l} \log_2 \left( 1 + \frac{p_{n,k,l} h_{n,k,l}}{\sigma^2 + \xi_{n,l}} \right)$$ (8)

where $\xi_{n,l} = \sum_{j=1,j \neq l}^{L} \sum_{k=1}^{K} P_{k,max} g_{n,k,jl}$.

A tighter LB can be derived by using Algorithm 1 where each subcarrier is allocated to the user that maximizes Q<sub>n,k,l</sub> where:

$$Q_{n,k,l} = \frac{p_{n,k,l} h_{n,k,l}}{\xi_{n,l} + \sigma^2}$$ (9)

Thus, Q<sub>n,k,l</sub> is an SINR term for each user k at each subcarrier n in each cell l assuming worst case interference. We collect these SINR terms into a vector **q**<sub>n,l</sub> = [q<sub>n,1,l</sub>, q<sub>n,2,l</sub>, ...., q<sub>n,K,l</sub>] and then stack all the vectors in a matrix **Q**<sub>l</sub> ∈ ℝ<sup>N×K</sup>. The resulting allocations based on this criteria are then used to compute the LB network throughput using (1).

Note that if ξ<sub>n,l</sub> = 0, than Q<sub>n,k,l</sub> becomes the marginal rate which is shown to be a near-optimal criterion in single cell network scenarios without ICI [2]. Moreover, equal power allocation has insignificant performance loss in high SINR regime compared to the optimal water-filling solution [2], [4], thus power equalization is implemented in Algorithm 1. For the low SINR regime, we can incorporate water-filling rather than equalization in a straightforward manner.

## B. Upper Bound on the Optimal Network Throughput

Establishing an UB is significantly important in order to calibrate the performance of sub-optimal resource allocation schemes with respect to the optimal solution. The UB can be derived

March 19, 2018                                                                      DRAFT
