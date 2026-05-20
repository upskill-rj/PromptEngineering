# Event Bus Overview

An **Event Bus** is a messaging architecture pattern used in distributed systems and **microservices** to enable asynchronous communication between applications, services, and systems.

Instead of one service directly calling another service, services publish **events** to the Event Bus, and interested consumers subscribe to those events.

Common Event Bus technologies include:

* Apache Pulsar
* Apache Kafka
* RabbitMQ
* Amazon EventBridge
* Azure Event Grid
* Google Pub/Sub

---

# Why Event Bus is Used

Traditional synchronous REST calls create tight coupling.

Example:

```text
Order Service → Payment Service → Inventory Service → Shipping Service
```

If one service fails, the whole chain may fail.

With Event Bus:

```text
Order Service → Event Bus → Multiple Consumers
```

This creates:

* Loose coupling
* Scalability
* Reliability
* Real-time processing
* Event-driven architecture

---

# Real-Time Example

## E-Commerce Order Flow

```text
1. User places order
2. Order Service publishes "OrderCreated" event
3. Event Bus distributes event to:
   - Payment Service
   - Inventory Service
   - Notification Service
   - Analytics Service
```

Each consumer works independently.

---

# Types of Event Bus Systems

| Type                        | Description                   | Example Usecase            |
| --------------------------- | ----------------------------- | -------------------------- |
| Message Queue               | One producer → one consumer   | Order processing           |
| Publish/Subscribe (Pub-Sub) | One producer → many consumers | Notifications              |
| Event Streaming             | Continuous real-time streams  | Fraud detection            |
| Event Sourcing              | Store all events permanently  | Banking audit              |
| CQRS + Event Bus            | Separate read/write systems   | High-scale enterprise apps |

---

# 1. Message Queue

## Flow

```text
Producer → Queue → Consumer
```

Only one consumer processes the message.

## Features

* Reliable delivery
* Task processing
* Retry mechanism
* Dead Letter Queue (DLQ)

## Tools

* RabbitMQ
* ActiveMQ
* Amazon SQS

## Usecases

* Email sending
* Invoice generation
* Background jobs
* Batch processing

---

# 2. Publish/Subscribe (Pub-Sub)

## Flow

```text
Publisher → Topic → Multiple Subscribers
```

Many consumers receive same event.

## Features

* Broadcast communication
* Loose coupling
* Real-time notification

## Tools

* Apache Pulsar
* Apache Kafka
* Google Pub/Sub

## Usecases

* Stock market updates
* Chat applications
* Push notifications
* IoT telemetry

---

# 3. Event Streaming

Processes continuous event streams in real time.

## Flow

```text
Producer → Stream → Stream Processing → Consumers
```

## Features

* High throughput
* Real-time analytics
* Replay events
* Large-scale streaming

## Tools

* Apache Kafka
* Apache Pulsar
* Apache Flink
* Apache Spark

## Usecases

* Fraud detection
* Real-time recommendation engine
* AI/ML streaming pipelines
* Log analytics

---

# Apache Pulsar Architecture

## High-Level Architecture

```text
Producer
   ↓
Broker
   ↓
Topic
   ↓
BookKeeper Storage
   ↓
Consumers
```

---

# Core Components of Apache Pulsar

## 1. Producer

Application sending messages/events.

### Example

```text
Order Service publishes OrderCreated event
```

### Features

* Async publishing
* Batch messaging
* Compression
* Encryption

---

## 2. Broker

Central messaging server.

### Responsibilities

* Receive events
* Route messages
* Manage subscriptions
* Load balancing

### Features

* Stateless architecture
* Horizontal scaling
* Multi-tenant support

---

## 3. Topic

Logical channel where events are stored.

### Types

| Topic Type      | Description                     |
| --------------- | ------------------------------- |
| Non-Partitioned | Single topic                    |
| Partitioned     | Multiple partitions for scaling |

### Example

```text
orders-topic
payments-topic
shipment-topic
```

---

# Partitioning

Partitioning improves scalability.

## Example

```text
orders-topic-partition-1
orders-topic-partition-2
orders-topic-partition-3
```

Different brokers handle different partitions.

---

# 4. Consumer

Applications reading messages.

## Subscription Types in Pulsar

| Subscription Type | Description                   | Usecase               |
| ----------------- | ----------------------------- | --------------------- |
| Exclusive         | One consumer only             | Sequential processing |
| Shared            | Multiple consumers share load | Parallel jobs         |
| Failover          | Backup consumer available     | HA systems            |
| Key_Shared        | Same key → same consumer      | Ordered events        |

---

# 5. Apache BookKeeper

Distributed storage layer used by Pulsar.

## Responsibilities

* Persistent storage
* Replication
* Durability
* Recovery

## Benefits

* Fast writes
* High availability
* Message replay

---

# 6. ZooKeeper

Used for coordination and metadata.

## Responsibilities

* Cluster management
* Broker coordination
* Configuration management

(Note: Newer Pulsar versions are reducing ZooKeeper dependency.)

---

# Pulsar Message Flow

```text
Producer
   ↓
Pulsar Broker
   ↓
Topic Partition
   ↓
BookKeeper Ledger
   ↓
Consumer Subscription
   ↓
Consumer ACK
```

---

# Apache Pulsar Features

| Feature                    | Description                          |
| -------------------------- | ------------------------------------ |
| Multi-Tenancy              | Multiple teams/apps use same cluster |
| Geo-Replication            | Replicate across regions             |
| Message Replay             | Re-read old events                   |
| Tiered Storage             | Move old data to cloud storage       |
| Schema Registry            | JSON/Avro schema validation          |
| Exactly-Once Support       | Avoid duplicate processing           |
| Built-in Queue + Streaming | Single platform                      |

---

# Kafka vs Pulsar

| Feature              | Kafka                  | Pulsar                    |
| -------------------- | ---------------------- | ------------------------- |
| Storage Architecture | Broker handles storage | Separate storage layer    |
| Scalability          | Good                   | Better horizontal scaling |
| Multi-Tenancy        | Limited                | Strong                    |
| Message Replay       | Yes                    | Yes                       |
| Geo Replication      | Complex                | Built-in                  |
| Queue + Streaming    | Mostly streaming       | Both native               |
| Cloud Native         | Moderate               | Strong                    |

---

# Event Bus in Microservices Architecture

## Traditional Architecture

```text
Frontend → API → Service → DB
```

## Event-Driven Architecture

```text
Frontend
   ↓
API Gateway
   ↓
Order Service
   ↓
Event Bus
   ↓
Payment Service
Inventory Service
Notification Service
Analytics Service
```

---

# Security Components

| Security Feature   | Purpose                    |
| ------------------ | -------------------------- |
| TLS/SSL            | Encrypt communication      |
| Authentication     | Verify producers/consumers |
| Authorization      | Access control             |
| OAuth/JWT          | Secure APIs                |
| Message Encryption | Protect sensitive data     |

---

# Scalability Components

| Component     | Purpose             |
| ------------- | ------------------- |
| Partitioning  | Parallel processing |
| Load Balancer | Distribute traffic  |
| Clustering    | High availability   |
| Auto Scaling  | Dynamic scaling     |
| Replication   | Fault tolerance     |

---

# Monitoring & Observability

| Tool          | Purpose             |
| ------------- | ------------------- |
| Prometheus    | Metrics collection  |
| Grafana       | Dashboards          |
| ELK Stack     | Log analytics       |
| Jaeger        | Trace microservices |
| OpenTelemetry | Unified telemetry   |

---

# AI/ML Usecases of Event Bus

| AI Usecase                | Description                     |
| ------------------------- | ------------------------------- |
| Real-Time Fraud Detection | Stream transactions to ML model |
| Recommendation Engine     | Analyze clickstream events      |
| Predictive Maintenance    | IoT sensor streaming            |
| AI Chatbots               | Process live conversations      |
| GenAI Pipelines           | Stream prompts/responses        |

---

# OCI / AWS / Azure Integration

| Cloud                       | Event Bus Service       |
| --------------------------- | ----------------------- |
| Oracle Cloud Infrastructure | OCI Streaming           |
| Amazon Web Services         | EventBridge, Kinesis    |
| Microsoft Azure             | Event Grid, Service Bus |
| Google Cloud                | Pub/Sub                 |

---

# Interview Questions & Answers

## 1. What is Event Bus?

An Event Bus is a messaging mechanism that enables asynchronous communication between services using events.

---

## 2. Difference between Queue and Pub/Sub?

| Queue           | Pub/Sub            |
| --------------- | ------------------ |
| One consumer    | Multiple consumers |
| Task processing | Event broadcasting |

---

## 3. Why Pulsar over Kafka?

Pulsar provides:

* Better multi-tenancy
* Separate storage/compute
* Native queue + streaming
* Easier geo-replication

---

## 4. What is partitioning?

Partitioning divides topics into multiple segments for parallel processing and scalability.

---

## 5. What is message replay?

Consumers can re-read historical events from storage for recovery or analytics.

---

# Simple Interview Summary

## Apache Pulsar in 2-3 Lines

Apache Pulsar is a distributed event-streaming platform used for real-time messaging, queueing, and event-driven microservices communication. It separates compute and storage using Brokers and BookKeeper, providing high scalability, durability, and multi-tenant architecture.
