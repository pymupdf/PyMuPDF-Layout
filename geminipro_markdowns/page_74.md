3. Create the A → C relationship (or the B → C relationship).
4. Synchronize to system C, and ensure that A → C is established:
   - A → B, A → C, A → D, B → C, B → D, and C → D
   - A → B, A → C, and B → C

Figure 11-84 shows an example of a triangle topology (A → B, A → C, and B → C).

![Figure 11-84: Triangle topology](figure-11-84.png)

**Figure 11-84 (summary):** A diagram shows three nodes, A, B, and C, connected to each other, forming a triangle.

Figure 11-85 shows an example of a fully connected topology (A → B, A → C, A → D, B → D, and C → D).

![Figure 11-85: Fully connected topology](figure-11-85.png)

**Figure 11-85 (summary):** A diagram shows four nodes, A, B, C, and D. Each node is connected to every other node, including diagonally, forming a fully connected mesh.

Figure 11-85 is a fully connected mesh in which every system has a partnership to each of the three other systems. This topology enables volumes to be replicated between any pair of systems, for example A → B, A → C, and B → C.

Figure 11-86 shows a daisy-chain topology.

![Figure 11-86: Daisy-chain topology](figure-11-86.png)

**Figure 11-86 (summary):** A diagram shows four nodes, A, B, C, and D, connected sequentially in a line.

Although systems can have up to three partnerships, volumes can be part of only one remote copy relationship, for example A → B.

> **System partnership intermix:** All of the preceding topologies are valid for the intermix of the IBM SAN Volume Controller with the Storwize V7000 if the Storwize V7000 is set to the replication layer and running IBM Spectrum Virtualize code 6.3.0 or later.