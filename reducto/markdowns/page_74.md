3. Create the A → C relationship (or the B → C relationship).

4. Synchronize to system C, and ensure that A → C is established: A-BA-C, A. & D. B → C, B D, and C and B → C

Figure 11-84 shows an example of a triangle topology (A → B, A → C, and B →C).

The image shows a triangle topology with nodes A, B, and C. The connections are A to B, A to C, and B to C.


Figure 11-84 Triangle topology

Figure 11-85 shows an example of a fully connected topology (A→B, AC, A → D, B → D, and C → D).

| Node | Position | Connected to |
|------|----------|--------------|
| A    | top-left | B, C, D |
| B    | bottom-left | A, C, D |
| C    | top-right | A, B, D |
| D    | bottom-right | A, B, C |

Figure 11-85 Fully connected topology

Figure 11-85 is a fully connected mesh in which every system has a partnership to each of the three other systems. This topology enables volumes to be replicated between any pair of systems, for example A → B, A → C, and B →C.

Figure 11-86 shows a daisy-chain topology.

A-B- C D

Figure 11-86 Daisy-chain topology

Although systems can have up to three partnerships, volumes can be part of only one remote copy relationship, for example A →B.

System partnership intermix: All of the preceding topologies are valid for the intermix of the IBM SAN Volume Controller with the Storwize V7000 if the Storwize V7000 is set to the replication layer and running IBM Spectrum Virtualize code 6.3.0 or later.

Chapter 11. Advanced Copy Services 517