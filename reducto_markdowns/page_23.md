# A. The Hamiltonian

7

Let us consider the non-Hermitian FFA model defined by the following relations for the energy dispersion \( E(k) \) and spectral coupling \( v(k) \)

\[
E(k)=-2 \kappa_{0} \cos k, v(k)=-\sqrt{\frac{2}{\pi}} \kappa_{a} \sin k
\]

where \( \kappa_{0}, \kappa_{a} \) are two real-valued positive constants and \( 0 \leq k \leq \pi \). The Hermitian limit of this model, attained by assuming \( \operatorname{Im}\left(E_{a}\right)=0 \), is a special case of the FFA model previously investigated in Ref.[36], which is exactly solvable (see also [29]). Note that the continuous spectrum of \( H \) spans the band \( \left(E_{1}, E_{2}\right) \), with \( E_{2}=-E_{1}=2 \kappa_{0} \). The density of states for this model is given by
\[
\rho(E)=\left(\frac{\partial E}{\partial l}\right)^{-1}=\left\{\begin{array}{l}
\sqrt{\frac{1}{4 \kappa_{0}^{2}-E^{2}}}-2 \kappa_{0}<E<2 \kappa_{0}
\end{array}\right.
\]

\[
\rho(E)=\left(\frac{\partial E}{\partial k}\right)=\left\{\begin{array}{l}
\sqrt{4 \kappa_{0}^{2}-E^{2}} \\
0
\end{array}\right.
\]
which shows van-Hove singularities at the band edges, whereas the positive spectral function \( V(E) \), defined by \( V(E)=\rho(E) \mid v(E) \mid^{2} \), reads
\[
V(E)=\left\{\begin{array}{l}
\frac{\kappa_{a}^{2}}{\pi \kappa_{0}} \sqrt{1-\left(\frac{E}{2 \kappa_{0}}\right)^{2}} \\
0
\end{array}\right.
\]

which is non-singular. Substitution of Eq.(49) into Eq.(11) yields the following expression for the self-energy \( \Sigma(z) \) [46]
\[
\Sigma(z)=-i \frac{\kappa_{a}^{2}}{2 \kappa_{0}^{2}}\left(\sqrt{4 \kappa_{0}^{2}-z^{2}}+i z\right)
\]
and thus [see Eq.(12)]
\[
\Delta(\mathcal{E})=\operatorname{Re}\left(\Sigma\left(z=\mathcal{E} \pm i 0^{+}\right)\right)=
\]
\[
=\left\{\begin{array}{l}
\frac{\kappa_{a}^{2}}{2 \kappa_{0}^{2}}\left(\mathcal{E}+\sqrt{\mathcal{E}^{2}-4 \kappa_{0}^{2}}\right) \quad \mathcal{E}<-2 \kappa_{0} \\
\frac{\kappa_{a}^{2}}{2 \kappa_{0}^{2}} \mathcal{E} \quad -2 \kappa_{0} \leq \mathcal{E} \leq 2 \kappa_{0} \\
\frac{\kappa_{a}^{2}}{2 \kappa_{0}^{2}}\left(\mathcal{E}-\sqrt{\mathcal{E}^{2}-4 \kappa_{0}^{2}}\right) \quad \mathcal{E}>2 \kappa_{0}
\end{array}\right.
\]

The condition for the non-Hermitian Hamiltonian to possess a real-valued spectrum (i.e. to avoid complex-valued energies arising from bound states outside the continuum) is derived in Appendix B. Precisely, let \( \xi_{1,2} \) be the two roots of the second-order algebraic equation
\[
\xi^{2}+\frac{E_{a}}{\kappa_{0}} \xi+1-\left(\kappa_{a} / \kappa_{0}\right)^{2}=0
\]

Then the Hamiltonian \( H \) has a real-valued energy spectrum if and only if \( |\xi_{1,2}| \leq 1 \). Figure 2 shows the domain in the plane \( \left(\operatorname{Im}\left(E_{a}\right) / \kappa_{0}, \kappa_{a} / \kappa_{0}\right) \) where \( H \) has a purely continuous energy spectrum for a few increasing values of the ratio \( \left|\operatorname{Re}\left(E_{a}\right) / \kappa_{0}\right| \). The domain lies in the sector

The figure shows four plots displaying domains (shaded gray regions) in the (Im(Ea)/K0, Ka/K0) parameter space where a non-Hermitian Hamiltonian H has a purely continuous, real-valued energy spectrum. Each plot corresponds to different values of Re(Ea)/K0 (0, ±0.5, ±1, ±1.8), showing how the allowed domain shrinks as this parameter increases in magnitude. The boundaries of these shaded regions mark where spectral singularities occur in the system.

FIG. 2: Domains of non-existence of bound states for the Hamiltonian \( H \) in the \( \left(\operatorname{Im}\left(E_{a}\right) / \kappa_{0}, \kappa_{a} / \kappa_{0}\right) \) plane (shaded regions) for increasing values of the ratio \( \left|\operatorname{Re}\left(E_{a}\right)\right| / \kappa_{0} \). For a non-Hermitian Hamiltonian, i.e. \( \operatorname{Im}\left(E_{a}\right) \neq 0 \), in the shaded regions the energy spectrum of \( H \) is real-valued and purely continuous. Spectral singularities occur at the boundary of the shaded regions.

\( \kappa_{a} / \kappa_{0} \leq \sqrt{2} \) and shrinks toward \( \operatorname{Im}\left(E_{a}\right) / \kappa_{0}=\kappa_{a} / \kappa_{0}=0 \) as \( \left|\operatorname{Re}\left(E_{a}\right) / \kappa_{0}\right| \rightarrow 2^{-} \). For \( \left|\operatorname{Re}\left(E_{a}\right) / \kappa_{0}\right| \leq 2 \), bound states do exist for any value of \( \kappa_{a} / \kappa_{0} \) and \( \operatorname{Im}\left(E_{a}\right) / \kappa_{0} \). The wider domain is attained for \( \operatorname{Re}\left(E_{a}\right)=0 \). In particular, for \( \operatorname{Re}\left(E_{a}\right)=0 \) and \( \kappa_{a} / \kappa_{0}=\sqrt{2} \), from Eq. (52) it follows that \( H \) has a real-valued energy spectrum provided that
\[
-2 \kappa_{0}<\operatorname{Im}\left(E_{a}\right)<2 \kappa_{0}
\]

Let us now consider the occurrence of spectral singularities. According to Eqs.(19) and (20) and using Eqs.(49) and (51), a spectral singularity at energy \( \mathcal{E}=\mathcal{E}_{0} \), inside the interval \( \left(-2 \kappa_{0}, 2 \kappa_{0}\right) \), is found provided that the following two equations are simultaneously satisfied
\[
\begin{aligned}
\operatorname{Im}\left(E_{a}\right) & =\pm \frac{\kappa_{a}^{2}}{\kappa_{0}} \sqrt{1-\left(\frac{\mathcal{E}_{0}}{2 \kappa_{0}}\right)^{2}} \\
\operatorname{Re}\left(E_{a}\right) & =\left(1-\frac{\kappa_{a}^{2}}{2 \kappa_{0}^{2}}\right) \mathcal{E}_{0}.
\end{aligned}
\]

For arbitrarily given values of \( E_{a}, \kappa_{a} \) and \( \kappa_{0} \), the above conditions are generally not satisfied [nowhere for \( \mathcal{E}_{0} \) in the range \( \left(-2 \kappa_{0}, 2 \kappa_{0}\right) \)], i.e. the non-Hermitian FFA Hamiltonian is generally diagonalizable. Spectral singularities appear solely when a constraint among \( \operatorname{Re}\left(E_{a}\right) / \kappa_{0}, \operatorname{Im}\left(E_{a}\right) / \kappa_{0} \) and \( \kappa_{a} / \kappa_{0} \) is satisfied. Let us first assume \( \kappa_{a} / \kappa_{0} \) strictly smaller that \( \sqrt{2} \). In this case, a single spectral singularity, at the energy \( \mathcal{E}_{0}= \)

=