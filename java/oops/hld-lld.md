# 🚀 System Design (HLD + LLD Together)

## Enterprise Architect Interview Preparation

This is one of the most important topics for:

* Deloitte
* Accenture
* Oracle
* Banking / FinTech / Product companies

At architect level, interviewers expect you to explain:

* **HLD (High-Level Design)** → architecture view
* **LLD (Low-Level Design)** → implementation view

---

# 🧠 What is System Design?

System Design means designing:

* scalable systems
* reliable systems
* maintainable systems
* high-performance enterprise applications

---

# 🔥 Difference Between HLD and LLD

| HLD                  | LLD                    |
| -------------------- | ---------------------- |
| Macro architecture   | Class-level design     |
| Services/components  | Methods/classes        |
| Scalability focus    | Coding focus           |
| Infra/network        | OOPS/design patterns   |
| Technology selection | Implementation details |

---

# 🏗️ Example System

# 🛒 E-Commerce Platform (Amazon/Flipkart Style)

We will design:

* Order Management
* Payment
* Inventory
* Notification
* User Service

---

# 🚀 PART 1 — HIGH LEVEL DESIGN (HLD)

---

# 🏗️ HLD Architecture Diagram

```text id="7ohcq4"
                Angular UI
                     ↓
               API Gateway
                     ↓
-------------------------------------------------
| Order | Payment | Inventory | User | Invoice |
-------------------------------------------------
                     ↓
                 Kafka Event Bus
                     ↓
---------------------------------------
| Notification | Analytics | AI Ops |
---------------------------------------
                     ↓
        Oracle / PostgreSQL / MongoDB
                     ↓
               Redis Cache
```

---

# 🔥 HLD Components Explained

---

# 1. 🌐 Frontend Layer

## Technology

* Angular

## Responsibilities

* User interaction
* API calls
* Authentication UI

---

# 2. 🚪 API Gateway

## Technology

* Spring Cloud Gateway
* Kong
* NGINX

---

## Responsibilities

* Routing
* JWT validation
* Rate limiting
* Request aggregation

---

# 🔥 Flow

```text id="y6fkjk"
Client Request
      ↓
API Gateway
      ↓
Microservices
```

---

# 3. ☕ Microservices Layer

Each service owns:

* business logic
* database
* deployment lifecycle

---

# 🔥 Example Services

| Service              | Responsibility   |
| -------------------- | ---------------- |
| Order Service        | Order management |
| Payment Service      | Payments         |
| Inventory Service    | Stock            |
| User Service         | Authentication   |
| Notification Service | Email/SMS        |

---

# 4. 🔄 Communication Design

---

# 🔹 Synchronous Communication

REST APIs

```text id="i6l8qb"
Order Service → Payment Service
```

Used for:

* immediate response
* transactional workflows

---

# 🔹 Asynchronous Communication

Kafka/RabbitMQ

```text id="1c1y2n"
OrderCreated Event
    ↓
Notification Service
Analytics Service
```

Used for:

* scalability
* loose coupling

---

# 5. 🧠 Database Design

---

# 🔥 Database per Service Pattern

| Service   | Database   |
| --------- | ---------- |
| Order     | PostgreSQL |
| Payment   | Oracle     |
| Analytics | MongoDB    |

---

# 🎯 Benefits

* Loose coupling
* Independent scaling

---

# 6. ⚡ Caching Layer

## Technology

* Redis

---

## Use Cases

* Product catalog
* User session
* Frequently accessed APIs

---

# 7. ☸️ Kubernetes Layer

```text id="4mq1na"
Docker
   ↓
Kubernetes Pod
   ↓
Service
   ↓
Ingress
```

---

# Responsibilities

* Auto scaling
* Self healing
* Rolling deployments

---

# 8. 📊 Observability

| Tool       | Purpose             |
| ---------- | ------------------- |
| Prometheus | Metrics             |
| Grafana    | Dashboards          |
| ELK        | Logs                |
| Jaeger     | Distributed tracing |

---

# 9. 🔐 Security Design

---

# 🔥 OAuth2 + JWT Flow

```text id="g3g7uc"
User Login
    ↓
Auth Service
    ↓
JWT Token
    ↓
API Gateway Validation
```

---

# 🚀 PART 2 — LOW LEVEL DESIGN (LLD)

---

# 🎯 LLD Focus Areas

* Classes
* Interfaces
* DTOs
* APIs
* Design patterns
* Relationships

---

# 🛒 Example: Order Service LLD

---

# 📁 Structure

```text id="jlwmvc"
order-service
 ├── controller
 ├── service
 ├── repository
 ├── entity
 ├── dto
 ├── mapper
 ├── exception
 └── config
```

---

# 🔥 LLD Layered Architecture

```text id="w1z7eu"
Controller
    ↓
Service
    ↓
Repository
    ↓
Database
```

---

# 🔹 Entity Design

```java id="p4s2uw"
@Entity
public class Order {

    @Id
    private Long id;

    private String productId;

    private int quantity;

    private double amount;
}
```

---

# 🔹 Repository Pattern

```java id="x3ukxh"
@Repository
public interface OrderRepository
extends JpaRepository<Order, Long> {
}
```

---

# 🔹 Service Layer

```java id="8ixg0m"
public interface OrderService {

    Order create(Order order);
}
```

---

# 🔹 Service Implementation

```java id="kr0h7x"
@Service
public class OrderServiceImpl
implements OrderService {

    @Autowired
    private OrderRepository repository;

    public Order create(Order order) {

        return repository.save(order);
    }
}
```

---

# 🔹 Controller Layer

```java id="f1mk92"
@RestController
@RequestMapping("/orders")
public class OrderController {

    @Autowired
    private OrderService service;

    @PostMapping
    public Order create(
        @RequestBody Order order) {

        return service.create(order);
    }
}
```

---

# 🧠 OOPS in LLD

| OOPS Principle | Example               |
| -------------- | --------------------- |
| Encapsulation  | Private entity fields |
| Abstraction    | Service interfaces    |
| Inheritance    | BaseEntity            |
| Polymorphism   | Payment strategies    |

---

# 🔥 Design Patterns Used

| Pattern    | Use Case                 |
| ---------- | ------------------------ |
| Factory    | Payment object creation  |
| Strategy   | Payment method selection |
| Repository | DB abstraction           |
| Builder    | DTO creation             |
| Observer   | Kafka events             |
| Facade     | ERP integration          |
| Saga       | Distributed transactions |

---

# 📚 Saga Pattern Example

---

# 🛒 Order Flow

```text id="fajc1l"
Order Created
     ↓
Inventory Reserved
     ↓
Payment Completed
```

---

# ❌ Failure Case

```text id="q4e83h"
Payment Failed
     ↓
Compensation Transaction
     ↓
Release Inventory
```

---

# 🎯 Why Saga?

Microservices cannot use traditional DB transactions across services.

---

# 🚀 API Design (LLD)

---

# 🔹 REST API Example

```http id="8xvfd1"
POST /orders
GET /orders/{id}
PUT /orders/{id}
DELETE /orders/{id}
```

---

# 🔥 DTO Example

```java id="x3uhlp"
public class OrderRequest {

    private String productId;

    private int quantity;
}
```

---

# ⚡ Exception Handling

```java id="s1cmqv"
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String>
    handle(Exception ex) {

        return ResponseEntity
               .badRequest()
               .body(ex.getMessage());
    }
}
```

---

# ☸️ Kubernetes Deployment (Production)

---

# 🔹 Deployment YAML

```yaml id="1mif9l"
apiVersion: apps/v1
kind: Deployment

metadata:
  name: order-service
```

---

# 🔹 HPA

```yaml id="j57cw9"
minReplicas: 2
maxReplicas: 10
```

---

# 🔥 Production Enhancements

| Component  | Purpose       |
| ---------- | ------------- |
| Redis      | Caching       |
| Kafka      | Event-driven  |
| ELK        | Logging       |
| Prometheus | Monitoring    |
| Grafana    | Visualization |
| Jenkins    | CI/CD         |
| Terraform  | IaC           |

---

# 🧠 Real Interview Flow

---

# 🔥 How to Answer System Design Interviews

## Step 1 → Clarify Requirements

Ask:

* Users?
* TPS?
* Availability?
* Consistency requirements?

---

## Step 2 → Explain HLD

Talk about:

* services
* communication
* scaling
* DB design

---

## Step 3 → Explain LLD

Talk about:

* entities
* APIs
* design patterns
* OOPS

---

## Step 4 → Discuss Non-Functional Requirements

| NFR         | Solution        |
| ----------- | --------------- |
| Scalability | Kubernetes      |
| Reliability | Circuit breaker |
| Performance | Redis           |
| Security    | JWT/OAuth2      |
| Monitoring  | ELK/Grafana     |

---

# 🎯 Architect-Level Interview Answer

> “I approach system design by separating HLD and LLD concerns. At the HLD level, I define scalable microservices architecture with API Gateway, Kafka-based event-driven communication, database-per-service, caching, and Kubernetes deployment. At the LLD level, I design entities, APIs, DTOs, repositories, and service abstractions using OOPS and design patterns like Strategy, Factory, Repository, and Saga to ensure maintainability and extensibility.”

---

