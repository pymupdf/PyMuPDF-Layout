4

# KABALAN GASPARD

\( a_{k} \) is defined to be \( a_{(k \mod p)} \) for all \( k \notin\{0, \ldots, p-1\} \) \( \left(a_{p-1}=0\right. \), trivially). And so
\[
\sum_{k=0}^{p-2}\left(a_{p-k}-a_{1}\right) \zeta^{k}=\overline{u}=\zeta^{-t} u=\sum_{k=0}^{p-2}\left(a_{k+t}-a_{(p-1)+t}\right) \zeta^{k} \) by 1 and therefore, since this rep-
resentation is unique, we get

(1.1) \( a_{k+t}-a_{(p-1)+t}=a_{p-k}-a_{1} \) for all \( 0 \leq k \leq p-1 \)

Letting \( k_{0} \) be the mod \( p \) solution to \( k+t \equiv p-k(p) \), we get \( a_{k_{0}+t}=a_{p-k_{0}} \) and so (1.1) yields \( a_{(p-1)+t}=a_{1} \). (1.1) then becomes

(1.2) \( a_{k+t}=a_{p-k}=a_{-k} \) for all \( 0 \leq k \leq p-1 \)

Since replacing \( k \) by \( -(k+t) \) in (1.2) leaves the equation invariant, we get \( \frac{p-1}{2} \) pairs of equal terms with distinct indices amongst \( a_{0}, \ldots, a_{p-1} \) (the 'remaining' term being \( a_{k_{0}+t} \) ). Let \( b_{1}, \ldots, b_{\frac{p-1}{2}} \) be representatives of these distinct pairs, and let \( b_{k_{0}+t}=a_{k_{0}+t} \) (we have simply selected and reordered the \( a_{i} \) 's).

Now by the proof of 1, there is a unique \( c \) modulo \( p \) such that \( \zeta^{c} u \) is primary, and this \( c \) is the solution to \( a x \equiv b(p) \) where \( u \equiv a+b \lambda\left(\lambda^{2}\right) \) where \( \lambda=(1-\zeta) \). Now \( u=\sum_{k=0}^{p-2} a_{k} \zeta^{k} \).

Writing, as a polynomial, \( f(x)=\sum_{k=0}^{p-2} a_{k} x^{k} \), we can find \( a \) and \( b \) by finding the coefficients of 1 and \( x \) respectively of \( f(1-x) \) since \( \zeta=1-\lambda \). Making elementary use of the Binomial Theorem, we see that \( f(1-x)=\sum_{k=0}^{p-2} a_{k}\left(1-x\right)^{k}=\sum_{k=0}^{p-2} a_{k}-\sum_{k=0}^{p-2} k a_{k} x+\ldots \) (we only need the first two terms). So \( c \) is the solution to

(1.3)
\[
\left(\sum_{k=0}^{p-2} a_{k}\right) x \equiv-\sum_{k=0}^{p-2} k a_{k}(p)
\]

Which, since \( a_{p-1}=0 \), is equivalent to

(1.4)
\[
\left(\sum_{k=0}^{p-1} a_{k}\right) x \equiv-\sum_{k=0}^{p-1} k a_{k}(p)
\]

Now \( k_{0}+t \equiv p-k_{0}(p) \Rightarrow k_{0}+t \equiv-(k_{0}+t)+t(p) \Rightarrow\left(k_{0}+t\right) \equiv 2^{-1} t \Rightarrow b_{k_{0}+t}=a_{k_{0}+t}= \)
\( a_{2^{-1} t} \). Finally, note that for \( a_{i}=a_{t-i}=b_{l} \) for \( 1 \leq l \leq \frac{p-1}{2} \) by (1.2), \( i a_{i}+(t-i) a_{t-i}=t b_{l} \).

=