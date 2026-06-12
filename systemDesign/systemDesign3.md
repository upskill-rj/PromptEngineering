# Advanced System Design – Networking, APIs, Communication Protocols & Connectivity

These topics are frequently asked in **Solution Architect, System Design, Java Architect, Cloud Architect, Kubernetes, OCI, AWS, and GCP interviews**.

---

# 1. API (Application Programming Interface)

### Purpose

A contract that allows two applications to communicate.

### Example

```text
Mobile App
    |
API
    |
Banking System
```

### Real Use Case

```text
Paytm → UPI API → Bank
```

The API defines:

* Request format
* Response format
* Authentication
* Error handling

---

# 2. REST API

### Purpose

Most common API style over HTTP.

### Characteristics

* Stateless
* Resource-oriented
* JSON based

### Example

```http
GET /users/101
```

Response

```json
{
  "id":101,
  "name":"Rahul"
}
```

### Tools

* Spring Boot
* NodeJS
* FastAPI
* ASP.NET

### Use Cases

* E-commerce
* ERP
* Banking
* Mobile Apps

---

# 3. GraphQL

### Purpose

Client requests exactly what it needs.

### Example

Instead of:

```http
GET /user
```

Client asks:

```graphql
{
 user {
   name
   email
 }
}
```

### Benefits

* Less network traffic
* Flexible queries
* Single endpoint

### Use Cases

* Mobile Applications
* Complex Dashboards
* Social Media Platforms

---

# 4. gRPC

### Purpose

High-performance communication between services.

### Technology

* HTTP/2
* Protocol Buffers

### Example

```protobuf
GetUser(id=101)
```

### Benefits

* Very Fast
* Binary Protocol
* Streaming Support

### Use Cases

* Microservices
* Trading Systems
* AI Platforms

---

# 5. HTTP

### Purpose

Application communication protocol.

### Example

```http
GET /products
```

### Methods

```text
GET
POST
PUT
DELETE
PATCH
```

---

# 6. HTTP/1.1

### Features

* One request per connection
* Head-of-line blocking
* Text protocol

### Problem

```text
Request 1
Request 2
Request 3
```

Can become slow.

---

# 7. HTTP/2

### Features

* Multiplexing
* Header Compression
* Single Connection

### Example

```text
1 TCP Connection
     |
Multiple Requests
```

### Benefits

* Faster websites
* Better performance

---

# 8. HTTP/3

### Features

Uses UDP instead of TCP.

### Protocol

```text
HTTP/3
   |
QUIC
   |
UDP
```

### Benefits

* Faster reconnections
* Reduced latency
* Better mobile performance

Used by:

* Google
* Meta
* Cloudflare

---

# 9. QUIC

### Purpose

Modern transport protocol developed by Google.

### Features

* Built on UDP
* TLS integrated
* Faster handshakes

### Example

```text
HTTP/3
   |
QUIC
   |
UDP
```

### Use Cases

* Video Streaming
* Mobile Networks
* Real-time Apps

---

# 10. WebSocket

### Purpose

Persistent two-way communication.

### Example

```text
Client <======> Server
```

Connection remains open.

### Use Cases

* Stock Trading
* Chat Applications
* Live Notifications
* Multiplayer Games

---

# 11. Webhook

### Purpose

Server-to-server callback mechanism.

### Example

```text
Payment Completed
      |
Webhook Triggered
      |
ERP System Updated
```

### Use Cases

* Payment Gateways
* GitHub Events
* CI/CD Pipelines

---

# 12. NAT (Network Address Translation)

### Purpose

Translate private IPs to public IPs.

### Example

```text
Private
192.168.1.10

Public
45.x.x.x
```

### Benefits

* Conserves IPv4 addresses
* Security isolation

### Use Cases

Home Routers, Cloud Networks

---

# 13. WebRTC

### Purpose

Peer-to-peer real-time communication.

### Features

* Audio
* Video
* Screen Sharing

### Example

```text
Browser <----> Browser
```

### Use Cases

* Video Conferencing
* Online Meetings
* Telemedicine

---

# 14. STUN

### Purpose

Helps discover public IP and NAT type.

### Example

```text
Browser
   |
STUN Server
   |
Returns Public IP
```

### Use Case

WebRTC connection establishment.

---

# 15. TURN

### Purpose

Relay traffic when direct connection fails.

### Example

```text
Client A
   |
TURN Server
   |
Client B
```

### Use Case

Strict corporate firewalls.

---

# 16. ICE (Interactive Connectivity Establishment)

### Purpose

Framework that chooses best connection path.

### Process

```text
STUN Candidate
TURN Candidate
Local Candidate
```

ICE selects optimal route.

### Use Case

WebRTC.

---

# 17. SSH (Secure Shell)

### Purpose

Secure remote server access.

### Example

```bash
ssh user@server
```

### Benefits

* Encryption
* Authentication

### Use Cases

* Linux Administration
* Kubernetes Nodes
* Cloud VMs

---

# 18. Bastion Host

### Purpose

Secure jump server for private environments.

### Architecture

```text
Admin
  |
Bastion Host
  |
Private Servers
```

### Benefits

* Controlled access
* Auditability

### Use Cases

OCI, AWS, GCP Production Environments

---

# 19. SSH Tunneling

### Purpose

Securely forward traffic through SSH.

### Example

```bash
ssh -L 1521:db-server:1521
```

### Flow

```text
Laptop
   |
SSH Tunnel
   |
Oracle DB
```

### Use Cases

* Database Access
* Secure Development

---

# 20. VPN (Virtual Private Network)

### Purpose

Create encrypted network between locations.

### Example

```text
Laptop
   |
VPN
   |
Corporate Network
```

### Benefits

* Encryption
* Secure Access

### Technologies

* IPSec
* OpenVPN
* WireGuard

---

# 21. Proxy Server

### Purpose

Acts as intermediary between client and server.

### Flow

```text
Client
   |
Proxy
   |
Internet
```

### Types

### Forward Proxy

Used by clients.

Example:

```text
Corporate Internet Access
```

### Reverse Proxy

Used by servers.

Tools:

* [NGINX](https://nginx.org/?utm_source=chatgpt.com)
* [HAProxy](https://www.haproxy.org/?utm_source=chatgpt.com)

Example:

```text
Internet
   |
NGINX
   |
Application Servers
```

---

# 22. Tor Network

### Purpose

Privacy-focused anonymous routing network.

### Flow

```text
User
  |
Relay 1
  |
Relay 2
  |
Relay 3
  |
Destination
```

### Benefits

* Conceals source IP
* Enhances anonymity

### Use Cases

* Privacy Protection
* Research in restrictive environments

### Limitation

Higher latency due to multiple relay hops.

---

# Communication Technology Comparison

| Technology | Purpose                          | Typical Use Case       |
| ---------- | -------------------------------- | ---------------------- |
| REST API   | Application communication        | Web & Mobile Apps      |
| GraphQL    | Flexible data retrieval          | Dashboards             |
| gRPC       | High-speed service communication | Microservices          |
| WebSocket  | Real-time bidirectional          | Chat, Trading          |
| Webhook    | Event notification               | Payment systems        |
| HTTP/1.1   | Traditional web traffic          | Legacy systems         |
| HTTP/2     | Multiplexed communication        | Modern websites        |
| HTTP/3     | Low latency communication        | Mobile/Web apps        |
| QUIC       | Fast transport protocol          | HTTP/3                 |
| WebRTC     | Real-time peer communication     | Video calls            |
| SSH        | Secure administration            | Server management      |
| VPN        | Secure network access            | Remote employees       |
| Proxy      | Traffic mediation                | Enterprise networks    |
| Tor        | Anonymous routing                | Privacy-focused access |

---

# Enterprise End-to-End Example

```text
User
 |
DNS
 |
IPv4 / IPv6
 |
TCP / QUIC
 |
TLS
 |
HTTP/2 or HTTP/3
 |
Load Balancer
 |
Reverse Proxy (NGINX)
 |
API Gateway
 |
REST API / GraphQL / gRPC
 |
Microservices
 |
Kafka
 |
Redis
 |
Oracle DB
 |
Object Storage
 |
Monitoring (Prometheus/Grafana)
 |
Logging (OpenSearch/Splunk)
 |
Tracing (OpenTelemetry/Jaeger)
```

This architecture is commonly used in large-scale banking systems, ERP platforms, OCI/AWS/GCP cloud deployments, Kubernetes-based microservices, video conferencing systems (WebRTC), payment gateways, and AI-enabled enterprise applications.
