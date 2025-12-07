![Figure A.5: Support under concave treatment response](figure-A.5.png)

**Figure A.5 (summary):** A coordinate graph with axes $Y_0$ and $Y_1$. Two lines intersect: one is the line $Y_1 = Y_0$, and the other is $Y_1 = \frac{t_1 - t_W}{t_0 - t_W}Y_0 - \frac{t_1 - t_0}{t_0 - t_W}w$. A yellow shaded region extends upwards from the intersection, bounded by the two lines.

The function $\varphi$ can be readily shown to be nonincreasing. Thus, at the optimum $B_k = (-\infty, b_k)$ with $b_{k+1} \le b_k$ and $b_k \in [-\infty, \infty]$ for every integer $k$. By Theorem 1, for $\delta > 0$, $B_k^D$ is written as

$$
\begin{aligned}
B_k^D &= \{y_1 \in \mathbb{R} \mid \exists y_0 < b_k \text{ s.t. } 0 \le y_1 - y_0 < \delta \text{ and } (t_0 - t_W) y_1 - (t_1 - t_W) y_0 \le - (t_1 - t_0) w\} \\
&\quad \cup \{y_1 \in \mathbb{R} \mid \exists y_0 < b_{k+1} \text{ s.t. } y_1 - y_0 \ge \delta \text{ and } (t_0 - t_W) y_1 - (t_1 - t_W) y_0 \le - (t_1 - t_0) w\} \,.
\end{aligned}
$$

Note that $Y_1 = Y_0 + \delta$ and $Y_1 = \frac{t_1-t_W}{t_0-t_W}Y_0 - \frac{t_1-t_0}{t_0-t_W}w$ intersect at $\left( \frac{t_0-t_W}{t_1-t_0}\delta + y_{-1}, \frac{t_1-t_W}{t_1-t_0}\delta + w \right)$. I consider the following three cases: a) $b_{k+1} \le b_k \le \frac{t_0-t_W}{t_1-t_0}\delta + w$, b) $b_{k+1} \le \frac{t_0-t_W}{t_1-t_0}\delta + w \le b_k$, and c) $\frac{t_0-t_W}{t_1-t_0}\delta + w \le b_{k+1} \le b_k$.

![Figure A.6: $B_k^D$ for $B_k = (-\infty, b_k)$ and $B_{k+1} = (-\infty, b_{k+1})$](figure-A.6.png)

**Figure. A.6 (summary):** Three graphs labeled (a), (b), and (c) on $Y_0, Y_1$ axes showing different geometric configurations of the region $B_k^D$. The regions are defined by vertical boundaries at $b_{k+1}$ and $b_k$ and the diagonal lines $Y_1 = Y_0 + \delta$ and the treatment response line.
- **(a):** Shaded region is L-shaped, bounded by $b_{k+1}$ and $b_k$.
- **(b):** Shaded region is split or transitional, with the intersection point between the $b$ bounds.
- **(c):** Shaded region shifts relative to the intersection point.

**Figure. A.6:** $B_k^D$ for $B_k = (-\infty, b_k)$ and $B_{k+1} = (-\infty, b_{k+1})$

**Case a)** $b_{k+1} \le b_k \le \frac{t_0-t_W}{t_1-t_0}\delta + w$

If $b_{k+1} \le b_k \le \frac{t_0-t_W}{t_1-t_0}\delta + w$, as illustrated in Figure A.5(a), for any $y_0 < b_{k+1} \le \frac{t_0-t_W}{t_1-t_0}\delta + w$, there exists