in (a) and (b), respectively. Therefore, from consideration of Case a, b and c,

sup

\( \sum^{\infty} \)

\( \left\{B_{k}\right\}_{k=-\infty}^{\infty} k=-\infty \)

\( \max \left\{\mu_{0, W}\left(B_{k} \mid w\right)-\mu_{1, W}\left(B_{k}^{D} \mid w\right), 0\right\} \)

\(=\sup\)

Σ

max

[ ] \( F_{0, W} \)

\( F_{0, W}\left(b_{k} \mid w\right)-F_{1, W} \)

\( t_{1} \)

\( -t_{W} \)

\( -b_{k+1} \)

\( t_{1} \)

\( \left\{b_{k}\right\}_{k=-\infty}^{\infty} \) \( k=-\infty \) \( k=-\infty \)

- \( \left.\frac{t_{1}-t_{0}}{t_{0}-t_{W}} w \mid w\right), 0\right\} \)

\( t_{0}-t_{W} \)

- where \( \frac{t_{0}-t_{W}}{t_{1}-t_{0}} \delta+w \leq b_{k+1} \leq b_{k} \). Consequently, the sharp upper bound is written as follows: letting \( F_{\Delta, W}^{U}(\delta \mid w) \) be the sharp upper bound on \( \operatorname{Pr}\left(Y_{1}-Y_{0} \leq \delta \mid W=w\right) \),

\[
\begin{aligned}
F_{\Delta}^{U}(\delta) & =\int F_{\Delta, W}^{U}(\delta \mid w) d F_{W}(w) \\
& =\int\left\{1-\sup _{\left\{B_{k}\right\}_{k=-\infty}^{\infty}} \sum_{k=-\infty}^{\infty} \max \left\{\mu_{0, W}\left(B_{k} \mid w\right)-\mu_{1, W}\left(B_{k}^{D} \mid w\right), 0\right\}\right\} d F_{W} \\
& =1+\int_{\left\{b_{k}\right\}_{k=-\infty}^{\infty}} \operatorname{inf} \sum_{k=-\infty}^{\infty} \min \left\{F_{1, W}\left(\frac{t_{1}-t_{W}}{t_{0}-t_{W}} b_{k+1}-\frac{t_{1}-t_{0}}{t_{0}-t_{W}} w \mid w\right)-F_{0, W}\left(b_{k} \mid w\right), 0\right\} d F_{W} \\
\text { where } \frac{t_{0}-t_{W}}{t_{1}-t_{0}} \delta+w & \leq b_{k+1} \leq b_{k} .
\end{aligned}
\]

## Appendix B

Appendix B presents the procedure used to compute the sharp lower bound under MTR in Section 4 and Section 5. The following lemma is useful for reducing computational costs:

Lemma B.1 Let

\[
\left\{a_{k}\right\}_{k=-\infty}^{\infty} \in \underset{\left\{a_{k}\right\}_{k=-\infty}^{\infty} \in \mathcal{A}_{\delta}}{\arg \max } \sum \max \left\{F_{1}\left(a_{k+1}\right)-F_{0}\left(a_{k}\right), 0\right\},
\]
where \( \mathcal{A}_{\delta}=\left\{\left\{a_{k}\right\}_{k=-\infty}^{\infty} ; 0 \leq a_{k+1}-a_{k} \leq \delta \text { for each integer } k\right\} \).

It is innocuous to assume that \( \left\{a_{k}\right\}_{k=-\infty}^{\infty} \) satisfies \( a_{k+2}-a_{k}>\delta \) for each integer \( k \).

Proof. I will show that for any sequence \( \left\{a_{k}\right\}_{k=-\infty}^{\infty} \in \mathcal{A}_{\delta} \) satisfying \( a_{k+2}-a_{k} \leq \delta \) for some integer \( k \), one can construct \( \left\{\tilde{a}_{k}\right\}_{k=-\infty}^{\infty} \in \mathcal{A}_{\delta} \) with \( \tilde{a}_{k+2}-\tilde{a}_{k}>\delta \) for each integer \( k \) and

k=-∞

\( \max \left\{F_{1}\left(a_{k+1}\right)-F_{0}\left(a_{k}\right), 0\right\} \leq \)

∞

\( \max \left\{F_{1}\left(\tilde{a}_{k+1}\right)-F_{1}\left(\tilde{a}_{k}\right), 0\right\} \).

\( k=-\infty \)

72

=