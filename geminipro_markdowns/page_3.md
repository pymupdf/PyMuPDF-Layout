![Figure 3: Efficiency results for two contrived model structures: varying sized blocks of fixed correlation (left), and fixed sized blocks of varying correlation (right).](figure-3.png)

**Figure 3 (summary):** This figure contains two line charts comparing the efficiency of three MCMC algorithms: "All Blocked," "All Scalar," and "Auto Blocking."
- **Left Chart:** Plots Efficiency vs. Correlation. As correlation increases from 0.2 to 0.8, the efficiency of all algorithms decreases. "Auto Blocking" consistently shows significantly higher efficiency than "All Scalar" and "All Blocked."
- **Right Chart:** Plots Efficiency vs. Model Size (N). As model size increases from 20 to 100, the efficiency of all algorithms decreases. "Auto Blocking" again demonstrates far superior efficiency compared to the other two methods, although its efficiency drops sharply with increasing model size.

## Random Effects Model

In the random effects model (Table 1), automated blocking generates an MCMC algorithm identical to the Informed Blocking algorithm (blocking each $α_i, β_i$ pair), which produces a tenfold improvement in Efficiency over the most efficient static algorithm – for this model, All Scalar sampling. The cut height $h = 0.1$ indicates that only the $α_i, β_i$ pairs exhibit posterior correlations above 0.9. The Informed Cross-Level algorithm requires a substantially longer Runtime and produces a high ESS, which results in nearly identical Efficiency as the efficiently blocked Auto Blocking algorithm.

## Auto-Regressive Model

In the auto-regressive model (Table 1), an AR process value exhibited the slowest mixing under All Scalar sampling. When all 24 model parameters (AR process values, fixed effects, and one hyper-parameter) are blocked, the algorithm Runtime is nearly halved. This decrease in Runtime is largely due to the dependency structure inherent to the AR process. Scalar sampling of AR process values requires nearly a three-fold increase in density evaluations of the process values (since it's a