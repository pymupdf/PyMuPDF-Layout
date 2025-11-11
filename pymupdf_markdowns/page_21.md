Now I present the constrained optimization procedure to compute the sharp lower bound under MTR. I

pay particular attention to the special case where _ak_ +1 _−_ _ak_ = _δ_ for each integer _k_ at the optimum. In this


case, the lower bound reduces to



sup
0 _≤y≤δ_



_∞_
� max ( _F_ 1 ( _y_ + ( _k_ + 1) _δ_ ) _−_ _F_ 0 ( _y_ + _kδ_ ) _,_ 0) _,_ (B.1)


_k_ = _−∞_



and computation of (B.1) poses a simple one-dimensional optimization problem.


Let



_V_ ( _δ_ ) = sup
0 _≤y≤δ_



_∞_
� max ( _F_ 1 ( _y_ + ( _k_ + 1) _δ_ ) _−_ _F_ 0 ( _y_ + _kδ_ ) _,_ 0) _,_


_k_ = _−∞_



and



_VK_ ( _δ_ ) = max
_y∈{y_ _[∗]_ + _kδ}_ _[∞]_ _k_ = _−∞_



_K_
� max ( _F_ 1 ( _y_ + ( _k_ + 1) _δ_ ) _−_ _F_ 0 ( _y_ + _kδ_ ) _,_ 0) _,_


_k_ = _−K_



where _y_ _[∗]_ _∈_ arg max
0 _≤y≤δ_



_∞_
� _k_ = _−∞_ [max (] _[F]_ [1][ (] _[y]_ [ + (] _[k]_ [ + 1)] _[ δ]_ [)] _[ −]_ _[F]_ [0][ (] _[y]_ [ +] _[ kδ]_ [)] _[,]_ [ 0) and] _[ K]_ [ is a nonnegative integer.]



**Step 1.** Compute _V_ ( _δ_ ) _._


**Step 2.** To further reduce computational costs, set _K_ to be a nonnegative integer satisfying _|V_ ( _δ_ ) _−_ _VK_ ( _δ_ ) _| <_


_ε_ for small _ε >_ 0 _._ [24]


**Step 3.** For _J_ = _K_, solve the following optimization problem:



sup
_{ak}_ _[J]_ _k_ = _−J_ _[∈S]_ _δ_ _[J,K]_ ( _y_ �)



_J_
� max _{F_ 1 ( _ak_ +1) _−_ _F_ 0 ( _ak_ ) _,_ 0 _},_ (B.2)


_k_ = _−J_



where






_,_





_Sδ_ _[J,K]_ ( _y_ ) =







_{ak}_ _[J]_ _k_ = _−J_ [;] _[ a][J][ ≤]_ _[y]_ [ +] _[ Kδ, a][−][J][ ≥]_ _[y][ −]_ _[Kδ,]_ [ 0] _[ ≤]_ _[a][k]_ [+1] _[ −]_ _[a][k][ ≤]_ _[δ,]_


_δ < ak_ +2 _−_ _ak_ for each integer _k_



�
_y_ = arg max
_y∈{y_ _[∗]_ + _kδ}_ _[∞]_ _k_ = _−∞_



_K_
� max ( _F_ 1 ( _y_ + ( _k_ + 1) _δ_ ) _−_ _F_ 0 ( _y_ + _kδ_ ) _,_ 0) _._


_k_ = _−K_



**Step 4.** Repeat Step 3 for _J_ = _K_ + 1 _, . . .,_ 2 _K._ [25]


It is not straightforward to solve the problem (B.2) numerically in Step 3; the function max _{x,_ 0 _}_ is non

differentiable. Furthermore in practice, marginal distribution functions are often estimated in a complicated


24I put _ε_ = 10 _−_ 5 for the implementation in Section 4 and Section 5.
25By Lemma B.1, I considered _J_ = _K, K_ + 1 _, . . .,_ 2 _K_ for the sequence _{ak}_ _[J]_ _k_ = _−J_ [and compared the values of local maxima]
achieved by _{ak}_ _[J]_ _k_ = _−J_ [with] _[ V][K]_ [ (] _[δ]_ [)]


74


