a k is defined to be a ( k mod p ) for all k / ∈ { 0 , ..., p -1 } ( a p -1 = 0, trivially). And so p -2 ∑ k =0 ( a p -k -a 1 ) ζ k = u = ζ -t u = p -2 ∑ k =0 ( a k + t -a ( p -1)+ t ) ζ k by 1 and therefore, since this representation is unique, we get

<!-- formula-not-decoded -->

Letting k 0 be the mod p solution to k + t ≡ p -k ( p ), we get a k 0 + t = a p -k 0 and so (1.1) yields a ( p -1)+ t = a 1 . (1.1) then becomes

<!-- formula-not-decoded -->

Since replacing k by -( k + t ) in (1.2) leaves the equation invariant, we get p -1 2 pairs of equal terms with distinct indices amongst a 0 , ..., a p -1 (the 'remaining' term being a k 0 + t ). Let b 1 , ..., b p -1 2 be representatives of these distinct pairs, and let b k 0 + t = a k 0 + t (we have simply selected and reordered the a i 's).

Now by the proof of 1, there is a unique c modulo p such that ζ c u is primary, and this c is the solution to ax ≡ b ( p ) where u ≡ a + bλ ( λ 2 ) where λ = (1 -ζ ). Now u = p -2 ∑ k =0 a k ζ k .

Writing, as a polynomial, f ( x ) = p -2 ∑ k =0 a k x k , we can find a and b by finding the coefficients of 1 and x respectively of f (1 -x ) since ζ = 1 -λ . Making elementary use of the Binomial Theorem, we see that f (1 -x ) = p -2 ∑ k =0 a k (1 -x ) k = p -2 ∑ k =0 a k -p -2 ∑ k =0 ka k x + ... (we only need the first two terms). So c is the solution to

<!-- formula-not-decoded -->

Which, since a p -1 = 0, is equivalent to

<!-- formula-not-decoded -->

Now k 0 + t ≡ p -k 0 ( p ) ⇒ k 0 + t ≡ -( k 0 + t ) + t ( p ) ⇒ ( k 0 + t ) ≡ 2 -1 t ⇒ b k 0 + t = a k 0 + t = a 2 -1 t . Finally, note that for a i = a t -i = b l for 1 ≤ l ≤ p -1 2 by (1.2), ia i +( t -i ) a t -i = tb l .