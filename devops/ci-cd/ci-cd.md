# CI/CD Main Components, Architecture Flow, OWASP & Security (Enterprise Interview Guide)

For senior/architect interviews, they expect:

* End-to-end CI/CD architecture
* DevSecOps integration
* OWASP understanding
* Security scanning
* Cloud-native deployment
* Enterprise governance
* Rollback/recovery strategies

Your profile strongly aligns with:

* Spring Boot
* Jenkins
* Kubernetes
* Docker
* Enterprise delivery
* Cloud-native modernization 

---

# 1. What is CI/CD?

## CI = Continuous Integration

> Developers continuously integrate code into shared repository where automated build and testing happen.

---

## CD = Continuous Delivery / Continuous Deployment

> Automates packaging, deployment, release, and monitoring processes.

---

# 2. What is DevSecOps?

DevSecOps

DevSecOps means:

> Integrating security into every stage of CI/CD pipeline instead of applying security only at production stage.

---

# 3. Complete Enterprise CI/CD + Security Architecture

```text id="m7k2p4"
Developer
   ↓
Git Repository
   ↓
Webhook Trigger
   ↓
Jenkins Pipeline
   ↓
Build (Maven/Gradle)
   ↓
Unit Testing
   ↓
Static Code Analysis
   ↓
OWASP Security Scan
   ↓
Artifact Packaging (JFrog)
   ↓
Artifact Repository(JFrog)
   ↓
Docker Image Build
   ↓
Container Security Scan
   ↓
Docker Registry
   ↓
Kubernetes Deployment
   ↓
Runtime Security
   ↓
Monitoring & Logging
   ↓
Alerts & Feedback
```

---

# 4. Main CI/CD Components

| Component              | Purpose                |
| ---------------------- | ---------------------- |
| Git                    | Source code management |
| Jenkins                | Pipeline orchestration |
| Maven/Gradle           | Build automation       |
| JUnit/Mockito          | Unit testing           |
| SonarQube              | Code quality           |
| OWASP Dependency Check | Vulnerability scanning |
| Nexus/Artifactory      | Artifact storage       |
| Docker                 | Containerization       |
| Trivy/Snyk             | Container security     |
| Kubernetes             | Orchestration          |
| Prometheus/Grafana     | Monitoring             |
| ELK/Splunk             | Logging                |
| Vault                  | Secret management      |

---

# 5. End-to-End CI/CD Flow

---

# STEP 1 — Developer Commits Code

Git

```bash id="g4m8k2"
git add .
git commit -m "feature added"
git push
```

Purpose:

* Version control
* Collaboration
* Branch management

---

# STEP 2 — Webhook Triggers Pipeline

Git webhook automatically triggers:

Jenkins

```text id="v8k2m4"
Git Push
   ↓
Webhook
   ↓
Jenkins Trigger
```

---

# STEP 3 — Source Code Checkout

Jenkins downloads latest code.

```text id="k5m9p1"
Git Clone
```

---

# STEP 4 — Build Stage

Apache Maven

Command:

```bash id="n2k8m5"
mvn clean install
```

Purpose:

* Compile code
* Resolve dependencies
* Package application

Output:

```text id="f8m3k1"
app.jar
```

---

# STEP 5 — Unit Testing

Tools:

* JUnit
* Mockito

Purpose:

* Validate application logic
* Catch bugs early

Command:

```bash id="r5m2k8"
mvn test
```

---

# STEP 6 — Static Code Analysis

SonarQube

Checks:

* Code quality
* Code smells
* Vulnerabilities
* Duplicates
* Test coverage

---

# STEP 7 — OWASP Security Scanning

OWASP

OWASP provides:

* Security standards
* Vulnerability guidelines
* Secure coding practices

---

# OWASP Top 10 Security Risks

| Risk                      | Meaning              |
| ------------------------- | -------------------- |
| Injection                 | SQL injection        |
| Broken Authentication     | Weak login/auth      |
| Sensitive Data Exposure   | Data leakage         |
| Security Misconfiguration | Improper setup       |
| XSS                       | Cross-site scripting |
| Broken Access Control     | Unauthorized access  |

---

# OWASP Dependency Check

Purpose:

* Detect vulnerable libraries/dependencies

Example:

```text id="p8m1k3"
Log4j vulnerability detection
```

---

# Security Scan Flow

```text id="y7k4m2"
Source Code
   ↓
Dependency Check
   ↓
CVE Detection
   ↓
Build Failure if High Risk
```

---

# 8. SAST (Static Application Security Testing)

Checks source code security before runtime.

Tools:

* SonarQube
* Checkmarx
* Fortify

Detects:

* SQL Injection
* Hardcoded secrets
* Insecure coding

---

# 9. DAST (Dynamic Application Security Testing)

Tests running application.

Tools:

* OWASP ZAP
* Burp Suite

Checks:

* API vulnerabilities
* Runtime attacks
* Authentication flaws

---

# 10. Artifact Packaging

Build creates:

```text id="u3m9k5"
JAR/WAR
```

Example:

```text id="x8k2m4"
employee-service.jar
```

---

# 11. Artifact Repository

Tools:

* Nexus
* Artifactory

Purpose:

* Store versioned artifacts
* Dependency management
* Rollback support

---

# 12. Docker Containerization

Docker

Purpose:

* Package application
* Ensure environment consistency

---

# Docker Flow

```text id="t4m8k1"
JAR File
   ↓
Docker Image
   ↓
Container
```

---

# Dockerfile Example

```dockerfile id="q2m7k5"
FROM openjdk:17

COPY target/app.jar app.jar

ENTRYPOINT ["java","-jar","app.jar"]
```

---

# 13. Container Security Scanning

Tools:

* Trivy
* Snyk
* Aqua Security

Checks:

* OS vulnerabilities
* Image vulnerabilities
* Secrets exposure

---

# Container Scan Flow

```text id="w5k2m9"
Docker Image
    ↓
Security Scan
    ↓
Block Vulnerable Images
```

---

# 14. Docker Registry

Stores Docker images.

Examples:

* Docker Hub
* AWS ECR
* Azure ACR

---

# 15. Kubernetes Deployment

Kubernetes

Purpose:

* Auto scaling
* Self healing
* Load balancing
* Orchestration

---

# Kubernetes Deployment Flow

```text id="j9m4k2"
Docker Registry
      ↓
Kubernetes Deployment
      ↓
Pods
      ↓
Services
      ↓
Ingress
```

---

# 16. Kubernetes Security

Important enterprise topic.

---

## Features

| Feature               | Purpose              |
| --------------------- | -------------------- |
| RBAC                  | Role-based access    |
| Network Policies      | Restrict traffic     |
| Secrets               | Secure credentials   |
| Pod Security          | Restrict containers  |
| Admission Controllers | Security enforcement |

---

# 17. Secret Management

Tools:

* Vault
* Kubernetes Secrets

Purpose:

* Store passwords securely
* Avoid hardcoded credentials

---

# 18. Runtime Security

Tools:

* Falco
* Prisma Cloud

Checks:

* Suspicious container activity
* Unauthorized access
* Runtime attacks

---

# 19. Monitoring & Observability

Prometheus
Grafana

Tracks:

* CPU
* Memory
* API latency
* Pod failures
* Error rates

---

# 20. Centralized Logging

```text id="m2k8p5"
Application Logs
      ↓
ELK/Splunk
      ↓
Search & Analysis
```

---

# ELK Stack

| Component     | Purpose    |
| ------------- | ---------- |
| Elasticsearch | Storage    |
| Logstash      | Processing |
| Kibana        | Dashboard  |

---

# 21. Alerting System

Alerts triggered for:

* Failed deployment
* Security vulnerability
* High CPU
* Service downtime

Notifications:

* Slack
* Email
* PagerDuty

---

# 22. Rollback Strategy

If deployment fails:

```text id="z5m1k7"
Deployment Failure
      ↓
Automatic Rollback
      ↓
Previous Stable Version Restored
```

---

# 23. Blue-Green Deployment

```text id="a7k3m8"
Blue → Current Version
Green → New Version
```

Traffic switched after validation.

---

# 24. Canary Deployment

Deploy new version to limited users first.

Benefits:

* Reduced production risk
* Safe rollout

---

# 25. Infrastructure as Code (IaC)

Tools:

* Terraform
* Ansible

Purpose:

* Automate infrastructure provisioning

---

# 26. Enterprise Security Layers

```text id="p2m9k4"
Code Security
Dependency Security
Container Security
Cluster Security
Runtime Security
API Security
Network Security
Monitoring Security
```

---

# 27. API Security

Commonly implemented using:

* OAuth2
* JWT
* API Gateway
* Rate limiting

---

# 28. Enterprise DevSecOps Flow

```text id="v1k8m5"
Developer
   ↓
Git Push
   ↓
CI Pipeline
   ↓
Code Scan
   ↓
OWASP Scan
   ↓
Container Scan
   ↓
Deployment
   ↓
Runtime Monitoring
```

---

# 29. Real Enterprise Architecture

```text id="h4m7k2"
React/Angular UI
       ↓
API Gateway
       ↓
Spring Boot Microservices
       ↓
Kafka/Event Bus
       ↓
Database
```

Secured through:

* OAuth2
* JWT
* RBAC
* OWASP scanning
* Kubernetes security

---

# 30. Most Asked Interview Questions

---

## Q1. What is DevSecOps?

> DevSecOps integrates security into every phase of CI/CD pipeline.

---

## Q2. What is OWASP?

> OWASP is an organization providing application security standards and vulnerability guidelines.

---

## Q3. Difference Between SAST and DAST?

| SAST                 | DAST             |
| -------------------- | ---------------- |
| Static code analysis | Runtime testing  |
| Before deployment    | After deployment |

---

## Q4. Why container scanning is needed?

> To identify vulnerabilities in Docker images and OS packages.

---

## Q5. What is RBAC?

> Role-Based Access Control restricts access based on user roles.

---

# 31. Architect-Level Interview Answer

> “In our enterprise DevSecOps architecture, Git commits triggered Jenkins CI/CD pipelines. Maven handled builds, JUnit executed automated testing, SonarQube and OWASP Dependency Check performed static code and vulnerability scanning, Docker containerized applications, Trivy scanned container images, and Kubernetes orchestrated secure deployments with RBAC, secrets management, and runtime monitoring. Monitoring and centralized logging were implemented using Prometheus, Grafana, and ELK/Splunk.”
