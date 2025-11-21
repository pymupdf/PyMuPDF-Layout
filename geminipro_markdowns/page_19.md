![Figure A.5: Support under concave treatment response](figure-a5.png)

**Figure A.5 (summary):** A coordinate graph plotting $Y_1$ versus $Y_0$. Two lines are shown: the identity line $Y_1 = Y_0$ and the line $Y_1 = \frac{t_1 - t_W}{t_0 - t_W} Y_0 - \frac{t_1 - t_0}{t_0 - t_W} w$. A yellow shaded region indicates the support area located between these lines above their intersection.

The function $\varphi$ can be readily shown to be nonincreasing. Thus, at the optimum $B_k = (-\infty, b_k)$ with $b_{k+1} \leq b_k$ and $b_k \in [-\infty, \infty]$ for every integer $k$. By Theorem 1, for $\delta > 0$, $B_k^D$ is written as

$$
\begin{aligned}
B_k^D = \quad & \{y_1 \in \mathbb{R} \mid \exists y_0 < b_k \text{ s.t. } 0 \leq y_1 - y_0 < \delta \text{ and } (t_0 - t_W) y_1 - (t_1 - t_W) y_0 \leq - (t_1 - t_0) w\} \\
\cup \, & \{y_1 \in \mathbb{R} \mid \exists y_0 < b_{k+1} \text{ s.t. } y_1 - y_0 \geq \delta \text{ and } (t_0 - t_W) y_1 - (t_1 - t_W) y_0 \leq - (t_1 - t_0) w\} \,.
\end{aligned}
$$

Note that $Y_1 = Y_0 + \delta$ and $Y_1 = \frac{t_1 - t_W}{t_0 - t_W} Y_0 - \frac{t_1 - t_0}{t_0 - t_W} w$ intersect at $\left( \frac{t_0 - t_W}{t_1 - t_0} \delta + w, \frac{t_1 - t_W}{t_1 - t_0} \delta + w \right)$. I consider the following three cases: a) $b_{k+1} \leq b_k \leq \frac{t_0 - t_W}{t_1 - t_0} \delta + w$, b) $b_{k+1} \leq \frac{t_0 - t_W}{t_1 - t_0} \delta + w \leq b_k$, and c) $\frac{t_0 - t_W}{t_1 - t_0} \delta + w \leq b_{k+1} \leq b_k$.

![Figure A.6: B_k^D for different conditions](figure-a6.png)

**Figure A.6:** $B_k^D$ for $B_k = (-\infty, b_k)$ and $B_{k+1} = (-\infty, b_{k+1})$. The figure contains three subplots (a), (b), and (c) illustrating the geometric support regions in the $Y_1, Y_0$ plane corresponding to the three cases described in the text.

**Case a)** $b_{k+1} \leq b_k \leq \frac{t_0 - t_W}{t_1 - t_0} \delta + w$

If $b_{k+1} \leq b_k \leq \frac{t_0 - t_W}{t_1 - t_0} \delta + w$, as illustrated in Figure A.6(a), for any $y_0 < b_{k+1} \leq \frac{t_0 - t_W}{t_1 - t_0} \delta + w$, there exists