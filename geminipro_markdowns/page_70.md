*Draft Document for Review December 11, 2019 1:55 pm 8459ch06.fm*

# Chapter 6. Installing Red Hat OpenShift 3.11 on IBM PowerVC

environment. The Master, Infrastructure and Compute Roles are deployed to a single node (Figure 6-1).

![Figure 6-1: OpenShift Container Platform 3.11 all-in-one](figure-6-1.png)

**Figure 6-1 (summary):** The diagram depicts an "all-in-one" OpenShift architecture where all components reside on a single node.
- **Users & Roles:** Automation/CI/CD Tools, Cluster Administrators, Developers, and Application Owners interact with the system.
- **Ingress:** Web Console runs on port 8443; Router listens on ports 80 & 443.
- **Core Services:** Includes Registry, Jenkins, S2I, Prometheus, K8s Operators, and OLM.
- **Workloads:** PODs and PVC Storage are hosted within the same node.
- **Application Access:** Application Users connect via HTTP/HTTPS (`http://<myapp>.ocp.example.com`) through the Router.

- Seven nodes deployment is highly available and suitable for production. The Master and Infrastructure Roles are deployed to three Nodes, the Computer Role is deployed to three Worker Nodes, and the Load Balancer is deployed to a single Node (Figure 6-2).

![Figure 6-2: OpenShift Container Platform 3.11 6xNodes + Load Balancer](figure-6-2.png)

**Figure 6-2 (summary):** The diagram shows a distributed architecture with high availability.
- **Load Balancer [LB]:** Sits in front of the cluster to manage traffic from Automation tools, Administrators, Developers, and Owners.
- **Master Nodes (Cluster of 3):** The LB routes traffic to Routers residing on three nodes labeled "Master - Infra," which also host the Registry.
- **Application Nodes:** A separate group of Worker nodes (numbered 2) hosts the Application PODs and PVC Storage.
- **Traffic Flow:** External requests flow through the Load Balancer to the Master Nodes (Routers), which then direct traffic to the Application Nodes.