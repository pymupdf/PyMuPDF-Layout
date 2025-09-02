![Figure 2: Concave treatment response and convex treatment response](figure-2.png)

**Figure 2 (summary):** The figure displays two plots side-by-side. The left plot, titled "Concave Treatment Response Function," shows Potential Outcome Yt on the y-axis versus Treatment Level t on the x-axis. The curve is concave, rising from the origin and flattening out. The right plot, titled "Convex Treatment Response Function," shows the same axes, but with a convex curve that rises from the origin at an accelerating rate.

---

Concavity and convexity of the treatment response function imply $\text{Pr}\left(\frac{Y_0-W}{t_0-t_w} \geq \frac{Y_1-Y_0}{t_1-t_0}, Y_1 \geq Y_0 \geq W\right) = 1$ and $\text{Pr}\left(\frac{Y_0-W}{t_0-t_w} \leq \frac{Y_1-Y_0}{t_1-t_0}, Y_1 \geq Y_0 \geq W\right) = 1$, respectively, where $t_d$ is a level of input for each treatment status $d \in \{0,1\}$ while $t_w$ is a level of input without the treatment and $t_w < t_0 < t_1$. Given $W = w$, concavity and convexity of the treatment response function restrict the support of $(Y_0, Y_1)$ to the region below the straight line $Y_1 = \frac{t_1-t_w}{t_0-t_w}Y_0 - \frac{t_1-t_0}{t_0-t_w}w$ and above the straight line $Y_1 = Y_0$, and to the region above two straight lines $Y_1 = \frac{t_1-t_w}{t_0-t_w}Y_0 - \frac{t_1-t_0}{t_0-t_w}w$ and $Y_1 = Y_0$, respectively, as shown in Figures 1(b) and (c).

**Example 3 (Roy Model)** In the Roy model, individuals self-select into treatment when their benefits from the treatment are greater than nonpecuniary costs for treatment participation. The extended Roy model assumes that the nonpecuniary cost is deterministic with the following selection equation:

$$
D = \mathbf{1}\{Y_1 - Y_0 \geq \mu_C(Z)\}
$$

where $\mu_C(Z)$ represents nonpecuniary costs with a vector of observables $Z$. Then treated ($D=1$) and untreated people ($D=0$) are the observed groups satisfying support restrictions $\{Y_1 - Y_0 \geq \mu_C(Z)\}$ and $\{Y_1 - Y_0 < \mu_C(Z)\}$, respectively.

**Example 4 (DTE conditional on Potential Outcomes)** The conditional DTE for the unobservable subgroup whose potential outcomes belong to a certain set $C$ is written as

$$
\text{Pr}\{Y_1 - Y_0 \leq \delta | (Y_0, Y_1) \in C\}
$$