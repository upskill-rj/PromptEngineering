# Database Overview

A **database** is an organized collection of data that allows applications to **store, retrieve, update, and manage information efficiently**.

👉 Example:

* Banking system stores customer accounts, transactions, loans
* E-commerce stores products, orders, payments
* AI applications store embeddings, training data, chat history

---

# 🔷 Why Databases are Important

Databases help applications achieve:

* Data persistence
* Fast retrieval
* Security
* Scalability
* Concurrent access
* Backup & recovery
* Analytics & reporting

---

# 🔷 High-Level Database Architecture

```text
Application Layer
       ↓
API / Service Layer
       ↓
Database Engine
       ↓
Storage Layer (Disk / SSD / Cloud Storage)
```

---

# 🔷 Core Database Components

| Component            | Purpose                        | Example               |
| -------------------- | ------------------------------ | --------------------- |
| Tables / Collections | Store data                     | Customer table        |
| Schema               | Structure of data              | Columns, datatype     |
| Query Engine         | Executes queries               | SQL engine            |
| Indexes              | Improve search speed           | Search by customer ID |
| Transactions         | Ensure consistency             | Money transfer        |
| Cache                | Faster access                  | Redis                 |
| Replication          | Copy data across servers       | HA setup              |
| Backup & Recovery    | Disaster recovery              | Point-in-time restore |
| Security             | Authentication & authorization | RBAC                  |
| Connection Pool      | Manage DB connections          | HikariCP              |

---

# 🔷 Types of Databases

# 1. Relational Database (RDBMS)

Stores data in **tables with rows and columns**.

### 🔹 Examples

* Oracle Database
* MySQL
* PostgreSQL
* Microsoft SQL Server

---

## 🔹 Components of RDBMS

| Component    | Description                 |
| ------------ | --------------------------- |
| Tables       | Store structured data       |
| Rows         | Individual records          |
| Columns      | Attributes                  |
| Primary Key  | Unique identifier           |
| Foreign Key  | Relationship between tables |
| SQL          | Query language              |
| Transactions | ACID compliance             |

---

## 🔹 Example

### Banking System

```text
CUSTOMER Table
- Customer_ID
- Name
- Account_No

TRANSACTION Table
- Txn_ID
- Amount
- Customer_ID
```

---

## 🔹 Use Cases

* Banking
* ERP systems
* Financial applications
* HRMS
* Inventory management

---

## 🔹 Advantages

* Strong consistency
* ACID transactions
* Structured schema
* Complex joins

---

## 🔹 Interview Answer

> “Relational databases store structured data in tables and use SQL for querying. They are ideal for transactional systems like banking and ERP where consistency and ACID compliance are critical.”

---

# 2. NoSQL Database

Designed for **high scalability and flexible schema**.

---

## 🔹 Types of NoSQL Databases

| Type         | Example   | Use Case             |
| ------------ | --------- | -------------------- |
| Document DB  | MongoDB   | JSON documents       |
| Key-Value DB | Redis     | Caching              |
| Column DB    | Cassandra | Big data             |
| Graph DB     | Neo4j     | Relationship mapping |

---

# 🔷 A. Document Database

Stores data as JSON-like documents.

### 🔹 Example

* MongoDB

```json
{
  "name": "Rahul",
  "skills": ["Java", "Spring Boot"]
}
```

---

## 🔹 Use Cases

* E-commerce catalogs
* AI chat applications
* Content management
* Dynamic schemas

---

## 🔹 Advantages

* Flexible schema
* Horizontal scaling
* JSON support

---

# 🔷 B. Key-Value Database

Stores data as key-value pairs.

### 🔹 Examples

* Redis
* Amazon DynamoDB

---

## 🔹 Example

```text
SessionID → User Data
```

---

## 🔹 Use Cases

* Caching
* Session management
* Real-time analytics

---

# 🔷 C. Column-Family Database

Optimized for large-scale distributed data.

### 🔹 Examples

* Apache Cassandra
* Apache HBase

---

## 🔹 Use Cases

* IoT
* Event logging
* Telecom systems
* Time-series data

---

# 🔷 D. Graph Database

Stores relationships between entities.

### 🔹 Example

* Neo4j

---

## 🔹 Use Cases

* Social networks
* Fraud detection
* Recommendation engines

---

# 🔷 Database Concepts

# 1. ACID Properties

Important in relational databases.

| Property    | Meaning                |
| ----------- | ---------------------- |
| Atomicity   | All or nothing         |
| Consistency | Valid state maintained |
| Isolation   | Concurrent safety      |
| Durability  | Permanent storage      |

---

## 🔹 Example

Bank transfer:

* Debit and credit both succeed
* If one fails → rollback

---

# 2. CAP Theorem

Distributed databases trade between:

| Term                | Meaning                  |
| ------------------- | ------------------------ |
| Consistency         | Same data everywhere     |
| Availability        | System always responds   |
| Partition Tolerance | Survives network failure |

---

# 🔷 Database Scaling

# Vertical Scaling

Increase server power.

```text
More CPU + RAM
```

---

# Horizontal Scaling

Add more servers.

```text
DB Sharding / Clustering
```

---

# 🔷 Database Optimization Components

| Component          | Purpose             |
| ------------------ | ------------------- |
| Indexing           | Faster queries      |
| Partitioning       | Split huge tables   |
| Sharding           | Distributed scaling |
| Replication        | High availability   |
| Query Optimization | Better performance  |
| Caching            | Reduce DB load      |

---

# 🔷 Database Security

| Security Feature | Example                |
| ---------------- | ---------------------- |
| Authentication   | Username/password      |
| Authorization    | Role-based access      |
| Encryption       | TDE, SSL               |
| Auditing         | User activity tracking |
| Backup           | Disaster recovery      |

---

# 🔷 Databases in Microservices

Each microservice can own its database.

```text
Order Service → Orders DB
Payment Service → Payment DB
User Service → User DB
```

---

# 🔷 Databases in Cloud

# AWS

* Amazon RDS
* Amazon Aurora
* Amazon DynamoDB

# Azure

* Azure SQL Database
* Azure Cosmos DB

# OCI

* Oracle Autonomous Database
* Oracle Exadata

# GCP

* Google Cloud SQL
* Google BigQuery

---

# 🔷 AI & Modern Database Use Cases

| AI Use Case           | Database          |
| --------------------- | ----------------- |
| ChatGPT memory        | Vector DB         |
| Recommendation Engine | Graph DB          |
| Fraud Detection       | Cassandra + Kafka |
| RAG Application       | Vector Search     |
| IoT Analytics         | Time-series DB    |

---

# 🔷 Vector Databases (Important for AI)

Stores vector embeddings for semantic search.

### 🔹 Examples

* Pinecone
* FAISS
* OpenSearch

---

## 🔹 AI Example

```text
User asks question
↓
Embedding generated
↓
Vector DB searches similar content
↓
LLM generates response
```

---

# 🔷 Database Architecture Example (Interview)

# E-Commerce Architecture

```text
Frontend (React)
      ↓
API Gateway
      ↓
Microservices
 ├── User Service → PostgreSQL
 ├── Product Service → MongoDB
 ├── Cart Service → Redis
 └── Analytics → Cassandra
```

---

# 🔷 Interview-Oriented Summary

> “Databases are systems used to store and manage application data efficiently. Relational databases like PostgreSQL and Oracle are ideal for transactional systems requiring ACID compliance, while NoSQL databases like MongoDB and Cassandra support scalability and flexible schemas. Modern architectures use distributed databases, caching, replication, and cloud-native managed database services to support microservices, AI, and high-scale enterprise applications.”
