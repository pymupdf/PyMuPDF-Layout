Legend
- Black solid: True DTE
- Red dashed: Makarov lower
- Red dash-dot (or different red dash): Makarov upper
- Blue solid: New lower bound
Axes: x ∈ [0,30], y ∈ [0,1] (all subplots)

| Subplot | k1 | k2 | Key observation |
|---:|---:|---:|---|
| (1,1) top-left | 1 | 1 | All curves rise quickly to 1. Order (typical): Makarov lower < New lower < True DTE < Makarov upper. New lower closer to True than Makarov lower. |
| (1,2) top-center | 1 | 10 | Curves slower to rise; New lower substantially closer to True than Makarov lower. Makarov upper is the loosest bound. |
| (1,3) top-right | 1 | 40 | New lower remains closer to True; Makarov lower much lower for small x. |
| (2,1) middle-left | 5 | 1 | Curves rise moderately; New lower nearly overlaps True at higher x and is above Makarov lower for most x. |
| (2,2) center | 5 | 10 | New lower and True DTE are close across much of x; Makarov lower is noticeably looser (lower). |
| (2,3) middle-right | 5 | 40 | New lower closer to True than Makarov lower; Makarov upper still the largest envelope. |
| (3,1) bottom-left | 10 | 1 | All curves shift right (slower increase); New lower is closer to True than Makarov lower for most x. |
| (3,2) bottom-center | 10 | 10 | New lower nearly matches True at moderate x; Makarov lower is distinctly lower. |
| (3,3) bottom-right | 10 | 40 | New lower and True are very close for much of the range; Makarov bounds give a much wider interval. |

Overall summary: across all nine panels the New lower bound (blue) is generally tighter (closer to the True DTE, black) than the Makarov lower (red), while the Makarov upper provides the largest (loosest) upper bound.

Figure 12: New bounds v.s. Makarov bounds

F0 and F1 over the support causes more triangles having positive probability lower bounds, which leads the improvement of my new lower bound. On the other hand, the Makarov lower bound gets no such informational gain because it uses only one triangle while my new lower bound takes advantage of multiple triangles.

## 5 Application to the Distribution of Effects of Smoking on Birth Weight

In this section, I apply the results presented in Section 3 to an empirical analysis of the distribution of smoking effects on infant birth weight. Smoking not only has a direct impact on infant birth weight, but is also associated with unobservable factors that affect infant birth weight. I identify marginal distributions of potential infant birth weight with and without smoking by making use of a state cigarette tax hike in Massachusetts (MA) in January 1993 as a source of exogenous variation. I focus on pregnant women who change their smoking behavior from smoking to nonsmoking in response to the tax increase. To identify the distribution of smoking effects, I impose a MTR restriction that smoking has nonpositive effects on infant birth weight with probability one. I propose an estimation procedure and report estimates of the DTE

30