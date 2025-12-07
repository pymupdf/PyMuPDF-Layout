environment. The Master, Infrastructure and Compute Roles are deployed to a single node (Figure 6-1).

![Figure 6-1: OpenShift Container Platform 3.11 all-in-one](figure-6-1.png)

**Figure 6-1 (summary):** An "all-in-one" architecture diagram showing four user roles (Automation/CI/CD Tools, Cluster Administrators, Developers, and Application Owners) connecting to a single node. The node contains the Web Console (port 8443), Router (ports 80 & 443), Registry, CI/CD tools (Jenkins, S2I), Prometheus, K8s Operators, OLM, PODs, and PVC Storage. Application Users connect externally via the Router.

- **Seven nodes deployment** is highly available and suitable for production. The Master and Infrastructure Roles are deployed to three Nodes, the Computer Role is deployed to three Worker Nodes, and the Load Balancer is deployed to a single Node (Figure 6-2).

![Figure 6-2: OpenShift Container Platform 3.11 6xNodes + Load Balancer](figure-6-2.png)

**Figure 6-2 (summary):** A distributed architecture diagram showing user roles connecting to a Load Balancer [LB]. The LB distributes traffic to a cluster consisting of:
1.  **Master Nodes:** Three nodes containing Routers, Master-Infra services, and the Registry.
2.  **Application Nodes:** Nodes containing Application PODs and PVC Storage.