environment. The Master, Infrastructure and Compute Roles are deployed to a single node (Figure 6-1).

![Figure 6-1: OpenShift Container Platform 3.11 all-in-one](figure-6-1.png)

**Figure 6-1 (summary):** A diagram showing a single-node "all-in-one" OpenShift deployment.
- **External Users:** Automation Tools, Administrators, Developers, and Application Owners interact with the system. Application Users access deployed applications.
- **Entry Points:**
    1.  **Web Console:** Accessed at `https://ocp.example.com:8443`.
    2.  **Router:** Routes traffic on ports 80 & 443 to applications at `http://<myapp>.ocp.example.com` and `https://<myapp>.ocp.example.com:443`.
- **Internal Components (on the single node):**
    3.  **PODs:** Running application containers.
    4.  **PVC Storage:** Persistent storage for applications.
    - Other services include Registry, Jenkins, S2I, Prometheus, K8s Operators, and OLM.

Seven nodes deployment is highly available and suitable for production. The Master and Infrastructure Roles are deployed to three Nodes, the Computer Role is deployed to three Worker Nodes, and the Load Balancer is deployed to a single Node (Figure 6-2).

![Figure 6-2: OpenShift Container Platform 3.11 6xNodes + Load Balancer](figure-6-2.png)

**Figure 6-2 (summary):** A diagram of a high-availability, six-node OpenShift deployment with a load balancer.
- **Architecture:**
    - A Load Balancer (LB) is the single entry point for all users.
    - **1. Master Nodes:** A cluster of three nodes running Master and Infra roles, including Routers and the Registry.
    - **2. Application Nodes:** A cluster of three nodes running application PODs, connected to PVC Storage.
- **Traffic Flow:** Users (Administrators, Developers, etc.) connect through the LB, which distributes requests to the Master Nodes. Application Users access their apps via the LB, which routes traffic to the appropriate application pods on the Application Nodes.