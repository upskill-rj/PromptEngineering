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
