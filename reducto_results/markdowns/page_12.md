Key details from the image:

*   **(A)** Node Assignments: Shows partitions identified using Louvain, with a color-coded Community ID legend.
*   **(B)** Association Matrix: Represents node association weights, with a color-coded scale from 0 to 100.
*   **(C)** Z-Score Rand Index Matrix: Displays the Z-score Rand index between partition pairs.
*   **(D)** Scatterplot: Compares mean Z-score Rand index to the number of events.
*   **(E)** Correlation Plot: Mean Z-score Rand index and event count correlation plotted against subject ID. Most subjects exhibit positive correlations.

Figure 5: Partition degeneracy and correlation with excursion count. (A) As an example, we show the set of 100 partitions obtained by maximizing modularity for a single instance of dFC (169 events). (B) The association matrix for this set of partitions. Each element in the association matrix counts the number of times that two nodes were assigned to the same partition. The node order is the same as in Figure 4. (C) Matrix of z-score Rand indices for all pairs of the 100 partitions shown in panel (A). (D) We show the scatterplot of mean z-score Rand index for each time point plotted against the event count, both calculated at the same time point, for one representative participant. (E) Correlation coefficients for z-score Rand index and event count plotted across participants. Note that of the 80 participants, only four exhibited negative correlations.

| Legend color | Network label |
|---:|---|
| Red | CONT (control) |
| Yellow/Orange | DMN (default mode) |
| Green | DAN (dorsal attention) |
| Cyan/Teal | LIM (limbic) |
| Blue | VAN (ventral attention) |
| Purple/Magenta | SMN (somatomotor) |
| Pink | VIS (visual) |

| Panel | Description / data extracted |
|---:|---|
| A | Mean difference association matrix across all participants (Δ_ij). Colorbar range: −0.10 to +0.10 (values indicate change in co-assignment probability between excursion vs non-excursion conditions). Node order same as Fig. 4. |
| B | Statistically significant node-pair differences in co-assignment between conditions. Colors denote which condition shows greater co-assignment (labels on figure: "Non > Excursions" vs "Excursions > Non"). Matrix is a significance mask over panel A. |
| C | Bar plot: number of significant co-assignment changes per node (nodes ordered by rank). Y-axis range shown 0–60 (max ≈60). Bars are colored by network (legend above). Top-ranked nodes (highest counts) are predominantly DMN.

Figure 6: Default mode network dissociates during mass-excursions. A) Mean difference in association matrices constructed during non-mass excursions and excursions. B) Node pairs that were statistically more or less likely to be observed in the same community during nonexcursions compared to excursions. The network labels are taken from Yeo et al. (2011), with labels corresponding to networks for control (CONT), default mode (DMN), dorsal attention (DAN), limbic (LIM), ventral attention (VAN), somatomotor network (SMN), and visual (VIS). C) We sum the rows of the matrix in panel B) to identify regions that that consistently change their community co-assignments with other regions. The regions that change the most are predominantly regions associated with DMN.

43