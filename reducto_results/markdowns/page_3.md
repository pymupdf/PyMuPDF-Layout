| Category | Correlation=0.2 | Correlation=0.5 | Correlation=0.8 |
|---|---|---|---|
| All Blocked | ~230 | ~210 | ~100 |
| All Scalar | ~900 | ~150 | ~30 |
| Auto Blocking | ~180 | ~30 | ~6500 |

| Category | Model Size (N) = 20 | Model Size (N) = 50 | Model Size (N) = 100 |
|---|---|---|---|
| All Blocked | ~1600 | ~300 | ~100 |
| All Scalar | ~6500 | ~1400 | ~25 |
| Auto Blocking | ~200 | ~100 | ~40 |

The chart displays efficiency (effective samples / time) vs. correlation and model size (N) for different MCMC algorithms. The algorithms include "All Blocked," "All Scalar," and "Auto Blocking."

Figure 3: Efficiency results for two contrived model structures: varying sized blocks of fixed correlation (left), and fixed sized blocks of varying correlation (right).

## Random Effects Model

In the random effects model (Table 1), automated blocking generates an MCMC algorithm identical to the Informed Blocking algorithm (blocking each αi, βi pair), which produces a tenfold improve ment in Efficiency over the most efficient static algorithm – for this model, All Scalar sampling. The cut height h = 0.1 indicates that only the αi, βi pairs exhibit posterior correlations above 0.9. The Informed Cross-Level algorithm requires a substantially longer Runtime and produces a high ESS, which results in nearly identical Efficiency as the efficiently blocked Auto Blocking algorithm.

## Auto-Regressive Model

In the auto-regressive model (Table 1), an AR process value exhibited the slowest mixing under All Scalar sampling. When all 24 model parameters (AR process values, fixed effects, and one hyper-parameter) are blocked, the algorithm Runtime is nearly halved. This decrease in Runtime is largely due to the dependency structure inherent to the AR process. Scalar sampling of AR process values requires nearly a three-fold increase in density evaluations of the process values (since it’s a

23