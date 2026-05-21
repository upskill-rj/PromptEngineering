# NoSQL Overview

**NoSQL (Not Only SQL)** databases are non-relational databases designed for:

* High scalability
* Distributed systems
* Flexible schema
* Large-scale real-time applications
* Big data & AI workloads

Unlike traditional relational databases, NoSQL databases do not always use tables and fixed schemas.

---

# 🔷 Why NoSQL?

Traditional RDBMS works well for:

* Banking
* ERP
* Financial systems

But modern applications require:

* Massive scalability
* Flexible data models
* Real-time processing
* Global distribution

NoSQL solves these challenges.

---

# 🔷 NoSQL Architecture

```text id="3x0oif"
Application
    ↓
API / Microservices
    ↓
NoSQL Database Cluster
    ↓
Distributed Storage Nodes
```

---

# 🔷 Core Components of NoSQL

| Component           | Purpose                     |
| ------------------- | --------------------------- |
| Collections/Buckets | Store documents/data        |
| Sharding            | Horizontal scaling          |
| Replication         | High availability           |
| Partitioning        | Data distribution           |
| Indexing            | Faster queries              |
| Query Engine        | Data retrieval              |
| Cache Layer         | Improve performance         |
| Distributed Nodes   | Scale across servers        |
| Event Streaming     | Real-time updates           |
| Security            | Authentication & encryption |

---

# 🔷 Types of NoSQL Databases

| Type             | Example   | Best Use Case     |
| ---------------- | --------- | ----------------- |
| Document DB      | MongoDB   | Dynamic JSON data |
| Key-Value DB     | Redis     | Caching           |
| Column-Family DB | Cassandra | Big data          |
| Graph DB         | Neo4j     | Relationships     |
| Time-Series DB   | InfluxDB  | IoT metrics       |
| Vector DB        | Pinecone  | AI embeddings     |

---

# 1. Document Database

Stores data in JSON/BSON documents.

---

## 🔹 Examples

* MongoDB
* Couchbase

---

## 🔹 Document Example

```json id="l3l0ae"
{
  "employeeId": 101,
  "name": "Rahul",
  "skills": ["Java", "Spring Boot"],
  "address": {
    "city": "Delhi"
  }
}
```

---

## 🔹 Components

| Component   | Purpose            |
| ----------- | ------------------ |
| Collection  | Group of documents |
| Document    | JSON record        |
| BSON        | Binary JSON        |
| Indexes     | Query optimization |
| Replica Set | High availability  |
| Shards      | Horizontal scaling |

---

## 🔹 Use Cases

| Use Case           | Why Document DB?    |
| ------------------ | ------------------- |
| E-commerce catalog | Flexible schema     |
| CMS systems        | Dynamic content     |
| AI chat apps       | JSON conversations  |
| User profiles      | Variable attributes |

---

## 🔹 Advantages

* Flexible schema
* Easy JSON integration
* High scalability
* Fast development

---

# 2. Key-Value Database

Stores data as:

```text id="l21j64"
Key → Value
```

---

## 🔹 Examples

* Redis
* Amazon DynamoDB

---

## 🔹 Example

```text id="s3x0hv"
SESSION_101 → User session data
```

---

## 🔹 Components

| Component         | Purpose           |
| ----------------- | ----------------- |
| Key               | Unique identifier |
| Value             | Data              |
| In-memory storage | Ultra-fast access |
| Expiration TTL    | Auto removal      |
| Replication       | HA                |

---

## 🔹 Use Cases

| Use Case            | Example             |
| ------------------- | ------------------- |
| Caching             | API responses       |
| Session management  | Login sessions      |
| Gaming leaderboards | Real-time scores    |
| Shopping carts      | Temporary cart data |

---

## 🔹 Advantages

* Extremely fast
* Simple architecture
* Real-time processing

---

# 3. Column-Family Database

Stores data by columns instead of rows.

Optimized for:

* Large datasets
* Analytics
* Distributed systems

---

## 🔹 Examples

* Apache Cassandra
* Apache HBase

---

## 🔹 Architecture

```text id="a6a6xk"
Row Key
   ↓
Column Families
   ↓
Columns
```

---

## 🔹 Components

| Component     | Purpose             |
| ------------- | ------------------- |
| Column Family | Related columns     |
| Partition Key | Data distribution   |
| Cluster Nodes | Distributed storage |
| Replication   | Availability        |
| SSTables      | Persistent storage  |

---

## 🔹 Use Cases

| Use Case             | Why Cassandra?      |
| -------------------- | ------------------- |
| IoT systems          | Massive writes      |
| Telecom billing      | Scalability         |
| Log analytics        | Distributed storage |
| Real-time monitoring | High throughput     |

---

## 🔹 Advantages

* Massive scalability
* Fault tolerance
* High write performance

---

# 4. Graph Database

Stores relationships between entities.

---

## 🔹 Examples

* Neo4j
* Amazon Neptune

---

## 🔹 Components

| Component       | Purpose              |
| --------------- | -------------------- |
| Nodes           | Entities             |
| Edges           | Relationships        |
| Properties      | Attributes           |
| Graph Traversal | Relationship queries |

---

## 🔹 Example

```text id="g1uvp9"
Rahul → FRIEND → Amit
```

---

## 🔹 Use Cases

| Use Case              | Why Graph DB?          |
| --------------------- | ---------------------- |
| Social networks       | Relationships          |
| Fraud detection       | Connection analysis    |
| Recommendation engine | Linked preferences     |
| Network topology      | Infrastructure mapping |

---

# 5. Time-Series Database

Optimized for timestamp-based data.

---

## 🔹 Examples

* InfluxDB
* TimescaleDB

---

## 🔹 Use Cases

| Use Case     | Example             |
| ------------ | ------------------- |
| IoT sensors  | Temperature metrics |
| Monitoring   | CPU usage           |
| DevOps       | Logs & metrics      |
| Stock market | Price history       |

---

# 6. Vector Database (AI Important)

Stores vector embeddings for semantic search.

---

## 🔹 Examples

* Pinecone
* FAISS
* Weaviate

---

## 🔹 AI Architecture

```text id="4j2dms"
Text
 ↓
Embedding Model
 ↓
Vector Database
 ↓
Similarity Search
 ↓
LLM Response
```

---

## 🔹 Use Cases

| AI Use Case            | Description         |
| ---------------------- | ------------------- |
| RAG systems            | Semantic search     |
| Chatbots               | Context retrieval   |
| Recommendation systems | Similarity matching |
| Image search           | Vector comparison   |

---

# 🔷 CAP Theorem in NoSQL

Distributed systems choose between:

| Term                | Meaning                   |
| ------------------- | ------------------------- |
| Consistency         | Same data everywhere      |
| Availability        | Always responds           |
| Partition Tolerance | Survives network failures |

---

## 🔹 Examples

| Database  | Focus |
| --------- | ----- |
| MongoDB   | CP    |
| Cassandra | AP    |
| Redis     | CA/AP |

---

# 🔷 NoSQL Scaling Concepts

# Horizontal Scaling

```text id="74xhmw"
Server1
Server2
Server3
```

Add more servers instead of bigger hardware.

---

# Sharding

Distribute data across nodes.

---

# Replication

Copies data to multiple servers.

Benefits:

* High availability
* Disaster recovery
* Fault tolerance

---

# 🔷 NoSQL vs SQL

| SQL              | NoSQL                     |
| ---------------- | ------------------------- |
| Fixed schema     | Flexible schema           |
| ACID             | BASE/Eventual consistency |
| Vertical scaling | Horizontal scaling        |
| Complex joins    | Fast distributed access   |
| Banking systems  | Big data systems          |

---

# 🔷 BASE Properties

Used in NoSQL systems.

| Property              | Meaning                  |
| --------------------- | ------------------------ |
| Basically Available   | System remains available |
| Soft State            | Temporary inconsistency  |
| Eventually Consistent | Data syncs eventually    |

---

# 🔷 NoSQL Security Components

| Component      | Purpose           |
| -------------- | ----------------- |
| Authentication | User validation   |
| Authorization  | Access control    |
| Encryption     | Data protection   |
| Audit Logging  | Activity tracking |
| Backup         | Disaster recovery |

---

# 🔷 NoSQL in Microservices

```text id="52lnvt"
User Service → MongoDB
Cache Service → Redis
Analytics → Cassandra
AI Search → Vector DB
```

---

# 🔷 NoSQL in Cloud Platforms

# AWS

* Amazon DynamoDB
* Amazon DocumentDB

# Azure

* Azure Cosmos DB

# OCI

* Oracle NoSQL Database

# GCP

* Google Cloud Bigtable
* Google Firestore

---

# 🔷 Real Enterprise Architecture Example

# E-Commerce Architecture

```text id="f4btxh"
Frontend (React)
      ↓
API Gateway
      ↓
Microservices
 ├── User Service → MongoDB
 ├── Cart Service → Redis
 ├── Analytics → Cassandra
 ├── Recommendation → Neo4j
 └── AI Search → Vector DB
```

---

# 🔷 Interview-Oriented Summary

> “NoSQL databases are non-relational distributed databases designed for scalability, flexibility, and high-performance workloads. Different types include document databases like MongoDB, key-value stores like Redis, column-family databases like Cassandra, graph databases like Neo4j, and vector databases for AI applications. They are widely used in microservices, big data, IoT, caching, analytics, and AI-driven applications where traditional relational databases face scalability limitations.”
