```markdown
## Chapter 6. Installing Red Hat OpenShift 3.11 on IBM PowerVC

environment. The Master, Infrastructure and Compute Roles are deployed to a single node (Figure 6-1).

![Figure 6-1 OpenShift Container Platform 3.11 all-in-one](figure-6-1.png)

**Figure 6-1 (summary):** This diagram illustrates an OpenShift Container Platform 3.11 "all-in-one" deployment.
It shows various user roles (Automation CI/CD Tools, Cluster Administrators, Developers, Application Owners) accessing a Web Console (1) and a Router (2).
The Web Console connects to PODs (3), PVC Storage (4), and a cluster of services including Registry, Jenkins, S21, Prometheus, K8s Operators, and OLM.
Application Users interact with the system via the Router, accessing applications at `http://<myapp>.ocp.example.com` and `https://<myapp>.ocp.example.com:443`.

**Seven nodes deployment** is highly available and suitable for production. The Master and Infrastructure Roles are deployed to three Nodes, the Computer Role is deployed to three Worker Nodes, and the Load Balancer is deployed to a single Node (Figure 6-2).

![Figure 6-2 OpenShift Container Platform 3.11 6xNodes + Load Balancer](figure-6-2.png)

**Figure 6-2 (summary):** This diagram depicts an OpenShift Container Platform 3.11 deployment with "6xNodes + Load Balancer".
User roles (Automation CI/CD Tools, Cluster Administrators, Developers, Application Owners) access the system through a Load Balancer (LB).
The Load Balancer directs traffic to Master Nodes (1), which consist of Routers, Master-Infra nodes, and Registry.
It also directs traffic to Application Nodes (2), which contain APP PODs and PVC Storage.
Application Users directly access applications at `http://<myapp>.ocp.example.com` and `https://<myapp>.ocp.example.com:443`.
```