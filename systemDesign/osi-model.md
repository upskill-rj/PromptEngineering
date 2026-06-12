# OSI Model (Open Systems Interconnection) – System Design Perspective

The OSI Model is a conceptual framework that explains how data travels from one computer to another across a network. It consists of **7 layers**, where each layer provides services to the layer above it.

---

# OSI Layer Flow

```text
User Application
       |
7. Application Layer
       |
6. Presentation Layer
       |
5. Session Layer
       |
4. Transport Layer
       |
3. Network Layer
       |
2. Data Link Layer
       |
1. Physical Layer
       |
Network Cable/WiFi
       |
Destination System
```

---

# Example Flow

When you open:

```text
https://amazon.com
```

The request goes through:

```text
Application  → HTTP/HTTPS
Presentation → TLS Encryption
Session      → Session Management
Transport    → TCP
Network      → IP Routing
Data Link    → Ethernet/WiFi
Physical     → Electrical Signals
```

The server processes it and sends the response back through the same layers in reverse order.

---

# Layer 7 – Application Layer

### Purpose

Provides network services directly to end-user applications.

### Protocols

* HTTP/HTTPS
* FTP
* SMTP
* DNS
* SSH

### Example

When a browser sends an HTTPS request to Amazon.

### System Design Use Case

REST APIs, GraphQL APIs, Microservices communication, API Gateway interactions.

---

# Layer 6 – Presentation Layer

### Purpose

Handles data formatting, encryption, compression, and encoding.

### Functions

* TLS/SSL Encryption
* JSON Serialization
* XML Formatting
* UTF-8 Encoding

### Example

Converting Java objects into JSON and encrypting them using TLS.

### System Design Use Case

Secure API communication, data transformation, API payload formatting.

---

# Layer 5 – Session Layer

### Purpose

Establishes, maintains, and terminates communication sessions.

### Functions

* Session Management
* Authentication Sessions
* Connection Recovery

### Example

Keeping a user logged into an e-commerce website.

### System Design Use Case

User sessions, WebSocket connections, video conferencing sessions.

---

# Layer 4 – Transport Layer

### Purpose

Provides end-to-end communication and reliability.

### Protocols

* TCP
* UDP
* QUIC

### Example

TCP ensures online banking transactions arrive completely and in order.

### System Design Use Case

gRPC, REST APIs, Kafka communication, video streaming, gaming.

---

# Layer 3 – Network Layer

### Purpose

Routes packets between networks.

### Protocols

* IPv4
* IPv6
* ICMP

### Example

Routing packets from India to a server hosted in the US.

### System Design Use Case

Cloud networking, VPCs, routing tables, multi-region deployments.

---

# Layer 2 – Data Link Layer

### Purpose

Transfers data between devices on the same local network.

### Protocols

* Ethernet
* WiFi (802.11)
* ARP

### Example

Communication between a laptop and a WiFi router.

### System Design Use Case

Data center networking, Kubernetes node communication, cloud infrastructure.

---

# Layer 1 – Physical Layer

### Purpose

Transmits raw bits over physical media.

### Components

* Network Cables
* Fiber Optics
* Wireless Signals
* Switch Ports

### Example

Electrical signals traveling through Ethernet cables.

### System Design Use Case

Data center infrastructure, cloud networking hardware, high-speed fiber connectivity.

---

# OSI Layer Mapping with Modern Technologies

| OSI Layer    | Modern Technologies                       |
| ------------ | ----------------------------------------- |
| Application  | REST API, GraphQL, gRPC, DNS, HTTP        |
| Presentation | TLS, SSL, JSON, XML, Base64               |
| Session      | WebSocket, Login Sessions, OAuth Sessions |
| Transport    | TCP, UDP, QUIC                            |
| Network      | IPv4, IPv6, NAT, Routing                  |
| Data Link    | Ethernet, WiFi, VLAN                      |
| Physical     | Fiber, Cable, Wireless Networks           |

---

# OSI Mapping to a Typical Banking Application

```text
Customer Opens Banking App
          |
Application Layer
(HTTPS, REST API)
          |
Presentation Layer
(TLS Encryption, JSON)
          |
Session Layer
(Login Session, JWT)
          |
Transport Layer
(TCP)
          |
Network Layer
(IP Routing)
          |
Data Link Layer
(WiFi/Ethernet)
          |
Physical Layer
(Fiber/Cable)
          |
Bank Server
```

---

# OSI Layer Mapping in Microservices Architecture

```text
User
 |
Browser
 |
HTTP/HTTPS
 |
API Gateway
 |
REST/gRPC APIs
 |
Microservices
 |
Kafka
 |
Database
```

| Component   | OSI Layer               |
| ----------- | ----------------------- |
| REST API    | Application             |
| GraphQL     | Application             |
| gRPC        | Application + Transport |
| TLS         | Presentation            |
| JWT Session | Session                 |
| TCP         | Transport               |
| IP          | Network                 |
| Ethernet    | Data Link               |
| Fiber Cable | Physical                |

---

# Interview Summary (2-3 Lines per Layer)

| Layer        | What It Does                                                                          |
| ------------ | ------------------------------------------------------------------------------------- |
| Application  | Provides services to end-user applications such as HTTP, REST APIs, DNS, and GraphQL. |
| Presentation | Handles encryption, encoding, serialization, and data formatting.                     |
| Session      | Manages user sessions, authentication, and connection state.                          |
| Transport    | Ensures reliable or fast communication using TCP, UDP, or QUIC.                       |
| Network      | Routes packets between networks using IP addresses.                                   |
| Data Link    | Transfers data within local networks using MAC addresses and Ethernet/WiFi.           |
| Physical     | Sends raw bits through cables, fiber optics, or wireless signals.                     |

### Interview One-Liner

**"In system design, Application, Presentation, Session, and Transport layers are most visible to developers, while Network, Data Link, and Physical layers are primarily managed by cloud providers, network engineers, and infrastructure teams. Understanding all seven layers helps diagnose performance, security, scalability, and connectivity issues end-to-end."**


=================


# OSI Layer Mapping with Tools, Components, Examples & Use Cases (Interview Quick Notes)

## Layer 7 – Application Layer

### Purpose

Provides network services directly to applications and end users.

### Tools/Protocols

* HTTP/HTTPS
* REST API
* GraphQL
* gRPC
* DNS
* WebSocket

### Example

Browser sends an HTTPS request to an E-commerce application.

### Use Case

Microservices communication, API Gateway, Banking Apps, ERP Systems.

---

## Layer 6 – Presentation Layer

### Purpose

Handles data formatting, encryption, serialization, compression, and encoding.

### Tools/Technologies

* TLS/SSL
* JSON
* XML
* Base64
* Protobuf
* GZIP

### Example

Spring Boot converts Java Object → JSON and encrypts data using TLS.

### Use Case

Secure API communication, Data Exchange, Kafka Messages.

---

## Layer 5 – Session Layer

### Purpose

Creates, manages, and terminates communication sessions.

### Tools/Technologies

* JWT
* OAuth2
* SSO
* Session Cookies
* WebSocket Sessions

### Example

User logs into Amazon and remains authenticated for several hours.

### Use Case

Authentication, User Sessions, Video Calls, Chat Applications.

---

## Layer 4 – Transport Layer

### Purpose

Provides reliable or high-speed communication between systems.

### Tools/Protocols

* TCP
* UDP
* QUIC

### Example

Online payment transactions use TCP while Zoom video uses UDP.

### Use Case

REST APIs, gRPC, Kafka, Streaming Platforms, Gaming.

---

## Layer 3 – Network Layer

### Purpose

Routes packets between different networks and locations.

### Tools/Components

* IPv4
* IPv6
* NAT
* Routers
* VPN
* VPC

### Example

A request travels from India to a server hosted in OCI Mumbai Region.

### Use Case

Cloud Networking, Multi-Region Deployments, Hybrid Cloud.

---

## Layer 2 – Data Link Layer

### Purpose

Transfers data between devices on the same local network.

### Tools/Components

* Ethernet
* WiFi
* MAC Address
* VLAN
* Network Switch

### Example

Laptop communicates with the office WiFi router.

### Use Case

Data Centers, Kubernetes Clusters, Corporate Networks.

---

## Layer 1 – Physical Layer

### Purpose

Transmits raw bits through physical media.

### Tools/Components

* Fiber Optic Cable
* Ethernet Cable
* Wireless Signals
* Network Interface Cards (NIC)

### Example

Internet traffic travels through undersea fiber optic cables.

### Use Case

Cloud Infrastructure, Data Centers, ISP Networks.

---

# OSI Layer Mapping with Modern System Design Components

| OSI Layer    | Tools/Components                        | Example Use Case                 |
| ------------ | --------------------------------------- | -------------------------------- |
| Application  | REST API, GraphQL, gRPC, DNS, WebSocket | E-commerce, Banking APIs         |
| Presentation | TLS, SSL, JSON, XML, Protobuf, GZIP     | Secure API Payloads              |
| Session      | JWT, OAuth2, SSO, Cookies               | User Login & Authentication      |
| Transport    | TCP, UDP, QUIC                          | Payments, Streaming, Gaming      |
| Network      | IPv4, IPv6, NAT, VPN, Routers           | Cloud Networking                 |
| Data Link    | Ethernet, WiFi, VLAN, Switches          | Office & Data Center Networks    |
| Physical     | Fiber, Cable, NIC, Wireless             | Internet Backbone Infrastructure |

---

# Real Enterprise Example (OCI + Kubernetes + Microservices)

```text
User Browser
    |
HTTP/HTTPS
(Application)
    |
TLS Encryption
(Presentation)
    |
JWT Session
(Session)
    |
TCP
(Transport)
    |
IPv4/VPN/NAT
(Network)
    |
Ethernet/VLAN
(Data Link)
    |
Fiber Cable
(Physical)
    |
OCI Load Balancer
    |
API Gateway
    |
Spring Boot Microservices
    |
Kafka
    |
Oracle DB
```

### Interview Summary

* **Application Layer** → APIs, DNS, WebSockets.
* **Presentation Layer** → Encryption, Serialization, Encoding.
* **Session Layer** → Login Sessions, JWT, OAuth.
* **Transport Layer** → TCP, UDP, QUIC.
* **Network Layer** → IP Routing, NAT, VPN.
* **Data Link Layer** → Ethernet, WiFi, VLAN.
* **Physical Layer** → Fiber, Cables, Hardware.

This mapping is frequently used when explaining end-to-end request flow in **Java/Spring Boot, Kubernetes, OCI, AWS, GCP, Kafka, Banking, ERP, and Microservices system design interviews**.
