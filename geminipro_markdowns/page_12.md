![Figure 5: Partition degeneracy and correlation with excursion count.](figure-5.png)

**Figure 5 (summary):** This figure comprises five panels illustrating partition degeneracy and its correlation with event counts.
- **(A)** A heatmap showing 100 different partitions of network nodes into communities, identified using the Louvain algorithm for a single instance.
- **(B)** An association matrix heatmap, where each cell's color represents how often two nodes were assigned to the same partition.
- **(C)** A heatmap of z-score Rand indices, comparing the similarity between all pairs of the 100 partitions.
- **(D)** A scatter plot for one participant, correlating the number of events with the mean z-score Rand index.
- **(E)** A line plot of correlation coefficients between the z-score Rand index and event count for 80 participants.

**Figure 5:** Partition degeneracy and correlation with excursion count. (A) As an example, we show the set of 100 partitions obtained by maximizing modularity for a single instance of dFC (169 events). (B) The association matrix for this set of partitions. Each element in the association matrix counts the number of times that two nodes were assigned to the same partition. The node order is the same as in Figure 4. (C) Matrix of z-score Rand indices for all pairs of the 100 partitions shown in panel (A). (D) We show the scatterplot of mean z-score Rand index for each time point plotted against the event count, both calculated at the same time point, for one representative participant. (E) Correlation coefficients for z-score Rand index and event count plotted across participants. Note that of the 80 participants, only four exhibited negative correlations.

---

![Figure 6: Default mode network dissociates during mass-excursions.](figure-6.png)

**Figure 6 (summary):** This figure has three panels demonstrating how the default mode network (DMN) dissociates during mass-excursions.
- **(A)** A heatmap showing the mean difference in association matrices between non-mass excursions and excursions across all participants.
- **(B)** A heatmap highlighting node pairs that are statistically more or less likely to be in the same community during non-excursions versus excursions.
- **(C)** A bar chart ranking brain regions by the total number of significant changes in their community co-assignments. The bars are colored by network (DMN, CONT, VIS, etc.), showing that DMN regions change the most.

**Figure 6:** Default mode network dissociates during mass-excursions. A) Mean difference in association matrices constructed during non-mass excursions and excursions. B) Node pairs that were statistically more or less likely to be observed in the same community during non-excursions compared to excursions. The network labels are taken from Yeo et al. (2011), with labels corresponding to networks for control (CONT), default mode (DMN), dorsal attention (DAN), limbic (LIM), ventral attention (VAN), somatomotor network (SMN), and visual (VIS). C) We sum the rows of the matrix in panel B) to identify regions that that consistently change their community co-assignments with other regions. The regions that change the most are predominantly regions associated with DMN.