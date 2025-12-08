![Figure 3: Efficiency results for two contrived model structures: varying sized blocks of fixed correlation (left), and fixed sized blocks of varying correlation (right).](figure-3.png)

**Figure 3 (summary):**
Two line charts showing Efficiency (effective samples / time) for different MCMC algorithms (All Blocked, All Scalar, Auto Blocking).
- **Left Chart (Correlation vs Efficiency):** The "Auto Blocking" algorithm (blue) shows significantly higher efficiency than "All Blocked" (orange) and "All Scalar" (green). Auto Blocking efficiency decreases as correlation increases (from ~900 at 0.2 to ~300 at 0.8). The other algorithms remain below 250.
- **Right Chart (Model size (N) vs Efficiency):** "Auto Blocking" starts with very high efficiency (~6500) at N=20, dropping sharply as model size increases to 100. "All Blocked" and "All Scalar" start much lower (~1500) and drop to near zero.

### Random Effects Model

In the random effects model (Table 1), automated blocking generates an MCMC algorithm identical to the Informed Blocking algorithm (blocking each $\alpha_i$, $\beta_i$ pair), which produces a tenfold improvement in Efficiency over the most efficient static algorithm – for this model, All Scalar sampling. The cut height $h = 0.1$ indicates that only the $\alpha_i$, $\beta_i$ pairs exhibit posterior correlations above 0.9. The Informed Cross-Level algorithm requires a substantially longer Runtime and produces a high ESS, which results in nearly identical Efficiency as the efficiently blocked Auto Blocking algorithm.

### Auto-Regressive Model

In the auto-regressive model (Table 1), an AR process value exhibited the slowest mixing under All Scalar sampling. When all 24 model parameters (AR process values, fixed effects, and one hyper-parameter) are blocked, the algorithm Runtime is nearly halved. This decrease in Runtime is largely due to the dependency structure inherent to the AR process. Scalar sampling of AR process values requires nearly a three-fold increase in density evaluations of the process values (since it’s a