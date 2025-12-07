6

## III. BOUNDS ON THE NETWORK THROUGHPUT

### A. Lower Bound on the Optimal Network Throughput

A LB for the optimum multi-cell network throughput can be computed by considering worst case ICI. Observing the dependency of ICI on the subcarrier allocation and power allocation variables, we assume that each user in each cell is transmitting on each subcarrier with its maximum power. A simple LB for the average network throughput $\mathcal{C}$ taking the worst case ICI into account can be written as follows:

$$
\mathcal{C}(\mathbf{A}_l, \mathbf{P}_l) \ge \frac{1}{L} \sum_{l=1}^L \sum_{k=1}^K \sum_{n=1}^N \alpha_{n,k,l} \log_2 \left( 1 + \frac{p_{n,k,l}h_{n,k,l}}{\sigma^2 + \xi_{n,l}} \right) \tag{8}
$$

where $\xi_{n,l} = \sum_{j=1,j \neq l}^L \sum_{k=1}^K P_{k,\max} g_{n,k,j,l}$.

A tighter LB can be derived by using Algorithm 1 where each subcarrier is allocated to the user that maximizes $Q_{n,k,l}$ where:

$$
Q_{n,k,l} = \frac{p_{n,k,l}h_{n,k,l}}{\xi_{n,l} + \sigma^2} \tag{9}
$$

Thus, $Q_{n,k,l}$ is an SINR term for each user $k$ at each subcarrier $n$ in each cell $l$ assuming worst case interference. We collect these SINR terms into a vector $\mathbf{q}_{n,l} = [q_{n,1,l}, q_{n,2,l}, \dots, q_{n,K,l}]$ and then stack all the vectors in a matrix $\mathbf{Q}_l \in \mathbb{R}^{N \times K}$. The resulting allocations based on this criteria are then used to compute the LB network throughput using (1).

Note that if $\xi_{n,l} = 0$, than $Q_{n,k,l}$ becomes the marginal rate which is shown to be a near-optimal criterion in single cell network scenarios without ICI [2]. Moreover, equal power allocation has insignificant performance loss in high SINR regime compared to the optimal water-filling solution [2], [4], thus power equalization is implemented in Algorithm 1. For the low SINR regime, we can incorporate water-filling rather than equalization in a straightforward manner.

### B. Upper Bound on the Optimal Network Throughput

Establishing an UB is significantly important in order to calibrate the performance of sub-optimal resource allocation schemes with respect to the optimal solution. The UB can be derived

March 19, 2018
DRAFT