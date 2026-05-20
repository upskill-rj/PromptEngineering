# SQL & PL Overview

# 🔷 What is SQL?

**SQL (Structured Query Language)** is a standard language used to interact with relational databases.

It is used for:

* Storing data
* Retrieving data
* Updating records
* Deleting records
* Managing database objects
* Security & permissions

---

## 🔹 Real Example

### Banking Application

```sql id="d6pzjw"
SELECT * FROM CUSTOMER
WHERE ACCOUNT_TYPE='SAVINGS';
```

👉 Retrieves all savings account customers.

---

# 🔷 What is PL/SQL?

**PL/SQL (Procedural Language/SQL)** is Oracle’s procedural extension of SQL.

It combines:

* SQL
* Variables
* Loops
* Conditions
* Exception handling
* Procedures/functions

---

## 🔹 Why PL/SQL?

SQL alone is declarative.

PL/SQL adds:

* Business logic
* Automation
* Batch processing
* Error handling

---

# 🔷 SQL vs PL/SQL

| Feature        | SQL                 | PL/SQL                   |
| -------------- | ------------------- | ------------------------ |
| Type           | Query language      | Programming language     |
| Execution      | Single statement    | Block execution          |
| Logic          | No loops/conditions | Supports loops & IF      |
| Usage          | Data operations     | Business logic           |
| Performance    | Individual queries  | Better batch performance |
| Error Handling | Limited             | Exception handling       |

---

# 🔷 SQL Architecture

```text id="m0t55u"
Application
    ↓
SQL Parser
    ↓
Query Optimizer
    ↓
Execution Engine
    ↓
Database Storage
```

---

# 🔷 Components of SQL

| Component         | Purpose             |
| ----------------- | ------------------- |
| Queries           | Retrieve data       |
| Tables            | Store records       |
| Views             | Virtual tables      |
| Indexes           | Faster search       |
| Constraints       | Data integrity      |
| Joins             | Combine tables      |
| Transactions      | ACID operations     |
| Stored Procedures | Reusable logic      |
| Triggers          | Automatic execution |

---

# 🔷 Types of SQL Commands

# 1. DDL — Data Definition Language

Used to define database structure.

---

## 🔹 Commands

| Command  | Purpose            |
| -------- | ------------------ |
| CREATE   | Create objects     |
| ALTER    | Modify structure   |
| DROP     | Delete objects     |
| TRUNCATE | Remove all records |

---

## 🔹 Example

```sql id="s2g7cb"
CREATE TABLE EMPLOYEE (
   EMP_ID NUMBER,
   NAME VARCHAR2(100)
);
```

---

## 🔹 Use Case

* Creating ERP tables
* Defining schemas
* Designing application database structure

---

# 2. DML — Data Manipulation Language

Used to manipulate records.

---

## 🔹 Commands

| Command | Purpose     |
| ------- | ----------- |
| INSERT  | Add data    |
| UPDATE  | Modify data |
| DELETE  | Remove data |
| MERGE   | Upsert      |

---

## 🔹 Example

```sql id="gwnjlwm"
INSERT INTO EMPLOYEE
VALUES (101,'Rahul');
```

---

## 🔹 Use Case

* Customer onboarding
* Order processing
* Financial transactions

---

# 3. DQL — Data Query Language

Used to retrieve data.

---

## 🔹 Command

| Command | Purpose          |
| ------- | ---------------- |
| SELECT  | Retrieve records |

---

## 🔹 Example

```sql id="jlwm9p"
SELECT NAME,SALARY
FROM EMPLOYEE
WHERE SALARY > 50000;
```

---

# 4. DCL — Data Control Language

Controls security and permissions.

---

## 🔹 Commands

| Command | Purpose       |
| ------- | ------------- |
| GRANT   | Give access   |
| REVOKE  | Remove access |

---

## 🔹 Example

```sql id="o8n6x9"
GRANT SELECT ON EMPLOYEE TO HR_USER;
```

---

## 🔹 Use Case

* Role-based security
* Database access management

---

# 5. TCL — Transaction Control Language

Controls transactions.

---

## 🔹 Commands

| Command   | Purpose          |
| --------- | ---------------- |
| COMMIT    | Save changes     |
| ROLLBACK  | Undo changes     |
| SAVEPOINT | Partial rollback |

---

## 🔹 Example

```sql id="0om8bg"
UPDATE ACCOUNT
SET BALANCE = BALANCE - 1000
WHERE ID=1;

COMMIT;
```

---

# 🔷 SQL Components in Detail

# 1. Tables

Store structured data.

```text id="focf5y"
EMPLOYEE
---------
ID
NAME
SALARY
```

---

# 2. Constraints

Ensure data integrity.

| Constraint  | Example            |
| ----------- | ------------------ |
| PRIMARY KEY | Unique ID          |
| FOREIGN KEY | Relationship       |
| UNIQUE      | No duplicates      |
| NOT NULL    | Mandatory value    |
| CHECK       | Validate condition |

---

# 3. Joins

Combine data from multiple tables.

---

## 🔹 Types of Joins

| Join       | Purpose           |
| ---------- | ----------------- |
| INNER JOIN | Matching records  |
| LEFT JOIN  | All left records  |
| RIGHT JOIN | All right records |
| FULL JOIN  | All records       |

---

## 🔹 Example

```sql id="f2x6dd"
SELECT E.NAME, D.DEPT_NAME
FROM EMPLOYEE E
JOIN DEPARTMENT D
ON E.DEPT_ID = D.ID;
```

---

# 4. Indexes

Improve query performance.

---

## 🔹 Example

```sql id="10fc8r"
CREATE INDEX IDX_EMP_NAME
ON EMPLOYEE(NAME);
```

---

## 🔹 Use Case

* Faster search
* High-volume banking systems
* ERP reports

---

# 5. Views

Virtual tables based on queries.

---

## 🔹 Example

```sql id="yqjof0"
CREATE VIEW ACTIVE_EMP AS
SELECT * FROM EMPLOYEE
WHERE STATUS='ACTIVE';
```

---

# 🔷 PL/SQL Components

# 1. PL/SQL Block Structure

```sql id="k2w58t"
DECLARE
   v_name VARCHAR2(50);

BEGIN
   SELECT NAME INTO v_name
   FROM EMPLOYEE
   WHERE ID=101;

   DBMS_OUTPUT.PUT_LINE(v_name);

EXCEPTION
   WHEN NO_DATA_FOUND THEN
      DBMS_OUTPUT.PUT_LINE('No Record');
END;
```

---

# 🔷 PL/SQL Sections

| Section   | Purpose        |
| --------- | -------------- |
| DECLARE   | Variables      |
| BEGIN     | Logic          |
| EXCEPTION | Error handling |
| END       | End block      |

---

# 🔷 PL/SQL Objects

| Object    | Purpose               |
| --------- | --------------------- |
| Procedure | Reusable logic        |
| Function  | Returns value         |
| Trigger   | Auto execution        |
| Package   | Group related logic   |
| Cursor    | Row-by-row processing |

---

# 🔷 1. Procedure

Reusable business logic.

---

## 🔹 Example

```sql id="s8e8uv"
CREATE OR REPLACE PROCEDURE GET_EMP
AS
BEGIN
   DBMS_OUTPUT.PUT_LINE('Employee Data');
END;
```

---

## 🔹 Use Case

* Batch jobs
* Payroll processing
* Financial reconciliation

---

# 🔷 2. Function

Returns a value.

---

## 🔹 Example

```sql id="fj9b0l"
CREATE FUNCTION GET_BONUS
RETURN NUMBER
IS
BEGIN
   RETURN 5000;
END;
```

---

# 🔷 3. Trigger

Executes automatically.

---

## 🔹 Example

```sql id="vx82ye"
CREATE TRIGGER AUDIT_EMP
AFTER INSERT ON EMPLOYEE
BEGIN
   DBMS_OUTPUT.PUT_LINE('Inserted');
END;
```

---

## 🔹 Use Case

* Audit logging
* Security monitoring
* Auto notifications

---

# 🔷 4. Cursor

Processes rows one by one.

---

## 🔹 Example

```sql id="3h8cbi"
CURSOR EMP_CURSOR IS
SELECT NAME FROM EMPLOYEE;
```

---

## 🔹 Use Case

* Batch processing
* ETL jobs
* Reporting systems

---

# 🔷 SQL in Enterprise Architecture

```text id="7b51n9"
Frontend
   ↓
Spring Boot API
   ↓
Hibernate/JPA
   ↓
SQL Queries
   ↓
Oracle/PostgreSQL
```

---

# 🔷 SQL with Java Example

```java id="6rmx7u"
String sql = "SELECT * FROM EMPLOYEE";
PreparedStatement ps = conn.prepareStatement(sql);
```

---

# 🔷 SQL Optimization Concepts

| Concept            | Purpose               |
| ------------------ | --------------------- |
| Indexing           | Faster search         |
| Partitioning       | Split huge tables     |
| Query Optimization | Better execution plan |
| Normalization      | Reduce redundancy     |
| Caching            | Faster reads          |

---

# 🔷 Normalization

Organizing data efficiently.

---

## 🔹 Types

| Type | Purpose                      |
| ---- | ---------------------------- |
| 1NF  | Atomic values                |
| 2NF  | Remove partial dependency    |
| 3NF  | Remove transitive dependency |

---

# 🔷 Example

Before normalization:

```text id="y2b4mx"
EMPLOYEE
- Name
- Department
- Manager
```

After normalization:

```text id="4n3y2g"
EMPLOYEE Table
DEPARTMENT Table
```

---

# 🔷 SQL in Cloud Platforms

# AWS

* Amazon RDS
* Amazon Aurora

# Azure

* Azure SQL Database

# OCI

* Oracle Autonomous Database

# GCP

* Google Cloud SQL

---

# 🔷 SQL & PL/SQL Use Cases

| Domain     | Use Case           |
| ---------- | ------------------ |
| Banking    | Transactions       |
| ERP        | Finance & payroll  |
| Healthcare | Patient records    |
| E-Commerce | Orders & inventory |
| Telecom    | Billing systems    |
| AI Systems | Metadata storage   |

---

# 🔷 SQL in AI Applications

| AI Area    | SQL Usage             |
| ---------- | --------------------- |
| RAG        | Store metadata        |
| AI Agents  | Query enterprise data |
| Analytics  | Training datasets     |
| Monitoring | Logs & metrics        |

---

# 🔷 Interview-Oriented Answer

> “SQL is a standard language used to manage and query relational databases, while PL/SQL extends SQL with procedural capabilities such as loops, conditions, and exception handling. SQL is mainly used for CRUD operations and schema management, whereas PL/SQL is widely used for implementing business logic, batch processing, automation, triggers, and stored procedures in enterprise systems like banking, ERP, and cloud-native applications.”
