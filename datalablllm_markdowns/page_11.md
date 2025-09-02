# $\text{Appendix C: On the parametrization of the trade-off}$ $curve$

**Lemma 11**  $\lambda$  parametrizes all points on the CQ and CE trade-off curves with the possible exception of those lying on segments of constant slope.

**Proof.** We prove the lemma for the case of the  $CQ$  tradeoff curve. The proof for the CE trade-off curve is similar. Let  $(C(t), Q(t))$  for  $0 < t < 1$  be a parametrization of the trade-off curve with  $C(0)$  equal to the classical capacity and  $Q(1)$  equal to the quantum capacity. The function  $C(t)$  is monotonically decreasing and the function  $Q(t)$ is monotonically increasing. The graph of the trade-off curve is convex and, therefore, has one-sided directional derivatives at all points  $[70]$ . It is also monotonically  $\text{decreasing.}$ 

Consider the function  $f_{\lambda}(\mathcal{N})$  where

$$f_{\lambda}(\mathcal{N}) \equiv \max_{\rho^{XBE}} I(X;B) + \lambda I(A \rangle BX).$$

For any  $0 \le t \le 1$ , we have  $f_{\lambda}(\mathcal{N}) = C(t) + \lambda Q(t)$  if and only if

$$C(t) + \lambda Q(t) \ge C(s) + \lambda Q(s). \tag{C1}$$

for all  $0 \leq s \leq 1$ . Perhaps more instructively, if  $s < t$ and  $Q(s) \neq Q(t)$ , this inequality can be written as

$$\frac{C(s) - C(t)}{Q(s) - Q(t)} \ge -\lambda$$

because of the monotonicity of the functions  $C$  and  $Q$ . Likewise, when  $s > t$ , it has the form

$$\frac{C(s) - C(t)}{Q(s) - Q(t)} \leq -\lambda.$$

If  $(C(t), Q(t))$  is a point on the graph at which the derivative is not constant, then setting  $-\lambda$  to be the slope of the graph will lead to Eq.  $(C1)$  being satisfied. If the graph is not differentiable at  $(C(t), Q(t))$ , then the slope must drop discontinuously at that point. Setting  $-\lambda$  to any value in the gap will again lead to the condition being satisfied.  $\blacksquare$ 

At points where the graph is differentiable but the slope is constant,  $\lambda$  might not be a good parameter. These points, however, are in the convex hull of the points that  $\lambda$  does parametrize.

# Appendix D: Form of the $CQ$ Trade-off Curve for **Qubit Dephasing Channels**

We first prove two important lemmas and then prove a theorem that gives the exact form of the  $CQ$  trade-off curve

**Lemma 12** Let  $\mathcal{N}$  be a generalized dephasing channel. In the optimization task for the  $CQ$  trade-off curve, it

suffices to consider a classical-quantum state with diagonal conditional density operators, in the sense that the following inequality holds:

$$I\left(X;B\right)_{\rho} + \lambda I\left(A\rangle BX\right)_{\rho} \leq I\left(X;B\right)_{\theta} + \lambda I\left(A\rangle BX\right)_{\theta},$$

 $where$ 

$$\rho^{XABE} \equiv \sum_{x} p_{X}\left(x\right) \left|x\right\rangle \left\langle x\right|^{X} \otimes U_{\mathcal{N}}^{A^{\prime} \rightarrow BE}(\phi_{x}^{AA^{\prime}}),\n$$

$$\n\theta^{XABE} \equiv \sum_{x} p_{X}\left(x\right) \left|x\right\rangle \left\langle x\right|^{X} \otimes U_{\mathcal{N}}^{A^{\prime} \rightarrow BE}(\varphi_{x}^{AA^{\prime}}),$$

 $U_{\mathcal{N}}^{A' \rightarrow BE}$  is an isometric extension of  $\mathcal{N}$ ,  $\varphi_{x}^{A'} = \Delta(\varphi_{x}^{A'}) = \Delta(\varphi_{x}^{A'})$ , and  $\Delta$  is the completely dephasing  $channel.$ 

**Proof.** The proof of this lemma is similar to the proof of Lemma 9 in Ref. [71]. Consider another classicalquantum state  $\sigma$  in addition to the two presented in the statement of the theorem:

$$\sigma^{XAYE} \equiv \sum_{x} p_X(x) |x\rangle \langle x|^X \otimes (\Delta^{B \to Y} \circ U_{\mathcal{N}}^{A' \to BE}) (\phi_x^{AA'}).$$

Then the following chain of inequalities holds for all  $\lambda \geq$ 1:

$$\begin{split} &I\left(X;B\right)_{\rho} + \lambda I\left(A\rangle BX\right)_{\rho} \\ &= H\left(B\right)_{\rho} + (\lambda - 1)\,H\left(B|X\right)_{\rho} - \lambda H\left(E|X\right)_{\rho} \\ &\leq H\left(Y\right)_{\sigma} + (\lambda - 1)\,H\left(Y|X\right)_{\sigma} - \lambda H\left(E|X\right)_{\sigma} \\ &= H\left(B\right)_{\theta} + (\lambda - 1)\,H\left(B|X\right)_{\theta} - \lambda H\left(E|X\right)_{\theta} \\ &= I\left(X;B\right)_{\theta} + \lambda I\left(A\rangle BX\right)_{\theta}. \end{split}$$

The first equality follows from entropic manipulations. The inequality follows because the entropies  $H(B)_{\rho}$  and  $H(B|X)$ <sub>o</sub> can only increase under a complete dephasing [61]. The second equality follows because  $\mathcal{N} \circ \Delta = \Delta \circ \mathcal{N}$ and  $\mathcal{N}^c \circ \Delta = \mathcal{N}^c$  for a generalized dephasing channel  $\mathcal{N}$ , and the final equality follows from entropic manipulations.  $\blacksquare$ 

 $\textbf{Lemma 13} \ \textit{An} \quad \textit{ensemble} \quad \textit{of} \quad \textit{the} \quad \textit{following} \quad \textit{form}$ parametrizes all points on the CQ trade-off curve for a qubit dephasing channel:

$$\frac{1}{2}\left|0\right\rangle\left\langle 0\right|^{X}\otimes\psi_{0}^{AA'}+\frac{1}{2}\left|1\right\rangle\left\langle 1\right|^{X}\otimes\psi_{1}^{AA'},\tag{D1}$$

where  $\psi_0^{AA'}$  and  $\psi_1^{AA'}$  are pure states, defined as follows for  $\mu \in [0, 1/2]$ :

$$\text{Tr}_{A}\left\{\psi_{0}^{AA'}\right\} = \mu\left|0\right\rangle\left\langle 0\right|^{A'} + \left(1-\mu\right)\left|1\right\rangle\left\langle 1\right|^{A'}, \quad \text{(D2)}$$

$$\text{Tr}_{A}\left\{\psi_{1}^{AA'}\right\} = (1-\mu)\left|0\right\rangle\left\langle 0\right|^{A'} + \mu\left|1\right\rangle\left\langle 1\right|^{A'}. \quad \text{(D3)}$$

**Proof.** We assume without loss of generality that the dephasing basis is the computational basis. Consider a