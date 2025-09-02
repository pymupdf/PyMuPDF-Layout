
# A. The Hamiltonian

Let us consider the non-Hermitian FFA model defined by the following relations for the energy dispersion \( E(k) \) and spectral coupling \( v(k) \)

$$
E(k) = -2 \kappa_0 \cos k, \quad v(k) = -\sqrt{\frac{2}{\pi}} \kappa_a \sin k \tag{47}
$$

where \(\kappa_0, \kappa_a\) are two real-valued positive constants and \(0 \leq k \leq \pi\). The Hermitian limit of this model, attained by assuming \(\mathrm{Im}(E_a) = 0\), is a special case of the FFA model previously investigated in Ref.[36], which is exactly solvable (see also [29]). Note that the continuous spectrum of \(H\) spans the band \((E_1, E_2)\), with \(E_2 = -E_1 = 2 \kappa_0\). The density of states for this model is given by

$$
\rho(E) = \left(\frac{\partial E}{\partial k}\right)^{-1} = \begin{cases}
\frac{1}{\sqrt{4 \kappa_0^2 - E^2}} & -2 \kappa_0 < E < 2 \kappa_0 \\
0 & |E| > 2 \kappa_0
\end{cases} \tag{48}
$$

which shows van-Hove singularities at the band edges, whereas the positive spectral function \(V(E)\), defined by \(V(E) = \rho(E) |v(E)|^2\), reads

$$
V(E) = \begin{cases}
\frac{\kappa_a^2}{\pi \kappa_0} \sqrt{1 - \left(\frac{E}{2 \kappa_0}\right)^2} & -2 \kappa_0 < E < 2 \kappa_0 \\
0 & |E| > 2 \kappa_0
\end{cases} \tag{49}
$$

which is non-singular. Substitution of Eq.(49) into Eq.(11) yields the following expression for the self-energy \(\Sigma(z)\) [46]

$$
\Sigma(z) = -i \frac{\kappa_a^2}{2 \kappa_0^2} \left( \sqrt{4 \kappa_0^2 - z^2} + i z \right) \tag{50}
$$

and thus [see Eq.(12)]

$$
\Delta(\mathcal{E}) = \mathrm{Re} \left( \Sigma(z = \mathcal{E} \pm i 0^+) \right) = 
\begin{cases}
\frac{\kappa_a^2}{2 \kappa_0^2} \left( \mathcal{E} + \sqrt{\mathcal{E}^2 - 4 \kappa_0^2} \right) & \mathcal{E} < -2 \kappa_0 \\
\frac{\kappa_a^2}{2 \kappa_0^2} \mathcal{E} & -2 \kappa_0 \leq \mathcal{E} \leq 2 \kappa_0 \\
\frac{\kappa_a^2}{2 \kappa_0^2} \left( \mathcal{E} - \sqrt{\mathcal{E}^2 - 4 \kappa_0^2} \right) & \mathcal{E} > 2 \kappa_0
\end{cases} \tag{51}
$$

The condition for the non-Hermitian Hamiltonian to possess a real-valued spectrum (i.e. to avoid complex-valued energies arising from bound states outside the continuum) is derived in Appendix B. Precisely, let \(\xi_{1,2}\) be the two roots of the second-order algebraic equation

$$
\xi^2 + \frac{E_a}{\kappa_0} \xi + 1 - \left(\frac{\kappa_a}{\kappa_0}\right)^2 = 0. \tag{52}
$$

Then the Hamiltonian \(H\) has a real-valued energy spectrum if and only if \(|\xi_{1,2}| \leq 1\). Figure 2 shows the domain in the plane \(\left(\frac{\mathrm{Im}(E_a)}{\kappa_0}, \frac{\kappa_a}{\kappa_0}\right)\) where \(H\) has a purely continuous energy spectrum for a few increasing values of the ratio \(\left|\frac{\mathrm{Re}(E_a)}{\kappa_0}\right|\). The domain lies in the sector \(\frac{\kappa_a}{\kappa_0} \leq \sqrt{2}\) and shrinks toward \(\mathrm{Im}(E_a)/\kappa_0 = \kappa_a/\kappa_0 = 0\) as \(\left|\mathrm{Re}(E_a)/\kappa_0\right| \to 2^-\). For \(\left|\mathrm{Re}(E_a)/\kappa_0\right| \leq 2\), bound states do exist for any value of \(\kappa_a/\kappa_0\) and \(\mathrm{Im}(E_a)/\kappa_0\). The wider domain is attained for \(\mathrm{Re}(E_a) = 0\). In particular, for \(\mathrm{Re}(E_a) = 0\) and \(\kappa_a/\kappa_0 = \sqrt{2}\), from Eq.(52) it follows that \(H\) has a real-valued energy spectrum provided that

$$
-2 \kappa_0 < \mathrm{Im}(E_a) < 2 \kappa_0. \tag{53}
$$

Let us now consider the occurrence of spectral singularities. According to Eqs.(19) and (20) and using Eqs.(49) and (51), a spectral singularity at energy \(\mathcal{E} = \mathcal{E}_0\), inside the interval \((-2 \kappa_0, 2 \kappa_0)\), is found provided that the following two equations are simultaneously satisfied

$$
\mathrm{Im}(E_a) = \pm \frac{\kappa_a^2}{\kappa_0} \sqrt{1 - \left(\frac{\mathcal{E}_0}{2 \kappa_0}\right)^2} \tag{54}
$$

$$
\mathrm{Re}(E_a) = \left(1 - \frac{\kappa_a^2}{2 \kappa_0^2}\right) \mathcal{E}_0. \tag{55}
$$

For arbitrarily given values of \(E_a\), \(\kappa_a\) and \(\kappa_0\), the above conditions are generally not satisfied [nowhere for \(\mathcal{E}_0\) in the range \((-2 \kappa_0, 2 \kappa_0)\)], i.e. the non-Hermitian FFA Hamiltonian is generally diagonalizable. Spectral singularities appear solely when a constraint among \(\mathrm{Re}(E_a)/\kappa_0\), \(\mathrm{Im}(E_a)/\kappa_0\) and \(\kappa_a/\kappa_0\) is satisfied. Let us first assume \(\kappa_a/\kappa_0\) strictly smaller than \(\sqrt{2}\). In this case, a single spectral singularity, at the energy \(\mathcal{E}_0 =\)

----

### Figure 2: Domains of non-existence of bound states for the Hamiltonian \(H\) in the \((\mathrm{Im}(E_a)/\kappa_0, \kappa_a/\kappa_0)\) plane (shaded regions) for increasing values of the ratio \(|\mathrm{Re}(E_a)|/\kappa_0\). For a non-Hermitian Hamiltonian, i.e. \(\mathrm{Im}(E_a) \neq 0\), in the shaded regions the energy spectrum of \(H\) is real-valued and purely continuous. Spectral singularities occur at the boundary of the shaded regions.

| Re(\\(E\_a\\))/\\(\kappa\_0\\) = 0  | Re(\\(E\_a\\))/\\(\kappa\_0\\) = 0                                                           | Re(\\(E\_a\\))/\\(\kappa\_0\\) = ±0.5 | Re(\\(E\_a\\))/\\(\kappa\_0\\) = ±0.5                                           |
| ----------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------- |
| κₐ/κ₀                               | Im(\\(E\_a\\))/κ₀                                                                            | κₐ/κ₀                                 | Im(\\(E\_a\\))/κ₀                                                               |
| 1.6                                 | shaded region from about -1.5 to 1.5 at κₐ/κ₀ \~ 0.5, narrowing to 0 at κₐ/κ₀=0 and κₐ/κ₀=√2 | 1.6                                   | shaded region narrower than left plot, roughly between -1 and 1 at κₐ/κ₀ \~ 0.5 |
| 1.4                                 |                                                                                              | 1.4                                   |                                                                                 |
| 1.2                                 |                                                                                              | 1.2                                   |                                                                                 |
| 1                                   |                                                                                              | 1                                     |                                                                                 |
| Re(\\(E\_a\\))/\\(\kappa\_0\\) = ±1 |                                                                                              | Re(\\(E\_a\\))/\\(\kappa\_0\\) = ±1.8 |                                                                                 |
| κₐ/κ₀                               | Im(\\(E\_a\\))/κ₀                                                                            | κₐ/κ₀                                 | Im(\\(E\_a\\))/κ₀                                                               |
| 1.6                                 | shaded region narrow and elongated, roughly from 0 to 1 in Im(\\(E\_a\\))/κ₀ at κₐ/κ₀ \~ 0.5 | 1.6                                   | no shaded region (empty)                                                        |
| 1.4                                 |                                                                                              | 1.4                                   |                                                                                 |
| 1.2                                 |                                                                                              | 1.2                                   |                                                                                 |
| 1                                   |                                                                                              | 1                                     |                                                                                 |


