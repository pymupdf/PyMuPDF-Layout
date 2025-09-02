7

where

\[
\begin{aligned}
A & =\frac{\left(x_{3}^{2}+y_{2}^{2}\right)^{d} \mid x_{3}^{2}+\left(y_{3}-y_{1}\right)^{2}\right|^{d}}{\left(x_{3}^{2}+\left(y_{2}-y_{1}\right)^{2}\right)^{d}\left(x_{3}^{2}+y_{3}^{2}\right)^{d}}, \\
B & =\frac{\left[\left(x_{3}-x_{1}\right)^{2}+\left(y_{2}-y_{1}\right)^{2}\right]^{d}}{\left(x_{3}-x_{1}\right)^{2 d}} \\
& \times \frac{\left[\left(x_{3}-x_{1}\right)^{2}+\left(y_{3}-y_{2}\right)^{2}\right]^{d}}{\left[\left(y_{3}-y_{1}\right)^{2}+\left(x_{3}-x_{1}\right)^{2}\right]^{d}}, \\
\text { and } \\
C & =\frac{\left|x_{1}^{2}+y_{1}^{2}\right|^{d}\left|x_{1}^{2}+\left(y_{2}-y_{1}\right)^{2}\right|^{d}}{\left|x_{1}\right|^{2 d}\left|y_{2}^{2}+x_{1}^{2}\right|^{d}}.
\end{aligned}
\]

We write
\[
A B C-B-C+1=(A-1) B C+(B-1)(C-1)
\]

It is apparent form Eq. (A12) that the leading singularity originates from the first term, \( \left(A-1\right) B C \approx A-1 \approx-2 d\left(y_{1}-0\right)\left(y_{3}-y_{2}\right) \). Introducing new variables as in the Sec. III and integrating over \( x_{i} \) s we obtain
\[
\begin{aligned}
\Sigma^{(6)} & =2 d \mathrm{i} \frac{\left(J a^{d}\right)^{6} \Gamma(5-6 d)}{\left(-\mathrm{i}\left(\omega-k_{y}\right)\right)^{5-6 d}} \\
& \times \int_{0}^{\infty} \prod_{i=1}^{3} d \xi_{i} \frac{\xi_{1}^{1-2 d} \xi_{2}^{-2 d} \xi_{3}^{1-2 d}}{\left(\alpha+\xi_{1}+\xi_{2}+\xi_{3}\right)^{5-6 d}} .
\end{aligned}
\]

Here again, the integrals are divergent on the upper limit. Similarly to the previous section we differentiate it once with respect to the variable \( \alpha \) introduced in Eq. (14) in order to isolate the leading logarithmic singularity,

\[
\begin{aligned}
\frac{\partial \Sigma^{(6)}}{\partial \alpha} & =-\frac{2 d \mathrm{i} \alpha^{-1}\left(\mathcal{J} a^{d}\right)^{6} \Gamma(6-6 d)}{\left(-\mathrm{i}\left(\omega-k_{y}\right)\right)^{5-6 d}} \\
& \times \int_{0}^{\infty} \prod_{i=1}^{3} d \xi_{i} \frac{\xi_{1}^{1-2 d} \xi_{2}^{-2 d} \xi_{3}^{1-2 d}}{\left(1+\xi_{1}+\xi_{2}+\xi_{3}\right)^{6-6 d}} .
\end{aligned}
\]

The remaining integrals are easily evaluated. The subsequent integration over \( \alpha \) restores the singularity in the

[1] Ar. Abanov, A. V. Chubukov and J. Schmalian, Adv. Phys. 52, 119 (2003) and references therein.

[2] S. Sachdev, M. A. Metlitski, Y. Qi and C. Xu, arXiv: 0907.3732 and references therein.

[3] M. Khodas and A. M. Tsvelik, arXiv:0910.3967.

self energy correction,

\[
\begin{aligned}
\mathfrak{c}^{(6)} & =2 d \frac{-\mathrm{i}\left(J a^{d}\right)^{6} \Gamma\left(1-2 d\right) \Gamma^{2}\left(2-2 d\right)}{\left(-\mathrm{i}\left(\omega-k_{y}\right)\right)^{5-6 d}} \\
& \times\left(\log \alpha+C\right),
\end{aligned}
\]

where \( C \) is an integration constant. The singular part of Eq. (A15) is given by Eq. (24).

## Appendix B: Leading singularities at the shadow
mass shell, \( \omega \sim k_{y} \) to the fourth order.

In this appendix we evaluate the singular contributions to the Green function at the shadow mass shell, \( \omega \sim k_{y} \) to fourth order in the coupling constant. We start with the expression (A1) introduced in App. A 1. In contrast to the discussion in App. A 1 we anticipate the singularity at \( \omega=k_{y} \) to come from the region \( y_{2} \gg x_{2} \), and introduce new variables accordingly, \( x_{2}=\xi y_{2}, y_{1}=\eta y_{2} \). Performing integration over \( y_{2} \) we obtain
\[
\begin{aligned}
\Sigma^{(4)} & =\mathrm{i}\left(J a^{d}\right)^{4} \int_{0}^{\infty} d \xi \int_{0}^{1} d \eta \frac{\Gamma\left(3-4 d\right) \eta^{-2 d}\left(1-\eta\right)^{-2 d}}{\left[\left(-\mathrm{i}\left(\left(\omega-k_{y}\right)+\left(\omega-k_{x}\right) \xi\right)\right)\right]^{3-4 d}} \\
& \times\left[\frac{\left|\left(1-\eta\right)^{2}+\xi^{2}\right|^{d}\left|\eta^{2}+\xi^{2}\right|^{d}}{\left|1+\xi^{2}\right|^{d}\left|\xi^{2}\right|^{2 d}}-1\right] .
\end{aligned}
\]

\[
\begin{aligned}
\Sigma^{(4)} & =\mathrm{i}\left(\mathcal{J} a^{d}\right)^{4} \int_{0}^{\infty} d \xi \int_{0}^{1} d \eta \frac{\Gamma\left(3-4 d\right) \eta^{-2 d}\left(1-\eta\right)^{-2 d}}{\left[\left(-i\left(\omega-k_{y}\right)+\left(\omega-k_{x}\right) \xi\right)\right]^{3-4 d}} \\
& \times\left[\frac{\left|1-\eta\right|^{2}+\xi^{2} \mid \eta^{2}+\xi^{2} \mid^{d}}{\left|1+\xi^{2} \mid \xi \mid^{2 d}\right|}-1\right] .
\end{aligned}
\]

We notice that the singularity at \( \omega \sim k_{y} \) comes from the region of small \( \xi \). Therefore we keep only the first term in the square brackets in Eq. (B1). After performing remaining integrations over \( \xi_{i} \) s we obtain

\[
\begin{aligned}
\Sigma^{(4)} & =\frac{\mathrm{i}\left(\mathcal{J} a^{d}\right)^{4} \Gamma\left(1-2 d\right) \Gamma\left(2-2 d\right) \alpha^{2-2 d}}{\left(-\mathrm{i}\left(\omega-k_{x}\right)\right)^{3-4 d}} . \\
\end{aligned}
\]

We stress that contrary to the mass shell singularities discussed in App. A, where it was important to compute the self-energy, at the shadow mass shell it is enough to consider the Green function itself.

[4] N. Doiron-Leyraud et.al., Nature (London) 447, 565 (2007).

[5] E. A. Yelland et.al., Phys. Rev. Lett. 100, 047003 (2008).

[6] S. Sachdev, arXiv:0907.0008.

=