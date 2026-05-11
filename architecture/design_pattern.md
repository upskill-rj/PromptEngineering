# Design Patterns — Interview Overview

## 🔷 What are Design Patterns?

Design patterns are **reusable software design solutions** used to solve commonly occurring problems in software architecture and application development.

They help improve:

* maintainability
* scalability
* flexibility
* reusability
* clean architecture

---

# 🎯 Simple Interview Definition

> “Design patterns are proven reusable software design solutions used to solve recurring architectural and coding problems in enterprise applications.”

---

# 🔷 Why Design Patterns are Important

Without design patterns:
❌ tightly coupled code
❌ difficult maintenance
❌ low scalability
❌ duplicated logic

With design patterns:
✅ reusable architecture
✅ loose coupling
✅ better scalability
✅ clean code organization
✅ enterprise maintainability

---

# 🔷 Categories of Design Patterns

| Category   | Purpose                  |
| ---------- | ------------------------ |
| Creational | Object creation          |
| Structural | Object composition       |
| Behavioral | Communication & behavior |

---

# 🔷 High-Level Enterprise Architecture Usage

```text id="jlwm6a"
Frontend
   |
API Gateway
   |
Spring Boot Microservices
   |
Kafka / Redis / DBaaS
```

Design patterns are used across:

* microservices
* APIs
* cloud-native systems
* AI-native systems

---

# 🔷 CREATIONAL DESIGN PATTERNS

These patterns deal with:

* object creation
* lifecycle management

---

# 1. Singleton Pattern

Ensures only one instance of a class exists throughout the application.

Used for:

* configuration managers
* cache managers
* logging services

```text id="jlwm6b"
Application → Single Shared Instance
```

---

# 2. Factory Pattern

Creates objects without exposing object creation logic to clients.

Used when object type selection happens dynamically.

Example:

* payment gateway selection
* cloud provider selection

---

# 3. Abstract Factory Pattern

Creates families of related objects.

Useful for:

* multi-cloud systems
* UI themes
* database abstraction

---

# 4. Builder Pattern

Constructs complex objects step-by-step.

Used for:

* immutable objects
* API request creation
* large configuration objects

---

# 5. Prototype Pattern

Creates new objects by cloning existing objects.

Improves performance when object creation is expensive.

---

# 🔷 STRUCTURAL DESIGN PATTERNS

These patterns focus on:

* object relationships
* system composition

---

# 6. Adapter Pattern

Converts one interface into another compatible interface.

Used in:

* legacy system integration
* third-party APIs

```text id="jlwm6c"
Legacy API → Adapter → Modern Service
```

---

# 7. Facade Pattern

Provides simplified interface to complex subsystems.

Commonly used in:

* microservices orchestration
* enterprise APIs

---

# 8. Proxy Pattern

Acts as intermediary between client and actual object.

Used for:

* security
* lazy loading
* remote service access

Examples:

* API gateway
* caching proxy

---

# 9. Decorator Pattern

Dynamically adds functionality without modifying original class.

Used in:

* logging
* security
* monitoring

---

# 10. Composite Pattern

Treats individual objects and groups uniformly.

Common in:

* UI hierarchies
* file systems
* menu structures

---

# 11. Bridge Pattern

Separates abstraction from implementation.

Useful for:

* multi-platform systems
* cloud abstraction layers

---

# 🔷 BEHAVIORAL DESIGN PATTERNS

These patterns manage:

* communication
* workflow
* object interaction

---

# 12. Observer Pattern

Objects subscribe to receive updates automatically.

Used heavily in:

* event-driven systems
* Kafka consumers
* UI notifications

```text id="jlwm6d"
Publisher → Subscribers
```

---

# 13. Strategy Pattern

Encapsulates interchangeable algorithms or behaviors.

Used for:

* payment strategies
* authentication methods
* AI model selection

---

# 14. Command Pattern

Encapsulates requests as objects.

Useful for:

* workflow engines
* task queues
* undo operations

---

# 15. Chain of Responsibility Pattern

Passes requests through processing chain until handled.

Used in:

* API filters
* authentication pipelines
* middleware

---

# 16. Template Method Pattern

Defines common workflow structure while allowing subclasses to customize steps.

Used in:

* framework design
* batch processing

---

# 17. State Pattern

Changes object behavior based on internal state.

Used in:

* order processing
* workflow systems

---

# 18. Mediator Pattern

Centralizes communication between multiple objects.

Useful in:

* chat systems
* orchestration engines

---

# 19. Iterator Pattern

Provides sequential access to collection elements.

Common in:

* Java collections
* streaming systems

---

# 20. Visitor Pattern

Separates operations from object structures.

Used in:

* compilers
* reporting engines

---

# 🔷 Enterprise Design Patterns in Microservices

| Pattern   | Enterprise Use Case      |
| --------- | ------------------------ |
| Singleton | Config manager           |
| Factory   | Cloud provider selection |
| Observer  | Kafka events             |
| Strategy  | Payment methods          |
| Proxy     | API Gateway              |
| Facade    | Aggregator service       |

---

# 🔷 Design Patterns in Spring Boot

Spring Boot internally uses many design patterns.

| Pattern   | Spring Example  |
| --------- | --------------- |
| Singleton | Spring Beans    |
| Factory   | BeanFactory     |
| Proxy     | AOP             |
| Template  | JdbcTemplate    |
| Observer  | Event listeners |

---

# 🔷 Design Patterns in Cloud-Native Systems

```text id="jlwm6e"
API Gateway → Proxy Pattern
Kafka → Observer Pattern
Kubernetes Controllers → Singleton + Observer
```

---

# 🔷 Design Patterns in AI-Native Systems

| Pattern                 | AI Use Case            |
| ----------------------- | ---------------------- |
| Strategy                | LLM selection          |
| Factory                 | Agent creation         |
| Observer                | AI event streaming     |
| Facade                  | AI orchestration layer |
| Chain of Responsibility | Prompt filtering       |

---

# 🔷 Real Enterprise Example (Your Background)

## Finance / Reporting Platform

Architecture:

```text id="jlwm6f"
React UI
   |
API Gateway
   |
Spring Boot Microservices
   |
Kafka / Redis / Oracle DB
```

Patterns used:

* Singleton → configuration beans
* Observer → Kafka consumers
* Strategy → report generation logic
* Proxy → API Gateway
* Factory → service initialization

This strongly aligns with your enterprise Java background. 

---

# 🔷 Common Interview Questions

---

## Q1. What are design patterns?

> “Design patterns are reusable software design solutions used to solve recurring architectural and coding problems.”

---

## Q2. Difference between Factory and Abstract Factory?

| Factory                 | Abstract Factory            |
| ----------------------- | --------------------------- |
| Creates one object type | Creates families of objects |

---

## Q3. Why Singleton pattern?

> “Singleton ensures only one shared instance exists for globally used components like configuration or cache managers.”

---

## Q4. Where Observer pattern used?

> “Observer pattern is widely used in event-driven systems, messaging systems, and Kafka-based architectures.”

---

## Q5. What is Strategy pattern?

> “Strategy pattern allows switching algorithms or behaviors dynamically at runtime.”

---

# 🔷 Architect-Level Answer (Best for You)

> “Design patterns provide reusable architectural solutions that improve scalability, maintainability, and flexibility in enterprise systems. In our cloud-native microservices platforms using Spring Boot, Kafka, Redis, Kubernetes, and OCI, we extensively used patterns like Singleton, Factory, Strategy, Observer, Proxy, and Facade to implement scalable APIs, event-driven communication, orchestration layers, and distributed enterprise workflows.”

---

# 🔥 Advanced Enterprise Patterns (Important for Architect Interviews)

## Microservices Patterns

| Pattern         | Purpose                  |
| --------------- | ------------------------ |
| Saga            | Distributed transactions |
| Circuit Breaker | Fault tolerance          |
| CQRS            | Read/write separation    |
| API Gateway     | Centralized routing      |
| Event Sourcing  | Event persistence        |

---

# 🔷 Cloud-Native Pattern Mapping

```text id="jlwm6g"
NGINX → Proxy Pattern
Kafka → Observer Pattern
Redis → Cache Pattern
Kubernetes → Controller Pattern
```

---

# 🔷 AI-Native Pattern Mapping

```text id="jlwm6h"
AI Agent → Strategy + Command
RAG → Facade
AI Guardrails → Chain of Responsibility
```

