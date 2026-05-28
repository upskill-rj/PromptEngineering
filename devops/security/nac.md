# What is NAC (Network Access Control)?

Network Access Control (NAC) is a cybersecurity solution that controls and secures access to a network by verifying users, devices, and security policies before allowing connectivity.

It ensures that only authorized and compliant devices/users can access enterprise resources such as servers, applications, cloud systems, Wi-Fi, VPNs, and databases.

---

# Simple Definition for Interview

“NAC is a security mechanism that authenticates and validates users/devices before granting network access, helping organizations prevent unauthorized access, malware spread, and non-compliant devices from entering the corporate network.”

---

# NAC Architecture Workflow

```text
User / Device
      ↓
Switch / Wireless Controller / VPN
      ↓
NAC Server
      ↓
Authentication (AD/LDAP/MFA)
      ↓
Policy Validation
      ↓
Access Decision
      ↓
Production Network / Guest Network / Quarantine VLAN
```

---

# Main Components of NAC

| Component             | Purpose                   |
| --------------------- | ------------------------- |
| NAC Server            | Central policy engine     |
| Authentication Server | Validates users/devices   |
| Endpoint Agent        | Checks device health      |
| Policy Engine         | Applies access rules      |
| Switch/WLC/VPN        | Enforces network access   |
| SIEM Integration      | Security monitoring       |
| Quarantine Network    | Isolates infected devices |

---

# How NAC Works

## 1. Device Connection

A laptop/mobile device connects to:

* LAN
* Wi-Fi
* VPN
* Cloud network

---

## 2. Authentication

NAC verifies:

* Username/password
* MFA
* Certificates
* Device identity

Using:

* Active Directory
* LDAP
* RADIUS

---

## 3. Security Compliance Check

NAC checks:

* Antivirus installed?
* OS patched?
* Firewall enabled?
* Device encrypted?
* Jailbroken/rooted?

---

## 4. Access Decision

| Condition              | Action               |
| ---------------------- | -------------------- |
| Authorized & compliant | Full access          |
| Unauthorized           | Block access         |
| Non-compliant          | Quarantine VLAN      |
| Guest device           | Guest network access |

---

# Example Use Case

An employee connects a laptop to office Wi-Fi.

NAC verifies:

* Employee identity
* Corporate antivirus
* Latest security patches

If compliant → Access granted.

If antivirus missing → Device moved to quarantine network.

---

# NAC Security Use Cases

| Use Case            | Benefit                     |
| ------------------- | --------------------------- |
| BYOD Security       | Secure personal devices     |
| Zero Trust          | Verify every device         |
| Guest Access        | Restricted temporary access |
| IoT Security        | Control smart devices       |
| Remote VPN Security | Validate remote endpoints   |
| Malware Containment | Isolate infected systems    |

---

# NAC in Enterprise Security Architecture

```text
Users/Devices
      ↓
Switches / Wi-Fi / VPN
      ↓
NAC Solution
      ↓
IAM / Active Directory
      ↓
Firewall / Segmentation
      ↓
Servers / Cloud / Applications
      ↓
SIEM Monitoring
```

---

# NAC and Zero Trust Security

NAC is a foundational component of Zero Trust Architecture because it follows:

> “Never Trust, Always Verify”

It continuously validates:

* User identity
* Device health
* Location
* Security posture

before granting access.

---

# Integration with Cloud & OCI

In cloud environments like Oracle Cloud Infrastructure, NAC integrates with:

* IAM
* VPN
* WAF
* Security Zones
* Cloud Guard
* Kubernetes security

### Example

A remote employee connecting to OCI VPN must pass NAC checks before accessing Kubernetes clusters or databases.

---

# Popular NAC Tools

| Tool                     | Purpose                  |
| ------------------------ | ------------------------ |
| Cisco ISE                | Enterprise NAC           |
| Aruba Networks ClearPass | BYOD & policy management |
| Fortinet FortiNAC        | IoT & network security   |
| Palo Alto Networks NAC   | Zero Trust integration   |
| Forescout                | Agentless NAC            |

---

# NAC vs Firewall

| NAC                         | Firewall                          |
| --------------------------- | --------------------------------- |
| Controls who enters network | Controls traffic between networks |
| Verifies device compliance  | Filters packets                   |
| Identity-based              | Rule-based                        |
| Endpoint-focused            | Traffic-focused                   |

---

# Scalability & Monitoring

| Area              | Solution                     |
| ----------------- | ---------------------------- |
| Scalability       | Distributed NAC clusters     |
| High Availability | Redundant NAC servers        |
| Monitoring        | SIEM, Splunk, ELK            |
| Automation        | AI-driven policy enforcement |
| Compliance        | PCI-DSS, HIPAA, ISO27001     |

---

# Monitoring Workflow

```text
Endpoint Events
      ↓
NAC Logs
      ↓
SIEM / Splunk / ELK
      ↓
Threat Detection
      ↓
Automated Response
```

Tools:

* Splunk
* Elastic
* IBM QRadar

---

# 2–3 Line Interview Answer

“NAC (Network Access Control) is a security solution that authenticates and validates users and devices before granting network access. It enforces security policies like antivirus compliance, MFA, and device posture checks, helping organizations implement Zero Trust security, prevent unauthorized access, and isolate infected systems automatically.”
