Draft Document for Review December 11, 2019 1:55 pm

8459ch06.fm

environment. The Master, Infrastructure and Compute Roles are deployed to a single node (Figure 6-1).

The image illustrates an OpenShift Container Platform 3.11 all-in-one setup.

Key entities:

*   **Users**: Automation CI/CD Tools, Cluster Administrators, Developers, Application Owners, Application Users
*   **Components**: Web Console :8443 (https://ocp.example.com:8443), Router :80 & :443, PODs, PVC Storage, REGISTRY, Jenkins, S2I, Prometheus, K8s Operators, OLM

Figure 6-1 OpenShift Container Platform 3.11 all-in-one

- Seven nodes deployment is highly available and suitable for production. The Master and Infrastructure Roles are deployed to three Nodes, the Computer Role is deployed to three Worker Nodes, and the Load Balancer is deployed to a single Node (Figure 6-2).

- Platform: OpenShift Container Platform 3.11 — 6x Nodes + Load Balancer

- Actors (clients of the cluster):
  - Automation CI/CD Tools
  - Cluster Administrators
  - Developers
  - Application Owners
  - Application Users

- Entry/Ingress:
  - Load Balancer [LB] receives traffic from all actors
  - External endpoints shown:
    - http://<myapp>.ocp.example.com
    - https://<myapp>.ocp.example.com:443

- Master Nodes (labeled 1):
  - Routers (handle incoming requests from LB)
  - 3× Master - Infra nodes (red)
  - Registry (container image registry)

- Application Nodes (labeled 2):
  - Multiple app nodes each running APP POD(s) (example POD C shown in each)
  - PVC Storage (persistent volumes represented by stacked disks)

- Relationships:
  - Actors → LB → Routers → Master/Infra
  - Application traffic routed to Application Nodes where pods run and use PVC storage

Figure 6-2 OpenShift Container Platform 3.11 6xNodes + Load Balancer

Chapter 6. Installing Red Hat OpenShift 3.11 on IBM PowerVC 105