# OpenSearch – Complete Architecture, Components, Tools, Use Cases & Examples

## What is OpenSearch?

OpenSearch is an open-source distributed search, analytics, observability, and log management platform derived from Elasticsearch 7.10.

It is used for:

* Full-text search
* Log analytics
* Application monitoring
* Security analytics
* SIEM
* Observability dashboards
* AI-powered search

### Real Example

An e-commerce application stores millions of products.

Instead of querying Oracle/MySQL directly:

```text
Customer Search
      |
      v
OpenSearch
      |
      v
Results in milliseconds
```

Search:

```text
"Apple iPhone 15 Pro 256GB"
```

returns results in milliseconds using inverted indexes.

---

# Why OpenSearch?

Traditional databases are optimized for:

* Transactions (OLTP)
* ACID compliance

Search engines are optimized for:

* Text search
* Analytics
* Aggregations
* Real-time querying

OpenSearch provides:

* Fast searches
* Horizontal scaling
* Near real-time indexing
* Analytics dashboards

---

# OpenSearch Architecture

```text
Application
      |
REST API
      |
OpenSearch Cluster
      |
+----------------+
| Master Nodes   |
| Data Nodes     |
| Ingest Nodes   |
+----------------+
      |
Storage
      |
Dashboards
```

---

# Core Components

## 1. Cluster

A cluster is a group of OpenSearch nodes.

Example:

```text
Production Cluster

Node1
Node2
Node3
Node4
```

Benefits:

* High Availability
* Scalability
* Fault Tolerance

---

## 2. Node

A node is a single OpenSearch server instance.

Example:

```text
Node-1
CPU: 16 Core
RAM: 64GB
Storage: 1TB
```

Types:

* Master Node
* Data Node
* Ingest Node
* Coordinating Node

---

## 3. Index

Equivalent of a database table.

Example:

```text
products
orders
customers
logs
```

Example Index:

```json
{
  "productId":1001,
  "name":"Laptop",
  "price":50000
}
```

---

## 4. Document

Equivalent of a row.

Example:

```json
{
  "id":1,
  "name":"Rahul",
  "city":"Delhi"
}
```

Stored in JSON format.

---

## 5. Shards

OpenSearch divides data into shards.

Example:

```text
Orders Index
     |
+----+----+----+
Shard1
Shard2
Shard3
```

Benefits:

* Parallel search
* Horizontal scaling

---

## 6. Replicas

Copies of shards.

```text
Primary Shard
      |
Replica Shard
```

Benefits:

* High availability
* Faster reads

---

# Node Types

## Master Node

Responsible for:

* Cluster management
* Node discovery
* Shard allocation

Example:

```text
Master-1
Master-2
Master-3
```

Best practice:

Use 3 dedicated master nodes.

---

## Data Node

Stores:

* Documents
* Indexes
* Shards

Handles:

* Search requests
* Aggregations

---

## Ingest Node

Processes data before storage.

Example:

```text
Application Logs
       |
Ingest Pipeline
       |
OpenSearch
```

Can:

* Parse logs
* Mask PII
* Enrich data

---

## Coordinating Node

Acts like a load balancer.

Receives:

```text
Search Requests
```

Routes requests to data nodes.

---

# Data Flow

```text
Application
      |
REST API
      |
Ingest Node
      |
Data Node
      |
Index
```

---

# OpenSearch Query Flow

User searches:

```text
"Best laptop under 50000"
```

Flow:

```text
Dashboard
      |
Coordinator Node
      |
Relevant Shards
      |
Results Aggregated
      |
Response Returned
```

---

# OpenSearch Dashboards

Equivalent to Kibana.

OpenSearch Dashboards provides:

* Visualizations
* Monitoring
* Search UI
* Dashboards
* Alerting

Example Dashboard:

```text
API Errors
CPU Usage
Response Time
Transactions
```

---

# OpenSearch Inverted Index

Most important concept.

Instead of:

```text
Document → Words
```

Stores:

```text
Word → Documents
```

Example:

```text
Laptop -> Doc1, Doc5, Doc9
Apple -> Doc2, Doc3
```

Search becomes extremely fast.

---

# OpenSearch for Log Analytics

Application Log:

```json
{
 "service":"payment",
 "status":"ERROR",
 "message":"DB timeout"
}
```

Pipeline:

```text
Application
     |
Fluent Bit
     |
OpenSearch
     |
Dashboard
```

Search:

```text
status:ERROR
```

returns all error logs instantly.

---

# OpenSearch Observability Stack

```text
Applications
      |
OpenTelemetry
      |
Fluent Bit
      |
OpenSearch
      |
Dashboards
```

Collects:

### Metrics

```text
CPU
Memory
Latency
```

### Logs

```text
Application Logs
Audit Logs
```

### Traces

```text
Request Flow
```

---

# Security Analytics / SIEM

Security logs:

```text
Firewall
VPN
Cloud Audit
IAM
```

Flow:

```text
Security Logs
       |
OpenSearch
       |
Threat Detection
```

Use Cases:

* Failed logins
* Unauthorized access
* Brute force attacks

---

# OpenSearch Supporting Tools

## Fluent Bit

Fluent Bit

Collects logs from:

* Kubernetes
* Linux
* Containers

Example:

```text
Pod Logs
    |
Fluent Bit
    |
OpenSearch
```

---

## Fluentd

Fluentd

Enterprise-grade log routing.

```text
Application
     |
Fluentd
     |
OpenSearch
```

---

## Logstash

Logstash

Performs:

* Parsing
* Transformation
* Enrichment

```text
Logs
 |
Logstash
 |
OpenSearch
```

---

## OpenTelemetry

OpenTelemetry

Collects:

* Metrics
* Logs
* Traces

```text
Application
      |
OpenTelemetry
      |
OpenSearch
```

---

## Beats

Data shippers.

Examples:

* Filebeat
* Metricbeat
* Auditbeat

Flow:

```text
Linux Server
      |
Filebeat
      |
OpenSearch
```

---

# OpenSearch Security Features

Security Plugin provides:

### Authentication

* LDAP
* SAML
* OAuth2
* JWT

### Authorization

Role-Based Access Control (RBAC)

Example:

```text
Admin
Developer
Auditor
```

---

## Encryption

TLS:

```text
Client
  |
HTTPS
  |
OpenSearch
```

Protects data in transit.

---

# OpenSearch in Kubernetes

Architecture:

```text
Kubernetes
    |
Fluent Bit
    |
OpenSearch Cluster
    |
Dashboards
```

Monitors:

* Pods
* Nodes
* Containers
* APIs

---

# OpenSearch on OCI

Architecture:

```text
OKE Cluster
      |
Fluent Bit
      |
OpenSearch
      |
Dashboards
```

Integrated with:

* OCI Logging
* OCI Monitoring
* OCI Object Storage

Use Case:

Centralized logging for Oracle Fusion integrations and microservices.

---

# OpenSearch vs Elasticsearch

| Feature     | OpenSearch            | Elasticsearch            |
| ----------- | --------------------- | ------------------------ |
| License     | Apache 2.0            | Elastic License          |
| Open Source | Yes                   | Limited                  |
| Dashboards  | OpenSearch Dashboards | Kibana                   |
| Security    | Included              | Some features commercial |
| Cost        | Free                  | Commercial options       |

---

# Real Enterprise Example (Java + Spring Boot + Kubernetes)

### Problem

10 microservices running on Kubernetes.

Need:

* Centralized logs
* Searchable errors
* Dashboards
* Alerts

### Solution

```text
Spring Boot Apps
       |
OpenTelemetry
       |
Fluent Bit
       |
OpenSearch
       |
Dashboards
       |
Email/Slack Alerts
```

### Example Search

```text
service=payment AND status=ERROR
```

### Result

```text
DB Timeout
Kafka Connection Failed
JWT Validation Failed
```

---

# Interview Answer (2–3 Minutes)

"OpenSearch is a distributed search and analytics engine used for full-text search, log analytics, observability, and security monitoring. Its core components include clusters, nodes, indexes, documents, shards, and replicas. Data is typically ingested through tools like Fluent Bit, Fluentd, Logstash, or OpenTelemetry and visualized using OpenSearch Dashboards. In cloud-native environments such as Kubernetes, OCI, AWS, or Azure, OpenSearch is commonly used as a centralized logging and observability platform, enabling fast searches, real-time analytics, alerting, and root-cause analysis across microservices and distributed systems."


============


# Logging Levels Explained (log.info, log.debug, log.error, log.warn, etc.)

Logging is one of the most important parts of Monitoring, Observability, OpenSearch, Splunk, ELK, Grafana, and Production Support.

A well-designed logging strategy helps developers and support teams quickly identify issues, troubleshoot incidents, and perform root cause analysis.

---

# Standard Logging Levels

Most Java frameworks such as Log4j, Logback, and SLF4J support the following levels:

```text
TRACE
DEBUG
INFO
WARN
ERROR
FATAL
```

Priority Order:

```text
TRACE
 ↓
DEBUG
 ↓
INFO
 ↓
WARN
 ↓
ERROR
 ↓
FATAL
```

---

# 1. TRACE

Most detailed level.

Used for:

* Method entry/exit
* Variable values
* Loop execution
* Deep troubleshooting

Example:

```java
log.trace("Entering calculateTax()");
log.trace("Tax Amount = {}", tax);
```

Output:

```text
Entering calculateTax()
Tax Amount = 1500
```

### Use Case

Debugging complex business logic.

Example:

```text
ERP Tax Calculation
Invoice Processing
AI Prompt Execution
```

Usually disabled in production.

---

# 2. DEBUG

Developer-focused information.

Used for:

* API request payloads
* SQL execution
* Kafka messages
* Service calls

Example:

```java
log.debug("Customer Request = {}", request);
```

Output:

```json
{
 "customerId":1001,
 "name":"Rahul"
}
```

### Use Case

Spring Boot microservice troubleshooting.

```java
log.debug("Calling Inventory Service");
```

---

# 3. INFO

Most commonly used level.

Captures business events and normal operations.

Example:

```java
log.info("Order Created Successfully");
```

Output:

```text
Order Created Successfully
```

### Use Cases

* User Login
* Order Created
* Payment Completed
* Kafka Message Consumed

Example:

```java
log.info("Payment completed for Order {}", orderId);
```

---

# 4. WARN

Unexpected but recoverable situations.

System continues to work.

Example:

```java
log.warn("Retrying database connection");
```

Output:

```text
Database connection unavailable.
Retry attempt 1 of 3
```

### Use Cases

* Slow API response
* High memory usage
* Retry mechanism activated
* Deprecated API used

Example:

```java
log.warn("Response time exceeded threshold");
```

---

# 5. ERROR

A failure occurred.

Current transaction failed.

Example:

```java
log.error("Payment processing failed");
```

Output:

```text
Payment processing failed
```

### Use Cases

* Database timeout
* Kafka failure
* API failure
* Authentication failure

Example:

```java
try {
   paymentService.process();
}
catch(Exception e){
   log.error("Payment failed", e);
}
```

---

# 6. FATAL

Critical system failure.

Application may stop functioning.

Example:

```java
log.fatal("Database unavailable. Application shutting down.");
```

### Use Cases

* Application startup failure
* JVM crash
* Database unavailable
* Security breach

Note:

Many modern frameworks treat FATAL as ERROR.

---

# Real Enterprise Example

## User Places Order

```java
log.info("Order received");
log.debug("Order Request={}");
log.info("Inventory validation started");
log.warn("Inventory service response delayed");
log.error("Payment gateway timeout");
```

Output:

```text
INFO  Order received
DEBUG Order Request={...}
INFO  Inventory validation started
WARN  Inventory response delayed
ERROR Payment gateway timeout
```

---

# Logging in Spring Boot

```java
@RestController
public class OrderController {

   private static final Logger log =
       LoggerFactory.getLogger(OrderController.class);

   @PostMapping("/order")
   public String createOrder() {

       log.info("Order creation started");

       try {
           log.debug("Calling inventory service");

           return "Success";

       } catch(Exception ex) {

           log.error("Order creation failed", ex);

           throw ex;
       }
   }
}
```

---

# Structured Logging (Recommended)

Instead of:

```java
log.info("User Rahul logged in");
```

Use:

```java
log.info(
"User Login userId={} source={}",
userId,
source
);
```

Output:

```json
{
 "event":"User Login",
 "userId":"1001",
 "source":"Mobile"
}
```

Benefits:

* OpenSearch searchable
* Splunk searchable
* Easy dashboards

---

# Components in Enterprise Logging Architecture

```text
Application
     |
     v
SLF4J
     |
Logback / Log4j2
     |
Log File
     |
Fluent Bit
     |
OpenSearch
     |
Dashboard
```

---

# Important Logging Components

## SLF4J

(Simple Logging Facade for Java)

Acts as abstraction layer.

```java
Logger log = LoggerFactory.getLogger(MyClass.class);
```

Benefits:

* Switch Log4j/Logback easily
* Standard API

---

## Logback

Default Spring Boot logging framework.

Features:

* High performance
* Rolling files
* Async logging

---

## Log4j2

Enterprise logging framework.

Features:

* Async logging
* JSON logging
* High throughput

Example:

```xml
<Root level="INFO">
```

---

# Log Collection Tools

## Fluent Bit

Collects logs from:

* Kubernetes
* Docker
* Linux

```text
Pod Logs
   |
Fluent Bit
   |
OpenSearch
```

---

## Fluentd

Enterprise log aggregation.

```text
Applications
      |
Fluentd
      |
OpenSearch
```

---

## Logstash

Transforms logs.

Example:

```text
Application Logs
      |
Logstash
      |
OpenSearch
```

Can:

* Parse JSON
* Remove sensitive data
* Enrich logs

---

# Log Storage Tools

### OpenSearch

Stores:

* Application Logs
* Kubernetes Logs
* Audit Logs

Example Query:

```text
service=payment
AND level=ERROR
```

---

### Splunk

Enterprise log analytics.

Search:

```spl
index=prod level=ERROR
```

---

# Observability Integration

```text
Application
     |
     +---- Logs
     +---- Metrics
     +---- Traces
     |
OpenTelemetry
     |
OpenSearch / Splunk
     |
Grafana Dashboards
```

---

# What Should Be Logged?

## INFO

```java
User Login
Order Created
Payment Success
Kafka Message Processed
```

## WARN

```java
Retry Started
Memory High
API Slow
```

## ERROR

```java
Database Failure
Authentication Failure
API Failure
```

## DEBUG

```java
SQL Query
Request Payload
Response Payload
```

## TRACE

```java
Method Entry
Method Exit
Variable Values
```

---

# Logging Best Practices

### Always Log

* Correlation ID
* Request ID
* User ID (masked if needed)
* Transaction ID

Example:

```java
log.info(
"Order Created orderId={} correlationId={}",
orderId,
correlationId
);
```

### Never Log

❌ Passwords

❌ Credit Card Numbers

❌ OTPs

❌ Secret Keys

❌ JWT Tokens

---

# Interview Answer (2–3 Minutes)

"Enterprise applications use multiple logging levels such as TRACE, DEBUG, INFO, WARN, ERROR, and FATAL. TRACE and DEBUG are mainly for development and troubleshooting, INFO captures business events, WARN indicates recoverable issues, and ERROR/FATAL represent failures. In Java applications, SLF4J acts as the logging facade while Logback or Log4j2 provide the implementation. Logs are collected using Fluent Bit, Fluentd, or Logstash, stored in OpenSearch or Splunk, and visualized through dashboards. Structured logging with correlation IDs enables effective monitoring, observability, and root-cause analysis in distributed microservices environments."
