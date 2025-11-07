- 3. Create the A → C relationship (or the B → C relationship). 

- 4. Synchronize to system C, and ensure that A → C is established: 

   - – A → B, A → C, A → D, B → C, B → D, and C → D – A → B, A → C, and B → C 

Figure 11-84 shows an example of a triangle topology (A → B, A → C, and B → C). 

**==> picture [130 x 114] intentionally omitted <==**

_Figure 11-84   Triangle topology_ 

Figure 11-85 shows an example of a fully connected topology (A → B, A → C, A → D, B → D, and C → D). 

**==> picture [151 x 122] intentionally omitted <==**

_Figure 11-85   Fully connected topology_ 

Figure 11-85 is a fully connected mesh in which every system has a partnership to each of the three other systems. This topology enables volumes to be replicated between any pair of systems, for example A → B, A → C, and B → C. 

Figure 11-86 shows a daisy-chain topology. 

**==> picture [181 x 36] intentionally omitted <==**

_Figure 11-86   Daisy-chain topology_ 

Although systems can have up to three partnerships, volumes can be part of only one remote copy relationship, for example A → B. 

**System partnership intermix:** All of the preceding topologies are valid for the intermix of the IBM SAN Volume Controller with the Storwize V7000 if the Storwize V7000 is set to the replication layer and running IBM Spectrum Virtualize code 6.3.0 or later. 

Chapter 11. Advanced Copy Services **517** 

