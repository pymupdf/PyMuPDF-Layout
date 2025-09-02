3. Create the A → C relationship (or the B → C relationship).

4. Synchronize to system C, and ensure that A → C is established:

	- A → B, A → C, A → D, B → C, B → D, and C → D

	- A → B, A → C, and B → C

- Figure 11-84 shows an example of a triangle topology (A \( \rightarrow \) B, \( A \rightarrow C \), and \( B \rightarrow C \) ).

The image shows a triangle network topology with three nodes labeled A, B, and C positioned at the vertices of a triangle. Node A is connected to both nodes B and C, node B is connected to both nodes A and C, and node C is connected to both nodes A and B. This creates a fully interconnected three-node network where each node has direct connections to the other two nodes.

Figure 11-84 Triangle topology

Figure 11-85 shows an example of a fully connected topology (A \( \rightarrow \) B, \( \mathrm{A} \rightarrow \mathrm{C}, \mathrm{A} \rightarrow \mathrm{D}, \mathrm{B} \rightarrow \mathrm{D} \), and \( \mathrm{C} \rightarrow \mathrm{D} \) ).

The image shows a network diagram with four nodes labeled A, B, C, and D arranged in a square formation. Each node is connected to every other node with direct links, creating a fully connected topology. The connections form a pattern where straight lines connect adjacent nodes and diagonal lines create an "X" pattern connecting opposite corners.

Figure 11-85 Fully connected topology

Figure 11-85 is a fully connected mesh in which every system has a partnership to each of the three other systems. This topology enables volumes to be replicated between any pair of systems, for example \( \mathrm{A} \rightarrow \mathrm{B}, \mathrm{A} \rightarrow \mathrm{C} \), and \( \mathrm{B} \rightarrow \mathrm{C} \).

Figure 11-86 shows a daisy-chain topology.

A-B- C D

Figure 11-86 Daisy-chain topology

Although systems can have up to three partnerships, volumes can be part of only one remote copy relationship, for example A → B.

System partnership intermix: All of the preceding topologies are valid for the intermix of the IBM SAN Volume Controller with the Storwize V7000 if the Storwize V7000 is set to the replication layer and running IBM Spectrum Virtualize code 6.3.0 or later.

Chapter 11. Advanced Copy Services 517

=