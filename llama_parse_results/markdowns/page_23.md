

7

## A. The Hamiltonian

Let us consider the non-Hermitian FFA model defined by the following relations for the energy dispersion E(k) and spectral coupling v(k)

$$E(k) = -2\kappa_0 \cos k , \quad v(k) = -\sqrt{\frac{2}{\pi}}\kappa_a \sin k \quad (47)$$

where κ<sub>0</sub>, κ<sub>a</sub> are two real-valued positive constants and 0 ≤ k ≤ π. The Hermitian limit of this model, attained by assuming Im(E<sub>a</sub>) = 0, is a special case of the FFA model previously investigated in Ref.[36], which is exactly solvable (see also [29]). Note that the continuous spectrum of H spans the band (E<sub>1</sub>, E<sub>2</sub>), with E<sub>2</sub> = -E<sub>1</sub> = 2κ<sub>0</sub>. The density of states for this model is given by

$$\rho(E) = \left(\frac{\partial E}{\partial k}\right)^{-1} = \begin{cases} \frac{1}{\sqrt{4\kappa_0^2-E^2}} & -2\kappa_0 < E < 2\kappa_0 \\ 0 & |E| > 2\kappa_0 \end{cases} \quad (48)$$

which shows van-Hove singularities at the band edges, whereas the positive spectral function V(E), defined by V(E) = ρ(E)|v(E)|<sup>2</sup>, reads

$$V(E) = \begin{cases} \frac{\kappa_a^2}{\pi\kappa_0}\sqrt{1-\left(\frac{E}{2\kappa_0}\right)^2} & -2\kappa_0 < E < 2\kappa_0 \\ 0 & |E| > 2\kappa_0 \end{cases} \quad (49)$$

which is non-singular. Substitution of Eq.(49) into Eq.(11) yields the following expression for the self-energy Σ(z) [46]

$$\Sigma(z) = -i\frac{\kappa_a^2}{2\kappa_0^2}\left(\sqrt{4\kappa_0^2 - z^2 + iz}\right) \quad (50)$$

and thus [see Eq.(12)]

$$\Delta(E) = \text{Re}[\Sigma(z = E \pm i0^+)] = \begin{cases} \frac{\kappa_a^2}{2\kappa_0^2}\left(E + \sqrt{E^2 - 4\kappa_0^2}\right) & E < -2\kappa_0 \\ \frac{\kappa_a^2}{2\kappa_0^2}E & -2\kappa_0 \leq E \leq 2\kappa_0 \\ \frac{\kappa_a^2}{2\kappa_0^2}\left(E - \sqrt{E^2 - 4\kappa_0^2}\right) & E > 2\kappa_0 \end{cases} \quad (51)$$

| **Re(Ea)/κ0=0**<br/>Plot showing κa/κ0 (y-axis, 0 to 1.6) vs Im(Ea)/κ0 (x-axis, -2 to 2)<br/>Shaded triangular region from (-1,0) to (0,1.6) to (1,0) | **Re(Ea)/κ0=±0.5**<br/>Plot showing κa/κ0 (y-axis, 0 to 1.6) vs Im(Ea)/κ0 (x-axis, -2 to 2)<br/>Shaded region with narrower triangular shape    |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Re(Ea)/κ0=±1**<br/>Plot showing κa/κ0 (y-axis, 0 to 1.6) vs Im(Ea)/κ0 (x-axis, -2 to 2)<br/>Shaded region with further narrowed triangular shape    | **Re(Ea)/κ0=±1.8**<br/>Plot showing κa/κ0 (y-axis, 0 to 1.6) vs Im(Ea)/κ0 (x-axis, -2 to 2)<br/>Shaded region with very narrow triangular shape |


**FIG. 2:** Domains of non-existence of bound states for the Hamiltonian H in the (Im(E<sub>a</sub>)/κ<sub>0</sub>, κ<sub>a</sub>/κ<sub>0</sub>) plane (shaded regions) for increasing values of the ratio |Re(E<sub>a</sub>)|/κ<sub>0</sub>. For a non-Hermitian Hamiltonian, i.e. Im(E<sub>a</sub>) ≠ 0, in the shaded regions the energy spectrum of H is real-valued and purely continuous. Spectral singularities occur at the boundary of the shaded regions.

The condition for the non-Hermitian Hamiltonian to possess a real-valued spectrum (i.e. to avoid complex-valued energies arising from bound states outside the continuum) is derived in Appendix B. Precisely, let ξ<sub>1,2</sub> be the two roots of the second-order algebraic equation

$$\xi^2 + \frac{E_a}{\kappa_0}\xi + 1 - (\kappa_a/\kappa_0)^2 = 0. \quad (52)$$

Then the Hamiltonian H has a real-valued energy spectrum if and only if |ξ<sub>1,2</sub>| ≤ 1. Figure 2 shows the domain in the plane (Im(E<sub>a</sub>)/κ<sub>0</sub>, κ<sub>a</sub>/κ<sub>0</sub>) where H has a purely continuous energy spectrum for a few increasing values of the ratio |Re(E<sub>a</sub>)|/κ<sub>0</sub>. The domain lies in the sector

κ<sub>a</sub>/κ<sub>0</sub> ≤ √2 and shrinks toward Im(E<sub>a</sub>)/κ<sub>0</sub> = κ<sub>a</sub>/κ<sub>0</sub> = 0 as |Re(E<sub>a</sub>)/κ<sub>0</sub>| → 2<sup>-</sup>. For |Re(E<sub>a</sub>)/κ<sub>0</sub>| ≤ 2, bound states do exist for any value of κ<sub>a</sub>/κ<sub>0</sub> and Im(E<sub>a</sub>)/κ<sub>0</sub>. The wider domain is attained for Re(E<sub>a</sub>) = 0. In particular, for Re(E<sub>a</sub>) = 0 and κ<sub>a</sub>/κ<sub>0</sub> = √2, from Eq.(52) it follows that H has a real-valued energy spectrum provided that

$$-2\kappa_0 < \text{Im}(E_a) < 2\kappa_0. \quad (53)$$

Let us now consider the occurrence of spectral singularities. According to Eqs.(19) and (20) and using Eqs.(49) and (51), a spectral singularity at energy E = E<sub>0</sub>, inside the interval (-2κ<sub>0</sub>, 2κ<sub>0</sub>), is found provided that the following two equations are simultaneously satisfied

$$\text{Im}(E_a) = \pm\frac{\kappa_a^2}{\kappa_0}\sqrt{1-\left(\frac{E_0}{2\kappa_0}\right)^2} \quad (54)$$

$$\text{Re}(E_a) = \left(1-\frac{\kappa_a^2}{2\kappa_0^2}\right)E_0. \quad (55)$$

For arbitrarily given values of E<sub>a</sub>, κ<sub>a</sub> and κ<sub>0</sub>, the above conditions are generally not satisfied [nowhere for E<sub>0</sub> in the range (-2κ<sub>0</sub>, 2κ<sub>0</sub>)], i.e. the non-Hermitian FFA Hamiltonian is generally diagonalizable. Spectral singularities appear solely when a constraint among Re(E<sub>a</sub>)/κ<sub>0</sub>, Im(E<sub>a</sub>)/κ<sub>0</sub> and κ<sub>a</sub>/κ<sub>0</sub> is satisfied. Let us first assume κ<sub>a</sub>/κ<sub>0</sub> strictly smaller that √2. In this case, a single spectral singularity, at the energy E<sub>0</sub> =