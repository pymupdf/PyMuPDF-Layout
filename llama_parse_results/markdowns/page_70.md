

Draft Document for Review December 11, 2019 1:55 pm                                                    8459ch06.fm

environment. The Master, Infrastructure and Compute Roles are deployed to a single node (Figure 6-1).

| User Types                                                                              | Access Points                                       | Components                                                            | External Access                                                                                                        |
| --------------------------------------------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Automation CI/CD Tools<br/>Cluster Administrators<br/>Developers<br/>Application Owners | Web Console :8443<br/>https\://ocp.example.com:8443 | REGISTRY<br/>Jenkins<br/>S2I<br/>Prometheus<br/>K8s Operators<br/>OLM | Router :80 & :443<br/>Application Users<br/>http\://\<myapp>.ocp.example.com<br/>https\://\<myapp>.ocp.example.com:443 |
| PODs<br/>POD POD<br/>POD POD                                                            |                                                     | PVC Storage                                                           |                                                                                                                        |


*Figure 6-1 OpenShift Container Platform 3.11 all-in-one*

► **Seven nodes deployment** is highly available and suitable for production. The Master and Infrastructure Roles are deployed to three Nodes, the Computer Role is deployed to three Worker Nodes, and the Load Balancer is deployed to a single Node (Figure 6-2).

| User Types                                                                              | Load Balancer                   | Master Nodes                                                      | Application Nodes                               | External Access                                                                                  |
| --------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Automation CI/CD Tools<br/>Cluster Administrators<br/>Developers<br/>Application Owners | Load Balancer \[LB]<br/>Routers | Master - Infra<br/>Master - Infra<br/>Master - Infra<br/>Registry | APP POD<br/>APP POD<br/>APP POD<br/>PVC Storage | Application Users<br/>http\://\<myapp>.ocp.example.com<br/>https\://\<myapp>.ocp.example.com:443 |


*Figure 6-2 OpenShift Container Platform 3.11 6xNodes + Load Balancer*

Chapter 6. Installing Red Hat OpenShift 3.11 on IBM PowerVC   105
