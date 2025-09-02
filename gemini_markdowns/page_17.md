![Figure 2: Concave treatment response and convex treatment response](figure-2.png)

**Figure 2 (summary):** This figure presents two plots side-by-side. The left plot shows a Concave Treatment Response Function, where Potential Outcome $Y_t$ increases with Treatment Level $t$ at a decreasing rate. The right plot shows a Convex Treatment Response Function, where Potential Outcome $Y_t$ increases with Treatment Level $t$ at an increasing rate.

Concavity and convexity of the treatment response function imply $\text{Pr} \left( \frac{Y_0-W}{t_0-t_W} \geq \frac{Y_1-Y_0}{t_1-t_0}, Y_1 \geq Y_0 \geq W \right) = 1$ and $\text{Pr} \left( \frac{Y_0-W}{t_0-t_W} \geq \frac{Y_1-Y_0}{t_1-t_0}, Y_1 \geq Y_0 \geq W \right) = 1$, respectively, where $t_d$ is a level of input for each treatment status $d \in \{0,1\}$ while $t_W$ is a level of input without the treatment and $t_W < t_0 < t_1$. Given $W = w$, concavity and convexity of the treatment response function restrict the support of $(Y_0, Y_1)$ to the region below the straight line $Y_1 = \frac{t_1-t_W}{t_0-t_W} Y_0 - \frac{t_1-t_0}{t_0-t_W} w$ and above the straight line $Y_1 = Y_0$, and to the region above two straight lines $Y_1 = \frac{t_1-t_W}{t_0-t_W} Y_0 - \frac{t_1-t_0}{t_0-t_W} w$ and $Y_1 = Y_0$, respectively, as shown in Figures 1(b) and (c).

**Example 3 (Roy Model)** In the Roy model, individuals self-select into treatment when their benefits from the treatment are greater than nonpecuniary costs for treatment participation. The extended Roy model assumes that the nonpecuniary cost is deterministic with the following selection equation:

$$
D = \mathbf{1} \{Y_1 - Y_0 \geq \mu_C (Z)\},
$$

where $\mu_C (Z)$ represents nonpecuniary costs with a vector of observables $Z$. Then treated ($D = 1$) and untreated people ($D = 0$) are the observed groups satisfying support restrictions $\{Y_1 – Y_0 \geq \mu_C (Z)\}$ and $\{Y_1 – Y_0 < \mu_C (Z)\}$, respectively.

**Example 4 (DTE conditional on Potential Outcomes)** The conditional DTE for the unobservable subgroup whose potential outcomes belong to a certain set $C$ is written as

$$
\text{Pr} \{Y_1 - Y_0 \leq \delta | (Y_0, Y_1) \in C\}.
$$