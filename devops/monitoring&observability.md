# Monitoring and Observability – Complete Overview

Monitoring and Observability are critical pillars of modern cloud-native architectures, microservices, Kubernetes, DevOps, SRE, and AI systems.

---

# 1. What is Monitoring?

Monitoring is the process of collecting predefined metrics, logs, and alerts to understand whether a system is healthy.

It answers:

* Is the application up?
* Is CPU usage high?
* Is database responding?
* Is API failing?

### Example

A payment service exposes:

* CPU = 85%
* Memory = 75%
* Response Time = 500ms
* Error Rate = 2%

Monitoring tools continuously collect these values and trigger alerts when thresholds are crossed.

---

# 2. What is Observability?

Observability goes beyond monitoring.

It helps understand WHY a problem occurred by analyzing:

1. Metrics
2. Logs
3. Traces

### Example

Monitoring tells:

"Checkout API response time increased from 200ms to 5 seconds."

Observability tells:

"Checkout API is waiting on Inventory Service, which is waiting on Oracle DB due to slow SQL execution."

---

# Monitoring vs Observability

| Monitoring      | Observability           |
| --------------- | ----------------------- |
| Detects issues  | Diagnoses issues        |
| Known problems  | Unknown problems        |
| Metrics focused | Metrics + Logs + Traces |
| Reactive        | Proactive               |
| Alerts based    | Root cause analysis     |

---

# Three Pillars of Observability

## 1. Metrics

Numerical measurements over time.

Examples:

* CPU Usage
* Memory Usage
* Disk Utilization
* Request Count
* Error Rate

### Sample Metric

```
CPU Usage = 80%
Response Time = 300ms
```

Collected every few seconds.

---

## 2. Logs

Detailed event records.

Example:

```json
{
 "timestamp":"2026-06-10",
 "service":"payment-service",
 "level":"ERROR",
 "message":"Database connection timeout"
}
```

Logs explain what happened.

---

## 3. Distributed Traces

Track requests across multiple services.

Example:

```
Client
 ↓
API Gateway
 ↓
Order Service
 ↓
Inventory Service
 ↓
Oracle Database
```

Trace shows:

```
Order Service      20ms
Inventory Service  5ms
Oracle DB         4000ms
```

Root cause identified immediately.

---

# Modern Observability Architecture

```text
Application
     |
     v
OpenTelemetry Agent
     |
     +------ Metrics
     +------ Logs
     +------ Traces
     |
     v
Observability Platform
     |
     +---- Grafana
     +---- Splunk
     +---- Datadog
     +---- New Relic
     |
     v
Dashboards + Alerts
```

---

# Key Components

## Metrics Collector

Collects system/application metrics.

Examples:

* Prometheus
* Datadog Agent
* Telegraf

---

## Log Aggregator

Collects logs from multiple systems.

Examples:

* ELK Stack
* Splunk
* Fluentd
* Fluent Bit

---

## Trace Collector

Collects distributed traces.

Examples:

* Jaeger
* Zipkin
* OpenTelemetry Collector

---

## Visualization Layer

Creates dashboards.

Examples:

* Grafana
* Kibana
* Datadog
* Splunk

---

## Alerting Engine

Sends alerts.

Examples:

* PagerDuty
* Opsgenie
* Grafana Alerts
* Prometheus AlertManager

---

# Popular Monitoring Tools

## Prometheus

Most popular Kubernetes monitoring tool.

Features:

* Time-series database
* Pull-based metrics
* Alerting
* Service discovery

Example:

```yaml
scrape_configs:
  - job_name: payment-service
```

Prometheus pulls metrics every 15 seconds.

---

## Grafana

Visualization platform.

Features:

* Dashboards
* Alerting
* Multiple data sources

Example Dashboard:

```
CPU Usage
Memory Usage
Request Rate
Latency
```

---

## Nagios

Traditional infrastructure monitoring.

Monitors:

* Servers
* Network devices
* Databases

Example:

```
Server Down
Disk Full
CPU High
```

---

## Sensu

Cloud-native monitoring.

Used for:

* Infrastructure
* Kubernetes
* Hybrid Cloud

---

# Log Monitoring Tools

## ELK Stack

### Elasticsearch

Stores logs.

### Logstash

Processes logs.

### Kibana

Visualizes logs.

Architecture:

```text
Application
    |
 Logstash
    |
Elasticsearch
    |
 Kibana
```

---

## Splunk

Enterprise log analytics platform.

Features:

* Search
* Dashboards
* AI-based anomaly detection

Example Query:

```spl
index=payment error
```

Finds all payment errors.

---

# Distributed Tracing Tools

## Jaeger

Popular Kubernetes tracing tool.

Architecture:

```text
Application
      |
      v
Jaeger Agent
      |
Collector
      |
Storage
      |
UI
```

Use Case:

Track slow microservice requests.

---

## Zipkin

Lightweight tracing platform.

Tracks:

```
API → Service → DB
```

latency.

---

# OpenTelemetry (Industry Standard)

Most important observability technology today.

Used by:

* OCI
* AWS
* Azure
* GCP
* Kubernetes

Provides:

* Metrics
* Logs
* Traces

through one framework.

Architecture:

```text
Application
      |
OpenTelemetry SDK
      |
Collector
      |
Backend
```

Backends:

* Grafana
* Datadog
* Splunk
* New Relic
* Jaeger

---

# Kubernetes Monitoring Architecture

```text
Pods
 |
Node Exporter
 |
Prometheus
 |
Grafana
```

Monitors:

* Pod CPU
* Memory
* Network
* Container Health

---

# OCI Monitoring & Observability

### OCI Monitoring

Collects:

* Compute Metrics
* OKE Metrics
* Database Metrics

Examples:

* CPU Utilization
* Memory Usage
* Storage IOPS

---

### OCI Logging

Collects:

* Application Logs
* Audit Logs
* Load Balancer Logs

---

### OCI Application Performance Monitoring (APM)

Provides:

* Distributed Tracing
* Root Cause Analysis
* User Experience Monitoring

Architecture:

```text
Java Application
      |
APM Agent
      |
OCI APM
      |
Dashboard
```

---

# AWS Monitoring Stack

Components:

* Amazon CloudWatch
* AWS X-Ray
* AWS CloudTrail

Use Case:

Monitor Lambda + ECS + RDS applications.

---

# Azure Monitoring Stack

Components:

* Azure Monitor
* Application Insights
* Log Analytics

---

# SRE Golden Signals

Google SRE uses four primary metrics:

### Latency

How fast requests complete.

Example:

```
95th percentile = 300ms
```

---

### Traffic

Number of requests.

Example:

```
5000 requests/min
```

---

### Errors

Failure percentage.

Example:

```
2% failed requests
```

---

### Saturation

Resource utilization.

Example:

```
CPU = 90%
```

---

# Real Interview Example

## Scenario

Users complain:

```
Order creation takes 15 seconds.
```

### Monitoring Shows

```
Order API Latency = 15 sec
```

### Logs Show

```
Oracle DB timeout
```

### Traces Show

```
API Gateway      10ms
Order Service    30ms
Inventory        50ms
Oracle DB       14800ms
```

### Root Cause

Slow database query.

### Fix

* Add indexes
* Tune SQL
* Increase connection pool
* Scale database

---

# Monitoring & Observability Tool Matrix

| Area          | Tools                                |
| ------------- | ------------------------------------ |
| Metrics       | Prometheus, Datadog, CloudWatch      |
| Visualization | Grafana, Kibana                      |
| Logging       | ELK, Splunk, Fluentd                 |
| Tracing       | Jaeger, Zipkin                       |
| Alerting      | AlertManager, PagerDuty, Opsgenie    |
| Cloud Native  | OpenTelemetry                        |
| OCI           | OCI Monitoring, OCI Logging, OCI APM |
| AWS           | CloudWatch, X-Ray                    |
| Azure         | Azure Monitor, App Insights          |
| GCP           | Cloud Monitoring, Cloud Trace        |

# Interview Answer (2-3 Minutes)

"Monitoring focuses on collecting predefined metrics and generating alerts when thresholds are breached, such as CPU, memory, or API latency. Observability extends monitoring by combining metrics, logs, and distributed traces to diagnose the root cause of issues in complex distributed systems. In modern cloud-native environments, OpenTelemetry is used to collect telemetry data, Prometheus gathers metrics, Grafana provides dashboards, ELK/Splunk manage logs, and Jaeger or Zipkin handle distributed tracing. Together they enable proactive monitoring, faster incident resolution, and improved system reliability."
