
21

## Appendix C: On the parametrization of the trade-off curve

**Lemma 11** λ parametrizes all points on the CQ and CE trade-off curves with the possible exception of those lying on segments of constant slope.

**Proof.** We prove the lemma for the case of the CQ trade-off curve. The proof for the CE trade-off curve is similar. Let $(C(t), Q(t))$ for $0 \leq t \leq 1$ be a parametrization of the trade-off curve with $C(0)$ equal to the classical capacity and $Q(1)$ equal to the quantum capacity. The function $C(t)$ is monotonically decreasing and the function $Q(t)$ is monotonically increasing. The graph of the trade-off curve is convex and, therefore, has one-sided directional derivatives at all points [70]. It is also monotonically decreasing.

Consider the function $f_λ(\mathcal{N})$ where

$$f_λ(\mathcal{N}) \equiv \max_{\rho^{XBE}} I(X; B) + λI(A\rangle BX).$$

For any $0 \leq t \leq 1$, we have $f_λ(\mathcal{N}) = C(t) + λQ(t)$ if and only if

$$C(t) + λQ(t) \geq C(s) + λQ(s). \quad (C1)$$

for all $0 \leq s \leq 1$. Perhaps more instructively, if $s < t$ and $Q(s) \neq Q(t)$, this inequality can be written as

$$\frac{C(s) - C(t)}{Q(s) - Q(t)} \geq -λ$$

because of the monotonicity of the functions $C$ and $Q$. Likewise, when $s > t$, it has the form

$$\frac{C(s) - C(t)}{Q(s) - Q(t)} \leq -λ.$$

If $(C(t), Q(t))$ is a point on the graph at which the derivative is not constant, then setting $-λ$ to be the slope of the graph will lead to Eq. (C1) being satisfied. If the graph is not differentiable at $(C(t), Q(t))$, then the slope must drop discontinuously at that point. Setting $-λ$ to any value in the gap will again lead to the condition being satisfied. ■

At points where the graph is differentiable but the slope is constant, λ might not be a good parameter. These points, however, are in the convex hull of the points that λ does parametrize.

## Appendix D: Form of the CQ Trade-off Curve for Qubit Dephasing Channels

We first prove two important lemmas and then prove a theorem that gives the exact form of the CQ trade-off curve.

**Lemma 12** Let $\mathcal{N}$ be a generalized dephasing channel. In the optimization task for the CQ trade-off curve, it suffices to consider a classical-quantum state with diagonal conditional density operators, in the sense that the following inequality holds:

$$I(X; B)_ρ + λI(A\rangle BX)_ρ \leq I(X; B)_θ + λI(A\rangle BX)_θ,$$

where

$$ρ^{XABE} \equiv \sum_x p_X(x) |x\rangle \langle x|^X \otimes U_{\mathcal{N}}^{A' \to BE}(\phi_x^{AA'}),$$

$$θ^{XABE} \equiv \sum_x p_X(x) |x\rangle \langle x|^X \otimes U_{\mathcal{N}}^{A' \to BE}(\zeta_x^{AA'}),$$

$U_{\mathcal{N}}^{A' \to BE}$ is an isometric extension of $\mathcal{N}$, $\zeta_x^{A'} = \Delta(\phi_x^{A'}) = \Delta(\phi_x^{A'})$, and $\Delta$ is the completely dephasing channel.

**Proof.** The proof of this lemma is similar to the proof of Lemma 9 in Ref. [71]. Consider another classical-quantum state σ in addition to the two presented in the statement of the theorem:

$$σ^{XAYE} \equiv \sum_x p_X(x) |x\rangle \langle x|^X \otimes (\Delta^{B \to Y} \circ U_{\mathcal{N}}^{A' \to BE})(\phi_x^{AA'}).$$

Then the following chain of inequalities holds for all $λ \geq 1$:

$$I(X; B)_ρ + λI(A\rangle BX)_ρ$$
$$= H(B)_ρ + (λ - 1)H(B|X)_ρ - λH(E|X)_ρ$$
$$\leq H(Y)_σ + (λ - 1)H(Y|X)_σ - λH(E|X)_σ$$
$$= H(B)_θ + (λ - 1)H(B|X)_θ - λH(E|X)_θ$$
$$= I(X; B)_θ + λI(A\rangle BX)_θ.$$

The first equality follows from entropic manipulations. The inequality follows because the entropies $H(B)_ρ$ and $H(B|X)_ρ$ can only increase under a complete dephasing [61]. The second equality follows because $\mathcal{N} \circ \Delta = \Delta \circ \mathcal{N}$ and $\mathcal{N}^c \circ \Delta = \mathcal{N}^c$ for a generalized dephasing channel $\mathcal{N}$, and the final equality follows from entropic manipulations. ■

**Lemma 13** An ensemble of the following form parametrizes all points on the CQ trade-off curve for a qubit dephasing channel:

$$\frac{1}{2}|0\rangle \langle 0|^X \otimes \psi_0^{AA'} + \frac{1}{2}|1\rangle \langle 1|^X \otimes \psi_1^{AA'}, \quad (D1)$$

where $\psi_0^{AA'}$ and $\psi_1^{AA'}$ are pure states, defined as follows for $μ \in [0, 1/2]$:

$$\text{Tr}_A\{\psi_0^{AA'}\} = μ|0\rangle \langle 0|^{A'} + (1-μ)|1\rangle \langle 1|^{A'}, \quad (D2)$$

$$\text{Tr}_A\{\psi_1^{AA'}\} = (1-μ)|0\rangle \langle 0|^{A'} + μ|1\rangle \langle 1|^{A'}. \quad (D3)$$

**Proof.** We assume without loss of generality that the dephasing basis is the computational basis. Consider a