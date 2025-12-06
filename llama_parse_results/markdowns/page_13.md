

4                                      KABALAN GASPARD

a<sub>k</sub> is defined to be a<sub>(k mod p)</sub> for all k ∉ {0, ..., p − 1} (a<sub>p−1</sub> = 0, trivially). And so

$$\sum_{k=0}^{p-2}(a_{p-k} - a_1)\zeta^k = \overline{u} = \zeta^{-t}u = \sum_{k=0}^{p-2}(a_{k+t} - a_{(p-1)+t})\zeta^k$$

by 1 and therefore, since this representation is unique, we get

(1.1)                  a<sub>k+t</sub> − a<sub>(p−1)+t</sub> = a<sub>p−k</sub> − a<sub>1</sub> for all 0 ≤ k ≤ p − 1

Letting k<sub>0</sub> be the mod p solution to k + t ≡ p − k (p), we get a<sub>k₀+t</sub> = a<sub>p−k₀</sub> and so (1.1) yields a<sub>(p−1)+t</sub> = a<sub>1</sub>. (1.1) then becomes

(1.2)                        a<sub>k+t</sub> = a<sub>p−k</sub> = a<sub>−k</sub> for all 0 ≤ k ≤ p − 1

Since replacing k by −(k + t) in (1.2) leaves the equation invariant, we get $$\frac{p-1}{2}$$ pairs of equal terms with distinct indices amongst a<sub>0</sub>, ..., a<sub>p−1</sub> (the 'remaining' term being a<sub>k₀+t</sub>). Let b<sub>1</sub>, ..., b<sub>(p−1)/2</sub> be representatives of these distinct pairs, and let b<sub>k₀+t</sub> = a<sub>k₀+t</sub> (we have simply selected and reordered the a<sub>i</sub>'s).

Now by the proof of 1, there is a unique c modulo p such that ζ<sup>c</sup>u is primary, and this c is the solution to ax ≡ b (p) where u ≡ a + bλ (λ<sup>2</sup>) where λ = (1 − ζ). Now $$u = \sum_{k=0}^{p-2} a_k \zeta^k$$.

Writing, as a polynomial, $$f(x) = \sum_{k=0}^{p-2} a_k x^k$$, we can find a and b by finding the coefficients of 1 and x respectively of f(1 − x) since ζ = 1 − λ. Making elementary use of the Binomial Theorem, we see that $$f(1 - x) = \sum_{k=0}^{p-2} a_k (1 - x)^k = \sum_{k=0}^{p-2} a_k - \sum_{k=0}^{p-2} ka_k x + ...$$ (we only need the first two terms). So c is the solution to

(1.3)                                  $$\left(\sum_{k=0}^{p-2} a_k\right) x \equiv -\sum_{k=0}^{p-2} ka_k \pmod{p}$$

Which, since a<sub>p−1</sub> = 0, is equivalent to

(1.4)                                  $$\left(\sum_{k=0}^{p-1} a_k\right) x \equiv -\sum_{k=0}^{p-1} ka_k \pmod{p}$$

Now k<sub>0</sub> + t ≡ p − k<sub>0</sub> (p) ⇒ k<sub>0</sub> + t ≡ −(k<sub>0</sub> + t) + t (p) ⇒ (k<sub>0</sub> + t) ≡ 2<sup>−1</sup>t ⇒ b<sub>k₀+t</sub> = a<sub>k₀+t</sub> = a<sub>2⁻¹t</sub>. Finally, note that for a<sub>i</sub> = a<sub>t−i</sub> = b<sub>l</sub> for 1 ≤ l ≤ $$\frac{p-1}{2}$$ by (1.2), ia<sub>i</sub> + (t − i)a<sub>t−i</sub> = tb<sub>l</sub>.