The image shows a phase portrait with red and blue trajectory arcs representing solutions to a dynamical system with different initial conditions. The red arcs correspond to initial value (0, 1.2) while the blue arcs correspond to initial value (0, 1.5). Both trajectories appear to converge toward a periodic solution, with the arcs forming closed-loop patterns in the upper and lower portions of the y₁-y₂ phase plane.

Figure 7: The red arcs are the trajectory of the system (5.60) with initial value (0, 1.2) and the blue arcs are the orbit with initial value (0, 1.5). Through simulation, we observe that the trajectories approach to the periodic solution of (5.60) as time increases.

where \( R=0.9 \) and \( \Gamma=\{x \mid x_{1}=0, x_{2} \leq 0\} \). It is easy to see that system (5.69) is of the form (5.57) and \( \Phi\left(x_{1}, x_{2}\right)=x_{1}=0 \). The system has a periodic solution

\[
\Psi_{\mu}(t)=(1+(1+\mu) \cos (t),-(1+\mu) \sin (t)),
\]

where \( t \in \mathbb{R} \) for \( \mu \in(-2,0] \).

The generating system of (5.69) has the following form

\[
\begin{aligned}
x_{1}^{\prime} & =x_{2}, \\
x_{2}^{\prime} & =-0.0001\left[x_{2}^{2}+(x_{1}-1)^{2}-1\right] x_{2}-x_{1}+1 \\
\Delta x_{2} \mid_{x \in \Gamma} & =-(1+R x_{2}) x_{2},
\end{aligned}
\]

and admits the periodic solution \( \Psi_{0}(t)=(1+\cos (t),-\sin (t)) \). By means of the equality \( \left\langle\nabla \Phi\left(x^{*}\right), f\left(x^{*}\right)\right\rangle= \) \( \langle(1,0),(0,1)\rangle=0 \) with \( x^{*}=(0,0) \in \partial \Gamma \), it is easy to say that \( x^{*} \) is a grazing point of \( \Psi_{0}(t) \).

Let us start with the linearization of system (5.71) around the periodic solution \( \Psi_{0}(t) \). Consider a near solution \( y(t)=y(t, 0, y^{*}+\Delta y) \), where \( \Delta y=\left(\Delta y_{1}, \Delta y_{2}\right) \), to the periodic solution \( \Psi_{0}(t) \). Assume that \( y(t) \) satisfies condition (N1), and it meets the surface of discontinuity \( \Gamma \) at the moment \( t=\xi \) and at the point \( \bar{y}=y\left(\xi, 0, y^{*}+\Delta y\right) \). Considering the formula (3.10) for the transversal point \( \bar{y}=\left(\bar{y}_{1}, \bar{y}_{2}\right) \), the first component \( \frac{\partial \tau(\bar{y})}{\partial y_{1}^{0}} \) can be evaluated as \( \frac{\partial \tau(\bar{y})}{\partial y_{1}^{0}}=-\frac{1}{\bar{y}_{2}} \). From the last equality, the singularity is seen at the grazing point. By taking into account (3.17) with (5.71) and \( \frac{\partial \tau(\bar{y})}{\partial y_{1}^{0}} \), we obtain that

35