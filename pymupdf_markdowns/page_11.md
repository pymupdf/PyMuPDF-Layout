**Appendix C: On the parametrization of the trade-off**

**curve**


**Lemma 11** _λ parametrizes all points on the CQ and CE_
_trade-off curves with the possible exception of those lying_
_on segments of constant slope._


**Proof.** We prove the lemma for the case of the CQ tradeoff curve. The proof for the CE trade-off curve is similar.
Let ( _C_ ( _t_ ) _, Q_ ( _t_ )) for 0 _≤_ _t ≤_ 1 be a parametrization of the
trade-off curve with _C_ (0) equal to the classical capacity
and _Q_ (1) equal to the quantum capacity. The function
_C_ ( _t_ ) is monotonically decreasing and the function _Q_ ( _t_ )
is monotonically increasing. The graph of the trade-off
curve is convex and, therefore, has one-sided directional
derivatives at all points [70]. It is also monotonically
decreasing.
Consider the function _f_ _λ_ ( _N_ ) where


_f_ _λ_ ( _N_ ) _≡_ max _ρ_ _XBE_ _I_ ( _X_ ; _B_ ) + _λI_ ( _A⟩BX_ ) _._


For any 0 _≤_ _t ≤_ 1, we have _f_ _λ_ ( _N_ ) = _C_ ( _t_ ) + _λQ_ ( _t_ ) if and
only if


_C_ ( _t_ ) + _λQ_ ( _t_ ) _≥_ _C_ ( _s_ ) + _λQ_ ( _s_ ) _._ (C1)


for all 0 _≤_ _s ≤_ 1. Perhaps more instructively, if _s < t_
and _Q_ ( _s_ ) _̸_ = _Q_ ( _t_ ), this inequality can be written as


_C_ ( _s_ ) _−_ _C_ ( _t_ )
_Q_ ( _s_ ) _−_ _Q_ ( _t_ ) _[≥−][λ]_


because of the monotonicity of the functions _C_ and _Q_ .
Likewise, when _s > t_, it has the form


_C_ ( _s_ ) _−_ _C_ ( _t_ )
_Q_ ( _s_ ) _−_ _Q_ ( _t_ ) _[≤−][λ.]_


If ( _C_ ( _t_ ) _, Q_ ( _t_ )) is a point on the graph at which the derivative is not constant, then setting _−λ_ to be the slope of the
graph will lead to Eq. (C1) being satisfied. If the graph
is not differentiable at ( _C_ ( _t_ ) _, Q_ ( _t_ )), then the slope must
drop discontinuously at that point. Setting _−λ_ to any
value in the gap will again lead to the condition being
satisfied.


At points where the graph is differentiable but the
slope is constant, _λ_ might not be a good parameter.
These points, however, are in the convex hull of the points
that _λ_ does parametrize.


**Appendix D: Form of the CQ Trade-off Curve for**
**Qubit Dephasing Channels**


We first prove two important lemmas and then prove
a theorem that gives the exact form of the CQ trade-off

curve.


**Lemma 12** _Let N be a generalized dephasing channel._
_In the optimization task for the CQ trade-off curve, it_



21


_suffices to consider a classical-quantum state with diag-_
_onal conditional density operators, in the sense that the_
_following inequality holds:_


_I_ ( _X_ ; _B_ ) _ρ_ + _λI_ ( _A⟩BX_ ) _ρ_ _≤_ _I_ ( _X_ ; _B_ ) _θ_ + _λI_ ( _A⟩BX_ ) _θ_ _,_


_where_


_ρ_ _[XABE]_ _≡_ � _p_ _X_ ( _x_ ) _|x⟩⟨x|_ _[X]_ _⊗_ _U_ _N_ _[A]_ _[′]_ _[→][BE]_ ( _φ_ _[AA]_ _x_ _[′]_ ) _,_


_x_

_θ_ _[XABE]_ _≡_ � _p_ _X_ ( _x_ ) _|x⟩⟨x|_ _[X]_ _⊗_ _U_ _N_ _[A]_ _[′]_ _[→][BE]_ ( _ϕ_ _[AA]_ _x_ _[′]_ ) _,_


_x_


_U_ _N_ _[A]_ _[′]_ _[→][BE]_ _is an isometric extension of N_ _,_ _ϕ_ _[A]_ _x_ _[′]_ =
∆( _ϕ_ _[A]_ _x_ _[′]_ [) = ∆(] _[φ]_ _[A]_ _x_ _[′]_ [)] _[, and]_ [ ∆] _[is the completely dephasing]_
_channel._


**Proof.** The proof of this lemma is similar to the proof
of Lemma 9 in Ref. [71]. Consider another classicalquantum state _σ_ in addition to the two presented in the
statement of the theorem:


_σ_ _[XAY E]_ _≡_ � _p_ _X_ ( _x_ ) _|x⟩⟨x|_ _[X]_ _⊗_ (∆ _[B][→][Y]_ _◦U_ _N_ _[A]_ _[′]_ _[→][BE]_ )( _φ_ _[AA]_ _x_ _[′]_ ) _._


_x_


Then the following chain of inequalities holds for all _λ ≥_
1:


_I_ ( _X_ ; _B_ ) _ρ_ + _λI_ ( _A⟩BX_ ) _ρ_
= _H_ ( _B_ ) _ρ_ + ( _λ −_ 1) _H_ ( _B|X_ ) _ρ_ _−_ _λH_ ( _E|X_ ) _ρ_
_≤_ _H_ ( _Y_ ) _σ_ + ( _λ −_ 1) _H_ ( _Y |X_ ) _σ_ _−_ _λH_ ( _E|X_ ) _σ_
= _H_ ( _B_ ) _θ_ + ( _λ −_ 1) _H_ ( _B|X_ ) _θ_ _−_ _λH_ ( _E|X_ ) _θ_
= _I_ ( _X_ ; _B_ ) _θ_ + _λI_ ( _A⟩BX_ ) _θ_ _._


The first equality follows from entropic manipulations.
The inequality follows because the entropies _H_ ( _B_ ) _ρ_ and
_H_ ( _B|X_ ) _ρ_ can only increase under a complete dephasing

[61]. The second equality follows because _N ◦_ ∆= ∆ _◦N_
and _N_ _[c]_ _◦_ ∆= _N_ _[c]_ for a generalized dephasing channel
_N_, and the final equality follows from entropic manipulations.


**Lemma 13** _An_ _ensemble_ _of_ _the_ _following_ _form_
_parametrizes_ _all_ _points_ _on_ _the_ _CQ_ _trade-off_ _curve_
_for a qubit dephasing channel:_


1
2 _[|]_ [0] _[⟩⟨]_ [0] _[|]_ _[X]_ _[ ⊗]_ _[ψ]_ 0 _[AA]_ _[′]_ + [1] 2 _[|]_ [1] _[⟩⟨]_ [1] _[|]_ _[X]_ _[ ⊗]_ _[ψ]_ 1 _[AA]_ _[′]_ _,_ (D1)


_where ψ_ 0 _[AA]_ _[′]_ _and ψ_ 1 _[AA]_ _[′]_ _are pure states, defined as follows_
_for µ ∈_ [0 _,_ 1 _/_ 2] _:_


Tr _A_ _ψ_ 0 _[AA]_ _[′]_ = _µ |_ 0 _⟩⟨_ 0 _|_ _[A]_ _[′]_ + (1 _−_ _µ_ ) _|_ 1 _⟩⟨_ 1 _|_ _[A]_ _[′]_ _,_ (D2)
� �

Tr _A_ _ψ_ 1 _[AA]_ _[′]_ = (1 _−_ _µ_ ) _|_ 0 _⟩⟨_ 0 _|_ _[A]_ _[′]_ + _µ |_ 1 _⟩⟨_ 1 _|_ _[A]_ _[′]_ _._ (D3)
� �


**Proof.** We assume without loss of generality that the
dephasing basis is the computational basis. Consider a


