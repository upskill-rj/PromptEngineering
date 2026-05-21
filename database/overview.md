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


=====================


# Database Overview

A **database** is a system used to store, organize, manage, and retrieve data efficiently for applications, analytics, AI systems, and enterprise platforms.

Databases support:

* Transactions
* Reporting
* Analytics
* AI/ML workloads
* Real-time processing
* Distributed systems

---

# 🔷 Types of Data in Databases

Data is mainly categorized into:

| Type                 | Description               |
| -------------------- | ------------------------- |
| Structured Data      | Organized in rows/columns |
| Semi-Structured Data | Flexible tagged format    |
| Unstructured Data    | No fixed format           |

---

# 🔷 1. Structured Data

Structured data follows a predefined schema.

Stored in:

* Tables
* Rows
* Columns

---

## 🔹 Examples

| EMP_ID | NAME  | SALARY |
| ------ | ----- | ------ |
| 101    | Rahul | 50000  |

---

## 🔹 Databases Used

* Oracle Database
* MySQL
* PostgreSQL
* Microsoft SQL Server

---

## 🔹 Components

| Component    | Purpose               |
| ------------ | --------------------- |
| Tables       | Store data            |
| Rows         | Records               |
| Columns      | Attributes            |
| Primary Keys | Unique identification |
| Foreign Keys | Relationships         |
| SQL Engine   | Query processing      |
| Indexes      | Performance           |
| Transactions | ACID compliance       |

---

## 🔹 Use Cases

| Domain     | Example          |
| ---------- | ---------------- |
| Banking    | Transactions     |
| ERP        | Finance/payroll  |
| HRMS       | Employee records |
| Healthcare | Patient data     |
| E-Commerce | Orders/payments  |

---

## 🔹 Advantages

* Strong consistency
* ACID transactions
* Structured schema
* Complex joins & analytics

---

## 🔹 Example SQL

```sql id="4d4i9t"
SELECT * FROM EMPLOYEE
WHERE SALARY > 50000;
```

---

# 🔷 2. Semi-Structured Data

Semi-structured data has flexible structure but includes tags/metadata.

Common formats:

* JSON
* XML
* YAML

---

## 🔹 Example JSON

```json id="ntvr66"
{
  "name": "Rahul",
  "skills": ["Java", "OCI"]
}
```

---

## 🔹 Databases Used

* MongoDB
* Couchbase
* Google Firestore

---

## 🔹 Components

| Component   | Purpose            |
| ----------- | ------------------ |
| Documents   | JSON/XML data      |
| Collections | Group of documents |
| Indexes     | Fast queries       |
| Replication | HA                 |
| Sharding    | Horizontal scaling |

---

## 🔹 Use Cases

| Use Case         | Example              |
| ---------------- | -------------------- |
| CMS              | Dynamic content      |
| AI chat systems  | Conversation history |
| Product catalogs | Flexible attributes  |
| Mobile apps      | User profiles        |

---

## 🔹 Advantages

* Flexible schema
* Easy scalability
* JSON integration
* Rapid development

---

# 🔷 3. Unstructured Data

Unstructured data has no predefined schema.

Examples:

* Images
* Videos
* Audio
* PDFs
* Emails
* Social media posts

---

# 🔷 Examples of Unstructured Data

| Type      | Example            |
| --------- | ------------------ |
| Image     | JPG, PNG           |
| Video     | MP4                |
| Audio     | MP3                |
| Documents | PDF                |
| Logs      | Server logs        |
| AI Data   | Chat conversations |

---

## 🔹 Storage Systems Used

* Amazon S3
* Google Cloud Storage
* Hadoop HDFS
* Elasticsearch

---

## 🔹 Components

| Component           | Purpose         |
| ------------------- | --------------- |
| Object Storage      | Store files     |
| Metadata Engine     | File indexing   |
| Search Engine       | Retrieval       |
| Distributed Storage | Scalability     |
| AI Processing       | NLP/CV analysis |

---

## 🔹 Use Cases

| Use Case     | Example              |
| ------------ | -------------------- |
| Social media | Images/videos        |
| AI training  | LLM datasets         |
| Healthcare   | MRI scans            |
| Streaming    | Netflix-like systems |
| Logging      | DevOps monitoring    |

---

# 🔷 Database Classification by Model

| Database Type  | Data Type         |
| -------------- | ----------------- |
| Relational DB  | Structured        |
| Document DB    | Semi-structured   |
| Key-Value DB   | Semi-structured   |
| Graph DB       | Relationship data |
| Time-Series DB | Timestamp data    |
| Vector DB      | AI embeddings     |

---

# 🔷 4. Relational Databases (RDBMS)

Stores structured data in tables.

---

## 🔹 Examples

* Oracle Database
* PostgreSQL

---

## 🔹 Features

| Feature     | Description             |
| ----------- | ----------------------- |
| SQL support | Standard query language |
| ACID        | Strong consistency      |
| Joins       | Complex relationships   |
| Constraints | Data integrity          |

---

## 🔹 Best Use Cases

* Banking
* ERP
* Accounting
* Inventory management

---

# 🔷 5. NoSQL Databases

Non-relational databases optimized for scale and flexibility.

---

## 🔹 Types

| Type         | Example   |
| ------------ | --------- |
| Document DB  | MongoDB   |
| Key-Value DB | Redis     |
| Column DB    | Cassandra |
| Graph DB     | Neo4j     |

---

## 🔹 Best Use Cases

* Real-time apps
* IoT
* Big data
* AI systems

---

# 🔷 6. Key-Value Database

```text id="0lz5fe"
Session_ID → User Data
```

---

## 🔹 Examples

* Redis
* Amazon DynamoDB

---

## 🔹 Use Cases

* Caching
* Session storage
* Gaming
* Real-time APIs

---

# 🔷 7. Column-Family Database

Stores data in column groups.

---

## 🔹 Examples

* Apache Cassandra
* Apache HBase

---

## 🔹 Use Cases

* Telecom
* IoT
* Event logging
* Analytics

---

# 🔷 8. Graph Database

Focuses on relationships.

---

## 🔹 Examples

* Neo4j
* Amazon Neptune

---

## 🔹 Use Cases

* Fraud detection
* Social networks
* Recommendation engines

---

# 🔷 9. Time-Series Database

Stores timestamp-based data.

---

## 🔹 Examples

* InfluxDB
* TimescaleDB

---

## 🔹 Use Cases

* Monitoring
* IoT sensors
* Stock market data
* DevOps metrics

---

# 🔷 10. Vector Database (AI)

Stores vector embeddings for semantic search.

---

## 🔹 Examples

* Pinecone
* Weaviate
* FAISS

---

## 🔹 AI Workflow

```text id="y31g26"
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

* RAG applications
* AI search
* Recommendation engines
* Semantic retrieval

---

# 🔷 Database Components

# 1. Storage Engine

Stores and retrieves data.

---

# 2. Query Engine

Executes SQL/queries.

---

# 3. Indexes

Improve search speed.

---

# 4. Cache

Reduces database load.

---

# 5. Replication

Copies data across servers.

---

# 6. Sharding

Distributes data horizontally.

---

# 7. Transactions

Ensures consistency.

---

# 8. Backup & Recovery

Disaster recovery support.

---

# 🔷 Database Scaling

# Vertical Scaling

```text id="lx9w9k"
Increase CPU/RAM
```

---

# Horizontal Scaling

```text id="f9hl2u"
Add more servers
```

---

# 🔷 Database in Enterprise Architecture

```text id="b6lsq7"
Frontend
   ↓
API Gateway
   ↓
Microservices
   ↓
Databases
 ├── PostgreSQL
 ├── MongoDB
 ├── Redis
 ├── Cassandra
 └── Vector DB
```

---

# 🔷 Database in Cloud Platforms

# AWS

* Amazon RDS
* Amazon DynamoDB
* Amazon S3

# Azure

* Azure SQL Database
* Azure Cosmos DB

# OCI

* Oracle Autonomous Database
* Oracle NoSQL Database

# GCP

* Google Cloud SQL
* Google BigQuery

---

# 🔷 Interview-Oriented Summary

> “Databases are systems used to manage structured, semi-structured, and unstructured data. Structured data is commonly stored in relational databases like Oracle and PostgreSQL, semi-structured data in document databases like MongoDB, and unstructured data in object storage and search systems like S3 and Elasticsearch. Modern enterprise architectures use multiple database types together to support transactions, analytics, AI workloads, real-time processing, and scalable cloud-native microservices.”
