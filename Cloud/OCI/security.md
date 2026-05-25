Let me break this down clearly — these are all part of the **application security ecosystem**.

---

## DAST — Dynamic Application Security Testing

DAST tests a **running application** from the outside, simulating how an attacker would probe it — without access to source code. It sends malicious inputs, unexpected requests, and observes responses.

**How it works:** A scanner acts as an external attacker, hitting your live app's endpoints, forms, and APIs.

**Use cases:**
- Finding SQL injection, XSS, and authentication flaws in a deployed app
- Testing APIs for broken access control
- CI/CD pipeline gate — block deployments if critical issues found
- Compliance validation (PCI-DSS, HIPAA require runtime testing)

**Common DAST tools:** OWASP ZAP, Burp Suite, Nikto, Invicti, Checkmarx DAST

---

## SAST — Static Application Security Testing *(contrast with DAST)*

Tests **source code without running it**. Catches issues at dev time. DAST and SAST are complementary — SAST finds code-level bugs, DAST finds runtime and config issues.

---

## OWASP — Open Worldwide Application Security Project

A **non-profit foundation** that produces free, open security standards, tools, and education used globally. It doesn't make commercial products — it produces knowledge.

**Key outputs:**
- **OWASP Top 10** — the most critical web app security risks (e.g. Broken Access Control, Injection, Cryptographic Failures). Used as a baseline for audits and compliance worldwide.
- **OWASP ASVS** — Application Security Verification Standard; a checklist for building secure apps
- **OWASP MASVS** — same but for mobile apps
- **OWASP Cheat Sheet Series** — practical developer guidance (JWT security, SQL injection prevention, etc.)
- **OWASP ZAP** — their flagship free DAST tool (see below)

**Use cases:**
- RE&F team uses OWASP Top 10 as a security checklist during design reviews
- Auditors use ASVS to certify that an app meets security standards
- Developers reference cheat sheets when implementing auth, crypto, input validation

---

## OWASP ZAP — Zed Attack Proxy

OWASP's **free, open-source DAST scanner**. It sits as a proxy between your browser/test runner and your app, intercepting and fuzzing traffic.

**Modes:**
| Mode | What it does |
|---|---|
| Automated scan | Crawls app and attacks automatically |
| Spider | Discovers all URLs/endpoints |
| Active scan | Sends attack payloads to found endpoints |
| Passive scan | Observes traffic without attacking (safe for prod) |
| API scan | Targets REST/GraphQL APIs via OpenAPI spec |

**Use cases for RE&F:**
- Scan the Spring Boot API with ZAP using your OpenAPI spec before each release
- Run ZAP in Docker inside your CI/CD pipeline as a quality gate
- Passive scan in staging to catch issues without breaking anything
- Find JWT misconfigurations, missing security headers, exposed endpoints

**CI/CD integration example:**
```bash
docker run -t owasp/zap2docker-stable zap-api-scan.py \
  -t http://staging-api:8080/v3/api-docs \
  -f openapi \
  -r zap-report.html
```

---

## Libraries

A **library** is a reusable collection of code your application imports to avoid writing common functionality from scratch.

**Types:**
- **Standard library** — built into the language (e.g. `java.util`, Python's `os`)
- **Third-party library** — written by someone outside your team (see below)
- **Internal library** — written by your own org, shared across teams

**Security concern:** Libraries can contain vulnerabilities. You inherit their bugs.

---

## Third-Party Libraries

Code written by **external individuals or organizations** that you pull into your project via a package manager (`npm`, `Maven`, `pip`, etc.).

**Examples in your RE&F stack:**
| Library | Purpose |
|---|---|
| `jjwt` | JWT generation and validation |
| `spring-security` | Auth framework |
| `lombok` | Boilerplate reduction |
| `axios` | HTTP client in React |
| `tailwindcss` | Styling |
| `flyway` | DB migrations |

**Security concerns:**
- A library you trust today can have a CVE published tomorrow
- Transitive dependencies — a library you import brings in *its* dependencies too (your real exposure is often 10x what you directly imported)
- Supply chain attacks — malicious code injected into a popular package

**How to manage:**
- **OWASP Dependency-Check** — scans your Maven/npm deps against the NVD vulnerability database
- **Snyk / GitHub Dependabot** — alerts and auto-PRs when a dep has a known CVE
- **Lock files** (`package-lock.json`, `pom.xml` version pins) — prevent surprise upgrades

---

## Other Tools and Components in the Ecosystem

### SCA — Software Composition Analysis
Scans all your dependencies (direct + transitive) for known CVEs. Think of it as DAST for your `pom.xml`.

**Tools:** OWASP Dependency-Check, Snyk, Black Duck, JFrog Xray

### IAST — Interactive Application Security Testing
Instruments your app from **inside** during test runs. An agent watches what code paths are hit and flags vulnerabilities in real time. More accurate than DAST, less disruptive than SAST.

**Tools:** Contrast Security, Seeker

### WAF — Web Application Firewall
Sits in front of your app and blocks malicious traffic (SQLi, XSS, bad bots) before it reaches your server. Complements DAST — DAST finds the hole, WAF patches it at the perimeter while you fix code.

**Tools:** AWS WAF, Cloudflare WAF, ModSecurity

### Secrets Scanning
Finds hardcoded API keys, passwords, and tokens accidentally committed to source code.

**Tools:** GitGuardian, TruffleHog, GitHub Secret Scanning

### SBOM — Software Bill of Materials
A machine-readable inventory of every library and component in your app. Increasingly required by enterprise procurement and government contracts.

**Tools:** CycloneDX, SPDX (formats); Syft, Trivy (generators)

---

## How They Fit Together (RE&F Context)

```
Dev writes code
    │
    ├─ SAST scans source code (in IDE or CI)
    ├─ SCA scans dependencies (OWASP Dependency-Check / Snyk)
    ├─ Secrets scanning (GitGuardian)
    │
    ▼
Code merged → CI/CD pipeline
    │
    ├─ Build runs SAST again
    ├─ DAST (OWASP ZAP) hits staging environment
    ├─ IAST agent runs during integration tests
    │
    ▼
Deploy to production
    │
    ├─ WAF filters live traffic
    └─ Monitoring / alerting for runtime anomalies
```

The key insight is that **no single tool covers everything** — DAST finds what SAST misses (runtime config, auth flows), SCA finds what both miss (vulnerable deps), and a WAF protects you while fixes are in flight.


# 3PLTA = Third Party License Tracking Application

* 3rd Party liceming Information of commercials and open-source componenets that are used to develop product and services
* Include BA (business approval) workflows
* Support release traching activities.

# Basic Terminology

* Licensed Technology (LT) - For everyone
	* Licemed API's (LAs)
	* Licenced Dataset (LDs)
* Business Approval (BA) - For each Team


#3PLTA relate to the Product Life Suite

* 3PLTA's a standalone app that exchange date with various PLS apps
* Product & Release Adimin (PRA)
* Compliance Dashboard / Security Compliame Systems (SCMS)
* Report Management System (RMS)
* One LT per version of a licensed technlogy
* Don't use an older version of an LT to avoid creating a new one
* BA to pre approval procur
* All Pre-Approved BA's (as well as security reviews BAs ad Legal Review BA's) are subject to random audit.
* D&E Legal reprentative - cosult



# Gather Required Information for LT & BA

1) Identify the 3rd party content.
2) confirm that the business approval is necessary.
3) Prepare your information.
	a) Name and exact version of components and dependencies.
	b) Results of seaches for known vulnerabilities
	c) URL for the main home page for the S/W.
	d) URL for the download location.
	e) If competitive or not reasonably current, justification and competitive approvals.

4) Infomation for how it will be uned in your product.

# Approval Chain

1) Obtain concept Approvals
2) Go through legal review
3) Obtain final Approval.

# Permissive Licenser ALWAYS Best.

# CDDL Licenses 
* CDDL is almost always tied to Oracle (or Sun) own and maintained technology.


# Fouth -Party Dependencies.

- A 3rd party dependency is technlogy you used that is not owned by company - These form the basis of your requests in 3PLTA
- Fourth-party dependencers are all dependencies of a 3rd party dependency - these must be included in the 3PLTA request for the 3rd prty  itself.
- Each 3rd party dependency incorporates copyrighted materials from its 4th-party dependencies.
- Company must therefore comply with the licencing obligations of 4th-party dependencies, just as we do for 3rd Party dependencies.
- 4th party dependencies are also vital for security assessment.
- 95% of all reported vulnerabilities in commercial s/w originates in these transitive dependencies of open source software.
- No security review of 3rd party material can be considered completes without reviewing its dependencies.
- 4th party dependencies do include
	- compiles and runtime dependencies
	- the full, transitive list of dependencies.
	
	
# How to Identify 4th party dependencies.

- Using Standard build tools

1) For Java - Maven or Gradle
2) Por Python- pipgrip or pipdeptree
3) For Node- npm
4) for Scala- sbt
5) for .NET/C#- NuGet Package Manage in Visual Studio or Switch

- 4th party dependency detail need to be recorded in 3PLTA

# Licensed Technology (Public Licenses & Copyright Notice Fields)
- Dependney Name
- Licenses and copyright notices

# Business Approval (Technology usage Not Field)
- Dependency names
- Dependency versions

# Populating the LT Public Licence field.

- Company has additional tools to assist in identifying 4th party depudencies.

1) Open Source Compliance Series (OSCS)
- Supports Java, Python, Node and Go (uning Attribute helper) 
- Fetches licenses and notices, and highlights known scurity vulnerabilities

2) Attribution Helper

- Supports Go, Node (does not produce accurate results for java)
- Fetches licences and notices. (Third Party Licenen.txt)
- Required by corporate Architects for Go projects.

# Common Cases

- No Dependencies-Means No required runtime or compile time dependencies
- Nested Model.

- Less Common cases
	- Flat Model (Dependencies) - Seprate request for each LT