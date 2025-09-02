![Figure A.5: Support under concave treatment response](figure-A.5.png)

**Figure A.5 (summary):** A 2D plot with axes $Y_0$ (horizontal) and $Y_1$ (vertical). Two lines are shown intersecting at the origin: the identity line $Y_1 = Y_0$ and a steeper line $Y_1 = \frac{t_1 - t_w}{t_0 - t_w} Y_0 - \frac{t_1 - t_0}{t_0 - t_w} w$. A yellow shaded region indicates the support area between the two lines in the first quadrant.

The function $\varphi$ can be readily shown to be nonincreasing. Thus, at the optimum $B_k = (-\infty, b_k)$ with $b_{k+1} \leq b_k$ and $b_k \in [-\infty, \infty]$ for every integer $k$. By Theorem 1, for $\delta > 0$, $B_k^D$ is written as

$$
\begin{aligned}
B_k^D = & \{y_1 \in \mathbb{R} | \exists y_0 < b_k \text{ s.t. } 0 \leq y_1 - y_0 < \delta \text{ and } (t_0 - t_w) y_1 - (t_1 - t_w) y_0 \leq -(t_1 - t_0) w \} \\
& \cup \{y_1 \in \mathbb{R} | \exists y_0 < b_{k+1} \text{ s.t. } y_1 - y_0 \geq \delta \text{ and } (t_0 - t_w) y_1 - (t_1 - t_w) y_0 \leq -(t_1 - t_0) w \} .
\end{aligned}
$$

Note that $Y_1 = Y_0 + \delta$ and $Y_1 = \frac{t_1-t_w}{t_0-t_w}Y_0 - \frac{t_1-t_0}{t_0-t_w}w$ intersect at $(\frac{t_0-t_w}{t_1-t_0}\delta + y_{-1}, \frac{t_1-t_w}{t_1-t_0}\delta + w)$. I consider the following three cases: a) $b_{k+1} \leq b_k \leq \frac{t_0-t_w}{t_1-t_0}\delta + w$, b) $b_{k+1} \leq \frac{t_0-t_w}{t_1-t_0}\delta + w \leq b_k$, and c) $\frac{t_0-t_w}{t_1-t_0}\delta + w \leq b_{k+1} \leq b_k$.

![Figure A.6: B_k^D for B_k = (-∞, b_k) and B_{k+1} = (-∞, b_{k+1})](figure-A.6.png)

**Figure A.6 (summary):** This figure contains three subplots (a), (b), and (c), each displaying a graph on the $Y_1$ vs $Y_0$ plane. They illustrate the set $B_k^D$ under the three different cases for the ordering of $b_k$, $b_{k+1}$, and a threshold value. Each plot shows two intersecting lines and a horizontal line for $Y_1 = Y_0 + \delta$. The region corresponding to $B_k^D$ is highlighted differently in each subplot (as a colored vertical bar), showing how its support changes.

**Case a)** $b_{k+1} \leq b_k \leq \frac{t_0-t_w}{t_1-t_0}\delta + w$

If $b_{k+1} \leq b_k \leq \frac{t_0-t_w}{t_1-t_0}\delta + w$, as illustrated in Figure A.5(a), for any $y_0 < b_{k+1} \leq \frac{t_0-t_w}{t_1-t_0}\delta + w$, there exists