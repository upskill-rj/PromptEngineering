# Basic Database, SQL & PL/SQL Interview Questions and Answers

# 🔷 Database Interview Questions

---

## 1. What is a database?

A database is an organized collection of data used to store, manage, and retrieve information efficiently.

### Example:

* Banking system storing customer and transaction data
* E-commerce storing products and orders

---

## 2. What are the different types of databases?

| Type          | Example       | Use Case        |
| ------------- | ------------- | --------------- |
| Relational DB | Oracle, MySQL | Banking, ERP    |
| NoSQL DB      | MongoDB       | Flexible schema |
| Key-Value DB  | Redis         | Caching         |
| Graph DB      | Neo4j         | Social network  |
| Column DB     | Cassandra     | Big data        |

---

## 3. Difference between RDBMS and NoSQL?

| RDBMS                 | NoSQL                                 |
| --------------------- | ------------------------------------- |
| Structured tables     | Flexible schema                       |
| SQL language          | JSON/document                         |
| ACID compliance       | High scalability                      |
| Best for transactions | Best for large-scale distributed apps |

---

## 4. What is a table?

A table stores data in rows and columns.

### Example:

| EMP_ID | NAME  |
| ------ | ----- |
| 101    | Rahul |

---

## 5. What is a primary key?

A primary key uniquely identifies each row in a table.

### Example:

```sql id="jtw7jk"
EMP_ID PRIMARY KEY
```

---

## 6. What is a foreign key?

A foreign key creates a relationship between two tables.

### Example:

```sql id="f7l15r"
EMPLOYEE.DEPT_ID → DEPARTMENT.ID
```

---

## 7. What is normalization?

Normalization organizes data to reduce redundancy and improve consistency.

---

## 8. What are normalization types?

| Type | Purpose                      |
| ---- | ---------------------------- |
| 1NF  | Atomic values                |
| 2NF  | Remove partial dependency    |
| 3NF  | Remove transitive dependency |

---

## 9. What is denormalization?

Combining tables to improve read performance.

Used in:

* Reporting systems
* Analytics systems

---

## 10. What is indexing?

Indexes improve query performance.

### Example:

```sql id="78xj2u"
CREATE INDEX IDX_NAME
ON EMPLOYEE(NAME);
```

---

## 11. What is database transaction?

A transaction is a logical unit of work.

### Example:

Money transfer between accounts.

---

## 12. What are ACID properties?

| Property    | Meaning           |
| ----------- | ----------------- |
| Atomicity   | All or nothing    |
| Consistency | Valid state       |
| Isolation   | Concurrent safety |
| Durability  | Permanent storage |

---

# 🔷 SQL Interview Questions

---

# 13. What is SQL?

SQL stands for Structured Query Language used to interact with relational databases.

---

# 14. What are different types of SQL commands?

| Type | Purpose           |
| ---- | ----------------- |
| DDL  | Structure         |
| DML  | Data manipulation |
| DQL  | Query             |
| DCL  | Security          |
| TCL  | Transactions      |

---

# 15. What is DDL?

DDL defines database objects.

### Commands:

* CREATE
* ALTER
* DROP
* TRUNCATE

---

# 16. Difference between DELETE, DROP, and TRUNCATE?

| DELETE         | TRUNCATE         | DROP                 |
| -------------- | ---------------- | -------------------- |
| Removes rows   | Removes all rows | Removes object       |
| Can rollback   | Minimal logging  | Deletes structure    |
| WHERE possible | No WHERE         | Entire table removed |

---

# 17. What is DML?

DML manipulates records.

### Commands:

* INSERT
* UPDATE
* DELETE
* MERGE

---

# 18. What is SELECT query?

Used to retrieve data.

### Example:

```sql id="yg7j7l"
SELECT * FROM EMPLOYEE;
```

---

# 19. Difference between WHERE and HAVING?

| WHERE           | HAVING         |
| --------------- | -------------- |
| Filters rows    | Filters groups |
| Before GROUP BY | After GROUP BY |

---

# 20. What is JOIN?

JOIN combines records from multiple tables.

---

# 21. Types of joins?

| Join       | Purpose        |
| ---------- | -------------- |
| INNER JOIN | Matching rows  |
| LEFT JOIN  | All left rows  |
| RIGHT JOIN | All right rows |
| FULL JOIN  | All rows       |

---

# 22. Example of INNER JOIN?

```sql id="d6y5x9"
SELECT E.NAME,D.DEPT_NAME
FROM EMPLOYEE E
INNER JOIN DEPARTMENT D
ON E.DEPT_ID=D.ID;
```

---

# 23. What is a view?

A virtual table based on SQL query.

### Example:

```sql id="k1h7u6"
CREATE VIEW ACTIVE_EMP AS
SELECT * FROM EMPLOYEE
WHERE STATUS='ACTIVE';
```

---

# 24. What is a stored procedure?

Reusable SQL program stored in DB.

---

# 25. What is a function?

Returns a value.

### Example:

```sql id="9lbj0m"
SELECT COUNT(*) FROM EMPLOYEE;
```

---

# 26. Difference between procedure and function?

| Procedure            | Function            |
| -------------------- | ------------------- |
| May not return value | Must return value   |
| Used for operations  | Used in expressions |

---

# 27. What is a trigger?

Automatically executes on database events.

### Example:

* Audit logging
* Auto notifications

---

# 28. What is a cursor?

Processes rows one by one.

Used in:

* Batch jobs
* ETL processing

---

# 29. What is GROUP BY?

Groups rows with same values.

### Example:

```sql id="7xqg76"
SELECT DEPT_ID,COUNT(*)
FROM EMPLOYEE
GROUP BY DEPT_ID;
```

---

# 30. What is ORDER BY?

Sorts data.

### Example:

```sql id="6uhf9w"
SELECT * FROM EMPLOYEE
ORDER BY SALARY DESC;
```

---

# 31. What is UNION?

Combines results of multiple queries.

---

# 32. Difference between UNION and UNION ALL?

| UNION              | UNION ALL        |
| ------------------ | ---------------- |
| Removes duplicates | Keeps duplicates |
| Slower             | Faster           |

---

# 33. What is subquery?

Query inside another query.

### Example:

```sql id="0e40ae"
SELECT NAME
FROM EMPLOYEE
WHERE SALARY >
(
SELECT AVG(SALARY)
FROM EMPLOYEE
);
```

---

# 34. What is a composite key?

Primary key using multiple columns.

---

# 35. What is SQL injection?

Security vulnerability caused by unsafe SQL queries.

### Prevention:

* Prepared statements
* Parameterized queries

---

# 🔷 PL/SQL Interview Questions

---

# 36. What is PL/SQL?

PL/SQL is Oracle’s procedural extension to SQL.

Supports:

* Loops
* Conditions
* Variables
* Exception handling

---

# 37. Structure of PL/SQL block?

```sql id="v86v1e"
DECLARE
BEGIN
EXCEPTION
END;
```

---

# 38. What are PL/SQL collections?

Stores multiple values.

Types:

* Associative array
* Nested table
* VARRAY

---

# 39. What is exception handling in PL/SQL?

Used to handle runtime errors.

### Example:

```sql id="7m72lf"
EXCEPTION
WHEN NO_DATA_FOUND THEN
DBMS_OUTPUT.PUT_LINE('No Data');
```

---

# 40. What are explicit and implicit cursors?

| Implicit       | Explicit               |
| -------------- | ---------------------- |
| Automatic      | User-defined           |
| Simple queries | Complex row processing |

---

# 41. What is BULK COLLECT?

Fetches multiple rows together for performance improvement.

---

# 42. What is FORALL?

Bulk DML operation for better performance.

---

# 43. What is package in PL/SQL?

Group of procedures/functions.

Benefits:

* Reusability
* Modularity
* Security

---

# 44. What is autonomous transaction?

Independent transaction inside another transaction.

Used for:

* Audit logging

---

# 45. Difference between COMMIT and ROLLBACK?

| COMMIT        | ROLLBACK       |
| ------------- | -------------- |
| Saves changes | Undoes changes |

---

# 🔷 Advanced SQL Questions

---

# 46. What is partitioning?

Splits large tables into smaller partitions.

Used in:

* Banking
* Telecom
* Large ERP systems

---

# 47. What is sharding?

Distributes database across servers.

---

# 48. What is replication?

Copies database to multiple servers for HA.

---

# 49. What is deadlock?

Two transactions waiting for each other indefinitely.

---

# 50. What is query optimization?

Improving SQL performance using:

* Indexing
* Execution plans
* Partitioning

---

# 🔷 Real-Time Interview Scenario Questions

---

# 51. How do you optimize slow SQL query?

### Answer:

* Analyze execution plan
* Add indexes
* Avoid full table scans
* Optimize joins
* Use partitioning
* Reduce nested subqueries

---

# 52. How do you handle millions of records?

### Answer:

* Partitioning
* Indexing
* Batch processing
* Parallel execution
* Caching

---

# 53. How do you ensure database security?

### Answer:

* RBAC
* Encryption
* Auditing
* Parameterized queries
* Secure credentials

---

# 54. How is SQL used in microservices?

### Answer:

Each microservice can own its own database.

Example:

```text id="11m13u"
User Service → PostgreSQL
Order Service → MySQL
Cache → Redis
```

---

# 55. Explain SQL in enterprise application architecture.

```text id="w1n67n"
Frontend
   ↓
Spring Boot APIs
   ↓
Hibernate/JPA
   ↓
SQL Queries
   ↓
Oracle/PostgreSQL
```

---

# 🔷 Cloud Database Interview Questions

---

# 56. What is managed database service?

Cloud provider manages:

* Backup
* Scaling
* Patching
* HA

Examples:

* Amazon RDS
* Azure SQL Database
* Oracle Autonomous Database

---

# 57. What is connection pooling?

Reusing DB connections to improve performance.

---

# 58. What is ORM?

ORM maps objects to database tables.

Examples:

* Hibernate
* JPA

---

# 🔷 AI + Database Questions

---

# 59. How databases are used in AI systems?

| AI Area         | Database Usage   |
| --------------- | ---------------- |
| RAG             | Store embeddings |
| Chat history    | NoSQL DB         |
| Analytics       | SQL DB           |
| Semantic search | Vector DB        |

---

# 60. What is vector database?

Stores vector embeddings for AI semantic search.

Examples:

* Pinecone
* FAISS

---

# 🔷 Final Interview Summary Answer

> “I have strong understanding of relational databases, SQL, and PL/SQL including schema design, joins, indexing, normalization, stored procedures, triggers, transactions, and query optimization. I have worked on enterprise applications involving Oracle/PostgreSQL databases, performance tuning, batch processing, and integration with Java Spring Boot microservices in cloud-native environments.”
