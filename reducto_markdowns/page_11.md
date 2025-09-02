21

# Appendix C: On the parametrization of the trade-off curve

Lemma 11 \( \lambda \) parametrizes all points on the CQ and CE trade-off curves with the possible exception of those lying on segments of constant slope.

Proof. We prove the lemma for the case of the CQ tradeoff curve. The proof for the CE trade-off curve is similar. Let \( \left(C(t), Q(t)\right) \) for \( 0 \leq t \leq 1 \) be a parametrization of the trade-off curve with \( C(0) \) equal to the classical capacity and \( Q(1) \) equal to the quantum capacity. The function \( C(t) \) is monotonically decreasing and the function \( Q(t) \) is monotonically increasing. The graph of the trade-off curve is convex and, therefore, has one-sided directional derivatives at all points [70]. It is also monotonically decreasing.

Consider the function \( f_{\lambda}(\mathcal{N}) \) where

\( f_{\lambda}(\mathcal{N}) \equiv \max _{\rho} \mathbb{X}_{\rho}^{\mathrm{X}_{B E}} I(X ; B)+\lambda I(A) B X) \).

For any \( 0 \leq t \leq 1 \), we have \( f_{\lambda}(\mathcal{N})=C(t)+\lambda Q(t) \) if and only if

\[
C(t)+\lambda Q(t) \geq C(s)+\lambda Q(s)
\]

for all \( 0 \leq s \leq 1 \). Perhaps more instructively, if \( s<t \) and \( Q(s) \neq Q(t) \), this inequality can be written as

\( \frac{C(s)-C(t)}{Q(s)-Q(t)} \geq -\lambda \)

because of the monotonicity of the functions \( C \) and \( Q \). Likewise, when \( s>t \), it has the form

\( \frac{C(s)-C(t)}{Q(s)-Q(t)} \leq -\lambda \).

If \( \left(C(t), Q(t)\right) \) is a point on the graph at which the derivative is not constant, then setting \( -\lambda \) to be the slope of the graph will lead to Eq. (C1) being satisfied. If the graph is not differentiable at \( \left(C(t), Q(t)\right) \), then the slope must drop discontinuously at that point. Setting \( -\lambda \) to any value in the gap will again lead to the condition being satisfied.

At points where the graph is differentiable but the slope is constant, \( \lambda \) might not be a good parameter. These points, however, are in the convex hull of the points that \( \lambda \) does parametrize.

## Appendix D: Form of the CQ Trade-off Curve for Qubit Dephasing Channels

We first prove two important lemmas and then prove a theorem that gives the exact form of the CQ trade-off curve.

Lemma 12 Let \( \mathcal{N} \) be a generalized dephasing channel. In the optimization task for the \( C Q \) trade-off curve, it

suffices to consider a classical-quantum state with diagonal conditional density operators, in the sense that the following inequality holds:

\( I\left(X ; B\right)_{\rho}+\lambda I\left(A\right\rangle B X\right)_{\rho} \leq I\left(X ; B\right)_{\theta}+\lambda I\left(A\right\rangle B X\right)_{\theta} \),

where

\[
\begin{aligned}
\rho^{X A B E} & \equiv \sum_{x} p_{X}(x) \mid x\rangle\langle x \mid^{X} \otimes U_{\mathcal{N}}^{A^{\prime} \rightarrow B E}\left(\phi_{x}^{A A^{\prime}}\right), \\
\theta^{X A B E} & \equiv \sum_{x} p_{X}(x) \mid x\rangle\langle x \mid^{X} \otimes U_{\mathcal{N}}^{A^{\prime} \rightarrow B E}\left(\varphi_{x}^{A A^{\prime}}\right),
\end{aligned}
\]
\( U_{\mathcal{N}}^{A^{\prime} \rightarrow B E} \) is an isometric extension of \( \mathcal{N}, \varphi_{x}^{A^{\prime}}=\Delta\left(\varphi_{x}^{A^{\prime}}\right)=\Delta\left(\phi_{x}^{A^{\prime}}\right) \), and \( \Delta \) is the completely dephasing channel.

Proof. The proof of this lemma is similar to the proof of Lemma 9 in Ref. [71]. Consider another classicalquantum state \( \sigma \) in addition to the two presented in the statement of the theorem:

\( r^{X A Y E} \equiv \sum p_{X}(x) \mid x\rangle\langle x \mid^{X} \otimes\left(\Delta^{B \rightarrow Y} \circ U_{\mathcal{N}}^{A^{\prime} \rightarrow B E}\right)\left(\phi_{x}^{A A^{\prime}}\right) \).

Then the following chain of inequalities holds for all \( \lambda \geq \) 1:

\( I\left(X ; B\right)_{\rho}+\lambda I\left(A\right\rangle B X\right)_{\rho} \)

\( { }=\left.H\left(B\right)_{\rho}+\left(\lambda-1\right) H\left(B \mid X\right)_{\rho}-\lambda H\left(E \mid X\right)_{\rho}\right. \)

\( \leq H(Y)_{\sigma}+(\lambda-1) H(Y \mid X)_{\sigma}-\lambda H(E \mid X)_{\sigma} \)

\( { }=\left.H(B)\right|_{\theta}+(\lambda-1) H\left(B \mid X\right)_{\theta}-\lambda H\left(E \mid X\right)_{\theta} \)

\( { }=I(X ; B)_{\theta}+\lambda I(A \mid B X)_{\theta} \).

The first equality follows from entropic manipulations. The inequality follows because the entropies \( H(B)_{\rho} \) and \( H(B \mid X)_{\rho} \) can only increase under a complete dephasing [61]. The second equality follows because \( \mathcal{N} \circ \Delta=\Delta \circ \mathcal{N} \) and \( \mathcal{N}^{c} \circ \Delta=\mathcal{N}^{c} \) for a generalized dephasing channel \( \mathcal{N} \), and the final equality follows from entropic manipulations. \[
\blacksquare
\]

Lemma 13 An ensemble of the following form parametrizes all points on the CQ trade-off curve for a qubit dephasing channel:

\[
\frac{1}{2} \left|0\right\rangle\left\langle0\right|^{X} \otimes \psi_{0}^{A A^{\prime}}+\frac{1}{2} \left|1\right\rangle\left\langle1\right|^{X} \otimes \psi_{1}^{A A^{\prime}}
\]

where \( \psi_{0}^{\mathrm{AA}^{\prime}} \) and \( \psi_{1}^{\mathrm{AA}^{\prime}} \) are pure states, defined as follows for \( \mu \in[0,1 / 2] \) :
\[
\begin{array}{l}
\operatorname{Tr}_{A}\left\{\psi_{0}^{\mathrm{AA}^{\prime}}\right\}=\mu \mid 0\rangle\left\langle 0\right\rangle^{A^{\prime}}+(1-\mu) \mid 1\rangle\left\langle 1\right\rangle^{A^{\prime}}, \quad \text { (D2) } \\
\operatorname{Tr}_{A}\left\{\psi_{1}^{\mathrm{AA}^{\prime}}\right\}=(1-\mu) \mid 0\rangle\left\langle 0\right\rangle^{A^{\prime}}+\mu \mid 1\rangle\left\langle 1\right\rangle^{A^{\prime}} . \quad \text { (D3) }
\end{array}
\]

Proof. We assume without loss of generality that the dephasing basis is the computational basis. Consider a

=