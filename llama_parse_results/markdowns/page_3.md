

| Panel                                  | X-Axis      | MCMC Algorithm                         | Data Points (X, Y)                 |               |                                    |
| -------------------------------------- | ----------- | -------------------------------------- | ---------------------------------- | ------------- | ---------------------------------- |
| Left Panel (Correlation vs Efficiency) | Correlation | All Blocked                            | (0.2, 230), (0.5, 170), (0.8, 50)  |               |                                    |
|                                        |             | All Scalar                             | (0.2, 850), (0.5, 400), (0.8, 300) |               |                                    |
|                                        |             | Auto Blocking                          | (0.2, 230), (0.5, 180), (0.8, 30)  |               |                                    |
|                                        |             | Right Panel (Model Size vs Efficiency) | Model size (N)                     | All Blocked   | (20, 1500), (50, 200), (100, 50)   |
|                                        |             |                                        |                                    | All Scalar    | (20, 7000), (50, 1700), (100, 800) |
|                                        |             |                                        |                                    | Auto Blocking | (20, 1400), (50, 180), (100, 40)   |


Figure 3: Efficiency results for two contrived model structures: varying sized blocks of fixed correlation (left), and fixed sized blocks of varying correlation (right).

## Random Effects Model

In the random effects model (Table 1), automated blocking generates an MCMC algorithm identical to the Informed Blocking algorithm (blocking each αi, βi pair), which produces a tenfold improvement in Efficiency over the most efficient static algorithm – for this model, All Scalar sampling. The cut height h = 0.1 indicates that only the αi, βi pairs exhibit posterior correlations above 0.9. The Informed Cross-Level algorithm requires a substantially longer Runtime and produces a high ESS, which results in nearly identical Efficiency as the efficiently blocked Auto Blocking algorithm.

## Auto-Regressive Model

In the auto-regressive model (Table 1), an AR process value exhibited the slowest mixing under All Scalar sampling. When all 24 model parameters (AR process values, fixed effects, and one hyper-parameter) are blocked, the algorithm Runtime is nearly halved. This decrease in Runtime is largely due to the dependency structure inherent to the AR process. Scalar sampling of AR process values requires nearly a three-fold increase in density evaluations of the process values (since it's a

23
