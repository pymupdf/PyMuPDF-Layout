

environment. The Master, Infrastructure and Compute Roles are deployed to a single node (Figure 6-1).

![](21ac95be2778732e577d82233d5ee6ab_img.jpg)

Figure 6-1 illustrates the OpenShift Container Platform 3.11 all-in-one deployment architecture. The diagram shows four main components (1, 2, 3, 4) and associated roles/users.

- **1. Web Console** (Port 8443, URL: https://ocp.example.com:8443) is accessible by Automation CI/CD Tools, Cluster Administrators, Developers, and Application Owners.
- **2. Router** (Port 80 & 443) is accessible by Application Users (URLs: http://<myapp>.ocp.example.com and https://<myapp>.ocp.example.com:443).
- **3. PODs** (POD C) are part of the application infrastructure.
- **4. PVC Storage** (Persistent Volume Claims) is part of the application infrastructure.

The central component is the **REGISTRY**, which contains Jenkins, S2I, Prometheus, K8s Operators, OLM, and other components.

Figure 6-1 OpenShift Container Platform 3.11 all-in-one

► **Seven nodes deployment** is highly available and suitable for production. The Master and Infrastructure Roles are deployed to three Nodes, the Computer Role is deployed to three Worker Nodes, and the Load Balancer is deployed to a single Node (Figure 6-2).

![](1559db1c389771b44f7dc11d48b06079_img.jpg)

Figure 6-2 illustrates the OpenShift Container Platform 3.11 6xNodes + Load Balancer deployment architecture. The diagram shows two main components (1, 2) and associated roles/users.

- **1. Master Nodes** (Dashed box) contain Routers and Registry. The Routers are associated with Master - Infra nodes. The Registry is associated with Master - Infra nodes.
- **2. Application Nodes** (Dashed box) contain APP PODs (POD C) and PVC Storage.

The Load Balancer [LB] is accessible by Automation CI/CD Tools, Cluster Administrators, Developers, Application Owners, and Application Users (URLs: http://<myapp>.ocp.example.com and https://<myapp>.ocp.example.com:443).

Figure 6-2 OpenShift Container Platform 3.11 6xNodes + Load Balancer