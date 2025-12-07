21

## Appendix C: On the parametrization of the trade-off
curve

Lemma 11 λ parametrizes all points on the CQ and CE trade-off curves with the possible exception of those lying on segments of constant slope.

Proof. We prove the lemma for the case of the CQ tradeoff curve. The proof for the CE trade-off curve is similar. Let (C (t), Q(t)) for 0 ≤ t ≤ 1 be a parametrization of the trade-off curve with C (0) equal to the classical capacity and Q(1) equal to the quantum capacity. The function C (t) is monotonically decreasing and the function Q (t) is monotonically increasing. The graph of the trade-off curve is convex and, therefore, has one-sided directional derivatives at all points [70]. It is also monotonically decreasing.

Consider the function fλ (N ) where

fx (N) = maxxBE I (X; B) + XI (A)BX).

For any 0 <t≤ 1, we have fx (N) = C(t) + XQ(t) if and only if

C(t)+Q (t) > C (s) + XQ (s). (C1)

for all 0 ≤ s ≤ 1. Perhaps more instructively, if s < t and Q(s) 6= Q(t), this inequality can be written as

C(s) - C (t)
≥ -λ
Q(s) - Q (t)

because of the monotonicity of the functions C and Q. Likewise, when s > t, it has the form

C (s) - C' (t) <-λ.
Q (s) - Q (t)

If (C (t), Q(t)) is a point on the graph at which the derivative is not constant, then setting −λ to be the slope of the graph will lead to Eq. (C1) being satisfied. If the graph is not differentiable at (C (t), Q(t)), then the slope must drop discontinuously at that point. Setting −λ to any value in the gap will again lead to the condition being satisfied.

At points where the graph is differentiable but the slope is constant, λ might not be a good parameter. These points, however, are in the convex hull of the points that λ does parametrize.

## Appendix D: Form of the CQ Trade-off Curve for Qubit Dephasing Channels

We first prove two important lemmas and then prove a theorem that gives the exact form of the CQ trade-off curve.

Lemma 12 Let N be a generalized dephasing channel. In the optimization task for the CQ trade-off curve, it

suffices to consider a classical-quantum state with diagonal conditional density operators, in the sense that the following inequality holds:

I (X; B),+ XI (A)BX), ≤ I (X; B), + \I (A)BX)µ‚ where

XABE = Σ px (x) |x) (x|* ® UA'→BE (6AA'), XABE = px (x) |x) (x|* ©UA'→BE (QAA'), ==

UA→BE is an isometric extension of N, A
A(x) = A(4), and A is the completely dephasing
channel.

Proof. The proof of this lemma is similar to the proof of Lemma 9 in Ref. [71]. Consider another classicalquantum state σ in addition to the two presented in the statement of the theorem:

XAYE = Σpx (x)|x) (x|*®(▲³→Y •¯ˆª¯ →BE ³) (OAA').

Then the following chain of inequalities holds for all λ ≥ 1:

I (X; B), + XI (A)BX), = H (B), + (A − 1) H (B|X), — \H (E|X), ≤ H (Y)+(\− 1) H (Y|X), — XH (E|X), = H (B), + ( − 1) H (B|X)。 — XH (E|X), = I (X; B)₁ + XI (A)BX), ·

The first equality follows from entropic manipulations. The inequality follows because the entropies H (B), and H (B|X), can only increase under a complete dephasing [61]. The second equality follows because No A = AN and NA Nc for a generalized dephasing channel N, and the final equality follows from entropic manipu- lations.

Lemma 13 An ensemble of the following form parametrizes all points on the CQ trade-off curve for a qubit dephasing channel:

1
± 0) (0³ ® øªª′ + ¦± 1) (1³ ® &ªª′, (D1)
2

where AA and AA' are pure states, defined as follows for μ ε [0,1/2]:

Tra 4 {^^'} = µ |0) (0|^′ + (1 − µ) |1) (1|ª′, (D2) Tra à {ú^^'} = (1 − µ) |0) (0|ª′ + µ |1) (1¦ª′ . (D3)

Proof. We assume without loss of generality that the dephasing basis is the computational basis. Consider a