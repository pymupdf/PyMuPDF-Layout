Now I present the constrained optimization procedure to compute the sharp lower bound under MTR. I pay particular attention to the special case where _ak_ +1 _− ak_ = _δ_ for each integer _k_ at the optimum. In this case, the lower bound reduces to 

**==> formula [351 x 32] intentionally omitted <==**

and computation of (B.1) poses a simple one-dimensional optimization problem. 

Let 

**==> formula [268 x 32] intentionally omitted <==**

and 

**==> formula [310 x 32] intentionally omitted <==**

where _y[∗] ∈_ arg max � _∞k_ = _−∞_[max (] _[F]_[1][ (] _[y]_[ + (] _[k]_[ + 1)] _[ δ]_[)] _[ −][F]_[0][ (] _[y]_[ +] _[ kδ]_[)] _[ ,]_[ 0) and] _[ K]_[ is a nonnegative integer.] 0 _≤y≤δ_ 

**Step 1.** Compute _V_ ( _δ_ ) _._ 

**Step 2.** To further reduce computational costs, set _K_ to be a nonnegative integer satisfying _|V_ ( _δ_ ) _− VK_ ( _δ_ ) _| < ε_ for small _ε >_ 0 _._[24] 

**Step 3.** For _J_ = _K_ , solve the following optimization problem: 

**==> formula [335 x 33] intentionally omitted <==**

where 

**==> formula [340 x 78] intentionally omitted <==**

**Step 4.** Repeat Step 3 for _J_ = _K_ + 1 _, . . . ,_ 2 _K._[25] 

It is not straightforward to solve the problem (B.2) numerically in Step 3; the function max _{x,_ 0 _}_ is nondifferentiable. Furthermore in practice, marginal distribution functions are often estimated in a complicated 

> 24I put _ε_ = 10 _−_ 5 for the implementation in Section 4 and Section 5. 

> 25By Lemma B.1, I considered _J_ = _K, K_ + 1 _, . . . ,_ 2 _K_ for the sequence _{ak}[J] k_ = _−J_[and compared the values of local maxima] achieved by _{ak}[J] k_ = _−J_[with] _[ V][K]_[ (] _[δ]_[)] 

74 

