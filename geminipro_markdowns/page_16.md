![Figure 7: The red arcs are the trajectory of the system (5.60) with initial value (0, 1.2) and the blue arcs are the orbit with initial value (0,1.5). Through simulation, we observe that the trajectories approach to the periodic solution of (5.60) as time increases.](figure-7.png)

**Figure 7 (summary):** A phase portrait plot of $y_2$ versus $y_1$. It displays two sets of trajectories, red and blue, starting from different initial conditions. Both sets of trajectories converge towards two distinct, stable, arc-shaped orbits, one in the upper half-plane ($y_2 > 0$) and one in the lower half-plane ($y_2 < 0$).

---

where $R = 0.9$ and $\Gamma = \{x|x_1 = 0, x_2 \le 0\}$. It is easy to see that system (5.69) is of the form (5.57) and $\Phi(x_1, x_2) = x_1 = 0$. The system has a periodic solution

$$
\Psi_\mu(t) = (1 + (1 + \mu) \cos(t), -(1 + \mu) \sin(t)),
\quad (5.70)
$$

where $t \in \mathbb{R}$ for $\mu \in (-2,0]$.

The generating system of (5.69) has the following form

$$
\begin{aligned}
x'_1 &= x_2, \\
x'_2 &= -0.0001[x_2^2 + (x_1 - 1)^2 - 1]x_2 - x_1 + 1, \\
\Delta x_2|_{x \in \Gamma} &= -(1 + R x_2)x_2,
\end{aligned}
\quad (5.71)
$$

and admits the periodic solution $\Psi_0(t) = (1+\cos(t), –\sin(t))$. By means of the equality $\langle\nabla\Phi(x^*), f(x^*)\rangle = \langle(1,0), (0, 1)\rangle = 0$ with $x^* = (0,0) \in \partial\Gamma$, it is easy to say that $x^*$ is a grazing point of $\Psi_0(t)$.

Let us start with the linearization of system (5.71) around the periodic solution $\Psi_0(t)$. Consider a near solution $y(t) = y(t, 0, y^* + \Delta y)$, where $\Delta y = (\Delta y_1, \Delta y_2)$, to the periodic solution $\Psi_0(t)$. Assume that $y(t)$ satisfies condition (N1), and it meets the surface of discontinuity $\Gamma$ at the moment $t = \xi$ and at the point $\bar{y} = y(\xi, 0, y^* + \Delta y)$. Considering the formula (3.10) for the transversal point $\bar{y} = (\bar{y}_1, \bar{y}_2)$, the first component $\frac{\partial\tau(\bar{y})}{\partial y_1^0}$ can be evaluated as $\frac{\partial\tau(\bar{y})}{\partial y_1^0} = -\frac{1}{\bar{y}_2}$. From the last equality, the singularity is seen at the grazing point. By taking into account (3.17) with (5.71) and $\frac{\partial\tau(\bar{y})}{\partial y_1^0}$, we obtain that