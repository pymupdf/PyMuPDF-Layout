```markdown
## Appendix C: On the parametrization of the trade-off curve

**Lemma 11** $\lambda$ parametrizes all points on the CQ and CE trade-off curves with the possible exception of those lying on segments of constant slope.

**Proof.** We prove the lemma for the case of the CQ trade-off curve. The proof for the CE trade-off curve is similar. Let $(C(t), Q(t))$ for $0 \le t \le 1$ be a parametrization of the trade-off curve with $C(0)$ equal to the classical capacity and $Q(1)$ equal to the quantum capacity. The function $C(t)$ is monotonically decreasing and the function $Q(t)$ is monotonically increasing. The graph of the trade-off curve is convex and, therefore, has one-sided directional derivatives at all points [70]. It is also monotonically decreasing.

Consider the function $f_\lambda(N)$ where

$$
f_\lambda(N) \equiv \max_{P_{XBE}} I(X; B) + \lambda I(A; BX)
$$

For any $0 \le t \le 1$, we have $f_\lambda(N) = C(t) + \lambda Q(t)$ if and only if

$$
C(t) + \lambda Q(t) \ge C(s) + \lambda Q(s) \quad \text{(C1)}
$$

for all $0 < s < 1$. Perhaps more instructively, if $s < t$ and $Q(s) \ne Q(t)$, this inequality can be written as

$$
\frac{C(s) - C(t)}{Q(s) - Q(t)} \ge -\lambda
$$

because of the monotonicity of the functions $C$ and $Q$. Likewise, when $s > t$, it has the form

$$
\frac{C(s) - C(t)}{Q(s) - Q(t)} \le -\lambda
$$

If $(C(t), Q(t))$ is a point on the graph at which the derivative is not constant, then setting $-\lambda$ to be the slope of the graph will lead to Eq. (C1) being satisfied. If the graph is not differentiable at $(C(t), Q(t))$, then the slope must drop discontinuously at that point. Setting $-\lambda$ to any value in the gap will again lead to the condition being satisfied.

At points where the graph is differentiable but the slope is constant, $\lambda$ might not be a good parameter. These points, however, are in the convex hull of the points that $\lambda$ does parametrize.

suffices to consider a classical-quantum state with diagonal conditional density operators, in the sense that the following inequality holds:

$$
I(X; B)_\rho + \lambda I(A; BX)_\rho \le I(X; B)_\theta + \lambda I(A; BX)_\theta,
$$

where

$$
\rho^{XABE} = \sum_x p_x(x) |x\rangle\langle x| \otimes U_N^{A' \to BE}(\tilde{\phi}_x^{AA'}),
$$

$$
\sigma^{XABE} = \sum_x p_x(x) |x\rangle\langle x| \otimes U_N^{A \to BE}(\phi_x^{AA'}),
$$

$U_N^{A' \to BE}$ is an isometric extension of $N$, $\tilde{\phi}_x^{A'} = \Delta(\tilde{\phi}_x^{A'})$, and $\Delta$ is the completely dephasing channel.

**Proof.** The proof of this lemma is similar to the proof of Lemma 9 in Ref. [71]. Consider another classical-quantum state $\sigma$ in addition to the two presented in the statement of the theorem:

$$
\sigma^{XAYE} = \sum_x p_x(x) |x\rangle\langle x| \otimes (\Delta^{B \to Y} \circ U_N^{A' \to BE})(\tilde{\phi}_x^{AA'}).
$$

Then the following chain of inequalities holds for all $\lambda \ge 1$:

$$
\begin{aligned}
I(X; B)_\rho + \lambda I(A; BX)_\rho &= H(B)_\rho + (\lambda - 1) H(B|X)_\rho - \lambda H(E|X)_\rho \\
&\le H(Y)_\sigma + (\lambda - 1) H(Y|X)_\sigma - \lambda H(E|X)_\sigma \\
&= H(B)_\theta + (\lambda - 1) H(B|X)_\theta - \lambda H(E|X)_\theta \\
&= I(X; B)_\theta + \lambda I(A; BX)_\theta.
\end{aligned}
$$

The first equality follows from entropic manipulations. The inequality follows because the entropies $H(B)_\rho$ and $H(B|X)_\rho$ can only increase under a complete dephasing [61]. The second equality follows because $N \circ \Delta = \Delta \circ N$ and $N^c \circ \Delta = N^c$ for a generalized dephasing channel $N$, and the final equality follows from entropic manipulations.

## Appendix D: Form of the CQ Trade-off Curve for Qubit Dephasing Channels

We first prove two important lemmas and then prove a theorem that gives the exact form of the CQ trade-off curve.

**Lemma 12** Let $N$ be a generalized dephasing channel. In the optimization task for the CQ trade-off curve, it

**Lemma 13** An ensemble of the following form parametrizes all points on the CQ trade-off curve for a qubit dephasing channel:

$$
\frac{1}{2} |0\rangle\langle 0|^X \otimes \psi_0^{AA'} + \frac{1}{2} |1\rangle\langle 1|^X \otimes \psi_1^{AA'}, \quad \text{(D1)}
$$

where $\psi_0^{AA'}$ and $\psi_1^{AA'}$ are pure states, defined as follows for $\mu \in [0, 1/2]$:

$$
\text{Tr}_A \{\psi_0^{AA'}\} = \mu |0\rangle\langle 0|^{A'} + (1 - \mu) |1\rangle\langle 1|^{A'}, \quad \text{(D2)}
$$

$$
\text{Tr}_A \{\psi_1^{AA'}\} = (1 - \mu) |0\rangle\langle 0|^{A'} + \mu |1\rangle\langle 1|^{A'}. \quad \text{(D3)}
$$

**Proof.** We assume without loss of generality that the dephasing basis is the computational basis. Consider a
```