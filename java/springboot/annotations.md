# What is Annotation in Java/Spring Boot?

## Simple Definition

An annotation is:

> Metadata (information) added to Java code that gives instructions to compiler, framework, or runtime environment.

Annotations do not directly execute business logic.
They provide configuration or behavior information.

---

# Real-Life Analogy

Think of annotation like:

* Sticky note on a file
* Label on an object
* Instruction tag

Example:

```text id="5qg90g"
"Fragile"
"Handle with care"
"Priority"
```

Similarly in Java:

```java id="h7zjlwm"
@Service
public class EmployeeService {
}
```

This tells Spring:

> “This class is a service component managed by Spring.”

---

# Basic Java Annotation Example

```java id="jlwmm1"
@Override
public String toString() {
    return "Hello";
}
```

`@Override` tells compiler:

> This method overrides parent class method.

---

# Why Annotations are Used?

Annotations reduce:

* XML configuration
* Boilerplate code
* Manual setup

They improve:

* Readability
* Maintainability
* Development speed

---

# Before Annotation (Old Spring XML)

```xml id="jlwmk0"
<bean id="employeeService"
      class="com.app.EmployeeService"/>
```

---

# After Annotation

```java id="jlwm7m"
@Service
public class EmployeeService {
}
```

Much simpler.

---

# Common Types of Annotations

| Type                | Example       |
| ------------------- | ------------- |
| Java Annotation     | @Override     |
| Spring Annotation   | @Service      |
| JPA Annotation      | @Entity       |
| Testing Annotation  | @Test         |
| Security Annotation | @PreAuthorize |

---

# Spring Boot Annotation Example

```java id="jlwm4d"
@RestController
@RequestMapping("/api")
public class EmployeeController {

}
```

Meaning:

* `@RestController`
  → REST API controller

* `@RequestMapping`
  → Base URL mapping

---

# How Annotations Work Internally?

Frameworks use:

* Reflection
* Runtime scanning

Spring scans annotations during startup.

Example:

```java id="4jlwmm"
@Service
```

Spring:

* Detects class
* Creates object (bean)
* Stores in IOC container

---

# Annotation Syntax

```java id="jlwmx8"
@AnnotationName
```

OR

```java id="5jlwm0"
@AnnotationName(value="test")
```

---

# Categories of Spring Annotations

| Category             | Examples             |
| -------------------- | -------------------- |
| Stereotype           | @Component, @Service |
| REST API             | @RestController      |
| Dependency Injection | @Autowired           |
| Database/JPA         | @Entity              |
| Transaction          | @Transactional       |
| Security             | @PreAuthorize        |
| Configuration        | @Bean                |

---

# Most Common Spring Boot Annotations

| Annotation             | Purpose                |
| ---------------------- | ---------------------- |
| @SpringBootApplication | Main application       |
| @RestController        | REST API               |
| @Service               | Business logic         |
| @Repository            | DB layer               |
| @Autowired             | Inject dependency      |
| @Entity                | Database table mapping |

---

# Benefits of Annotations

## 1. Less Configuration

No large XML files.

---

## 2. Cleaner Code

Readable and modern.

---

## 3. Faster Development

Framework auto-configures components.

---

## 4. Better Maintainability

Easy to manage enterprise applications.

---

# Interview Answer (Best Version)

> “Annotations are metadata added to Java code that provide instructions to the compiler or framework at compile time or runtime. In Spring Boot, annotations simplify configuration, dependency injection, REST API creation, transaction management, and component scanning, reducing boilerplate code and improving maintainability.”

---

# Architect-Level Answer

> “Annotations enable declarative programming in enterprise applications. Instead of manual XML configuration, frameworks like Spring Boot use annotations combined with reflection and IOC containers to automatically manage beans, transactions, security, REST APIs, and application configuration.”

---

# Common Interview Questions

## Q1. Are annotations executable code?

Answer:

> No. They are metadata/instructions interpreted by compiler/framework/runtime.

---

## Q2. How Spring reads annotations?

Answer:

> Spring uses reflection and component scanning during application startup.

---

## Q3. Difference Between Annotation and Interface?

| Annotation             | Interface        |
| ---------------------- | ---------------- |
| Metadata               | Contract         |
| Provides configuration | Defines behavior |

---

# Simple One-Line Definition

> “Annotations are metadata tags in Java used to provide configuration or behavioral instructions to frameworks, compiler, or runtime.”



================================================================

# Spring Boot Important Annotations (Interview Quick Revision)

---

# 1. @SpringBootApplication

```java id="jlwmxv"
@SpringBootApplication
```

Main Spring Boot annotation.
Combines:

* `@Configuration`
* `@EnableAutoConfiguration`
* `@ComponentScan`

---

# 2. @RestController

```java id="4ozxln"
@RestController
```

Used to create REST APIs.
Returns JSON/XML response directly.

---

# 3. @Controller

```java id="koc0d4"
@Controller
```

Used in Spring MVC applications.
Returns JSP/HTML views.

---

# 4. @Service

```java id="hnjlwm"
@Service
```

Marks business logic layer class.
Managed by Spring IOC container.

---

# 5. @Repository

```java id="5a8qxy"
@Repository
```

Marks DAO/database access layer.
Provides DB exception translation.

---

# 6. @Component

```java id="o0fxsz"
@Component
```

Generic Spring-managed bean.
Used when class doesn’t fit service/repository/controller.

---

# 7. @Autowired

```java id="s1cs39"
@Autowired
```

Performs dependency injection automatically.
Injects Spring-managed beans.

---

# 8. @Qualifier

```java id="x0l5m6"
@Qualifier("beanName")
```

Used with `@Autowired` to specify exact bean when multiple beans exist.

---

# 9. @Bean

```java id="54gb8p"
@Bean
```

Used inside configuration class to manually create Spring beans.

---

# 10. @Configuration

```java id="jlwmww"
@Configuration
```

Marks class as Spring configuration class.
Contains bean definitions.

---

# 11. @Value

```java id="9blh71"
@Value("${server.port}")
```

Reads values from properties/yaml files.

---

# 12. @PropertySource

```java id="wyapkt"
@PropertySource("app.properties")
```

Loads external property file.

---

# 13. @ComponentScan

```java id="u1z57r"
@ComponentScan
```

Tells Spring where to scan components/beans.

---

# 14. @EnableAutoConfiguration

```java id="mw9b48"
@EnableAutoConfiguration
```

Automatically configures Spring Boot application based on dependencies.

---

# 15. @RequestMapping

```java id="46ybxh"
@RequestMapping("/api")
```

Maps HTTP requests to controller methods/classes.

---

# 16. @GetMapping

```java id="0zv8wx"
@GetMapping("/users")
```

Handles HTTP GET requests.

---

# 17. @PostMapping

```java id="5j9j7s"
@PostMapping("/save")
```

Handles HTTP POST requests.

---

# 18. @PutMapping

```java id="j5tmny"
@PutMapping("/update")
```

Handles HTTP PUT requests.

---

# 19. @DeleteMapping

```java id="f8yab9"
@DeleteMapping("/delete")
```

Handles HTTP DELETE requests.

---

# 20. @PathVariable

```java id="rq8k5n"
@PathVariable Long id
```

Reads value from URL path.

Example:

```bash id="6w0i6r"
/users/10
```

---

# 21. @RequestParam

```java id="pd0p4z"
@RequestParam String name
```

Reads query parameter from URL.

Example:

```bash id="3k3ml4"
/users?name=rahul
```

---

# 22. @RequestBody

```java id="7lclv7"
@RequestBody Employee emp
```

Converts incoming JSON request into Java object.

---

# 23. @ResponseBody

```java id="qklnz4"
@ResponseBody
```

Returns data directly instead of view.

---

# 24. @CrossOrigin

```java id="mkb0lb"
@CrossOrigin
```

Enables CORS access from frontend applications.

---

# 25. @ExceptionHandler

```java id="km9g2v"
@ExceptionHandler(Exception.class)
```

Handles specific exceptions globally/local to controller.

---

# 26. @ControllerAdvice

```java id="9ux65r"
@ControllerAdvice
```

Global exception handling across all controllers.

---

# 27. @Entity

```java id="f1b4r7"
@Entity
```

Marks Java class as database entity/table.

---

# 28. @Table

```java id="8r6v0q"
@Table(name="EMPLOYEE")
```

Maps entity to database table.

---

# 29. @Id

```java id="iyf2n6"
@Id
```

Marks primary key field.

---

# 30. @GeneratedValue

```java id="psyljlwm"
@GeneratedValue
```

Automatically generates primary key value.

---

# 31. @Column

```java id="c8jlwm"
@Column(name="EMP_NAME")
```

Maps field to DB column.

---

# 32. @Transient

```java id="3o5ecy"
@Transient
```

Ignores field from database persistence.

---

# 33. @OneToOne

```java id="jhzr2n"
@OneToOne
```

Defines one-to-one entity relationship.

---

# 34. @OneToMany

```java id="bhmjlwm"
@OneToMany
```

Defines one-to-many relationship.

---

# 35. @ManyToOne

```java id="vjlwm6"
@ManyToOne
```

Defines many-to-one relationship.

---

# 36. @ManyToMany

```java id="jlwmc6"
@ManyToMany
```

Defines many-to-many relationship.

---

# 37. @JoinColumn

```java id="6wjlwm"
@JoinColumn(name="dept_id")
```

Specifies foreign key column.

---

# 38. @Transactional

```java id="6cjlwm"
@Transactional
```

Manages database transaction automatically.

Rollback occurs on failure.

---

# 39. @EnableScheduling

```java id="jlwm5g"
@EnableScheduling
```

Enables scheduled tasks.

---

# 40. @Scheduled

```java id="jlwm1q"
@Scheduled(cron="0 0 * * * ?")
```

Runs task automatically at fixed interval/time.

---

# 41. @Async

```java id="jlwmv4"
@Async
```

Executes method asynchronously in separate thread.

---

# 42. @EnableAsync

```java id="jlwmkq"
@EnableAsync
```

Enables async processing.

---

# 43. @Cacheable

```java id="jlwm0v"
@Cacheable("users")
```

Caches method result for better performance.

---

# 44. @EnableCaching

```java id="jlwmau"
@EnableCaching
```

Enables Spring cache support.

---

# 45. @Valid

```java id="jlwmx1"
@Valid
```

Triggers validation on request object.

---

# 46. @NotNull

```java id="8jlwm8"
@NotNull
```

Field cannot be null.

---

# 47. @Size

```java id="jlwmz5"
@Size(min=2,max=20)
```

Validates string/list size.

---

# 48. @Email

```java id="jlwmcv"
@Email
```

Validates email format.

---

# 49. @SpringBootTest

```java id="jlwm6g"
@SpringBootTest
```

Loads full Spring Boot context for testing.

---

# 50. @MockBean

```java id="jlwm7z"
@MockBean
```

Creates mock bean during unit testing.

---

# Security Annotations

---

# 51. @EnableWebSecurity

```java id="jlwm7x"
@EnableWebSecurity
```

Enables Spring Security configuration.

---

# 52. @PreAuthorize

```java id="6jlwmu"
@PreAuthorize("hasRole('ADMIN')")
```

Restricts method access based on roles.

---

# 53. @Secured

```java id="jlwm2v"
@Secured("ROLE_ADMIN")
```

Secures methods with roles.

---

# 54. @EnableMethodSecurity

```java id="jlwm9l"
@EnableMethodSecurity
```

Enables method-level security.

---

# Spring Cloud / Microservices Annotations

---

# 55. @EnableEurekaClient

```java id="jlwm8l"
@EnableEurekaClient
```

Registers microservice with Eureka server.

---

# 56. @FeignClient

```java id="9jlwm8"
@FeignClient(name="user-service")
```

Simplifies REST API communication between microservices.

---

# 57. @EnableFeignClients

```java id="jlwm48"
@EnableFeignClients
```

Enables Feign clients.

---

# 58. @RefreshScope

```java id="jlwmr8"
@RefreshScope
```

Refreshes configuration dynamically without restart.

---

# 59. @CircuitBreaker

```java id="jlwm0n"
@CircuitBreaker(name="paymentService")
```

Prevents cascading failures in microservices.

---

# 60. @Retry

```java id="jlwm1e"
@Retry(name="serviceRetry")
```

Retries failed service calls automatically.

---

# Architect-Level Interview Answer

> “Spring Boot annotations simplify enterprise application development by enabling declarative configuration, dependency injection, REST API development, transaction management, validation, security, scheduling, caching, and microservices integration with minimal boilerplate code.”

---

# Most Important Annotations for Interviews

Focus heavily on these:

```text id="zngjlwm"
@SpringBootApplication
@RestController
@Service
@Repository
@Autowired
@RequestMapping
@GetMapping
@PostMapping
@Entity
@Transactional
@Component
@Configuration
@Bean
@RequestBody
@PathVariable
@RequestParam
```

These are asked in almost every Spring Boot interview.
