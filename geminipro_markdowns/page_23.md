## A. The Hamiltonian

Let us consider the non-Hermitian FFA model defined by the following relations for the energy dispersion $E(k)$ and spectral coupling $v(k)$

$$
E(k) = -2\kappa_0 \cos k, \quad v(k) = -\sqrt{\frac{2}{\pi}} \kappa_a \sin k
$$
(47)

where $\kappa_0, \kappa_a$ are two real-valued positive constants and $0 \le k \le \pi$. The Hermitian limit of this model, attained by assuming $\text{Im}(E_a) = 0$, is a special case of the FFA model previously investigated in Ref. [36], which is exactly solvable (see also [29]). Note that the continuous spectrum of $H$ spans the band $(E_1, E_2)$, with $E_2 = -E_1 = 2\kappa_0$. The density of states for this model is given by

$$
\rho(E) = \left( \frac{\partial E}{\partial k} \right)^{-1} = 
\begin{cases}
    \frac{1}{\sqrt{4\kappa_0^2 - E^2}} & -2\kappa_0 < E < 2\kappa_0 \\
    0 & |E| > 2\kappa_0
\end{cases}
$$
(48)

which shows van-Hove singularities at the band edges, whereas the positive spectral function $V(E)$, defined by $V(E) = \rho(E)|v(E)|^2$, reads

$$
V(E) = 
\begin{cases}
    \frac{\kappa_a^2}{\pi\kappa_0} \sqrt{1 - \left(\frac{E}{2\kappa_0}\right)^2} & -2\kappa_0 < E < 2\kappa_0 \\
    0 & |E| > 2\kappa_0
\end{cases}
$$
(49)

which is non-singular. Substitution of Eq.(49) into Eq.(11) yields the following expression for the self-energy $\Sigma(z)$ [46]

$$
\Sigma(z) = -i\frac{\kappa_a^2}{2\kappa_0^2} (\sqrt{4\kappa_0^2 - z^2} + iz)
$$
(50)

and thus [see Eq.(12)]

$$
\Delta(\mathcal{E}) = \text{Re}\left(\Sigma(z = \mathcal{E} \pm i0^+)\right) =
\begin{cases}
    \frac{\kappa_a^2}{2\kappa_0^2}(\mathcal{E} + \sqrt{\mathcal{E}^2 - 4\kappa_0^2}) & \mathcal{E} < -2\kappa_0 \\
    \frac{\kappa_a^2}{2\kappa_0^2}\mathcal{E} & -2\kappa_0 \le \mathcal{E} \le 2\kappa_0 \\
    \frac{\kappa_a^2}{2\kappa_0^2}(\mathcal{E} - \sqrt{\mathcal{E}^2 - 4\kappa_0^2}) & \mathcal{E} > 2\kappa_0
\end{cases}
$$
(51)

The condition for the non-Hermitian Hamiltonian to possess a real-valued spectrum (i.e. to avoid complex-valued energies arising from bound states outside the continuum) is derived in Appendix B. Precisely, let $\xi_{1,2}$ be the two roots of the second-order algebraic equation

$$
\xi^2 + \frac{E_a}{\kappa_0} \xi + 1 - (\kappa_a/\kappa_0)^2 = 0.
$$
(52)

Then the Hamiltonian $H$ has a real-valued energy spectrum if and only if $|\xi_{1,2}| \le 1$. Figure 2 shows the domain in the plane $(\text{Im}(E_a)/\kappa_0, \kappa_a/\kappa_0)$ where $H$ has a purely continuous energy spectrum for a few increasing values of the ratio $|\text{Re}(E_a)/\kappa_0|$. The domain lies in the sector

![Figure 2: Domains of non-existence of bound states for the Hamiltonian H in the (Im(Ea)/κ₀, κₐ/κ₀) plane (shaded regions) for increasing values of the ratio |Re(Ea)|/κ₀. For a non-Hermitian Hamiltonian, i.e. Im(Ea) ≠ 0, in the shaded regions the energy spectrum of H is real-valued and purely continuous. Spectral singularities occur at the boundary of the shaded regions.](figure-2.png)

**Figure 2 (summary):** This figure contains four plots showing the domains of non-existence for bound states in a parameter plane. The vertical axis is $\kappa_a/\kappa_0$ and the horizontal axis is $\text{Im}(E_a)/\kappa_0$. Each plot corresponds to a different value of $|\text{Re}(E_a)/\kappa_0|$: 0, ±0.5, ±1, and ±1.8. The shaded region, representing a purely continuous and real-valued energy spectrum, is largest when $\text{Re}(E_a)/\kappa_0 = 0$ and shrinks progressively as $|\text{Re}(E_a)/\kappa_0|$ increases towards 2.

$\kappa_a/\kappa_0 \le \sqrt{2}$ and shrinks toward $\text{Im}(E_a)/\kappa_0 = \kappa_a/\kappa_0 = 0$ as $|\text{Re}(E_a)/\kappa_0| \to 2^-$. For $|\text{Re}(E_a)/\kappa_0| \le 2$, bound states do exist for any value of $\kappa_a/\kappa_0$ and $\text{Im}(E_a)/\kappa_0$. The wider domain is attained for $\text{Re}(E_a) = 0$. In particular, for $\text{Re}(E_a) = 0$ and $\kappa_a/\kappa_0 = \sqrt{2}$, from Eq.(52) it follows that $H$ has a real-valued energy spectrum provided that

$$
-2\kappa_0 < \text{Im}(E_a) < 2\kappa_0.
$$
(53)

Let us now consider the occurrence of spectral singularities. According to Eqs.(19) and (20) and using Eqs.(49) and (51), a spectral singularity at energy $E = E_0$, inside the interval $(-2\kappa_0, 2\kappa_0)$, is found provided that the following two equations are simultaneously satisfied

$$
\text{Im}(E_a) = \pm \frac{\kappa_a^2}{\kappa_0} \sqrt{1 - \left(\frac{E_0}{2\kappa_0}\right)^2}
$$
(54)

$$
\text{Re}(E_a) = \left(1 - \frac{\kappa_a^2}{2\kappa_0^2}\right) E_0.
$$
(55)

For arbitrarily given values of $E_a$, $\kappa_a$ and $\kappa_0$, the above conditions are generally not satisfied [nowhere for $E_0$ in the range $(-2\kappa_0, 2\kappa_0)]$, i.e. the non-Hermitian FFA Hamiltonian is generally diagonalizable. Spectral singularities appear solely when a constraint among $\text{Re}(E_a)/\kappa_0$, $\text{Im}(E_a)/\kappa_0$ and $\kappa_a/\kappa_0$ is satisfied. Let us first assume $\kappa_a/\kappa_0$ strictly smaller that $\sqrt{2}$. In this case, a single spectral singularity, at the energy $E_0 =$