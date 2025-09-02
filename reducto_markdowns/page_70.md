Draft Document for Review December 11, 2019 1:55 pm

8459ch06.fm

environment. The Master, Infrastructure and Compute Roles are deployed to a single node (Figure 6-1).

This diagram illustrates an OpenShift Container Platform 3.11 all-in-one deployment architecture where different user types (automation tools, cluster administrators, developers, and application owners) interact with the system through a web console and router. The platform contains various components including a registry, Jenkins, monitoring tools, and Kubernetes operators, all running on pods with persistent storage. Application users access their applications through the router, which handles traffic routing to the appropriate services within the OpenShift environment.

Figure 6-1 OpenShift Container Platform 3.11 all-in-one

Seven nodes deployment is highly available and suitable for production. The Master and Infrastructure Roles are deployed to three Nodes, the Computer Role is deployed to three Worker Nodes, and the Load Balancer is deployed to a single Node (Figure 6-2).

This diagram illustrates the OpenShift Container Platform 3.11 architecture with a 7-node deployment consisting of 6 nodes plus a load balancer. The left side shows Master Nodes (labeled as "1") containing three Master-Infra components, routers, registry, and a load balancer that handles traffic from various user types including automation tools, administrators, developers, application owners, and end users. The right side displays Application Nodes (labeled as "2") with three pods and PVC storage for running containerized applications.

Figure 6-2 OpenShift Container Platform 3.11 6xNodes + Load Balancer

Chapter 6. Installing Red Hat OpenShift 3.11 on IBM PowerVC 105

=