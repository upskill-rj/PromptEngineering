# Cloud Cheat Sheet for Interview (OCI, AWS, Azure, GCP)

# 1. Compute Services

| OCI              | AWS | Azure           | GCP            | Interview Explanation                                                                                                  |
| ---------------- | --- | --------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Compute Instance | EC2 | Virtual Machine | Compute Engine | Virtual servers used to host applications, APIs, and enterprise workloads with autoscaling and load balancing support. |

---

# 2. Kubernetes / Container Services

| OCI | AWS | Azure | GCP | Explanation                                                                                                               |
| --- | --- | ----- | --- | ------------------------------------------------------------------------------------------------------------------------- |
| OKE | EKS | AKS   | GKE | Managed Kubernetes services used for deploying containerized microservices with auto-healing, scaling, and orchestration. |

---

# 3. Serverless Services

| OCI           | AWS    | Azure           | GCP             | Explanation                                                                                 |
| ------------- | ------ | --------------- | --------------- | ------------------------------------------------------------------------------------------- |
| OCI Functions | Lambda | Azure Functions | Cloud Functions | Event-driven serverless compute services that execute code without managing infrastructure. |

---

# 4. Object Storage

| OCI            | AWS | Azure        | GCP           | Explanation                                                                                |
| -------------- | --- | ------------ | ------------- | ------------------------------------------------------------------------------------------ |
| Object Storage | S3  | Blob Storage | Cloud Storage | Scalable storage services used for backups, images, logs, AI datasets, and static content. |

---

# 5. Block Storage

| OCI          | AWS | Azure        | GCP             | Explanation                                                                                 |
| ------------ | --- | ------------ | --------------- | ------------------------------------------------------------------------------------------- |
| Block Volume | EBS | Managed Disk | Persistent Disk | High-performance storage volumes attached to VMs for databases and enterprise applications. |

---

# 6. Relational Database

| OCI                       | AWS | Azure     | GCP       | Explanation                                                                                   |
| ------------------------- | --- | --------- | --------- | --------------------------------------------------------------------------------------------- |
| Autonomous DB / Oracle DB | RDS | Azure SQL | Cloud SQL | Managed relational database services supporting automated backups, scaling, patching, and HA. |

---

# 7. NoSQL Database

| OCI       | AWS      | Azure     | GCP                  | Explanation                                                                                   |
| --------- | -------- | --------- | -------------------- | --------------------------------------------------------------------------------------------- |
| OCI NoSQL | DynamoDB | Cosmos DB | Firestore / Bigtable | Distributed NoSQL databases designed for low latency, high scalability, and flexible schemas. |

---

# 8. Networking

| OCI | AWS | Azure | GCP | Explanation                                                                                  |
| --- | --- | ----- | --- | -------------------------------------------------------------------------------------------- |
| VCN | VPC | VNet  | VPC | Virtual private network environments providing subnetting, routing, firewall, and isolation. |

---

# 9. Load Balancer

| OCI               | AWS     | Azure               | GCP                  | Explanation                                                                          |
| ----------------- | ------- | ------------------- | -------------------- | ------------------------------------------------------------------------------------ |
| OCI Load Balancer | ELB/ALB | Azure Load Balancer | Cloud Load Balancing | Distributes traffic across servers/services to improve scalability and availability. |

---

# 10. API Management

| OCI         | AWS         | Azure          | GCP         | Explanation                                                                    |
| ----------- | ----------- | -------------- | ----------- | ------------------------------------------------------------------------------ |
| API Gateway | API Gateway | API Management | API Gateway | Secures, manages, throttles, and monitors REST APIs and microservices traffic. |

---

# 11. Identity & Access Management

| OCI     | AWS     | Azure               | GCP       | Explanation                                                                              |
| ------- | ------- | ------------------- | --------- | ---------------------------------------------------------------------------------------- |
| OCI IAM | AWS IAM | Azure AD / Entra ID | Cloud IAM | Provides authentication, authorization, RBAC, policies, and secure cloud access control. |

---

# 12. Secrets & Key Management

| OCI       | AWS                   | Azure     | GCP                  | Explanation                                                           |
| --------- | --------------------- | --------- | -------------------- | --------------------------------------------------------------------- |
| OCI Vault | Secrets Manager / KMS | Key Vault | Secret Manager / KMS | Securely stores secrets, certificates, API keys, and encryption keys. |

---

# 13. Monitoring & Logging

| OCI                      | AWS        | Azure         | GCP              | Explanation                                                             |
| ------------------------ | ---------- | ------------- | ---------------- | ----------------------------------------------------------------------- |
| OCI Monitoring / Logging | CloudWatch | Azure Monitor | Cloud Monitoring | Used for metrics, logs, alerts, dashboards, tracing, and observability. |

---

# 14. Application Performance Monitoring

| OCI     | AWS   | Azure                | GCP         | Explanation                                                                          |
| ------- | ----- | -------------------- | ----------- | ------------------------------------------------------------------------------------ |
| OCI APM | X-Ray | Application Insights | Cloud Trace | Helps monitor application performance, distributed tracing, and bottleneck analysis. |

---

# 15. Messaging & Streaming

| OCI           | AWS               | Azure                   | GCP     | Explanation                                                                     |
| ------------- | ----------------- | ----------------------- | ------- | ------------------------------------------------------------------------------- |
| OCI Streaming | Kafka / SQS / SNS | Event Hub / Service Bus | Pub/Sub | Enables asynchronous communication and event-driven microservices architecture. |

---

# 16. DevOps / CI-CD

| OCI        | AWS          | Azure        | GCP         | Explanation                                                                |
| ---------- | ------------ | ------------ | ----------- | -------------------------------------------------------------------------- |
| OCI DevOps | CodePipeline | Azure DevOps | Cloud Build | Automates build, test, deployment, and release pipelines for applications. |

---

# 17. Infrastructure as Code (IaC)

| OCI              | AWS            | Azure     | GCP                | Explanation                                                                             |
| ---------------- | -------------- | --------- | ------------------ | --------------------------------------------------------------------------------------- |
| Resource Manager | CloudFormation | ARM/Bicep | Deployment Manager | Automates infrastructure provisioning using code templates and reusable configurations. |

---

# 18. DNS & Traffic Management

| OCI     | AWS     | Azure     | GCP       | Explanation                                                             |
| ------- | ------- | --------- | --------- | ----------------------------------------------------------------------- |
| OCI DNS | Route53 | Azure DNS | Cloud DNS | Manages domain routing, traffic policies, failover, and DNS resolution. |

---

# 19. CDN (Content Delivery Network)

| OCI     | AWS        | Azure     | GCP       | Explanation                                                                |
| ------- | ---------- | --------- | --------- | -------------------------------------------------------------------------- |
| OCI CDN | CloudFront | Azure CDN | Cloud CDN | Delivers static and dynamic content globally with low latency and caching. |

---

# 20. Security Services

| OCI              | AWS            | Azure              | GCP                     | Explanation                                                                                        |
| ---------------- | -------------- | ------------------ | ----------------------- | -------------------------------------------------------------------------------------------------- |
| WAF, Cloud Guard | WAF, GuardDuty | Defender for Cloud | Security Command Center | Provides threat detection, compliance, firewall protection, and cloud security posture management. |

---

# 21. AI / ML Services

| OCI             | AWS       | Azure       | GCP       | Explanation                                                                             |
| --------------- | --------- | ----------- | --------- | --------------------------------------------------------------------------------------- |
| OCI AI Services | SageMaker | Azure AI/ML | Vertex AI | Managed AI/ML platforms for model training, deployment, NLP, vision, and generative AI. |

---

# 22. Data Engineering / Analytics

| OCI           | AWS        | Azure   | GCP                 | Explanation                                                                              |
| ------------- | ---------- | ------- | ------------------- | ---------------------------------------------------------------------------------------- |
| OCI Data Flow | EMR / Glue | Synapse | Dataproc / Dataflow | Big data and analytics services used for ETL, Spark, Hadoop, and large-scale processing. |

---

# 23. Data Warehouse

| OCI                       | AWS      | Azure             | GCP      | Explanation                                                                             |
| ------------------------- | -------- | ----------------- | -------- | --------------------------------------------------------------------------------------- |
| Autonomous Data Warehouse | Redshift | Synapse Analytics | BigQuery | Cloud-native analytical databases optimized for BI, reporting, and analytics workloads. |

---

# 24. Hybrid / Multi-Cloud

| OCI              | AWS      | Azure     | GCP    | Explanation                                                                      |
| ---------------- | -------- | --------- | ------ | -------------------------------------------------------------------------------- |
| OCI Interconnect | Outposts | Azure Arc | Anthos | Enables hybrid cloud and multi-cloud infrastructure management and connectivity. |

---

# 25. Interview Closing Summary

“OCI, AWS, Azure, and GCP provide similar cloud capabilities across compute, storage, networking, databases, DevOps, security, monitoring, AI/ML, and Kubernetes. The main difference is naming and ecosystem integration, while the core architecture principles like scalability, security, automation, observability, and high availability remain similar across all cloud platforms.”
