## Appendix C: On the parametrization of the trade-off curve

Lemma 11 λ parametrizes all points on the CQ and CE trade-off curves with the possible exception of those lying on segments of constant slope.

Proof. We prove the lemma for the case of the CQ tradeoff curve. The proof for the CE trade-off curve is similar. Let ( C ( t ) , Q ( t )) for 0 ≤ t ≤ 1 be a parametrization of the trade-off curve with C (0) equal to the classical capacity and Q (1) equal to the quantum capacity. The function C ( t ) is monotonically decreasing and the function Q ( t ) is monotonically increasing. The graph of the trade-off curve is convex and, therefore, has one-sided directional derivatives at all points [70]. It is also monotonically decreasing.

Consider the function f λ ( N ) where

<!-- formula-not-decoded -->

For any 0 ≤ t ≤ 1, we have f λ ( N ) = C ( t ) + λQ ( t ) if and only if

<!-- formula-not-decoded -->

glyph[negationslash]

for all 0 ≤ s ≤ 1. Perhaps more instructively, if s &lt; t and Q ( s ) = Q ( t ), this inequality can be written as

<!-- formula-not-decoded -->

because of the monotonicity of the functions C and Q . Likewise, when s &gt; t , it has the form

<!-- formula-not-decoded -->

If ( C ( t ) , Q ( t )) is a point on the graph at which the derivative is not constant, then setting -λ to be the slope of the graph will lead to Eq. (C1) being satisfied. If the graph is not differentiable at ( C ( t ) , Q ( t )), then the slope must drop discontinuously at that point. Setting -λ to any value in the gap will again lead to the condition being satisfied.

At points where the graph is differentiable but the slope is constant, λ might not be a good parameter. These points, however, are in the convex hull of the points that λ does parametrize.

## Appendix D: Form of the CQ Trade-off Curve for Qubit Dephasing Channels

We first prove two important lemmas and then prove a theorem that gives the exact form of the CQ trade-off curve.

Lemma 12 Let N be a generalized dephasing channel. In the optimization task for the CQ trade-off curve, it suffices to consider a classical-quantum state with diagonal conditional density operators, in the sense that the following inequality holds:

<!-- formula-not-decoded -->

where

<!-- formula-not-decoded -->

U A ′ → BE N is an isometric extension of N , ϕ A ′ x = ∆( ϕ A ′ x ) = ∆( φ A ′ x ) , and ∆ is the completely dephasing channel.

Proof. The proof of this lemma is similar to the proof of Lemma 9 in Ref. [71]. Consider another classicalquantum state σ in addition to the two presented in the statement of the theorem:

<!-- formula-not-decoded -->

Then the following chain of inequalities holds for all λ ≥ 1:

<!-- formula-not-decoded -->

The first equality follows from entropic manipulations. The inequality follows because the entropies H ( B ) ρ and H ( B | X ) ρ can only increase under a complete dephasing [61]. The second equality follows because N ◦ ∆ = ∆ ◦N and N c ◦ ∆ = N c for a generalized dephasing channel N , and the final equality follows from entropic manipulations.

Lemma 13 An ensemble of the following form parametrizes all points on the CQ trade-off curve for a qubit dephasing channel:

<!-- formula-not-decoded -->

where ψ AA ′ 0 and ψ AA ′ 1 are pure states, defined as follows for µ ∈ [0 , 1 / 2] :

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Proof. We assume without loss of generality that the dephasing basis is the computational basis. Consider a