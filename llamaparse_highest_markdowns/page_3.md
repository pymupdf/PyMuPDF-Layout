

## Figure 3: Efficiency Results

| Correlation | All Blocked (Efficiency) | All Scalar (Efficiency) | Auto Blocking (Efficiency) |
| ----------- | ------------------------ | ----------------------- | -------------------------- |
| 0.2         | 240                      | 900                     | 850                        |
| 0.5         | 180                      | 400                     | 380                        |
| 0.8         | 60                       | 300                     | 280                        |


| Model size (N) | All Blocked (Efficiency) | All Scalar (Efficiency) | Auto Blocking (Efficiency) |
| -------------- | ------------------------ | ----------------------- | -------------------------- |
| 20             | 1500                     | 6500                    | 1400                       |
| 50             | 200                      | 1700                    | 180                        |
| 100            | 50                       | 800                     | 40                         |


**Figure 3:** Efficiency results for two contrived model structures: varying sized blocks of fixed correlation (left), and fixed sized blocks of varying correlation (right).

## Random Effects Model

In the random effects model (Table 1), automated blocking generates an MCMC algorithm identical to the Informed Blocking algorithm (blocking each α<sub>i</sub>, β<sub>i</sub> pair), which produces a tenfold improvement in Efficiency over the most efficient static algorithm – for this model, All Scalar sampling. The cut height h = 0.1 indicates that only the α<sub>i</sub>, β<sub>i</sub> pairs exhibit posterior correlations above 0.9. The Informed Cross-Level algorithm requires a substantially longer Runtime and produces a high ESS, which results in nearly identical Efficiency as the efficiently blocked Auto Blocking algorithm.

## Auto-Regressive Model

In the auto-regressive model (Table 1), an AR process value exhibited the slowest mixing under All Scalar sampling. When all 24 model parameters (AR process values, fixed effects, and one hyper-parameter) are blocked, the algorithm Runtime is nearly halved. This decrease in Runtime is largely due to the dependency structure inherent to the AR process. Scalar sampling of AR process values requires nearly a three-fold increase in density evaluations of the process values (since it's a

23
