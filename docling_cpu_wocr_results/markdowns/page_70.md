Automation

Cluster

CV/CD Tools

Automation

Cluster

Web Console :8443

Load Balancer [LB]

/ https://ocp.example.com:8443

Routers

Master - Infra

POD

POD.

POD

Master - Infra

POD

POD

POD

Registry

Master Nodes

PODS

PVC Storage

Master - Infra

Application

Aplication

Application

Figure 6-1   OpenShift Container Platform 3.11 all-in-one

<!-- image -->

- /SM590000 Seven nodes deployment is highly available and suitable for production. The Master and Infrastructure Roles are deployed to three Nodes, the Computer Role is deployed to three Worker Nodes, and the Load Balancer is deployed to a single Node (Figure 6-2).

Figure 6-2   OpenShift Container Platform 3.11 6xNodes + Load Balancer

<!-- image -->

http:/&lt;myapp&gt;.ocp.example.com https:/&lt;myapp&gt;.ocp.example.com:443