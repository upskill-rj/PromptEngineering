# System Design Components, Tools, Examples & Use Cases (Interview Notes)

## 1. System Design

### Purpose

System Design is the process of designing scalable, secure, reliable, and maintainable software systems that meet business requirements.

### Example

Designing an E-Commerce platform handling 10 million users and 100,000 transactions per minute.

### Focus Areas

* Scalability
* Reliability
* Security
* Performance
* Maintainability

---

# 2. Load Balancer

### Purpose

Distributes incoming traffic across multiple servers to prevent overload and improve availability.

### Tools

* [NGINX](https://nginx.org?utm_source=chatgpt.com)
* [HAProxy](https://www.haproxy.org?utm_source=chatgpt.com)
* [AWS Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/?utm_source=chatgpt.com)

### Example

```text
10000 Users
     |
Load Balancer
  /      \
App1    App2
```

### Use Case

Banking, ERP, E-commerce, Payment Systems.

---

# 3. API Gateway

### Purpose

Single entry point for all APIs.

### Responsibilities

* Authentication
* Authorization
* Routing
* Rate Limiting
* Logging

### Tools

* [Kong Gateway](https://konghq.com?utm_source=chatgpt.com)
* [Apigee](https://cloud.google.com/apigee?utm_source=chatgpt.com)
* [Spring Cloud Gateway](https://spring.io/projects/spring-cloud-gateway?utm_source=chatgpt.com)

### Example

```text
Client
   |
API Gateway
   |
Microservices
```

### Use Case

Microservices architecture.

---

# 4. Caching

### Purpose

Store frequently accessed data in memory to reduce database load.

### Tools

* Redis
* Memcached
* Hazelcast

### Example

```text
User
 |
Redis Cache
 |
Database
```

### Use Case

Product catalog, user profiles, sessions.

---

# 5. Multi-Level Caching

### Purpose

Use multiple cache layers to improve performance.

### Levels

```text
Browser Cache
      ↓
CDN Cache
      ↓
Application Cache
      ↓
Redis Cache
      ↓
Database
```

### Example

Amazon product details.

### Benefit

Reduces latency and database load.

---

# 6. CDN (Content Delivery Network)

### Purpose

Store static content closer to users.

### Tools

* [Cloudflare](https://www.cloudflare.com?utm_source=chatgpt.com)
* [Amazon CloudFront](https://aws.amazon.com/cloudfront/?utm_source=chatgpt.com)
* [Akamai](https://www.akamai.com?utm_source=chatgpt.com)

### Example

```text
India User
      |
Nearest CDN Node
      |
Image
```

### Use Case

Images, CSS, JS, Videos.

---

# 7. Rate Limiting

### Purpose

Limit the number of requests allowed in a time window.

### Example

```text
100 Requests / Minute
```

101st request is rejected.

### Tools

* Kong
* NGINX
* API Gateway

### Use Case

Prevent API abuse.

---

# 8. Throttling

### Purpose

Control request processing speed rather than completely blocking requests.

### Example

```text
Allowed:
10 Requests / Second
```

Extra requests are delayed.

### Use Case

Third-party integrations.

---

# 9. Clustering

### Purpose

Multiple servers work together as a single system.

### Example

```text
Node1
Node2
Node3
```

### Tools

* Kubernetes
* WebLogic Cluster
* Oracle RAC

### Use Case

High availability and scalability.

---

# 10. Bastion Host

### Purpose

Secure jump server to access private infrastructure.

### Example

```text
Admin
  |
Bastion Host
  |
Private Server
```

### Use Case

OCI, AWS, GCP Production Systems.

---

# 11. Reverse Proxy

### Purpose

Receives requests and forwards them to backend servers.

### Tools

* [NGINX](https://nginx.org?utm_source=chatgpt.com)
* [HAProxy](https://www.haproxy.org?utm_source=chatgpt.com)

### Example

```text
Internet
   |
Reverse Proxy
   |
App Servers
```

### Use Case

Load balancing and SSL termination.

---

# 12. Database

### Purpose

Persistent data storage.

### Tools

Relational:

* Oracle DB
* PostgreSQL
* MySQL

NoSQL:

* MongoDB
* Cassandra

### Use Case

Customer, Orders, Payments.

---

# 13. Message Queue

### Purpose

Asynchronous communication between services.

### Tools

* Apache Kafka
* RabbitMQ
* ActiveMQ

### Example

```text
Order Service
      |
Kafka
      |
Payment Service
```

### Use Case

Event-driven architecture.

---

# 14. Microservices

### Purpose

Break application into independent business services.

### Example

```text
User Service
Order Service
Payment Service
```

### Tools

* Java Spring Boot
* NodeJS
* Kubernetes

### Use Case

Large enterprise systems.

---

# 15. Docker

### Purpose

Package application and dependencies together.

### Example

```text
Docker
 |
Java App
 |
JDK
```

### Use Case

Portable deployments.

---

# 16. Kubernetes

### Purpose

Manage and orchestrate containers.

### Features

* Auto Scaling
* Self Healing
* Rolling Updates

### Use Case

Cloud-native applications.

---

# 17. Service Discovery

### Purpose

Automatically locate services.

### Tools

* Eureka
* Consul
* Kubernetes DNS

### Example

```text
Order Service
     |
Find Payment Service
```

### Use Case

Microservices.

---

# 18. Reliability

### Purpose

Ensure system continues working despite failures.

### Techniques

* Replication
* Failover
* Redundancy
* Auto Recovery

### Example

```text
Primary DB
    |
Replica DB
```

### Use Case

Banking systems.

---

# 19. Availability

### Purpose

Percentage of time system remains operational.

### Example

```text
99.99%
```

Maximum downtime ≈ 52 minutes/year.

### Use Case

Online banking, payments.

---

# 20. Scalability

### Purpose

Handle increasing traffic without performance degradation.

### Types

Vertical Scaling

```text
More CPU/RAM
```

Horizontal Scaling

```text
Add More Servers
```

### Use Case

Amazon Sale Events.

---

# 21. Maintainability

### Purpose

Ease of modifying, debugging, and enhancing systems.

### Practices

* Clean Code
* Modular Design
* Documentation
* Automated Testing

### Example

Adding a new Payment Service without impacting Order Service.

---

# 22. Observability

### Purpose

Understand internal system behavior.

### Components

* Logs
* Metrics
* Traces

### Use Case

Production troubleshooting.

---

# 23. Monitoring

### Purpose

Track health and performance.

### Tools

* [Prometheus](https://prometheus.io?utm_source=chatgpt.com)
* [Grafana](https://grafana.com?utm_source=chatgpt.com)

### Metrics

* CPU
* Memory
* TPS
* Latency

---

# 24. Logging

### Purpose

Record application events.

### Example

```java
log.info()
log.debug()
log.warn()
log.error()
```

### Tools

* Splunk
* OpenSearch
* ELK

---

# 25. Distributed Tracing

### Purpose

Track requests across multiple services.

### Tools

* [Jaeger](https://www.jaegertracing.io?utm_source=chatgpt.com)
* [OpenTelemetry](https://opentelemetry.io?utm_source=chatgpt.com)

### Example

```text
User
 |
API Gateway
 |
Order Service
 |
Payment Service
```

---

# 26. High Availability (HA)

### Purpose

Eliminate single points of failure.

### Example

```text
LB
 |
App1
App2
```

### Use Case

24×7 Production Systems.

---

# 27. Disaster Recovery (DR)

### Purpose

Recover from major outages.

### Techniques

* Cross Region Replication
* Backup
* Standby Environment

### Example

```text
Delhi DC
     |
Mumbai DR Site
```

### Use Case

Financial Institutions.

---

# 28. Security

### Purpose

Protect systems and data.

### Components

* OAuth2
* JWT
* TLS
* WAF
* VPN

### Use Case

Secure APIs and applications.

---

# 29. CI/CD

### Purpose

Automate build, test, and deployment.

### Tools

* Jenkins
* GitHub Actions
* Bamboo

### Example

```text
Code
 ↓
Build
 ↓
Test
 ↓
Deploy
```

### Use Case

Faster releases.

---

# End-to-End Enterprise Architecture

```text
Users
  |
CDN
  |
Load Balancer
  |
API Gateway
  |
Rate Limiting / Throttling
  |
Microservices
  |
Redis Cache
  |
Kafka
  |
Oracle DB Cluster
  |
Object Storage

Monitoring
Logging
Tracing
Security
CI/CD
Kubernetes
```

### Real-World Use Cases

* Banking Systems
* ERP Integrations
* Oracle Fusion Applications
* E-Commerce Platforms
* Payment Gateways
* OTT Streaming Platforms
* AI/GenAI Enterprise Applications
* OCI / AWS / GCP Cloud Architectures

These are the core topics expected from a Senior Software Engineer, Lead Engineer, Solution Architect, Technical Architect, Cloud Architect, or Enterprise Architect during system design interviews.
