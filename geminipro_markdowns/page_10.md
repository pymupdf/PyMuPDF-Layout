in (a) and (b), respectively. Therefore, from consideration of Case a, b and c,

$$
\sup_{\{B_k\}_{k=-\infty}^{\infty}} \sum_{k=-\infty}^{\infty} \max \left\{ \mu_{0,w}(B_k|w) - \mu_{1,w}(B_k^D|w), 0 \right\} \\
= \sup_{\{b_k\}_{k=-\infty}^{\infty}} \sum_{k=-\infty}^{\infty} \max \left\{ F_{0,w}(b_k|w) - F_{1,w}\left(\frac{t_1-t_w}{t_0-t_w} b_{k+1} - \frac{t_1-t_0}{t_0-t_w}w \middle| w\right), 0 \right\}
$$

where $\frac{t_0-t_w}{t_1-t_0} \delta + w \le b_{k+1} \le b_k$. Consequently, the sharp upper bound is written as follows: letting $F_{\Delta,w}^{U}(\delta|w)$ be the sharp upper bound on $\Pr(Y_1 - Y_0 \le \delta | W = w)$,

$$
F_{\Delta}^{U}(\delta) \\
= \int F_{\Delta,w}^{U}(\delta|w) dF_W(w) \\
= \int \left\{ 1 - \sup_{\{B_k\}_{k=-\infty}^{\infty}} \sum_{k=-\infty}^{\infty} \max\left\{\mu_{0,w}(B_k|w) - \mu_{1,w}(B_k^D|w), 0\right\} \right\} dF_W(w) \\
= 1 + \int \inf_{\{b_k\}_{k=-\infty}^{\infty}} \sum_{k=-\infty}^{\infty} \min\left\{ F_{1,w}\left(\frac{t_1-t_w}{t_0-t_w}b_{k+1} - \frac{t_1-t_0}{t_0-t_w}w \middle| w\right) - F_{0,w}(b_k|w), 0 \right\} dF_W(w)
$$

where $\frac{t_0-t_w}{t_1-t_0}\delta + w \le b_{k+1} \le b_k$.

# Appendix B

Appendix B presents the procedure used to compute the sharp lower bound under MTR in Section 4 and Section 5. The following lemma is useful for reducing computational costs:

## Lemma B.1
Let

$$
\{a_k\}_{k=-\infty}^{\infty} \in \underset{\{a_k\}_{k=-\infty}^{\infty} \in A_\delta}{\arg\max} \sum_{k=-\infty}^{\infty} \max \{F_1 (a_{k+1}) - F_0 (a_k), 0\}, \\
\text{where } A_\delta = \{\{a_k\}_{k=-\infty}^{\infty}; 0 \le a_{k+1} - a_k \le \delta \text{ for each integer } k \}.
$$

It is innocuous to assume that $\{a_k\}_{k=-\infty}^{\infty}$ satisfies $a_{k+2} - a_k > \delta$ for each integer $k$.

**Proof.** I will show that for any sequence $\{a_k\}_{k=-\infty}^{\infty} \in A_\delta$ satisfying $a_{k+2} - a_k \le \delta$ for some integer $k$, one can construct $\{\tilde{a}_k\}_{k=-\infty}^{\infty} \in A_\delta$ with $\tilde{a}_{k+2} - \tilde{a}_k > \delta$ for each integer $k$ and

$$
\sum_{k=-\infty}^{\infty} \max \{F_1(a_{k+1}) - F_0(a_k), 0\} \le \sum_{k=-\infty}^{\infty} \max \{F_1(\tilde{a}_{k+1}) - F_1(\tilde{a}_k), 0\}.
$$