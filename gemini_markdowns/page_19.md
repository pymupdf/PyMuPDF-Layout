![Figure A.5: Support under concave treatment response](figure-A.5.png)

**Figure A.5 (summary):** This 2D plot shows the coordinate axes $Y_0$ and $Y_1$. Two lines are depicted: $Y_1 = Y_0$ and another line, $Y_1 = \frac{t_1-t_w}{t_0-t_w}Y_0 - \frac{t_1-t_0}{t_0-t_w}w$. A triangular region, formed by the intersection of these two lines and above $Y_1=Y_0$, is shaded yellow, indicating the "Support under concave treatment response."

The function $\varphi$ can be readily shown to be nonincreasing. Thus, at the optimum $B_k = (-\infty, b_k)$ with $b_{k+1} \le b_k$ and $b_k \in [-\infty, \infty]$ for every integer $k$. By Theorem 1, for $\delta > 0$, $B_k^D$ is written as

$$
B_k^D = \left\{ y_1 \in \mathbb{R} \mid \exists y_0 < b_k \text{ s.t. } 0 \le y_1 - y_0 < \delta \text{ and } (t_0 - t_w) y_1 - (t_1 - t_w) y_0 \le -(t_1 - t_0) w \right\} \\
\cup \left\{ y_1 \in \mathbb{R} \mid \exists y_0 < b_{k+1} \text{ s.t. } y_1 - y_0 \ge \delta \text{ and } (t_0 - t_w) y_1 - (t_1 - t_w) y_0 \le -(t_1 - t_0) w \right\}.
$$

Note that $Y_1 = Y_0 + \delta$ and $Y_1 = \frac{t_1-t_w}{t_0-t_w} Y_0 - \frac{t_1-t_0}{t_0-t_w} w$ intersect at $\left(\frac{t_0-t_w}{t_1-t_0}\delta + y_1, \frac{t_1-t_w}{t_1-t_0}\delta + w\right)$. I consider the following three cases:
a) $b_{k+1} \le b_k < \frac{t_0-t_w}{t_1-t_0}\delta + w$
b) $b_{k+1} < \frac{t_0-t_w}{t_1-t_0}\delta + w \le b_k$
c) $\frac{t_0-t_w}{t_1-t_0}\delta + w \le b_{k+1} \le b_k$

![Figure A.6: $B_k^D$ for $B_k = (-\infty, b_k)$ and $B_{k+1} = (-\infty, b_{k+1})](figure-A.6.png)

**Figure A.6 (summary):** This figure comprises three sub-diagrams (a), (b), and (c), each illustrating the region $B_k^D$ on a $Y_0$ vs $Y_1$ plane, for different relationships between $b_k$, $b_{k+1}$, and the term $\frac{t_0-t_w}{t_1-t_0}\delta + w$. Each sub-diagram includes the lines $Y_1 = Y_0 + \delta$ and $Y_1 = \frac{t_1-t_w}{t_0-t_w}Y_0 - \frac{t_1-t_0}{t_0-t_w}w$. The region $B_k^D$ is represented by a vertical highlighted bar (purple or green), varying based on the conditions specified in cases (a), (b), and (c) from the main text. The positions of $b_k$ and $b_{k+1}$ on the $Y_0$ axis define the boundaries for the illustrated region.

**Case a)** $b_{k+1} \le b_k < \frac{t_0-t_w}{t_1-t_0}\delta + w$

If $b_{k+1} \le b_k < \frac{t_0-t_w}{t_1-t_0}\delta + w$, as illustrated in Figure A.6(a) (note: original PDF references A.5(a), which is likely a typo as A.6 shows the relevant cases), for any $y_0 < b_{k+1} \le \frac{t_0-t_w}{t_1-t_0}\delta + w$, there exists