# PMD (Programming Mistake Detector)

**PMD** is a static source code analysis tool that scans Java (and several other languages) for potential bugs, coding standard violations, code smells, security issues, performance problems, and maintainability concerns **without executing the code**.

Think of PMD as an automated code reviewer that checks your code against predefined best practices.

---

## Why PMD is Used

In large enterprise applications, PMD helps:

* Improve code quality
* Reduce technical debt
* Enforce coding standards
* Detect bugs early
* Improve maintainability
* Reduce code complexity
* Support CI/CD quality gates

---

## How PMD Works

```text
Developer Writes Code
          ↓
PMD Scanner
          ↓
Rules Engine
          ↓
Violations Found
          ↓
Developer Fixes Issues
```

Unlike JUnit, which runs code, PMD only analyzes the source code.

---

## Common Issues PMD Detects

### 1. Unused Variables

Bad:

```java
public void process() {
    int count = 10; // Never used
}
```

PMD Warning:

```text
Avoid unused local variables
```

---

### 2. Empty Catch Blocks

Bad:

```java
try {
    process();
}
catch(Exception e) {
}
```

PMD Warning:

```text
Empty catch block
```

---

### 3. Duplicate Code

Bad:

```java
if(user.equals("admin")) {
   System.out.println("Welcome");
}

if(user.equals("manager")) {
   System.out.println("Welcome");
}
```

PMD may suggest refactoring repeated logic.

---

### 4. High Cyclomatic Complexity

Bad:

```java
if(a){
 if(b){
   if(c){
      if(d){
      }
   }
 }
}
```

PMD Warning:

```text
Method complexity exceeds threshold
```

---

### 5. Unnecessary Object Creation

Bad:

```java
String str = new String("Hello");
```

Better:

```java
String str = "Hello";
```

---

## PMD Categories

| Category       | Purpose                  |
| -------------- | ------------------------ |
| Best Practices | Coding standards         |
| Error Prone    | Potential bugs           |
| Performance    | Inefficient code         |
| Security       | Security vulnerabilities |
| Design         | Design issues            |
| Documentation  | Missing documentation    |
| Code Style     | Formatting and naming    |

---

## PMD Architecture

```text
Java Source Code
        ↓
PMD Engine
        ↓
Rule Sets
        ↓
Violation Report
        ↓
Developer Fix
```

---

## PMD Rules Example

```xml
<ruleset name="Custom Rules">
   <rule ref="category/java/bestpractices.xml"/>
   <rule ref="category/java/errorprone.xml"/>
   <rule ref="category/java/performance.xml"/>
</ruleset>
```

---

## PMD with Maven

### pom.xml

```xml
<plugin>
   <groupId>org.apache.maven.plugins</groupId>
   <artifactId>maven-pmd-plugin</artifactId>
   <version>3.21.2</version>
</plugin>
```

Run:

```bash
mvn pmd:pmd
```

---

## PMD with Gradle

```gradle
plugins {
    id 'pmd'
}

pmd {
    toolVersion = '7.0.0'
}
```

Run:

```bash
gradle pmdMain
```

---

## PMD in CI/CD

```text
Git Commit
      ↓
Gradle/Maven Build
      ↓
PMD Analysis
      ↓
JUnit Tests
      ↓
SonarQube Scan
      ↓
Deploy
```

If PMD finds critical violations, the pipeline can fail before deployment.

---

## PMD vs Checkstyle vs SonarQube

| Tool       | Primary Focus                                            |
| ---------- | -------------------------------------------------------- |
| PMD        | Bugs, code smells, complexity                            |
| Checkstyle | Coding standards and formatting                          |
| SonarQube  | Overall code quality, security, coverage, technical debt |
| SpotBugs   | Bytecode-level bug detection                             |

---

## Real Enterprise Example

Suppose a Spring Boot microservice contains:

```java
public void createUser(User user) {

   if(user != null) {

      if(user.getName() != null) {

          if(user.getName().length() > 0) {

              // logic
          }
      }
   }
}
```

PMD may flag:

* High complexity
* Deep nesting
* Maintainability issues

Recommended refactoring:

```java
public void createUser(User user) {

   if(user == null ||
      user.getName() == null ||
      user.getName().isEmpty()) {
      return;
   }

   // business logic
}
```

---

## Interview Answer (2–3 Lines)

"PMD is a static code analysis tool that detects coding standard violations, code smells, complexity issues, performance problems, and potential bugs without executing the application. In Java projects, I integrate PMD with Maven/Gradle and CI/CD pipelines to enforce code quality before deployment."


==============



### Steps to Set Up PMD in a CI/CD DevOps Pipeline

PMD is typically integrated into the build stage of a pipeline so code quality checks run automatically on every commit, pull request, or deployment.

### 1. Add PMD to the Project

For Maven

Add the PMD plugin to pom.xml:

For Gradle

Add the PMD plugin to build.gradle:

### 2. Configure PMD Rules

Create a custom ruleset file, for example config/pmd/ruleset.xml:

Reference it in Maven or Gradle.

Maven

Gradle

### 3. Verify Locally

Run PMD before integrating into CI/CD.

Maven

Gradle

PMD reports are generated in:

* Maven: target/site/pmd.html

* Gradle: build/reports/pmd/main.html

### 4. Integrate with CI/CD Pipeline

Jenkins Pipeline Example

GitHub Actions Example

Create .github/workflows/pmd.yml:

Azure DevOps Pipeline Example

### 5. Fail the Build on Violations

Set PMD to fail the pipeline when rule violations exceed the threshold.

Maven

Gradle

This enforces code quality gates automatically.

### 6. Publish Reports and Metrics

Expose PMD reports in your CI/CD platform so developers can review issues.

Common report formats:

* HTML

* XML

* SARIF (for security/code scanning tools)

You can also integrate PMD results into SonarQube for centralized quality dashboards.

### 7. Recommended Pipeline Order

A typical enterprise pipeline sequence:

Running PMD early saves time by catching issues before expensive build and deployment steps.

### Best Practices

1. Keep rulesets focused

   Start with best practices, error-prone, and performance rules before adding stricter rules.

2. Fail fast

   Run PMD before unit tests or deployment stages to reduce wasted pipeline time.

3. Customize thresholds

   Adjust complexity and priority levels to match your team’s standards.

4. Review reports regularly

   Treat PMD findings as actionable technical debt items.

5. Combine with other tools

   Use PMD alongside Checkstyle, SpotBugs, SonarQube, and security scanners for comprehensive quality checks.

### Interview Summary (2–3 Lines)

“To set up PMD in a CI/CD pipeline, I add the PMD plugin to Maven or Gradle, configure custom rulesets, and run static analysis during the build stage. The pipeline is configured to fail on violations and publish PMD reports, ensuring code quality is enforced automatically before deployment.”
