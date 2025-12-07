

in (a) and (b), respectively. Therefore, from consideration of Case a, b and c,

$$\sup_{\{B_k\}_{k=-\infty}^\infty}\sum_{k=-\infty}^\infty \max\left\{\mu_{0,W}\left(B_k|w\right)-\mu_{1,W}\left(B_k^D|w\right),0\right\}$$
$$=\sup_{\{b_k\}_{k=-\infty}^\infty}\sum_{k=-\infty}^\infty \max\left\{F_{0,W}\left(b_k|w\right)-F_{1,W}\left(\frac{t_1-t_W}{t_0-t_W}b_{k+1}-\frac{t_1-t_0}{t_0-t_W}w|w\right),0\right\}$$

where  $\frac{t_0-t_W}{t_1-t_0}\delta+w\le b_{k+1}\le b_k$ . Consequently, the sharp upper bound is written as follows: letting  $F_{\Delta,W}^U(\delta|w)$  be the sharp upper bound on  $\Pr(Y_1-Y_0\le\delta|W=w)$ ,

$$F_\Delta^U(\delta)$$
$$=\int F_{\Delta,W}^U(\delta|w)dF_W(w)$$
$$=\int\left\{1-\sup_{\{B_k\}_{k=-\infty}^\infty}\sum_{k=-\infty}^\infty \max\left\{\mu_{0,W}\left(B_k|w\right)-\mu_{1,W}\left(B_k^D|w\right),0\right\}\right\}dF_W$$
$$=1+\int \inf_{\{b_k\}_{k=-\infty}^\infty}\sum_{k=-\infty}^\infty \min\left\{F_{1,W}\left(\frac{t_1-t_W}{t_0-t_W}b_{k+1}-\frac{t_1-t_0}{t_0-t_W}w|w\right)-F_{0,W}\left(b_k|w\right),0\right\}dF_W$$

where  $\frac{t_0-t_W}{t_1-t_0}\delta+w\le b_{k+1}\le b_k$ . ■

# Appendix B

Appendix B presents the procedure used to compute the sharp lower bound under MTR in Section 4 and Section 5. The following lemma is useful for reducing computational costs:

**Lemma B.1** Let

$$\{a_k\}_{k=-\infty}^\infty\in \arg\max_{\{a_k\}_{k=-\infty}^\infty\in\mathcal{A}_\delta}\sum_{k=-\infty}^\infty \max\left\{F_1\left(a_{k+1}\right)-F_0\left(a_k\right),0\right\},$$
$$\text{where }\mathcal{A}_\delta=\left\{\{a_k\}_{k=-\infty}^\infty;0\le a_{k+1}-a_k\le\delta\text{ for each integer }k\right\}.$$

It is innocuous to assume that  $\{a_k\}_{k=-\infty}^\infty$  satisfies  $a_{k+2}-a_k>\delta$  for each integer  $k$ .

**Proof.** I will show that for any sequence  $\{a_k\}_{k=-\infty}^\infty\in\mathcal{A}_\delta$  satisfying  $a_{k+2}-a_k\le\delta$  for some integer  $k$ , one can construct  $\{\widetilde{a}_k\}_{k=-\infty}^\infty\in\mathcal{A}_\delta$  with  $\widetilde{a}_{k+2}-\widetilde{a}_k>\delta$  for each integer  $k$  and

$$\sum_{k=-\infty}^\infty \max\left\{F_1\left(a_{k+1}\right)-F_0\left(a_k\right),0\right\}\le\sum_{k=-\infty}^\infty \max\left\{F_1\left(\widetilde{a}_{k+1}\right)-F_1\left(\widetilde{a}_k\right),0\right\}.$$