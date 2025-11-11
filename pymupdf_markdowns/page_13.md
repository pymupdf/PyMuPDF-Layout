4 KABALAN GASPARD



ak is defined to be a(k mod p) for all k /∈{0, ..., p − 1} (ap−1 = 0, trivially). And so
p−2 p−2
� (ap−k − a1)ζ [k] = u = ζ [−][t] u = � (ak+t − a(p−1)+t)ζ [k] by 1 and therefore, since this rep


p−2 p−2
� (ap−k − a1)ζ [k] = u = ζ [−][t] u = �

k=0 k=0



� (ak+t − a(p−1)+t)ζ [k] by 1 and therefore, since this rep
k=0



resentation is unique, we get


(1.1) ak+t − a(p−1)+t = ap−k − a1 for all 0 ≤ k ≤ p − 1


Letting k0 be the mod p solution to k + t ≡ p − k (p), we get ak0+t = ap−k0 and so (1.1)


yields a(p−1)+t = a1. (1.1) then becomes


(1.2) ak+t = ap−k = a−k for all 0 ≤ k ≤ p − 1


Since replacing k by −(k + t) in (1.2) leaves the equation invariant, we get [p][−] 2 [1] pairs of


equal terms with distinct indices amongst a0, ..., ap−1 (the ’remaining’ term being ak0+t). Let


b1, ..., b p−1 be representatives of these distinct pairs, and let bk0+t = ak0+t (we have simply

2


selected and reordered the ai’s).


Now by the proof of 1, there is a unique c modulo p such that ζ [c] u is primary, and this c

p−2
is the solution to ax ≡ b (p) where u ≡ a + bλ (λ [2] ) where λ = (1 − ζ). Now u = � akζ [k] .

k=0

p−2
Writing, as a polynomial, f (x) = � akx [k], we can find a and b by finding the coefficients of

k=0

1 and x respectively of f (1 − x) since ζ = 1 − λ. Making elementary use of the Binomial



p−2 p−2
� ak(1 − x) [k] = �

k=0 k=0



p−2
Theorem, we see that f (1 − x) = �



p−2 p−2
� ak − �

k=0 k=0



� kakx + ... (we only need the

k=0



first two terms). So c is the solution to



�



(1.3)



p−2


ak

�
� k=0



p−2
� kak (p)


k=0



p−1
� kak (p)


k=0



Which, since ap−1 = 0, is equivalent to



�



x ≡−


x ≡−



(1.4)



p−1


ak

�
� k=0



Now k0 + t ≡ p − k0 (p) ⇒ k0 + t ≡−(k0 + t) + t (p) ⇒ (k0 + t) ≡ 2 [−][1] t ⇒ bk0+t = ak0+t =


a2−1t. Finally, note that for ai = at−i = bl for 1 ≤ l ≤ [p][−] 2 [1] by (1.2), iai + (t − i)at−i = tbl.


