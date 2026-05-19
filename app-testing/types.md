# 1. Unit Testing

## What is Unit Testing?

Unit Testing verifies individual methods/classes/modules independently to ensure business logic works correctly.

Usually performed by developers during coding.

---

## Example

```java id="2azr0f"
assertEquals(1000, calculateSalary());
```

Validates salary calculation method output.

---

## Interview Points

* Fastest testing type
* Detects bugs early
* Mostly automated
* Tools:

  * JUnit
  * TestNG
  * Mockito

---

# 2. Integration Testing

## What is Integration Testing?

Integration Testing validates communication between multiple modules/services/databases/APIs.

Focuses on data flow and interaction.

---

## Example

Testing:

* Spring Boot API
* Database
* Kafka queue

all working together correctly.

---

## Interview Points

Validates:

* REST APIs
* DB integration
* Third-party systems
* Microservices communication

Tools:

* Postman
* RestAssured
* SoapUI

---

# 3. System Testing

## What is System Testing?

System Testing validates the complete end-to-end application in a production-like environment.

Ensures full system works as expected.

---

## Example

Testing entire e-commerce flow:

* Login
* Add to cart
* Payment
* Invoice generation

---

## Interview Points

* Covers complete business workflow
* Done after integration testing
* Includes functional + non-functional validation

---

# 4. Regression Testing

## What is Regression Testing?

Regression Testing ensures new code changes do not break existing functionality.

Very important during releases and enhancements.

---

## Example

After adding AI chatbot:

* Existing payment module
* Invoice module
* Authentication

should still work correctly.

---

## Interview Points

* Repeated after every release
* Usually automated
* Critical in Agile/CI-CD environments

Tools:

* Selenium
* TestNG
* Jenkins

---

# 5. User Acceptance Testing (UAT)

## What is UAT?

UAT validates whether application meets business/user expectations.

Performed by business users or clients.

---

## Example

Finance users validate:

* Tax reports
* ERP workflows
* Invoice approvals

before production release.

---

## Interview Points

* Final validation phase
* Focus on business scenarios
* Determines production readiness

---

# 6. Load Testing

## What is Load Testing?

Load Testing checks application behavior under expected user load.

Measures:

* Response time
* Throughput
* Stability

---

## Example

Testing:

* 10,000 concurrent users
* Login requests
* API calls

during finance quarter-end.

---

## Interview Points

Validates:

* Scalability
* Performance
* Resource utilization

Tools:

* Apache JMeter
* LoadRunner
* Gatling

---

# 7. Stress Testing

## What is Stress Testing?

Stress Testing checks application behavior beyond normal capacity limits.

Identifies breaking point and recovery capability.

---

## Example

Testing:

* 1 lakh users suddenly hitting payment gateway

to observe crash handling.

---

## Interview Points

* Tests extreme conditions
* Validates resilience
* Helps identify bottlenecks

---

# 8. Performance Testing

## What is Performance Testing?

Performance Testing measures:

* Speed
* Stability
* Scalability
* Resource usage

under different workloads.

---

## Example

API should respond within:

* 2 seconds under normal load

---

## Interview Points

Includes:

* Load testing
* Stress testing
* Spike testing
* Endurance testing

---

# 9. Smoke Testing

## What is Smoke Testing?

Smoke Testing verifies whether major functionalities are working after a new build deployment.

Quick validation before deeper testing.

---

## Example

Check:

* Login works
* APIs accessible
* Database connected

after deployment.

---

## Interview Points

* First level build validation
* Saves testing time
* Often automated in CI/CD

---

# 10. Sanity Testing

## What is Sanity Testing?

Sanity Testing validates a specific bug fix or small functionality after minor changes.

Focused and narrow testing.

---

## Example

After fixing invoice calculation bug:

* Validate only invoice module

instead of full application.

---

# 11. Functional Testing

## What is Functional Testing?

Functional Testing validates application features against business requirements.

Focuses on “what system should do.”

---

## Example

Validate:

* Tax calculation
* Login authentication
* Report generation

---

## Interview Points

* Business requirement validation
* Black-box testing
* Can be manual or automated

---

# 12. Non-Functional Testing

## What is Non-Functional Testing?

Validates system quality attributes like:

* Performance
* Security
* Reliability
* Scalability

---

## Example

Check:

* API response time
* Security vulnerabilities
* High availability

---

# 13. Security Testing

## What is Security Testing?

Security Testing identifies vulnerabilities and validates data protection mechanisms.

---

## Example

Testing:

* XSS
* SQL Injection
* Authentication bypass
* OAuth2 security

---

## Interview Points

Tools:

* OWASP ZAP
* Burp Suite
* SonarQube

---

# 14. API Testing

## What is API Testing?

API Testing validates backend services, request/response handling, authentication, and integrations.

---

## Example

Validate:

* REST API response
* HTTP status codes
* JWT token authentication

---

## Interview Points

Very important in:

* Microservices
* Cloud-native applications
* AI integrations

Tools:

* Postman
* RestAssured

---

# 15. End-to-End (E2E) Testing

## What is E2E Testing?

Validates complete business workflow across all integrated systems.

---

## Example

Oracle ERP Flow:

* Invoice upload
* Approval
* Payment
* Notification
* Reporting

---

## Interview Points

* Simulates real user journey
* Ensures system-wide reliability

---

# 16. Automation Testing

## What is Automation Testing?

Uses scripts/tools to execute test cases automatically.

Improves speed and repeatability.

---

## Example

Automated Selenium suite runs nightly regression tests.

---

## Interview Points

Benefits:

* Faster releases
* Better coverage
* CI/CD support

Tools:

* Selenium
* Cypress
* Playwright

---

# 17. AI-Powered Testing (Modern Trend)

## What is AI Testing?

AI-assisted testing uses machine learning and GenAI to improve software quality engineering.

---

## Example

AI can:

* Generate test cases
* Detect flaky tests
* Predict production failures
* Auto-heal Selenium locators

---

## Interview Points

Used in:

* AIOps
* Predictive QA
* Intelligent automation

Tools:

* OpenAI based copilots
* Testim
* Mabl
* Functionize

---

# Quick Interview Comparison Table

| Testing Type        | Purpose                    | Example               |
| ------------------- | -------------------------- | --------------------- |
| Unit Testing        | Test single method         | Salary calculation    |
| Integration Testing | Test module interaction    | API + DB              |
| System Testing      | Test complete system       | Full ERP workflow     |
| Regression Testing  | Ensure old features work   | After new release     |
| UAT                 | Business validation        | Finance user approval |
| Load Testing        | Expected traffic testing   | 10k users             |
| Stress Testing      | Extreme load testing       | Crash testing         |
| Security Testing    | Vulnerability validation   | XSS/SQL Injection     |
| API Testing         | Backend service validation | REST API              |
| Automation Testing  | Automated execution        | Selenium suite        |

---

# Interview-Ready Answer

> “Software testing ensures application quality, reliability, performance, and security. Unit testing validates individual methods, integration testing checks module interaction, regression testing ensures existing features are unaffected by changes, and UAT validates business requirements. Load, stress, and performance testing validate scalability and stability, while security testing protects applications from vulnerabilities. In enterprise projects, these testing practices are integrated into CI/CD pipelines using tools like JUnit, Selenium, Postman, JMeter, and AI-assisted testing platforms.”
