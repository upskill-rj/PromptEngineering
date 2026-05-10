# ORM, JPA, Hibernate & Related Java Concepts (Interview Guide)

For your experience level, interviewers usually expect:

* ORM fundamentals
* JPA architecture
* Hibernate internals
* Entity lifecycle
* Relationships
* Performance optimization
* Transaction management
* Enterprise best practices

Your profile already aligns strongly with:

* Spring Boot
* Hibernate
* JPA
* Oracle DB
* Microservices
* Enterprise applications 

---

# 1. What is ORM?

## ORM = Object Relational Mapping

Object-Relational Mapping

ORM is a technique that maps:

* Java Objects ↔ Database Tables

Meaning:

| Java     | Database |
| -------- | -------- |
| Class    | Table    |
| Object   | Row      |
| Variable | Column   |

---

# 2. Why ORM is Needed?

Without ORM:

* Developers write huge SQL manually
* JDBC boilerplate increases
* Object-to-table conversion is manual

ORM solves:

* Automatic mapping
* Less SQL
* Faster development
* Database abstraction
* Cleaner code

---

# 3. Without ORM (JDBC Example)

```java id="rjlwm1"
Connection con = DriverManager.getConnection(...);

PreparedStatement ps =
con.prepareStatement(
"insert into employee values(?,?)");

ps.setInt(1,101);
ps.setString(2,"Rahul");
```

Too much boilerplate.

---

# 4. With ORM (Hibernate/JPA)

```java id="jlwmw1"
Employee emp = new Employee();

emp.setId(101);
emp.setName("Rahul");

repository.save(emp);
```

ORM automatically generates SQL.

---

# 5. What is JPA?

## JPA = Java Persistence API

Jakarta Persistence

JPA is:

> A specification/API for ORM in Java.

Important:

* JPA is NOT implementation
* JPA defines rules/interfaces

---

# 6. What is Hibernate?

Hibernate ORM

Hibernate is:

> Most popular implementation of JPA.

---

# 7. Relationship Between ORM, JPA, Hibernate

```text id="jlwm3v"
ORM = Technique

JPA = Specification

Hibernate = Implementation
```

---

# 8. ORM Architecture Flow

```text id="jlwm8e"
Java Object
    ↓
JPA
    ↓
Hibernate
    ↓
SQL Generation
    ↓
Database
```

---

# 9. JPA Core Interfaces

| Interface         | Purpose                     |
| ----------------- | --------------------------- |
| EntityManager     | Main persistence operations |
| EntityTransaction | Transaction handling        |
| Query             | Execute JPQL/SQL            |
| PersistenceUnit   | Configuration               |

---

# 10. Important JPA Annotations

| Annotation      | Purpose           |
| --------------- | ----------------- |
| @Entity         | Table mapping     |
| @Table          | Table name        |
| @Id             | Primary key       |
| @Column         | Column mapping    |
| @GeneratedValue | Auto-generated ID |
| @Transient      | Ignore field      |
| @OneToMany      | Relationship      |
| @ManyToOne      | Relationship      |
| @JoinColumn     | Foreign key       |

---

# 11. Entity Example

```java id="2jlwmk"
@Entity
@Table(name="EMPLOYEE")
public class Employee {

    @Id
    @GeneratedValue
    private Long id;

    @Column(name="EMP_NAME")
    private String name;
}
```

---

# 12. What is Entity?

An entity is:

> A Java class mapped to database table.

---

# 13. What is Persistence?

Persistence means:

> Storing Java object data permanently into database.

---

# 14. Entity Lifecycle (VERY IMPORTANT)

## States of Entity

```text id="jlwm8z"
Transient
Persistent
Detached
Removed
```

---

## A. Transient

Object created but not saved.

```java id="jlwm6r"
Employee emp = new Employee();
```

---

## B. Persistent

Managed by Hibernate session.

```java id="6jlwmv"
session.save(emp);
```

---

## C. Detached

Session closed but object exists.

---

## D. Removed

Marked for deletion.

---

# 15. Hibernate Session

Session:

> Connection between Java app and database.

Used for:

* save
* update
* delete
* fetch

---

# 16. Hibernate SessionFactory

Creates Session objects.

Usually:

* One SessionFactory per application

---

# 17. JPA Repository (Spring Boot)

```java id="jlwm5c"
public interface EmployeeRepository
       extends JpaRepository<Employee, Long> {

}
```

Provides:

* save()
* findAll()
* delete()
* findById()

Automatically.

---

# 18. Hibernate Automatically Generates SQL

Example:

```java id="5jlwmg"
repository.save(emp);
```

Hibernate internally creates:

```sql id="jlwmn2"
INSERT INTO EMPLOYEE ...
```

---

# 19. JPQL

## JPQL = Java Persistence Query Language

Similar to SQL but works on entities.

Example:

```java id="jlwm1y"
SELECT e FROM Employee e
```

Uses:

* Entity names
* Object fields

NOT table names.

---

# 20. Native SQL Query

```java id="jlwm0g"
@Query(value="SELECT * FROM EMPLOYEE",
       nativeQuery=true)
```

Used for:

* Complex SQL
* Performance optimization

---

# 21. Fetch Types

| Type  | Meaning          |
| ----- | ---------------- |
| EAGER | Load immediately |
| LAZY  | Load when needed |

---

## Example

```java id="jlwm9e"
@OneToMany(fetch = FetchType.LAZY)
```

---

# 22. Lazy Loading

Data loads only when accessed.

Improves:

* Performance
* Memory usage

---

# 23. Cascade Types

| Cascade | Purpose        |
| ------- | -------------- |
| ALL     | All operations |
| PERSIST | Save child     |
| REMOVE  | Delete child   |

---

# 24. Relationship Mapping

---

## A. One-to-One

```java id="jlwmm7"
@OneToOne
```

Example:

* User ↔ Passport

---

## B. One-to-Many

```java id="jlwm5j"
@OneToMany
```

Example:

* Department → Employees

---

## C. Many-to-One

```java id="3jlwmu"
@ManyToOne
```

Example:

* Many employees belong to one department

---

## D. Many-to-Many

```java id="jlwmr1"
@ManyToMany
```

Example:

* Students ↔ Courses

---

# 25. Transactions

## @Transactional

```java id="9jlwmd"
@Transactional
```

Ensures:

* Commit on success
* Rollback on failure

ACID properties maintained.

---

# 26. First-Level Cache

Hibernate session cache.

Default enabled.

Improves performance.

---

# 27. Second-Level Cache

Shared across sessions.

Technologies:

* EhCache
* Redis
* Hazelcast

---

# 28. N+1 Query Problem

Common Hibernate issue.

Example:

* One query for departments
* N queries for employees

Causes:

* Performance degradation

Solutions:

* JOIN FETCH
* EntityGraph
* Batch fetching

---

# 29. Hibernate vs JDBC

| Hibernate      | JDBC             |
| -------------- | ---------------- |
| ORM framework  | Low-level API    |
| Less code      | More boilerplate |
| Auto SQL       | Manual SQL       |
| DB independent | DB specific      |

---

# 30. JPA vs Hibernate

| JPA           | Hibernate                |
| ------------- | ------------------------ |
| Specification | Implementation           |
| Standard API  | Actual framework         |
| Portable      | Vendor specific features |

---

# 31. Spring Data JPA

Spring Data JPA

Simplifies JPA further.

Provides:

* Repository abstraction
* Auto query generation
* Pagination
* Sorting

---

# 32. Repository Types

| Repository                 | Purpose          |
| -------------------------- | ---------------- |
| CrudRepository             | Basic CRUD       |
| PagingAndSortingRepository | Pagination       |
| JpaRepository              | Full JPA support |

---

# 33. Query Method Example

```java id="jlwm7k"
findByName(String name)
```

Spring automatically creates query.

---

# 34. Common Hibernate Interview Questions

---

## Q1. Difference Between save() and persist()?

| save()             | persist()    |
| ------------------ | ------------ |
| Returns ID         | No return    |
| Hibernate specific | JPA standard |

---

## Q2. Difference Between get() and load()?

| get()            | load()           |
| ---------------- | ---------------- |
| Immediate DB hit | Lazy proxy       |
| Returns null     | Throws exception |

---

## Q3. What is LazyInitializationException?

Occurs when:

* Lazy object accessed after session closed.

---

## Q4. What is Dirty Checking?

Hibernate automatically detects object changes and updates DB.

---

# 35. Enterprise Best Practices

| Area         | Best Practice       |
| ------------ | ------------------- |
| Transactions | Use service layer   |
| Fetching     | Prefer LAZY         |
| Queries      | Avoid N+1           |
| Performance  | Pagination          |
| DTO          | Use projections     |
| Security     | Avoid SQL injection |

---

# 36. Real Enterprise Flow

In your projects:

```text id="jlwm9z"
Controller
   ↓
Service
   ↓
JPA Repository
   ↓
Hibernate ORM
   ↓
Oracle Database
```

Strongly aligned with your:

* Spring Boot
* Hibernate
* Oracle
* Enterprise microservices experience 

---

# 37. Architect-Level Interview Answer

> “We used JPA with Hibernate as ORM layer in Spring Boot microservices to simplify database interaction, reduce JDBC boilerplate, and improve maintainability. We implemented entity relationships, transaction management, lazy loading, caching, and optimized queries for scalable enterprise applications.”

---

# 38. Advanced Topics for Senior Interviews

Know these:

* Entity lifecycle
* Persistence context
* Optimistic locking
* Pessimistic locking
* Batch processing
* JPQL vs Criteria API
* Hibernate caching
* Performance tuning
* Multi-tenancy
* Audit logging

---

# 39. Simple Final Definitions

## ORM

> Technique for mapping Java objects to database tables.

---

## JPA

> Java ORM specification/API.

---

## Hibernate

> Popular implementation of JPA.

---

## Spring Data JPA

> Spring abstraction layer over JPA/Hibernate.
