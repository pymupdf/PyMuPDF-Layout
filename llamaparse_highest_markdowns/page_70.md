

Draft Document for Review December 11, 2019 1:55 pm    8459ch06.fm

environment. The Master, Infrastructure and Compute Roles are deployed to a single node (Figure 6-1).

```mermaid
graph TD
    A[Automation CI/CD Tools] --> E[Web Console :8443<br/>https://ocp.example.com:8443]
    B[Cluster Administrators] --> E
    C[Developers] --> E
    D[Application Owners] --> E
    
    E --> F[Router :80 & :443]
    F --> G[Application Users<br/>http://myapp.ocp.example.com<br/>https://myapp.ocp.example.com:443]
    
    E --> H[PODs]
    E --> I[PVC Storage]
    
    E --> J[REGISTRY<br/>Jenkins<br/>S2I<br/>Prometheus<br/>K8s Operators<br/>OLM]
```

**Figure 6-1** OpenShift Container Platform 3.11 all-in-one

▶ **Seven nodes deployment** is highly available and suitable for production. The Master and Infrastructure Roles are deployed to three Nodes, the Computer Role is deployed to three Worker Nodes, and the Load Balancer is deployed to a single Node (Figure 6-2).

```mermaid
graph TD
    A[Automation CI/CD Tools] --> LB[Load Balancer LB]
    B[Cluster Administrators] --> LB
    C[Developers] --> LB
    D[Application Owners] --> LB
    E[Application Users] --> LB
    
    LB --> R[Routers]
    R --> M1[Master - Infra]
    R --> M2[Master - Infra] 
    R --> M3[Master - Infra]
    
    M1 --> REG[Registry]
    M2 --> REG
    M3 --> REG
    
    LB --> AN[Application Nodes]
    AN --> APP1[APP POD]
    AN --> APP2[APP POD]
    AN --> APP3[APP POD]
    AN --> PVC[PVC Storage]
    
    E --> AU[http://myapp.ocp.example.com<br/>https://myapp.ocp.example.com:443]
    
    subgraph "Master Nodes"
        M1
        M2
        M3
        REG
    end
    
    subgraph "Application Nodes"
        APP1
        APP2
        APP3
        PVC
    end
```

**Figure 6-2** OpenShift Container Platform 3.11 6xNodes + Load Balancer

Chapter 6. Installing Red Hat OpenShift 3.11 on IBM PowerVC   105
