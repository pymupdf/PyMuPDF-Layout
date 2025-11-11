**Appendix C: On the parametrization of the trade-off**

**curve**


**Lemma 11** _λ parametrizes all points on the CQ and CE_
_trade-off curves with the possible exception of those lying_
_on segments of constant slope._


Consider the function _fλ_ ( _N_ ) where


_fλ_ ( _N_ ) _≡_ max _ρXBE I_ ( _X_ ; _B_ ) + _λI_ ( _A⟩BX_ ) _._


For any 0 _≤_ _t ≤_ 1, we have _fλ_ ( _N_ ) = _C_ ( _t_ ) + _λQ_ ( _t_ ) if and
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



21


_I_ ( _X_ ; _B_ ) _ρ_ + _λI_ ( _A⟩BX_ ) _ρ ≤_ _I_ ( _X_ ; _B_ ) _θ_ + _λI_ ( _A⟩BX_ ) _θ,_


_where_


_ρ_ _[XABE]_ _≡_ � _pX_ ( _x_ ) _|x⟩⟨x|_ _[X]_ _⊗_ _UN_ _[A][′][→][BE]_ ( _φ_ _[AA]_ _x_ _[′]_ ) _,_


_x_

_θ_ _[XABE]_ _≡_ � _pX_ ( _x_ ) _|x⟩⟨x|_ _[X]_ _⊗_ _UN_ _[A][′][→][BE]_ ( _ϕ_ _[AA]_ _x_ _[′]_ ) _,_


_x_


_UN_ _[A][′][→][BE]_ _is an isometric extension of N_ _,_ _ϕ_ _[A]_ _x_ _[′]_ =
∆( _ϕ_ _[A]_ _x_ _[′]_ [) = ∆(] _[φ][A]_ _x_ _[′]_ [)] _[, and]_ [ ∆] _[is the completely dephasing]_
_channel._


**Proof.** The proof of this lemma is similar to the proof
of Lemma 9 in Ref. [71]. Consider another classicalquantum state _σ_ in addition to the two presented in the
statement of the theorem:


_σ_ _[XAY E]_ _≡_ � _pX_ ( _x_ ) _|x⟩⟨x|_ _[X]_ _⊗_ (∆ _[B][→][Y]_ _◦UN_ _[A][′][→][BE]_ )( _φ_ _[AA]_ _x_ _[′]_ ) _._


_x_


Then the following chain of inequalities holds for all _λ ≥_
1:


_I_ ( _X_ ; _B_ ) _ρ_ + _λI_ ( _A⟩BX_ ) _ρ_
= _H_ ( _B_ ) _ρ_ + ( _λ −_ 1) _H_ ( _B|X_ ) _ρ −_ _λH_ ( _E|X_ ) _ρ_
_≤_ _H_ ( _Y_ ) _σ_ + ( _λ −_ 1) _H_ ( _Y |X_ ) _σ −_ _λH_ ( _E|X_ ) _σ_
= _H_ ( _B_ ) _θ_ + ( _λ −_ 1) _H_ ( _B|X_ ) _θ −_ _λH_ ( _E|X_ ) _θ_
= _I_ ( _X_ ; _B_ ) _θ_ + _λI_ ( _A⟩BX_ ) _θ ._


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
2 _[|]_ [0] _[⟩⟨]_ [0] _[|][X][ ⊗]_ _[ψ]_ 0 _[AA][′]_ + [1] 2 _[|]_ [1] _[⟩⟨]_ [1] _[|][X][ ⊗]_ _[ψ]_ 1 _[AA][′]_ _,_ (D1)


_where ψ_ 0 _[AA][′]_ _and ψ_ 1 _[AA][′]_ _are pure states, defined as follows_
_for µ ∈_ [0 _,_ 1 _/_ 2] _:_


Tr _A_ _ψ_ 0 _[AA][′]_ = _µ |_ 0 _⟩⟨_ 0 _|_ _[A][′]_ + (1 _−_ _µ_ ) _|_ 1 _⟩⟨_ 1 _|_ _[A][′]_ _,_ (D2)
� �

Tr _A_ _ψ_ 1 _[AA][′]_ = (1 _−_ _µ_ ) _|_ 0 _⟩⟨_ 0 _|_ _[A][′]_ + _µ |_ 1 _⟩⟨_ 1 _|_ _[A][′]_ _._ (D3)
� �


**Proof.** We assume without loss of generality that the
dephasing basis is the computational basis. Consider a


