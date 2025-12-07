

1. Create the  $A \to C$  relationship (or the  $B \to C$  relationship).
2. Synchronize to system C, and ensure that  $A \to C$  is established:

$A \to B$ ,  $A \to C$ ,  $A \to D$ ,  $B \to C$ ,  $B \to D$ , and  $C \to D$   
 $A \to B$ ,  $A \to C$ , and  $B \to C$

Figure 11-84 shows an example of a triangle topology ( $A \to B$ ,  $A \to C$ , and  $B \to C$ ).

![Diagram showing a triangle topology with three nodes labeled A, B, and C. Node A is connected to B and C. Node B is connected to A and C. Node C is connected to A and B.](64662465bba247703fdec49c8f3309f9_img.jpg)

Diagram showing a triangle topology with three nodes labeled A, B, and C. Node A is connected to B and C. Node B is connected to A and C. Node C is connected to A and B.

Figure 11-84 Triangle topology

Figure 11-85 shows an example of a fully connected topology ( $A \to B$ ,  $A \to C$ ,  $A \to D$ ,  $B \to D$ , and  $C \to D$ ).

![Diagram showing a fully connected topology with four nodes labeled A, B, C, and D. Every node is connected to every other node, forming a complete graph.](0538daaa5583c23e17db3a12f2281a55_img.jpg)

Diagram showing a fully connected topology with four nodes labeled A, B, C, and D. Every node is connected to every other node, forming a complete graph.

Figure 11-85 Fully connected topology

Figure 11-85 is a fully connected mesh in which every system has a partnership to each of the three other systems. This topology enables volumes to be replicated between any pair of systems, for example  $A \to B$ ,  $A \to C$ , and  $B \to C$ .

Figure 11-86 shows a daisy-chain topology.

![Diagram showing a daisy-chain topology with four nodes labeled A, B, C, and D. The nodes are connected sequentially in a line: A is connected to B, B is connected to C, and C is connected to D.](1d7527f4316cfe2d342b08d1653d1592_img.jpg)

Diagram showing a daisy-chain topology with four nodes labeled A, B, C, and D. The nodes are connected sequentially in a line: A is connected to B, B is connected to C, and C is connected to D.

Figure 11-86 Daisy-chain topology

Although systems can have up to three partnerships, volumes can be part of only one remote copy relationship, for example  $A \to B$ .

**System partnership intermix:** All of the preceding topologies are valid for the intermix of the IBM SAN Volume Controller with the Storwize V7000 if the Storwize V7000 is set to the replication layer and running IBM Spectrum Virtualize code 6.3.0 or later.