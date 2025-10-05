Now I present the constrained optimization procedure to compute the sharp lower bound under MTR. I pay particular attention to the special case where _a k +1 _− a _k_ = _δ_ for each integer _k_ at the optimum. In this case, the lower bound reduces to 

**==> formula intentionally omitted <==**

and computation of (B.1) poses a simple one-dimensional optimization problem. 

Let 

**==> formula intentionally omitted <==**

and 

_K_ 

**==> formula intentionally omitted <==**

where _y <sup>[∗]</sup> _∈_ arg max � _∞k_ = _−∞_ <sup>[max (]</sup> _<sup>[F]</sup>_ <sup>[1]</sup> <sup>[ (]</sup> _<sup>[y]</sup>_ <sup>[ + (]</sup> _<sup>[k]</sup>_ <sup>[ + 1)]</sup> _<sup>[ δ]</sup>_ <sup>[)]</sup> _<sup>[ −]</sup> <sup>[F]</sup> <sup>[0]</sup> <sup>[ (]</sup> _<sup>[y]</sup>_ <sup>[ +]</sup> _<sup>[ kδ]</sup>_ <sup>[)]</sup> _<sup>[ ,]</sup>_ <sup>[ 0) and]</sup> _<sup>[ K]</sup>_ <sup>[ is a nonnegative integer.]</sup> 0 _≤y≤δ_ 

**Step 1.** Compute _V_ ( _δ_ ) _._ 

**Step 2.** To further reduce computational costs, set _K_ to be a nonnegative integer satisfying _|V_ ( _δ_ ) _− V _K_ ( _δ_ ) _| < ε for small _ε >_ 0 _._ <sup>[24]</sup> 

**Step 3.** For _J_ = _K_ , solve the following optimization problem: 

**==> formula intentionally omitted <==**

where 

**==> formula intentionally omitted <==**

**Step 4.** Repeat Step 3 for _J_ = _K_ + 1 _, . . . ,_ 2 _K._ <sup>[25]</sup> 

It is not straightforward to solve the problem (B.2) numerically in Step 3; the function max _{x,_ 0 _}_ is non- differentiable. Furthermore in practice, marginal distribution functions are often estimated in a complicated 

24 I put _ε_ = 10 _−_ 5 for the implementation in Section 4 and Section 5. 25 By Lemma B.1, I considered _J_ = _K, K_ + 1 _, . . . ,_ 2 _K_ for the sequence _{a k _} <sup>[J]</sup> _k_ = _−J_ <sup>[and compared the values of local maxima]</sup> achieved by _{a k _} <sup>[J]</sup> _k_ = _−J_ <sup>[with]</sup> _<sup>[ V]</sup> <sup>[K]</sup> <sup>[ (]</sup> _<sup>[δ]</sup>_ <sup>[)]</sup> 

74 

