
  
![The image shows three graphs and mathematical notation related to support under concave treatment response.]

Figure A.5: Support under concave treatment response

The function \(\varphi\) can be readily shown to be nonincreasing. Thus, at the optimum \(B_k = (-\infty, b_k)\) with \(b_{k+1} \leq b_k\) and \(b_k \in [-\infty, \infty]\) for every integer \(k\). By Theorem 1, for \(\delta > 0\), \(B_k^D\) is written as

$$
B_k^D = \{ y_1 \in \mathbb{R} \mid \exists y_0 < b_k \text{ s.t. } 0 \leq y_1 - y_0 < \delta \text{ and } (t_0 - t_W) y_1 - (t_1 - t_W) y_0 \leq - (t_1 - t_0) w \} \\
\cup \{ y_1 \in \mathbb{R} \mid \exists y_0 < b_{k+1} \text{ s.t. } y_1 - y_0 \geq \delta \text{ and } (t_0 - t_W) y_1 - (t_1 - t_W) y_0 \leq - (t_1 - t_0) w \}.
$$

Note that \(Y_1 = Y_0 + \delta\) and 

$$
Y_1 = \frac{t_1 - t_W}{t_0 - t_W} Y_0 - \frac{t_1 - t_0}{t_0 - t_W} w
$$

intersect at 

$$
\left( \frac{t_0 - t_W}{t_1 - t_0} \delta + y_{-1}, \quad \frac{t_1 - t_W}{t_1 - t_0} \delta + w \right).
$$

I consider the following three cases:

a) \(b_{k+1} \leq b_k \leq \frac{t_0 - t_W}{t_1 - t_0} \delta + w\),

b) \(b_{k+1} \leq \frac{t_0 - t_W}{t_1 - t_0} \delta + w \leq b_k\),

c) \(\frac{t_0 - t_W}{t_1 - t_0} \delta + w \leq b_{k+1} \leq b_k\).

----

### Figure A.6: \(B_k^D\) for \(B_k = (-\infty, b_k)\) and \(B_{k+1} = (-\infty, b_{k+1})\)

| (a)                                                                                                                                                                                                        | (b)                                                                                                                                                                                                        | (c)                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Y-axis: \\(Y\_1\\)X-axis: \\(Y\_0\\)Vertical lines at \\(b\_{k+1}\\) and \\(b\_k\\)Horizontal line at \\(Y\_1 = Y\_0 + \delta\\)Region \\(B\_k^D\\) shaded in purple between \\(b\_{k+1}\\) and \\(b\_k\\) | Y-axis: \\(Y\_1\\)X-axis: \\(Y\_0\\)Vertical lines at \\(b\_{k+1}\\) and \\(b\_k\\)Horizontal line at \\(Y\_1 = Y\_0 + \delta\\)Region \\(B\_k^D\\) shaded in purple between \\(b\_{k+1}\\) and \\(b\_k\\) | Y-axis: \\(Y\_1\\)X-axis: \\(Y\_0\\)Vertical lines at \\(b\_{k+1}\\) and \\(b\_k\\)Horizontal line at \\(Y\_1 = Y\_0 + \delta\\)Region \\(B\_k^D\\) shaded in green and purple |


----

### Case a) \(b_{k+1} \leq b_k \leq \frac{t_0 - t_W}{t_1 - t_0} \delta + w\)

If \(b_{k+1} \leq b_k \leq \frac{t_0 - t_W}{t_1 - t_0} \delta + w\), as illustrated in Figure A.5(a), for any \(y_0 < b_{k+1} \leq \frac{t_0 - t_W}{t_1 - t_0} \delta + w\), there exists

----

