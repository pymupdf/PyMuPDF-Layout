

## Figure 2: Treatment Response Functions

The page shows two graphs side by side:

**Concave Treatment Response Function**: A graph showing a curved line that starts steep and gradually flattens as it increases from left to right, with "Treatment Level t" on the x-axis and "Potential Outcome Y" on the y-axis.

**Convex Treatment Response Function**: A graph showing a curved line that starts relatively flat and becomes steeper as it increases from left to right, with "Treatment Level t" on the x-axis and "Potential Outcome Y" on the y-axis.

**Figure 2: Concave treatment response and convex treatment response**

Concavity and convexity of the treatment response function imply $$\text{Pr} \left( \frac{Y_0-W}{t_0-t_W} \geq \frac{Y_1-Y_0}{t_1-t_0}, Y_1 \geq Y_0 \geq W \right) = 1$$

and $$\text{Pr} \left( \frac{Y_0-W}{t_0-t_W} \geq \frac{Y_1-Y_0}{t_1-t_0}, Y_1 \geq Y_0 \geq W \right) = 1$$, respectively, where t<sub>d</sub> is a level of input for each treatment status d ∈ {0, 1} while t<sub>W</sub> is a level of input without the treatment and t<sub>W</sub> < t<sub>0</sub> < t<sub>1</sub>. Given W = w, concavity and convexity of the treatment response function restrict the support of (Y<sub>0</sub>, Y<sub>1</sub>) to the region below the straight line $$Y_1 = \frac{t_1-t_W}{t_0-t_W}Y_0 - \frac{t_1-t_0}{t_0-t_W}w$$ and above the straight line Y<sub>1</sub> = Y<sub>0</sub>, and to the region above two straight lines $$Y_1 = \frac{t_1-t_W}{t_0-t_W}Y_0 - \frac{t_1-t_0}{t_0-t_W}w$$ and Y<sub>1</sub> = Y<sub>0</sub>, respectively, as shown in Figures 1(b) and (c).

## Example 3 (Roy Model)
In the Roy model, individuals self-select into treatment when their benefits from the treatment are greater than nonpecuniary costs for treatment participation. The extended Roy model assumes that the nonpecuniary cost is deterministic with the following selection equation:

$$D = 1 \{Y_1 - Y_0 \geq \mu_C (Z)\},$$

where μ<sub>C</sub> (Z) represents nonpecuniary costs with a vector of observables Z. Then treated (D = 1) and untreated people (D = 0) are the observed groups satisfying support restrictions {Y<sub>1</sub> - Y<sub>0</sub> ≥ μ<sub>C</sub> (Z)} and {Y<sub>1</sub> - Y<sub>0</sub> < μ<sub>C</sub> (Z)}, respectively.

## Example 4 (DTE conditional on Potential Outcomes)
The conditional DTE for the unobservable subgroup whose potential outcomes belong to a certain set C is written as

$$\text{Pr} \{Y_1 - Y_0 \leq \delta | (Y_0, Y_1) \in C\}.$$

8
