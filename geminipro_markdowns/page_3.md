![Figure 3: Efficiency results for two contrived model structures](figure-3.png)

**Figure 3 (summary):** Two line plots comparing the Efficiency (effective samples / time) of three MCMC Algorithms: All Blocked (orange), All Scalar (green), and Auto Blocking (blue).
- **Left Plot (Efficiency vs Correlation):** Auto Blocking shows the highest efficiency (~900) at 0.2 correlation, dropping as correlation increases to 0.8. All Scalar and All Blocked remain lower (starting below 250).
- **Right Plot (Efficiency vs Model size N):** Auto Blocking demonstrates very high efficiency (~6500) at N=20, dropping sharply as model size increases to 100. The other algorithms show significantly lower efficiency throughout.

**Figure 3:** Efficiency results for two contrived model structures: varying sized blocks of fixed correlation (left), and fixed sized blocks of varying correlation (right).

### Random Effects Model

In the random effects model (Table 1), automated blocking generates an MCMC algorithm identical to the Informed Blocking algorithm (blocking each $\alpha_i, \beta_i$ pair), which produces a tenfold improvement in Efficiency over the most efficient static algorithm – for this model, All Scalar sampling. The cut height $h = 0.1$ indicates that only the $\alpha_i, \beta_i$ pairs exhibit posterior correlations above 0.9. The Informed Cross-Level algorithm requires a substantially longer Runtime and produces a high ESS, which results in nearly identical Efficiency as the efficiently blocked Auto Blocking algorithm.

### Auto-Regressive Model

In the auto-regressive model (Table 1), an AR process value exhibited the slowest mixing under All Scalar sampling. When all 24 model parameters (AR process values, fixed effects, and one hyper-parameter) are blocked, the algorithm Runtime is nearly halved. This decrease in Runtime is largely due to the dependency structure inherent to the AR process. Scalar sampling of AR process values requires nearly a three-fold increase in density evaluations of the process values (since it’s a