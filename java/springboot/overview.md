# 🚀 Spring Boot Internal Architecture

## 📘 What is Spring Boot?

Spring Boot is a framework built on top of the Spring Framework that helps create:

* Microservices
* REST APIs
* Enterprise applications

with:

* minimal configuration
* embedded servers
* production-ready features

---

# 🏗️ High-Level Spring Boot Architecture

```text id="87l2sf"
Client Request
      ↓
DispatcherServlet
      ↓
Controller Layer
      ↓
Service Layer
      ↓
Repository Layer
      ↓
Database
```

---

# 🔥 Internal Components of Spring Boot

| Component           | Responsibility          |
| ------------------- | ----------------------- |
| DispatcherServlet   | Front Controller        |
| Controller          | Handles HTTP requests   |
| Service             | Business logic          |
| Repository          | DB interaction          |
| Entity              | Database object mapping |
| IOC Container       | Bean management         |
| AutoConfiguration   | Automatic setup         |
| Embedded Server     | Tomcat/Jetty            |
| Spring Boot Starter | Dependency management   |

---

# 🧠 1. Spring Boot Startup Flow

---

# 🔹 Main Class

```java id="0qf7m2"
@SpringBootApplication
public class OrderApplication {

    public static void main(String[] args) {

        SpringApplication.run(
            OrderApplication.class, args);
    }
}
```

---

# 🔥 What Happens Internally?

When application starts:

```text id="4dltvi"
main()
   ↓
SpringApplication.run()
   ↓
Create IOC Container
   ↓
Scan Beans
   ↓
Auto Configuration
   ↓
Start Embedded Tomcat
   ↓
Application Ready
```

---

# 🧩 2. @SpringBootApplication Internals

```java id="x4p8fu"
@SpringBootApplication
```

is combination of:

```java id="9l1z6x"
@Configuration
@EnableAutoConfiguration
@ComponentScan
```

---

# 🔹 @Configuration

Used for Java-based configuration.

---

# 🔹 @ComponentScan

Scans:

* Controllers
* Services
* Repositories
* Components

---

# 🔹 @EnableAutoConfiguration

Automatically configures:

* DataSource
* JPA
* Tomcat
* Security

based on dependencies.

---

# 🧠 3. IOC Container (Core of Spring)

## 📘 IOC = Inversion of Control

Spring manages object creation instead of developer.

---

# 🔥 Traditional Java

```java id="jlwmm4"
OrderService service =
    new OrderService();
```

---

# 🔥 Spring Boot

```java id="nkgmrb"
@Autowired
private OrderService service;
```

---

# 🎯 Benefit

* Loose coupling
* Better testing
* Dependency management

---

# 🧩 4. Dependency Injection (DI)

## 📘 Definition

Inject dependencies automatically.

---

# 🔹 Constructor Injection (Recommended)

```java id="d1gv5p"
@Service
public class OrderService {

    private final PaymentService paymentService;

    public OrderService(
        PaymentService paymentService) {

        this.paymentService = paymentService;
    }
}
```

---

# 🎯 Why Important?

* Easier unit testing
* Better immutability
* Cleaner architecture

---

# 🌐 5. DispatcherServlet (Heart of Spring MVC)

## 📘 Front Controller Pattern

All requests first come here.

---

# 🔥 Flow

```text id="2m6l88"
HTTP Request
      ↓
DispatcherServlet
      ↓
Handler Mapping
      ↓
Controller
      ↓
Response
```

---

# 🔹 Example Controller

```java id="ls4qgl"
@RestController
@RequestMapping("/orders")
public class OrderController {

    @GetMapping("/{id}")
    public String getOrder(
        @PathVariable Long id) {

        return "Order Found";
    }
}
```

---

# 🧠 Internal Processing

```text id="ph8xzt"
DispatcherServlet
    ↓
Find Matching URL
    ↓
Call Controller Method
    ↓
Serialize Response JSON
```

---

# 🔥 6. Spring Bean Lifecycle

---

# 📘 Bean Lifecycle

```text id="4ld9hx"
Bean Creation
    ↓
Dependency Injection
    ↓
@PostConstruct
    ↓
Bean Ready
    ↓
Destroy
```

---

# 🔹 Example

```java id="e3lcvq"
@Component
public class CacheLoader {

    @PostConstruct
    public void init() {

        System.out.println("Cache Loaded");
    }
}
```

---

# 🧠 7. Spring Boot Auto Configuration

## 📘 Purpose

Automatically configure components.

---

# 🔥 Example

If dependency exists:

```xml id="7jlw3v"
spring-boot-starter-data-jpa
```

Spring Boot automatically configures:

* Hibernate
* DataSource
* EntityManager
* TransactionManager

---

# 🎯 Benefit

No XML configuration required.

---

# 🗄️ 8. Spring Data JPA Architecture

---

# 🔥 Flow

```text id="h9z33r"
Controller
   ↓
Service
   ↓
Repository
   ↓
Hibernate
   ↓
Database
```

---

# 🔹 Repository Example

```java id="sjh4a0"
@Repository
public interface OrderRepository
extends JpaRepository<Order, Long> {
}
```

---

# 🧠 Internally

Spring creates implementation dynamically.

---

# 🎯 Benefit

No boilerplate SQL.

---

# 🔥 9. Hibernate Internal Architecture

## 📘 Hibernate = ORM Framework

Maps:

```text id="x1jlha"
Java Objects ↔ Database Tables
```

---

# 🔹 Entity Example

```java id="4q3ay6"
@Entity
public class Order {

    @Id
    private Long id;

    private String product;
}
```

---

# 🔥 Internal Flow

```text id="vjlwm6"
Entity
   ↓
Hibernate Session
   ↓
SQL Generation
   ↓
Database
```

---

# 🎯 Benefit

Object-oriented DB interaction.

---

# 🌐 10. Embedded Server Architecture

Spring Boot includes:

* Tomcat
* Jetty
* Undertow

---

# 🔥 Flow

```text id="12ohah"
Client Request
     ↓
Embedded Tomcat
     ↓
Spring MVC
```

---

# 🎯 Benefit

No external server deployment needed.

---

# ⚡ 11. Spring Boot Microservices Architecture

```text id="xq4s9k"
Angular UI
     ↓
API Gateway
     ↓
Order Service
Payment Service
Inventory Service
     ↓
Kafka
     ↓
Oracle/Postgres
```

---

# 🔥 Common Enterprise Components

| Component     | Usage             |
| ------------- | ----------------- |
| Eureka        | Service discovery |
| Config Server | Central config    |
| Kafka         | Event-driven      |
| Redis         | Caching           |
| Resilience4j  | Circuit breaker   |
| ELK           | Logging           |
| Prometheus    | Monitoring        |

---

# 🛡️ 12. Spring Security Internal Flow

---

# 🔥 Authentication Flow

```text id="3kkt2r"
Client Request
     ↓
Security Filter Chain
     ↓
JWT Validation
     ↓
Authentication Manager
     ↓
Controller
```

---

# 🔹 JWT Security Example

```java id="n7ynwy"
http
  .authorizeHttpRequests()
  .anyRequest().authenticated()
  .and()
  .oauth2ResourceServer()
  .jwt();
```

---

# ☸️ 13. Spring Boot + Kubernetes Architecture

```text id="5xdy1s"
Docker Container
      ↓
Kubernetes Pod
      ↓
Service
      ↓
Ingress
```

---

# 🔥 Production Features

| Feature         | Purpose            |
| --------------- | ------------------ |
| Health Check    | Monitoring         |
| Liveness Probe  | Pod restart        |
| Readiness Probe | Traffic handling   |
| ConfigMap       | External config    |
| Secrets         | Secure credentials |

---

# 🧠 Real Request Lifecycle (Very Important)

---

# 🔥 End-to-End Flow

```text id="lwh3gw"
Client
   ↓
Tomcat
   ↓
DispatcherServlet
   ↓
Controller
   ↓
Service
   ↓
Repository
   ↓
Hibernate
   ↓
Database
```

---

# 🎯 Real Interview Explanation

> “Spring Boot internally uses IOC and Dependency Injection to manage beans and application lifecycle. Requests are handled by DispatcherServlet, routed to controllers, processed by services, and persisted through JPA/Hibernate repositories. AutoConfiguration reduces boilerplate setup, while embedded Tomcat simplifies deployment. In enterprise systems, Spring Boot integrates with Kafka, Redis, Kubernetes, and OAuth2 to build scalable microservices.”

---

# 🔥 Frequently Asked Interview Questions

---

## ❓ Difference between Spring and Spring Boot?

| Spring          | Spring Boot        |
| --------------- | ------------------ |
| Manual config   | Auto configuration |
| External server | Embedded server    |
| More setup      | Rapid development  |

---

## ❓ What is IOC?

👉 Spring manages object lifecycle instead of developer.

---

## ❓ Why Constructor Injection preferred?

* Immutability
* Easier testing
* Better design

---

## ❓ What is DispatcherServlet?

👉 Front controller handling all requests.

---

## ❓ How does Spring Boot auto configuration work?

👉 Uses:

* classpath scanning
* starter dependencies
* conditional annotations

---

