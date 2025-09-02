The figure compares the efficiency of three MCMC algorithms (All Blocked, All Scalar, and Auto Blocking) across two scenarios: varying correlation levels with fixed block sizes (left) and varying model sizes with fixed correlation (right). Auto Blocking shows the poorest performance, particularly at lower correlations and smaller model sizes, requiring significantly more effective samples compared to the other methods. All Blocked and All Scalar algorithms demonstrate similar and superior efficiency across both scenarios.

Figure 3: Efficiency results for two contrived model structures: varying sized blocks of fixed correlation (left), and fixed sized blocks of varying correlation (right).

## Random Effects Model

In the random effects model (Table 1), automated blocking generates an MCMC algorithm identical to the Informed Blocking algorithm (blocking each \( \alpha_{i}, \beta_{i} \) pair), which produces a tenfold improvement in Efficiency over the most efficient static algorithm - for this model, All Scalar sampling. The cut height \( h=0.1 \) indicates that only the \( \alpha_{i}, \beta_{i} \) pairs exhibit posterior correlations above 0.9. The Informed Cross-Level algorithm requires a substantially longer Runtime and produces a high ESS, which results in nearly identical Efficiency as the efficiently blocked Auto Blocking algorithm.

## Auto-Regressive Model

In the auto-regressive model (Table 1), an AR process value exhibited the slowest mixing under All Scalar sampling. When all 24 model parameters (AR process values, fixed effects, and one hyper-parameter) are blocked, the algorithm Runtime is nearly halved. This decrease in Runtime is largely due to the dependency structure inherent to the AR process. Scalar sampling of AR process values requires nearly a three-fold increase in density evaluations of the process values (since it's a

23

=