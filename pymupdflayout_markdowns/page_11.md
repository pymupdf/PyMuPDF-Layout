21 

## **Appendix C: On the parametrization of the trade-off curve 

**Lemma 11** _λ parametrizes all points on the CQ and CE trade-off curves with the possible exception of those lying _on segments of constant slope._ 

**Proof.** We prove the lemma for the case of the CQ trade- off curve. The proof for the CE trade-off curve is similar. Let ( _C_ ( _t_ ) _, Q_ ( _t_ )) for 0 _≤ t ≤ 1 be a parametrization of the trade-off curve with _C_ (0) equal to the classical capacity and _Q_ (1) equal to the quantum capacity. The function _C_ ( _t_ ) is monotonically decreasing and the function _Q_ ( _t_ ) is monotonically increasing. The graph of the trade-off curve is convex and, therefore, has one-sided directional derivatives at all points [70]. It is also monotonically decreasing. 

Consider the function _f λ ( _N_ ) where 

**==> formula intentionally omitted <==**

For any 0 _≤ t ≤ 1, we have _f λ ( _N_ ) = _C_ ( _t_ ) + _λQ_ ( _t_ ) if and only if 

**==> formula intentionally omitted <==**

for all 0 _≤ s ≤ 1. Perhaps more instructively, if _s < t_ and _Q_ ( _s_ ) _̸_ = _Q_ ( _t_ ), this inequality can be written as 

**==> formula intentionally omitted <==**

because of the monotonicity of the functions _C_ and _Q_ . Likewise, when _s > t_ , it has the form 

**==> formula intentionally omitted <==**

If ( _C_ ( _t_ ) _, Q_ ( _t_ )) is a point on the graph at which the deriva- tive is not constant, then setting _−λ_ to be the slope of the graph will lead to Eq. (C1) being satisfied. If the graph is not differentiable at ( _C_ ( _t_ ) _, Q_ ( _t_ )), then the slope must drop discontinuously at that point. Setting _−λ_ to any value in the gap will again lead to the condition being satisfied. 

At points where the graph is differentiable but the slope is constant, _λ_ might not be a good parameter. These points, however, are in the convex hull of the points that _λ_ does parametrize. 

## **Appendix D: Form of the CQ Trade-off Curve for Qubit Dephasing Channels 

We first prove two important lemmas and then prove a theorem that gives the exact form of the CQ trade-off curve. 

**Lemma 12** _Let N be a generalized dephasing channel. In the optimization task for the CQ trade-off curve, it 

_suffices to consider a classical-quantum state with diag- onal conditional density operators, in the sense that the _following inequality holds:_ 

**==> formula intentionally omitted <==**

_where_ 

**==> formula intentionally omitted <==**

_U N _<sup>[A]</sup> <sup>[′]</sup> _<sup>[→][BE]</sup> is an isometric extension of N _, ϕ _<sup>[A]</sup> x _<sup>[′]</sup>_ = ∆( _ϕ <sup>[A]</sup> _x <sup>[′]</sup> <sup>[) = ∆(]</sup> _<sup>[φ]</sup> <sup>[A]</sup> _x <sup>[′]</sup> <sup>[)]</sup> _<sup>[, and]</sup>_ <sup>[ ∆]</sup> _<sup>[is the completely dephasing]</sup> channel. 

**Proof.** The proof of this lemma is similar to the proof of Lemma 9 in Ref. [71]. Consider another classical- quantum state _σ_ in addition to the two presented in the statement of the theorem: 

**==> formula intentionally omitted <==**

Then the following chain of inequalities holds for all _λ ≥_ 1: 

**==> formula intentionally omitted <==**

The first equality follows from entropic manipulations. The inequality follows because the entropies _H_ ( _B_ ) _ρ_ and _H_ ( _B|X_ ) _ρ_ can only increase under a complete dephasing [61]. The second equality follows because _N ◦_ ∆= ∆ _◦N_ and _N <sup>[c]</sup> _◦_ ∆= _N <sup>[c]</sup> for a generalized dephasing channel _N_ , and the final equality follows from entropic manipu- lations. 

**Lemma 13** _An ensemble _of the _following form _parametrizes all _points on _the CQ _trade-off curve _for a qubit dephasing channel:_ 

**==> formula intentionally omitted <==**

_where ψ_ 0 _<sup>[AA]</sup> <sup>[′]</sup> _and ψ_ 1 _<sup>[AA]</sup> <sup>[′]</sup> _are pure states, defined as follows for µ ∈ [0 _,_ 1 _/_ 2] _:_ 

**==> formula intentionally omitted <==**

**==> formula intentionally omitted <==**

**Proof.** We assume without loss of generality that the dephasing basis is the computational basis. Consider a 

