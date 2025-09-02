

| y           | y                                              | Trajectory Type                                     |
| ----------- | ---------------------------------------------- | --------------------------------------------------- |
| -0.2 to 1.2 | 2 to -2                                        | Phase portrait showing red and blue trajectory arcs |
| Red arcs    | Upper: \~1.5 to \~0.8, Lower: \~-1.5 to \~-0.8 | Trajectory with initial value (0, 1.2)              |
| Blue arcs   | Upper: \~1.5 to \~1.2, Lower: \~-1.5 to \~-1.0 | Orbit with initial value (0, 1.5)                   |


**Figure 7:** The red arcs are the trajectory of the system (5.60) with initial value (0, 1.2) and the blue arcs are the orbit with initial value (0, 1.5). Through simulation, we observe that the trajectories approach to the periodic solution of (5.60) as time increases.

where *R* = 0.9 and Γ = {*x*|*x*<sub>1</sub> = 0, *x*<sub>2</sub> ≤ 0}. It is easy to see that system (5.69) is of the form (5.57) and Φ(*x*<sub>1</sub>, *x*<sub>2</sub>) = *x*<sub>1</sub> = 0. The system has a periodic solution

$$\Psi_\mu(t) = (1 + (1 + \mu) \cos(t), -(1 + \mu) \sin(t)), \qquad (5.70)$$

where *t* ∈ ℝ for *μ* ∈ (-2, 0].

The generating system of (5.69) has the following form

$$x'_1 = x_2,$$

$$x'_2 = -0.0001[x_2^2 + (x_1 - 1)^2 - 1]x_2 - x_1 + 1, \qquad (5.71)$$

$$\Delta x_2|_{x \in \Gamma} = -(1 + Rx_2)x_2,$$

and admits the periodic solution Ψ<sub>0</sub>(*t*) = (1+cos(*t*), -sin(*t*)). By means of the equality ⟨∇Φ(*x*<sup>*</sup>), *f*(*x*<sup>*</sup>)⟩ = ⟨(1, 0), (0, 1)⟩ = 0 with *x*<sup>*</sup> = (0, 0) ∈ ∂Γ, it is easy to say that *x*<sup>*</sup> is a grazing point of Ψ<sub>0</sub>(*t*).

Let us start with the linearization of system (5.71) around the periodic solution Ψ<sub>0</sub>(*t*). Consider a near solution *y*(*t*) = *y*(*t*, 0, *y*<sup>*</sup> + Δ*y*), where Δ*y* = (Δ*y*<sub>1</sub>, Δ*y*<sub>2</sub>), to the periodic solution Ψ<sub>0</sub>(*t*). Assume that *y*(*t*) satisfies condition (*N*1), and it meets the surface of discontinuity Γ at the moment *t* = *ξ* and at the point *ȳ* = *y*(*ξ*, 0, *y*<sup>*</sup> + Δ*y*). Considering the formula (3.10) for the transversal point *ȳ* = (*ȳ*<sub>1</sub>, *ȳ*<sub>2</sub>), the first component ∂*τ*(*ȳ*)/∂*y*<sub>1</sub><sup>0</sup> can be evaluated as ∂*τ*(*ȳ*)/∂*y*<sub>1</sub><sup>0</sup> = -1/*ȳ*<sub>2</sub>. From the last equality, the singularity is seen at the grazing point. By taking into account (3.17) with (5.71) and ∂*τ*(*ȳ*)/∂*y*<sub>1</sub><sup>0</sup>, we obtain that

35
