# System Design Topics – 2-4 Line Interview Explanations

## URL (Uniform Resource Locator)

A URL is the human-readable address used to access resources on the internet. It contains the protocol, domain name, port (optional), and resource path. Example: `https://amazon.com/products/123`.

---

## DNS (Domain Name System)

DNS translates domain names into IP addresses so computers can locate servers. It acts like the internet's phonebook. Example: `google.com → 142.250.x.x`.

---

## IP Address

An IP address uniquely identifies a device on a network. It enables communication between clients and servers. Example: `192.168.1.10`.

---

## IPv4

IPv4 is a 32-bit addressing scheme represented as four decimal numbers separated by dots. It supports approximately 4.3 billion addresses and is still widely used today.

---

## IPv6

IPv6 is a 128-bit addressing scheme designed to solve IPv4 address exhaustion. It provides a virtually unlimited address space and improved routing efficiency.

---

## NAT (Network Address Translation)

NAT converts private IP addresses into public IP addresses for internet communication. It helps conserve IPv4 addresses and adds a layer of network isolation.

---

## TCP (Transmission Control Protocol)

TCP is a reliable, connection-oriented protocol that guarantees ordered delivery of packets. It uses acknowledgments and retransmissions to ensure data integrity.

---

## UDP (User Datagram Protocol)

UDP is a lightweight, connectionless protocol that prioritizes speed over reliability. It is commonly used in gaming, VoIP, DNS, and video streaming.

---

## QUIC

QUIC is a modern transport protocol built on UDP that combines transport and security features. It reduces latency and improves connection establishment compared to TCP.

---

## HTTP

HTTP is the standard protocol used for communication between web clients and servers. It follows a request-response model and is stateless by design.

---

## HTTP/1.1

HTTP/1.1 introduced persistent connections but processes requests sequentially on a connection. It often suffers from head-of-line blocking.

---

## HTTP/2

HTTP/2 allows multiplexing multiple requests over a single TCP connection. It improves performance through header compression and parallel streams.

---

## HTTP/3

HTTP/3 runs on QUIC instead of TCP, reducing latency and improving performance on unstable networks. It is designed for faster and more reliable web communication.

---

## HTTPS

HTTPS is HTTP secured with TLS encryption. It provides confidentiality, integrity, and authentication for data exchanged between client and server.

---

## SSL (Secure Socket Layer)

SSL was the original protocol used to secure internet communication. It has been deprecated due to security vulnerabilities and replaced by TLS.

---

## TLS (Transport Layer Security)

TLS is the modern protocol for securing network communications. It encrypts data, verifies identities using certificates, and ensures message integrity.

---

## Certificate

A digital certificate contains a server's public key and identity information. It is issued by a trusted Certificate Authority and is used during TLS handshakes.

---

## API (Application Programming Interface)

An API is a contract that allows different applications to communicate. It defines request formats, response structures, authentication, and error handling.

---

## REST API

REST is an architectural style that uses HTTP methods such as GET, POST, PUT, and DELETE. REST APIs are stateless and typically exchange JSON data.

---

## GraphQL

GraphQL allows clients to request exactly the data they need from a single endpoint. It reduces over-fetching and under-fetching of data.

---

## gRPC

gRPC is a high-performance communication framework based on HTTP/2 and Protocol Buffers. It supports streaming and is commonly used for microservice communication.

---

## WebSocket

WebSocket provides a persistent, full-duplex communication channel between client and server. It is ideal for real-time applications such as chat and stock trading.

---

## Webhook

A webhook is an event-driven callback mechanism where one system automatically notifies another when an event occurs. Example: Payment success notification.

---

## WebRTC

WebRTC enables peer-to-peer audio, video, and data communication directly between browsers. It powers applications like video conferencing and screen sharing.

---

## STUN

STUN helps devices behind NAT discover their public IP address and network characteristics. It is commonly used in WebRTC connection setup.

---

## TURN

TURN acts as a relay server when direct peer-to-peer communication is not possible. It forwards traffic between endpoints in restrictive network environments.

---

## ICE

ICE is a framework that combines STUN and TURN to determine the best communication path between peers. It optimizes WebRTC connectivity.

---

## Encoding

Encoding converts data into a different format for storage or transmission. Examples include UTF-8, ASCII, and Base64. Encoding is not encryption.

---

## Serialization

Serialization converts objects into transferable formats such as JSON, XML, Avro, or Protobuf. It enables communication between distributed systems.

---

## Compression

Compression reduces the size of data before transmission or storage. Common algorithms include GZIP and Brotli, which improve network performance.

---

## Hashing

Hashing converts data into a fixed-length value using one-way algorithms. It is commonly used for password storage and integrity verification.

---

## Checksum

A checksum is a calculated value used to detect accidental data corruption. The sender and receiver compare checksums to verify data integrity.

---

## Encryption

Encryption transforms plaintext into ciphertext using cryptographic keys. Only authorized users with the correct key can decrypt the data.

---

## Symmetric Encryption

Symmetric encryption uses the same key for both encryption and decryption. It is fast and commonly used for encrypting large amounts of data.

---

## Asymmetric Encryption

Asymmetric encryption uses a public-private key pair. The public key encrypts data, while the private key decrypts it.

---

## Diffie-Hellman (DH)

Diffie-Hellman is a key exchange algorithm that allows two parties to securely establish a shared secret over an insecure network.

---

## ECDHE

ECDHE (Elliptic Curve Diffie-Hellman Ephemeral) is a modern key exchange mechanism used in TLS. It provides Perfect Forward Secrecy.

---

## Perfect Forward Secrecy (PFS)

PFS ensures that compromising a server's private key does not expose previously encrypted sessions. Each session uses unique temporary keys.

---

## Digital Signature

A digital signature verifies the authenticity and integrity of data. It uses a private key for signing and a public key for verification.

---

## Double Ratchet

Double Ratchet is an advanced encryption protocol used by secure messaging applications. It continuously rotates encryption keys to provide forward secrecy and post-compromise security.

---

## Proxy Server

A proxy server acts as an intermediary between a client and destination server. It can provide caching, filtering, anonymity, and security.

---

## Forward Proxy

A forward proxy sits between clients and the internet. Organizations often use it to control employee internet access and enforce security policies.

---

## Reverse Proxy

A reverse proxy sits in front of backend servers and handles incoming requests. It provides load balancing, SSL termination, caching, and security.

---

## VPN (Virtual Private Network)

A VPN creates an encrypted tunnel between a user and a private network. It enables secure remote access to corporate systems.

---

## SSH (Secure Shell)

SSH is a secure protocol for remote server administration. It encrypts communication and supports password or key-based authentication.

---

## Bastion Host

A bastion host is a hardened jump server used to access private infrastructure securely. It serves as the single entry point into protected environments.

---

## SSH Tunnel

SSH tunneling securely forwards network traffic through an encrypted SSH connection. It is often used to access private databases or internal services.

---

## Tor Network

Tor routes traffic through multiple volunteer-operated relays to conceal a user's identity and location. It focuses on privacy and anonymity but introduces additional latency.

---

## Load Balancer

A load balancer distributes incoming traffic across multiple servers. It improves availability, scalability, and fault tolerance.

---

## API Gateway

An API Gateway is the centralized entry point for APIs. It handles authentication, authorization, routing, throttling, logging, and monitoring.

---

## Cache (Redis)

A cache stores frequently accessed data in memory to reduce database load and improve response times. Redis is one of the most popular caching solutions.

---

## Message Queue (Kafka)

Kafka is a distributed event streaming platform used for asynchronous communication between systems. It enables high throughput and decouples services.

---

## Database

A database stores and manages application data. Relational databases provide ACID guarantees, while NoSQL databases prioritize scalability and flexibility.

---

## Docker

Docker packages applications and dependencies into portable containers. It ensures consistent behavior across development, testing, and production environments.

---

## Kubernetes

Kubernetes automates deployment, scaling, networking, and management of containers. It provides self-healing, service discovery, and rolling updates.

---

## Monitoring

Monitoring collects metrics such as CPU, memory, latency, and throughput. Tools like Prometheus and Grafana help detect performance issues proactively.

---

## Logging

Logging records application and system events for troubleshooting and auditing. Common log levels include INFO, DEBUG, WARN, and ERROR.

---

## Distributed Tracing

Distributed tracing follows a request across multiple services and systems. It helps identify bottlenecks and troubleshoot microservice architectures.

---

## Authentication

Authentication verifies the identity of a user or system. Common methods include passwords, OAuth2, SSO, and MFA.

---

## Authorization

Authorization determines what authenticated users are allowed to access. It is typically implemented using roles and permissions.

---

## JWT (JSON Web Token)

JWT is a compact, stateless authentication token containing claims about a user. It is commonly used for API security and microservices authentication.
