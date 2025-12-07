4 KABALAN GASPARD

$a_k$ is defined to be $a_{(k \bmod p)}$ for all $k \notin \{0, ..., p-1\}$ ($a_{p-1} = 0$, trivially). And so

$$
\sum_{k=0}^{p-2} (a_{p-k} - a_1)\zeta^k = \overline{u} = \zeta^{-t}u = \sum_{k=0}^{p-2} (a_{k+t} - a_{(p-1)+t})\zeta^k
$$

by 1 and therefore, since this representation is unique, we get

$$
a_{k+t} - a_{(p-1)+t} = a_{p-k} - a_1 \quad \text{for all } 0 \le k \le p-1 \tag{1.1}
$$

Letting $k_0$ be the $\bmod p$ solution to $k+t \equiv p-k \pmod p$, we get $a_{k_0+t} = a_{p-k_0}$ and so (1.1) yields $a_{(p-1)+t} = a_1$. (1.1) then becomes

$$
a_{k+t} = a_{p-k} = a_{-k} \quad \text{for all } 0 \le k \le p-1 \tag{1.2}
$$

Since replacing $k$ by $-(k+t)$ in (1.2) leaves the equation invariant, we get $\frac{p-1}{2}$ pairs of equal terms with distinct indices amongst $a_0, ..., a_{p-1}$ (the 'remaining' term being $a_{k_0+t}$). Let $b_1, ..., b_{\frac{p-1}{2}}$ be representatives of these distinct pairs, and let $b_{k_0+t} = a_{k_0+t}$ (we have simply selected and reordered the $a_i$'s).

Now by the proof of 1, there is a unique $c$ modulo $p$ such that $\zeta^c u$ is primary, and this $c$ is the solution to $ax \equiv b \pmod p$ where $u \equiv a + b\lambda \pmod{\lambda^2}$ where $\lambda = (1 - \zeta)$. Now $u = \sum_{k=0}^{p-2} a_k\zeta^k$. Writing, as a polynomial, $f(x) = \sum_{k=0}^{p-2} a_kx^k$, we can find $a$ and $b$ by finding the coefficients of $1$ and $x$ respectively of $f(1 - x)$ since $\zeta = 1 - \lambda$. Making elementary use of the Binomial Theorem, we see that $f(1 - x) = \sum_{k=0}^{p-2} a_k(1 - x)^k = \sum_{k=0}^{p-2} a_k - \sum_{k=0}^{p-2} ka_kx + ...$ (we only need the first two terms). So $c$ is the solution to

$$
\left(\sum_{k=0}^{p-2} a_k\right) x \equiv -\sum_{k=0}^{p-2} ka_k \pmod p \tag{1.3}
$$

Which, since $a_{p-1} = 0$, is equivalent to

$$
\left(\sum_{k=0}^{p-1} a_k\right) x \equiv -\sum_{k=0}^{p-1} ka_k \pmod p \tag{1.4}
$$

Now $k_0 + t \equiv p - k_0 \pmod p \Rightarrow k_0 + t \equiv -(k_0 + t) + t \pmod p \Rightarrow (k_0 + t) \equiv 2^{-1}t \Rightarrow b_{k_0+t} = a_{k_0+t} = a_{2^{-1}t}$. Finally, note that for $a_i = a_{t-i} = b_l$ for $1 \le l \le \frac{p-1}{2}$ by (1.2), $ia_i + (t - i)a_{t-i} = tb_l$.