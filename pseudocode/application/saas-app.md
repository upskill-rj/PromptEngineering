# OCI ERP Fusion — Complete Microservices Pseudocode Architecture

---

## TABLE OF CONTENTS
1. Infrastructure & Cloud (OCI)
2. DNS & WAF
3. Load Balancer (LBaaS)
4. API Gateway & OAuth 2.0
5. Kubernetes (OKE)
6. Microservices — Spring Boot
7. Frontend — React
8. REST API Contracts
9. Kafka (Event Streaming)
10. Redis (Caching)
11. Database Layer
12. Azure SharePoint Integration
13. DevSecOps / CI / CD Pipeline
14. Monitoring & Observability
15. Security & Secrets Management
16. End-to-End Request Flow

---

## 1. INFRASTRUCTURE & CLOUD (OCI)

```
INFRASTRUCTURE oci_tenancy:

  DEFINE compartments:
    - production_compartment
    - staging_compartment
    - dev_compartment
    - shared_services_compartment

  DEFINE vcn (virtual_cloud_network):
    cidr_block = "10.0.0.0/16"

    SUBNETS:
      - public_subnet   cidr="10.0.1.0/24"   (WAF, LBaaS)
      - private_subnet  cidr="10.0.2.0/24"   (API Gateway, Microservices)
      - data_subnet     cidr="10.0.3.0/24"   (Databases, Redis, Kafka)

    SECURITY_GROUPS:
      - allow_https_inbound     port=443   source=0.0.0.0/0
      - allow_internal_traffic  port=ALL   source=10.0.0.0/16
      - deny_all_else

  DEFINE object_storage:
    - bucket: erp-artifacts       (CI/CD build artifacts)
    - bucket: erp-backups         (database backups)
    - bucket: erp-sharepoint-sync (SharePoint documents)

  DEFINE vault:
    - store DB_PASSWORD
    - store KAFKA_SECRET
    - store OAUTH_CLIENT_SECRET
    - store SHAREPOINT_TOKEN
    - store REDIS_AUTH_TOKEN
    - store JWT_SIGNING_KEY
```

---

## 2. DNS & WAF

```
COMPONENT dns_service (OCI DNS):

  FUNCTION register_domain(domain):
    CREATE zone: erp.company.com
    ADD A_record:    erp.company.com         → LBaaS_public_IP
    ADD CNAME:       api.erp.company.com     → api-gateway.internal
    ADD CNAME:       app.erp.company.com     → frontend-service.internal
    ADD CNAME:       sharepoint.erp.company.com → sharepoint-proxy.internal
    SET ttl = 300
    SET health_check_endpoint = "/health"

  FUNCTION dns_failover():
    IF primary_region_health == UNHEALTHY:
      SWITCH traffic → secondary_region
      NOTIFY ops_team via PagerDuty


COMPONENT waf (OCI Web Application Firewall):

  FUNCTION configure_waf():

    RULES:
      - BLOCK SQL_INJECTION patterns
      - BLOCK XSS patterns
      - BLOCK CSRF patterns
      - BLOCK malicious_bots via user-agent fingerprinting
      - RATE_LIMIT per_ip = 1000 requests/minute
      - RATE_LIMIT per_api_key = 5000 requests/minute
      - GEO_BLOCK restricted_countries[]
      - ALLOW known_cidrs[] from OCI VCN

    OWASP_RULESET:
      ENABLE top_10_protections = TRUE
      SENSITIVITY_LEVEL = HIGH

    DDoS_PROTECTION:
      threshold = 10000 requests/second
      IF exceeded → trigger scrubbing_center
      ALERT security_team

    LOGGING:
      forward_logs → OCI Logging Analytics
      forward_logs → SIEM (Splunk/Datadog)

  FUNCTION inspect_request(request):
    FOR each rule IN waf_ruleset:
      IF rule.matches(request):
        IF rule.action == BLOCK:
          RETURN http_response(403, "Forbidden")
        IF rule.action == CHALLENGE:
          RETURN captcha_challenge()
    RETURN PASS → LBaaS
```

---

## 3. LOAD BALANCER (LBaaS)

```
COMPONENT lbaas (OCI Load Balancer as a Service):

  DEFINE listeners:
    - HTTPS listener on port 443  → backend_set: api_gateway_pool
    - HTTP  listener on port 80   → REDIRECT to HTTPS

  DEFINE backend_sets:

    api_gateway_pool:
      algorithm = ROUND_ROBIN  // or LEAST_CONNECTIONS / IP_HASH
      health_check:
        protocol = HTTPS
        path     = "/health"
        interval = 10s
        timeout  = 3s
        unhealthy_threshold = 3
      backends:
        - api_gateway_node_1:443
        - api_gateway_node_2:443
        - api_gateway_node_3:443

    frontend_pool:
      algorithm = IP_HASH        // sticky sessions for React SPA
      backends:
        - frontend_node_1:3000
        - frontend_node_2:3000

  FUNCTION handle_request(incoming_request):
    tls_terminate(incoming_request)      // SSL offloading at LBaaS
    inject_header("X-Request-ID", uuid())
    inject_header("X-Forwarded-For", client_ip)
    route → api_gateway_pool
    LOG request_metadata → OCI Logging

  SSL_POLICY:
    min_tls_version = TLS_1_2
    cipher_suites   = [TLS_AES_256_GCM_SHA384, TLS_CHACHA20_POLY1305]
    certificate     = oci_certificates_service.fetch("erp.company.com")
```

---

## 4. API GATEWAY & OAUTH 2.0

```
COMPONENT api_gateway (OCI API Gateway):

  DEFINE routes:
    /api/v1/finance/*      → finance-service:8080
    /api/v1/procurement/*  → procurement-service:8081
    /api/v1/hr/*           → hr-service:8082
    /api/v1/inventory/*    → inventory-service:8083
    /api/v1/reporting/*    → reporting-service:8084
    /api/v1/sharepoint/*   → sharepoint-proxy-service:8085
    /api/v1/notifications/ → notification-service:8086

  POLICIES:
    - authentication: OAUTH2_JWT
    - rate_limiting:  1000 req/min per client
    - request_transformation: inject correlation_id header
    - response_transformation: strip internal headers
    - cors: allow_origins=["https://app.erp.company.com"]

  FUNCTION route_request(request):
    token = extract_bearer_token(request.headers)
    claims = oauth_service.validate_token(token)

    IF claims == INVALID:
      RETURN http_response(401, "Unauthorized")

    IF NOT rbac.has_permission(claims.role, request.path, request.method):
      RETURN http_response(403, "Forbidden")

    apply_rate_limit(claims.client_id)
    inject_header("X-User-ID",   claims.sub)
    inject_header("X-Tenant-ID", claims.tenant)
    inject_header("X-Roles",     claims.roles)

    target_service = resolve_route(request.path)
    FORWARD request → target_service
    LOG route_event → kafka topic: api-gateway-logs


COMPONENT oauth_service (OCI Identity / Keycloak):

  DEFINE realms:
    - erp_internal_realm   (employees)
    - erp_partner_realm    (vendors, partners)
    - erp_system_realm     (service-to-service)

  DEFINE clients:
    - react_spa_client:         grant_type = AUTHORIZATION_CODE + PKCE
    - spring_boot_services:     grant_type = CLIENT_CREDENTIALS
    - sharepoint_connector:     grant_type = CLIENT_CREDENTIALS

  FUNCTION authorize(request):
    validate client_id, redirect_uri
    IF user NOT authenticated:
      REDIRECT → login_page
    ELSE:
      ISSUE authorization_code
      REDIRECT → redirect_uri?code=auth_code

  FUNCTION token_exchange(auth_code):
    VERIFY auth_code validity and expiry
    GENERATE access_token:
      type      = JWT
      algorithm = RS256
      expiry    = 15 minutes
      claims:
        sub, email, roles, tenant_id, permissions
    GENERATE refresh_token:
      expiry = 8 hours
      store  → redis (for revocation checks)
    RETURN { access_token, refresh_token, expires_in }

  FUNCTION validate_token(token):
    VERIFY signature using public_key from JWKS endpoint
    CHECK expiry
    CHECK revocation_list in Redis
    RETURN claims OR throw INVALID_TOKEN

  FUNCTION refresh_token(refresh_token):
    LOOKUP refresh_token in Redis
    IF not found OR expired:
      RETURN 401
    ISSUE new access_token
    ROTATE refresh_token
    RETURN new_tokens
```

---

## 5. KUBERNETES (OKE — Oracle Container Engine)

```
COMPONENT kubernetes_cluster (OKE):

  DEFINE node_pools:
    - system_pool:     nodes=3,  shape=VM.Standard.E4.Flex  (system services)
    - app_pool:        nodes=6,  shape=VM.Standard.E4.Flex  (microservices)
    - data_pool:       nodes=3,  shape=VM.Standard.E4.Flex  (Kafka, Redis)
    - monitoring_pool: nodes=2,  shape=VM.Standard.E3.Flex  (Prometheus, Grafana)

  NAMESPACES:
    - erp-system         (ingress, cert-manager, vault-agent)
    - erp-services       (all microservices)
    - erp-data           (Kafka, Redis operators)
    - erp-monitoring     (Prometheus, Grafana, Jaeger, Loki)
    - erp-cicd           (Tekton / ArgoCD)

  FUNCTION deploy_service(service_name, image, config):

    CREATE Deployment:
      replicas        = 3
      image           = registry.company.com/{service_name}:{tag}
      resources:
        requests: cpu=250m, memory=512Mi
        limits:   cpu=1,    memory=1Gi
      env_from:       ConfigMap, Secret (injected by Vault agent)
      liveness_probe:  GET /actuator/health/liveness   every 10s
      readiness_probe: GET /actuator/health/readiness  every 5s
      rolling_update:
        maxSurge         = 1
        maxUnavailable   = 0

    CREATE Service:
      type      = ClusterIP
      port      = 8080
      selector  = app: {service_name}

    CREATE HorizontalPodAutoscaler:
      min_replicas = 2
      max_replicas = 20
      metric: cpu_utilization > 70%
      metric: rps > 500

    CREATE PodDisruptionBudget:
      min_available = 2

  FUNCTION ingress_controller (NGINX Ingress):
    annotations:
      cert-manager.io/cluster-issuer: letsencrypt
      nginx.ingress.kubernetes.io/ssl-redirect: "true"
    rules:
      - host: api.erp.company.com → api-gateway-service:443
      - host: app.erp.company.com → frontend-service:3000

  FUNCTION network_policy():
    // Zero-trust: deny all by default
    DENY all ingress to namespace erp-services
    ALLOW ingress FROM api-gateway TO microservices on port 8080
    ALLOW egress FROM microservices TO data_subnet (Kafka, Redis, DB)
    ALLOW egress FROM microservices TO monitoring_namespace

  FUNCTION service_mesh (Istio):
    ENABLE mutual_tls between all services
    DEFINE traffic_policy:
      retries: max=3, perTryTimeout=2s
      circuit_breaker:
        consecutive_errors = 5
        interval           = 30s
        base_ejection_time = 30s
    DEFINE virtual_service:
      canary_routing: 90% stable, 10% canary
```

---

## 6. MICROSERVICES — SPRING BOOT

```
// ─────────────────────────────────────────────
// SHARED PATTERNS (applied to ALL services)
// ─────────────────────────────────────────────

PATTERN base_microservice:

  BOOTSTRAP application:
    LOAD config FROM OCI Vault via Spring Cloud Vault
    LOAD config FROM OCI Config Service
    CONNECT datasource (connection pool: HikariCP, max=20)
    CONNECT redis_cache
    CONNECT kafka_producer
    REGISTER service → service_registry (Eureka / Consul)
    EXPOSE actuator endpoints:
      /actuator/health, /actuator/metrics, /actuator/info, /actuator/prometheus

  INTERCEPTORS:
    MDCLoggingInterceptor:
      FOR every request:
        SET MDC[correlationId] = header["X-Request-ID"]
        SET MDC[userId]        = header["X-User-ID"]
        SET MDC[tenantId]      = header["X-Tenant-ID"]

    AuthorizationInterceptor:
      FOR every request:
        EXTRACT JWT from Authorization header
        VALIDATE with OAuth server (or local key cache)
        INJECT SecurityContext

  EXCEPTION_HANDLER:
    ON ValidationException     → 400 + error_details
    ON AuthorizationException  → 403 + message
    ON ResourceNotFoundException → 404 + resource_id
    ON ConflictException       → 409 + conflict_detail
    ON ANY unhandled exception → 500 + correlation_id (hide stack trace)
    LOG all exceptions with correlation_id → structured JSON log


// ─────────────────────────────────────────────
// FINANCE SERVICE
// ─────────────────────────────────────────────

SERVICE finance_service (port 8080):

  LAYERS:
    Controller → Service → Repository → Database

  FUNCTION createGeneralLedgerEntry(request):
    VALIDATE request (amount > 0, valid account codes)
    BEGIN transaction

      entry = GLEntry {
        id              = uuid()
        debit_account   = request.debit_account
        credit_account  = request.credit_account
        amount          = request.amount
        currency        = request.currency
        posting_date    = request.posting_date
        created_by      = current_user()
        status          = PENDING
      }

      SAVE entry → gl_entries table
      CALL oci_erp_fusion_api.post_journal(entry)   // OCI ERP Fusion API call
      UPDATE entry.status = POSTED
      PUBLISH kafka_event("finance.gl.entry.created", entry)
      INVALIDATE cache key("gl_summary:" + entry.period)

    COMMIT transaction
    RETURN entry

  FUNCTION getTrialBalance(period, tenant_id):
    cache_key = "trial_balance:" + tenant_id + ":" + period
    result = redis.get(cache_key)
    IF result EXISTS:
      RETURN result
    result = repository.fetchTrialBalance(period, tenant_id)
    redis.set(cache_key, result, ttl=300s)
    RETURN result


// ─────────────────────────────────────────────
// PROCUREMENT SERVICE
// ─────────────────────────────────────────────

SERVICE procurement_service (port 8081):

  FUNCTION createPurchaseOrder(request):
    VALIDATE supplier exists in vendor_master
    VALIDATE budget availability via finance_service.checkBudget(dept, amount)

    po = PurchaseOrder {
      po_number    = generate_po_number()
      supplier_id  = request.supplier_id
      line_items   = request.line_items
      total_amount = sum(line_items.amount)
      status       = DRAFT
      approver     = resolve_approver(request.dept, total_amount)
    }

    SAVE po → purchase_orders table
    CALL oci_erp_fusion_api.createPO(po)
    PUBLISH kafka_event("procurement.po.created", po)

    IF total_amount > approval_threshold:
      SEND approval_notification → notification_service
    RETURN po

  FUNCTION approvePurchaseOrder(po_id, approver_id):
    po = repository.findById(po_id)
    VERIFY approver_id == po.approver
    po.status = APPROVED
    SAVE po
    PUBLISH kafka_event("procurement.po.approved", po)
    SYNC document → sharepoint_proxy_service (attach PO PDF)
    RETURN po


// ─────────────────────────────────────────────
// HR SERVICE
// ─────────────────────────────────────────────

SERVICE hr_service (port 8082):

  FUNCTION onboardEmployee(request):
    VALIDATE no duplicate employee_number
    employee = Employee {
      id             = uuid()
      name           = request.name
      department     = request.department
      position       = request.position
      start_date     = request.start_date
      salary         = request.salary
      status         = ACTIVE
    }
    SAVE employee → employees table
    CALL oci_erp_fusion_api.createWorker(employee)
    PUBLISH kafka_event("hr.employee.onboarded", employee)
    TRIGGER provisioning → IT systems (via notification_service)
    CREATE sharepoint_folder for employee documents
    RETURN employee

  FUNCTION processPayroll(period):
    employees = repository.findActive()
    FOR each employee:
      pay_slip = calculatePaySlip(employee, period):
        gross  = employee.salary / 12
        tax    = computeTax(gross, employee.tax_code)
        net    = gross - tax - deductions
      SAVE pay_slip → payroll table
      CALL oci_erp_fusion_api.submitPayroll(pay_slip)
      PUBLISH kafka_event("hr.payroll.processed", pay_slip)
    RETURN payroll_summary


// ─────────────────────────────────────────────
// INVENTORY SERVICE
// ─────────────────────────────────────────────

SERVICE inventory_service (port 8083):

  FUNCTION adjustStock(sku, quantity, type):  // type = IN | OUT | ADJUST
    item = repository.findBySku(sku)
    IF type == OUT AND item.quantity < quantity:
      THROW InsufficientStockException

    item.quantity += (type == IN ? quantity : -quantity)
    item.last_updated = now()
    SAVE item → inventory table
    CALL oci_erp_fusion_api.updateInventory(item)
    PUBLISH kafka_event("inventory.stock.adjusted", item)

    IF item.quantity < item.reorder_point:
      PUBLISH kafka_event("inventory.reorder.triggered", item)
    INVALIDATE cache("inventory:" + sku)
    RETURN item
```

---

## 7. FRONTEND — REACT

```
COMPONENT react_frontend:

  ARCHITECTURE:
    - React 18 + TypeScript
    - Redux Toolkit (global state)
    - React Query (server state / caching)
    - React Router v6 (routing)
    - Axios (HTTP client with interceptors)
    - Material UI / Ant Design (component library)

  BOOTSTRAP app:
    LOAD environment config (API_BASE_URL, OAUTH_URL, CLIENT_ID)
    INITIALIZE OAuth2 PKCE flow (auth-code with code_verifier)
    SETUP Axios interceptor:
      ON request: attach Bearer token from token store
      ON 401 response: call refresh_token() then retry
      ON 403 response: redirect to unauthorized page
    SETUP React Query client:
      staleTime     = 30s
      cacheTime     = 5min
      retry         = 2
      errorBoundary = GlobalErrorBoundary
    RENDER <App> inside <AuthProvider> <QueryClientProvider> <ReduxProvider>

  FUNCTION login_flow():
    generate code_verifier = random_bytes(64)
    code_challenge = base64url(sha256(code_verifier))
    REDIRECT → OAuth /authorize?
      client_id, redirect_uri, response_type=code,
      scope, state=nonce, code_challenge, code_challenge_method=S256
    ON callback:
      VERIFY state == nonce
      EXCHANGE code + code_verifier → tokens via /token endpoint
      STORE access_token in memory (NOT localStorage)
      STORE refresh_token in httpOnly cookie
      REDIRECT → /dashboard

  FUNCTION route_guard(route):
    IF NOT authenticated:
      REDIRECT → /login
    IF NOT has_role(required_role):
      RENDER <UnauthorizedPage>
    ELSE:
      RENDER route.component

  COMPONENT Dashboard:
    ON mount:
      FETCH financial_summary    via useQuery("finance-summary")
      FETCH pending_approvals    via useQuery("pending-approvals")
      FETCH inventory_alerts     via useQuery("inventory-alerts")
      FETCH recent_activities    via useQuery("recent-activities")
    RENDER:
      <FinancialSummaryCard   data=financial_summary />
      <PendingApprovalsList   data=pending_approvals onApprove=handleApprove />
      <InventoryAlertWidget   data=inventory_alerts />
      <ActivityFeed           data=recent_activities />
      <RealTimeNotifications  socket=WebSocket("/ws/notifications") />

  COMPONENT CreatePurchaseOrder:
    formState = useForm(PO_VALIDATION_SCHEMA)
    ON submit:
      VALIDATE form
      CALL api.post("/api/v1/procurement/purchase-orders", formState)
      ON success:
        SHOW success_toast
        INVALIDATE query("purchase-orders")
        NAVIGATE → /procurement/orders/{new_po_id}
      ON error:
        DISPLAY field-level errors from API response
```

---

## 8. REST API CONTRACTS

```
REST_API_CONTRACTS:

  // Standard response envelope
  RESPONSE_ENVELOPE:
    {
      success:       boolean
      data:          object | array
      error:         { code, message, details[] }
      meta:          { page, size, total, correlationId }
      timestamp:     ISO8601
    }

  // Finance API
  POST   /api/v1/finance/gl-entries          → createGLEntry
  GET    /api/v1/finance/gl-entries          → listGLEntries     (paginated)
  GET    /api/v1/finance/trial-balance       → getTrialBalance   ?period=2024-Q1
  GET    /api/v1/finance/budget/{dept_id}    → getBudget
  POST   /api/v1/finance/budget/check        → checkBudgetAvailability

  // Procurement API
  POST   /api/v1/procurement/purchase-orders          → createPO
  GET    /api/v1/procurement/purchase-orders          → listPOs   (paginated+filtered)
  GET    /api/v1/procurement/purchase-orders/{id}     → getPO
  PATCH  /api/v1/procurement/purchase-orders/{id}/approve → approvePO
  PATCH  /api/v1/procurement/purchase-orders/{id}/reject  → rejectPO

  // HR API
  POST  /api/v1/hr/employees               → onboardEmployee
  GET   /api/v1/hr/employees               → listEmployees
  GET   /api/v1/hr/employees/{id}          → getEmployee
  PUT   /api/v1/hr/employees/{id}          → updateEmployee
  POST  /api/v1/hr/payroll/process         → processPayroll    ?period=2024-06

  // Inventory API
  GET   /api/v1/inventory/items            → listInventory
  POST  /api/v1/inventory/items/{sku}/adjust → adjustStock
  GET   /api/v1/inventory/items/{sku}      → getStockLevel

  // SharePoint API (proxy)
  POST  /api/v1/sharepoint/documents/upload  → uploadDocument
  GET   /api/v1/sharepoint/documents         → listDocuments    ?site=erp
  GET   /api/v1/sharepoint/documents/{id}    → getDocument

  VERSIONING_STRATEGY:
    current  = v1
    sunset   = v0 (deprecated, still supported 6 months)
    header   = "Deprecation: true" on v0 responses

  PAGINATION:
    query_params: page=0, size=20, sort=createdAt,desc
    response_meta: { page, size, total, totalPages }
```

---

## 9. KAFKA (EVENT STREAMING)

```
COMPONENT kafka_cluster (Confluent / OCI Streaming):

  DEFINE topics:
    finance.gl.entry.created        partitions=6,  replication=3
    finance.budget.updated          partitions=3,  replication=3
    procurement.po.created          partitions=6,  replication=3
    procurement.po.approved         partitions=3,  replication=3
    hr.employee.onboarded           partitions=3,  replication=3
    hr.payroll.processed            partitions=3,  replication=3
    inventory.stock.adjusted        partitions=6,  replication=3
    inventory.reorder.triggered     partitions=3,  replication=3
    notifications.outbound          partitions=6,  replication=3
    audit.events                    partitions=12, replication=3
    api-gateway-logs                partitions=6,  replication=3

  PRODUCER config:
    acks         = all
    retries      = 3
    compression  = snappy
    idempotence  = true

  CONSUMER_GROUPS:

    reporting-consumer-group:
      SUBSCRIBE TO: finance.*, procurement.*, hr.*, inventory.*
      FUNCTION process(event):
        UPSERT event_data → reporting_warehouse (Oracle ADW)
        UPDATE materialized_views

    notification-consumer-group:
      SUBSCRIBE TO: procurement.po.created, hr.employee.onboarded,
                    inventory.reorder.triggered
      FUNCTION process(event):
        RESOLVE recipients from event.payload
        ROUTE → email | SMS | in-app based on user preferences
        CALL notification_service.send(notification)

    audit-consumer-group:
      SUBSCRIBE TO: audit.events
      FUNCTION process(event):
        PERSIST → audit_log table (immutable, append-only)
        FORWARD → SIEM (Splunk)

    sharepoint-sync-consumer-group:
      SUBSCRIBE TO: procurement.po.approved, hr.employee.onboarded
      FUNCTION process(event):
        GENERATE PDF document from template + event.payload
        UPLOAD document → SharePoint via sharepoint_proxy_service

  SCHEMA_REGISTRY:
    USE Confluent Schema Registry (Avro / Protobuf)
    ENFORCE schema compatibility = BACKWARD
    VERSION schemas per topic
```

---

## 10. REDIS (CACHING)

```
COMPONENT redis_cluster (OCI Cache / Redis Enterprise):

  TOPOLOGY: Redis Cluster (3 masters, 3 replicas)
  SECURITY: TLS + AUTH token from OCI Vault

  CACHE_NAMESPACES:
    "session:{user_id}"          → user session data       TTL=8h
    "token:revoked:{jti}"        → revoked JWT tokens      TTL=15min
    "token:refresh:{user_id}"    → refresh token store     TTL=8h
    "gl_summary:{tenant}:{period}"  → GL summary cache     TTL=5min
    "trial_balance:{t}:{period}" → trial balance cache     TTL=5min
    "budget:{dept_id}"           → budget data             TTL=60s
    "inventory:{sku}"            → stock level cache       TTL=30s
    "rate_limit:{client_id}"     → rate limit counters     TTL=60s
    "lock:{resource_id}"         → distributed locks       TTL=30s

  FUNCTION cache_get(key):
    value = redis.get(key)
    IF value == nil:
      RETURN CACHE_MISS
    RETURN deserialize(value)

  FUNCTION cache_set(key, value, ttl):
    serialized = serialize(value)
    redis.setex(key, ttl, serialized)

  FUNCTION distributed_lock(resource_id, ttl=30s):
    lock_key = "lock:" + resource_id
    acquired = redis.set(lock_key, instance_id, NX, EX=ttl)
    IF NOT acquired:
      THROW ResourceLockedException
    TRY
      EXECUTE critical_section()
    FINALLY
      IF redis.get(lock_key) == instance_id:
        redis.del(lock_key)   // only release own lock

  FUNCTION rate_limit_check(client_id, limit=1000, window=60s):
    key   = "rate_limit:" + client_id
    count = redis.incr(key)
    IF count == 1:
      redis.expire(key, window)
    IF count > limit:
      THROW RateLimitExceededException
```

---

## 11. DATABASE LAYER

```
COMPONENT database_layer:

  PRIMARY_DB: Oracle Autonomous Transaction Processing (ATP)
    - Multi-AZ: PRIMARY in region-1, STANDBY in region-2
    - Data Guard: automatic failover < 30s
    - Encryption: TDE (Transparent Data Encryption) enabled
    - Connection pool: HikariCP (max=20 per service)

  ANALYTICS_DB: Oracle Autonomous Data Warehouse (ADW)
    - Read replica pattern (Kafka feeds ADW for reporting)
    - Used by: reporting_service, dashboards

  SCHEMA_DESIGN:

    TABLE gl_entries:
      id UUID PK, debit_account, credit_account, amount DECIMAL(18,2),
      currency CHAR(3), posting_date DATE, status ENUM(PENDING,POSTED,VOIDED),
      tenant_id UUID FK, created_by UUID, created_at TIMESTAMP,
      updated_at TIMESTAMP
      INDEX: (tenant_id, posting_date), (status), (created_by)

    TABLE purchase_orders:
      po_number VARCHAR PK, supplier_id UUID FK, total_amount DECIMAL(18,2),
      status ENUM(DRAFT,PENDING_APPROVAL,APPROVED,REJECTED,RECEIVED),
      approver_id UUID FK, department_id UUID FK,
      tenant_id UUID FK, created_at TIMESTAMP
      INDEX: (tenant_id, status), (approver_id)

    TABLE employees:
      id UUID PK, employee_number VARCHAR UNIQUE, name VARCHAR,
      department_id UUID FK, position VARCHAR, salary DECIMAL(15,2),
      status ENUM(ACTIVE,INACTIVE,TERMINATED), start_date DATE,
      tenant_id UUID FK, created_at TIMESTAMP
      INDEX: (tenant_id), (department_id), (employee_number)

    TABLE inventory_items:
      sku VARCHAR PK, name VARCHAR, quantity INT,
      unit_of_measure VARCHAR, reorder_point INT, unit_cost DECIMAL(12,4),
      warehouse_id UUID FK, last_updated TIMESTAMP
      INDEX: (warehouse_id), (quantity < reorder_point) -- partial index

    TABLE audit_log:
      id UUID PK, entity_type VARCHAR, entity_id UUID,
      action ENUM(CREATE,UPDATE,DELETE,APPROVE,REJECT),
      before_state JSONB, after_state JSONB,
      performed_by UUID, tenant_id UUID, timestamp TIMESTAMP
      PARTITION BY: timestamp (monthly)  -- for performance
      // append-only, no UPDATEs, no DELETEs

  MIGRATION_STRATEGY:
    TOOL: Flyway
    NAMING: V{version}__{description}.sql
    ON startup: auto-apply pending migrations
    ROLLBACK: manual (Flyway pro or custom down scripts)

  MULTI_TENANCY:
    STRATEGY: Row-level security (RLS) with tenant_id column
    ENFORCE: @TenantFilter Hibernate interceptor injects
             WHERE tenant_id = :currentTenantId on all queries
    ISOLATION: Each tenant's data is logically isolated
```

---

## 12. AZURE SHAREPOINT INTEGRATION

```
COMPONENT sharepoint_proxy_service (port 8085):

  AUTHENTICATION:
    USE OAuth 2.0 Client Credentials flow
    REGISTER app in Azure AD
    SCOPE: https://graph.microsoft.com/.default
    STORE client_secret → OCI Vault
    CACHE access_token in Redis (TTL = token.expires_in - 60s)

  FUNCTION upload_document(file, metadata):
    token = get_sharepoint_token()
    site_id = resolve_site(metadata.site_name)
    drive_id = resolve_drive(site_id, metadata.library)

    response = HTTP POST
      url = "https://graph.microsoft.com/v1.0/sites/{site_id}/drives/{drive_id}/items/{folder}:/{filename}:/content"
      headers: Authorization: Bearer {token}
      body: file_bytes

    IF response.status == 201:
      STORE document_metadata → local_db (erp_id ↔ sharepoint_item_id)
      PUBLISH kafka_event("sharepoint.document.uploaded", metadata)
      RETURN sharepoint_item_id
    ELSE:
      LOG error with correlation_id
      THROW SharePointUploadException

  FUNCTION list_documents(site, folder, filters):
    token = get_sharepoint_token()
    cache_key = "sp_docs:" + site + ":" + folder
    cached = redis.get(cache_key)
    IF cached: RETURN cached

    response = HTTP GET
      url = "https://graph.microsoft.com/v1.0/sites/{site}/drive/items/{folder_id}/children"
      headers: Authorization: Bearer {token}

    items = parse_graph_response(response)
    redis.set(cache_key, items, ttl=120s)
    RETURN items

  KAFKA_CONSUMER:
    SUBSCRIBE TO: procurement.po.approved
    ON event:
      pdf = generate_po_pdf(event.po_data)
      upload_document(pdf, {
        site: "erp-procurement",
        library: "Purchase Orders",
        folder: event.po_data.period,
        filename: "PO_" + event.po_data.po_number + ".pdf"
      })
```

---

## 13. DEVSECOPS / CI / CD PIPELINE

```
COMPONENT devsecops_pipeline:

  VCS: GitHub (feature branches → PR → main → release)
  CI:  GitHub Actions + Tekton Pipelines (on OKE)
  CD:  ArgoCD (GitOps) on OKE
  IaC: Terraform + OCI Resource Manager
  REGISTRY: OCI Container Registry (OCIR)

  BRANCHING_STRATEGY (GitFlow):
    main       → production
    release/*  → staging
    develop    → development
    feature/*  → PR targets develop
    hotfix/*   → PR targets main + develop

  CI_PIPELINE (triggered on PR / push):

    STAGE 1 — Code Quality:
      CHECKOUT source
      RUN mvn checkstyle:check (Java style)
      RUN eslint, prettier (React)
      RUN SonarQube analysis → enforce quality gate (coverage > 80%)
      ON fail: BLOCK merge

    STAGE 2 — Security Scanning (SAST):
      RUN OWASP Dependency Check (CVE scan on dependencies)
      RUN Semgrep (static analysis for security patterns)
      RUN Snyk (vulnerability scanning)
      RUN Trivy (container image scan for CVEs)
      IF CRITICAL CVE found: BLOCK pipeline, ALERT security_team
      PUBLISH scan_report → OCI Object Storage

    STAGE 3 — Build:
      BUILD: mvn clean package -DskipTests (Spring Boot JAR)
      BUILD: npm run build (React production bundle)
      BUILD Docker image:
        FROM eclipse-temurin:21-jre-alpine  // minimal base image
        COPY app.jar /app.jar
        RUN adduser --disabled-password appuser && chown appuser /app.jar
        USER appuser  // non-root
        EXPOSE 8080
        ENTRYPOINT ["java", "-jar", "/app.jar"]
      SCAN built image with Trivy again
      PUSH image → OCIR (tag: git_sha + semver)

    STAGE 4 — Tests:
      RUN unit_tests (JUnit 5, Jest)
      RUN integration_tests (Testcontainers: real DB + Kafka + Redis)
      RUN contract_tests (Spring Cloud Contract / Pact)
      RUN DAST: OWASP ZAP against staging environment
      PUBLISH test_reports + coverage → SonarQube

    STAGE 5 — Artifact Promotion:
      IF all stages pass AND PR approved:
        TAG image as release candidate
        UPLOAD helm_chart → OCI Helm Registry
        CREATE GitHub Release with changelog
        UPDATE ArgoCD app manifest (GitOps repo)

  CD_PIPELINE (ArgoCD GitOps):

    WATCH GitOps_repo for manifest changes

    DEPLOY to DEVELOPMENT:
      ON: push to develop branch
      SYNC ArgoCD app: erp-dev
      VERIFY health checks pass
      RUN smoke tests

    DEPLOY to STAGING:
      ON: push to release/* branch
      SYNC ArgoCD app: erp-staging
      DEPLOY as canary: 10% traffic
      MONITOR error_rate for 10 minutes
      IF error_rate > 1%: AUTO ROLLBACK
      ELSE: promote to 100%
      RUN integration test suite
      AWAIT manual approval gate

    DEPLOY to PRODUCTION:
      ON: approved release
      STRATEGY: Blue/Green deployment
        DEPLOY green_env (new version)
        HEALTH CHECK green_env
        SWITCH LBaaS → green_env (instant cutover)
        MONITOR 15 minutes
        IF issues: switch back to blue_env (< 30s rollback)
        AFTER stable: decommission blue_env
      POST_DEPLOY:
        RUN smoke tests on production
        SEND deployment_notification → Slack #deployments
        UPDATE JIRA tickets as DEPLOYED
        CREATE Confluence release notes entry

  INFRASTRUCTURE_AS_CODE (Terraform):

    STRUCTURE:
      /terraform
        /modules
          /oci-vcn, /oci-oke, /oci-atp, /oci-lbaas
          /oci-api-gateway, /oci-kafka, /oci-redis
        /environments
          /dev, /staging, /production

    WORKFLOW:
      PR opened → terraform plan (show diff)
      PR approved → terraform apply (auto in dev, manual in prod)
      STATE stored in OCI Object Storage (remote backend)
      DRIFT detection: run plan daily, alert on unexpected diffs

  SECRET_MANAGEMENT (OCI Vault + Vault Agent):
    NEVER store secrets in code or config files
    ALL secrets in OCI Vault
    Kubernetes pods use Vault Agent sidecar to inject secrets as env vars
    Secrets auto-rotate:
      DB passwords  → every 90 days
      API keys      → every 30 days
      TLS certs     → every 90 days (auto-renewed via cert-manager)
```

---

## 14. MONITORING & OBSERVABILITY

```
COMPONENT observability_stack:

  PILLARS: Metrics, Logs, Traces (The Three Pillars of Observability)

  // ─── METRICS ────────────────────────────────

  COMPONENT prometheus:
    SCRAPE every 15s:
      - Spring Boot Actuator /actuator/prometheus (JVM, HTTP, DB pool, Kafka)
      - Node Exporter (host CPU, memory, disk)
      - Kafka Exporter (consumer lag, throughput)
      - Redis Exporter (hit rate, memory, latency)
      - Kubernetes metrics-server (pod CPU/memory)

  COMPONENT grafana:
    DASHBOARDS:
      - Service Health Overview (error rates, latency p50/p95/p99, RPS)
      - JVM Metrics (heap, GC, threads)
      - Kafka Lag Dashboard (consumer group lag per topic/partition)
      - Redis Performance (hit rate, evictions, memory)
      - Infrastructure Overview (OKE node health, CPU, memory)
      - Business KPIs (POs created/day, payroll processed, GL entries)

    ALERTING RULES:
      IF http_error_rate > 5% for 2min:
        PAGE on-call via PagerDuty (P1)
      IF p99_latency > 2000ms for 5min:
        ALERT Slack #erp-alerts (P2)
      IF kafka_consumer_lag > 10000:
        ALERT Slack #erp-alerts (P2)
      IF pod_restart_count > 3 in 5min:
        ALERT + auto_investigate
      IF db_connection_pool_usage > 90%:
        PAGE on-call (P1)

  // ─── LOGS ───────────────────────────────────

  COMPONENT logging_stack (Loki + Grafana / OCI Logging):

    ALL services log in structured JSON:
      {
        timestamp:     ISO8601,
        level:         INFO|WARN|ERROR,
        service:       "finance-service",
        correlationId: "uuid",
        userId:        "uuid",
        tenantId:      "uuid",
        message:       "...",
        duration_ms:   123,
        http_status:   200,
        exception:     null | stack_trace
      }

    LOG LEVELS:
      DEBUG: local dev only
      INFO:  normal operations (request in/out, business events)
      WARN:  recoverable issues (cache miss, retry)
      ERROR: failures, exceptions (always with correlationId)

    PIPELINE:
      Fluent Bit (DaemonSet on OKE) → collect all pod logs
      → OCI Logging Analytics (long-term storage, 90 days)
      → Loki (recent logs, 7 days, for Grafana queries)
      → SIEM / Splunk (security events, audit logs, forever)

    LOG_SEARCH:
      Query by correlationId to trace full request path
        across multiple services

  // ─── TRACES ─────────────────────────────────

  COMPONENT distributed_tracing (Jaeger + OpenTelemetry):

    ALL services auto-instrument with OpenTelemetry Java Agent
    PROPAGATE trace context via W3C Trace Context headers
      (traceparent, tracestate)

    TRACE includes spans for:
      - Inbound HTTP request (LBaaS → API Gateway → Service)
      - Database queries (SQL text + duration)
      - Redis operations
      - Kafka produce/consume
      - External API calls (OCI ERP Fusion, SharePoint Graph API)
      - Inter-service HTTP calls

    SAMPLING:
      head_based_sampling = 10% (normal traffic)
      tail_based_sampling = 100% (all errors are captured)

    JAEGER UI:
      Search traces by: traceId, service, operation, tags
      Visualize: service dependency graph, latency histograms
      ALERT on trace errors → Grafana

  // ─── SYNTHETIC MONITORING ───────────────────

  COMPONENT synthetic_monitoring (OCI Synthetics):
    EVERY 1 minute from multiple regions:
      GET  https://app.erp.company.com/health
      POST https://api.erp.company.com/api/v1/finance/gl-entries (canary entry)
    IF response_time > 3s OR status != 200:
      ALERT on-call immediately

  // ─── OCI ERP FUSION MONITORING ──────────────

  COMPONENT erp_fusion_monitor:
    POLL OCI ERP Fusion API health every 5 min
    MONITOR ERP Fusion scheduled processes (payroll, GL posting)
    IF ERP Fusion API latency > 10s:
      ENABLE circuit_breaker in integration layer
      QUEUE requests in Kafka for retry
    TRACK ERP API quota consumption
      ALERT at 80% of daily quota
```

---

## 15. END-TO-END REQUEST FLOW

```
SCENARIO: Employee submits a Purchase Order via React app

STEP 1  — Browser → DNS
  User navigates to https://app.erp.company.com
  DNS resolves → LBaaS public IP

STEP 2  — LBaaS
  TLS terminated, HTTPS enforced
  X-Request-ID header injected
  Routed to API Gateway

STEP 3  — WAF inspection
  Request scanned for SQL injection, XSS
  Rate limit checked (Redis counter)
  PASS → API Gateway

STEP 4  — API Gateway
  JWT extracted and validated (signature, expiry, revocation in Redis)
  RBAC checked: user has PROCUREMENT_WRITE role
  Route matched: POST /api/v1/procurement/purchase-orders
  Headers injected: X-User-ID, X-Tenant-ID, X-Roles
  Forwarded → procurement-service (ClusterIP in OKE)

STEP 5  — Procurement Service (Spring Boot)
  MDC populated with correlationId, userId, tenantId
  Request validated (supplier exists, budget check → finance-service)
  BEGIN DB transaction
  PO saved → Oracle ATP
  OCI ERP Fusion API called (createPO)
  Kafka event published: procurement.po.created
  Transaction committed
  OpenTelemetry span closed
  Response returned: 201 Created { po_number, status, ... }

STEP 6  — Kafka consumers process event async
  reporting-consumer: UPDATE ADW warehouse
  notification-consumer: SEND email to procurement manager
  audit-consumer: PERSIST to audit_log

STEP 7  — Response path back
  procurement-service → API Gateway → LBaaS → Browser
  Total latency target: p99 < 500ms (synchronous path)

STEP 8  — Observability
  Structured log written with correlationId
  Prometheus counter incremented: po_created_total
  OpenTelemetry trace submitted to Jaeger
  Grafana dashboard updated in real time

STEP 9  — Approval flow (async, user action)
  Approver receives email notification (from Kafka consumer)
  Approver logs in, sees PO in pending_approvals dashboard
  PATCH /api/v1/procurement/purchase-orders/{id}/approve
  SharePoint PDF document auto-created and uploaded
  procurement.po.approved Kafka event fires
```

---

## 16. COMPONENT SUMMARY MAP

```
Internet
  └── OCI DNS (erp.company.com)
        └── OCI WAF (OWASP rules, DDoS, rate limit)
              └── OCI LBaaS (TLS termination, round-robin)
                    ├── OCI API Gateway (routing, OAuth validation, CORS)
                    │     └── OKE (Kubernetes cluster)
                    │           ├── finance-service       (Spring Boot)
                    │           ├── procurement-service   (Spring Boot)
                    │           ├── hr-service            (Spring Boot)
                    │           ├── inventory-service     (Spring Boot)
                    │           ├── reporting-service     (Spring Boot)
                    │           ├── notification-service  (Spring Boot)
                    │           └── sharepoint-proxy      (Spring Boot)
                    │
                    └── React Frontend (CDN / OKE pod)
                          └── OAuth2 PKCE (OCI Identity / Keycloak)

Data Layer:
  ├── Oracle ATP (primary OLTP database, multi-AZ)
  ├── Oracle ADW (analytics / reporting)
  ├── Redis Cluster (sessions, cache, rate limiting, distributed locks)
  └── Kafka Cluster (event streaming, async decoupling)

External:
  ├── OCI ERP Fusion (core ERP APIs)
  └── Azure SharePoint (via Microsoft Graph API)

DevSecOps:
  ├── GitHub (VCS, Actions CI)
  ├── Tekton (CI pipelines on OKE)
  ├── ArgoCD (GitOps CD)
  ├── SonarQube + Snyk + Trivy (security scanning)
  ├── Terraform + OCI Resource Manager (IaC)
  └── OCI Vault (secrets management)

Observability:
  ├── Prometheus + Grafana (metrics + alerting)
  ├── Loki + Fluent Bit (log aggregation)
  ├── Jaeger + OpenTelemetry (distributed tracing)
  ├── OCI Logging Analytics (long-term log storage)
  ├── PagerDuty (on-call alerting)
  └── Splunk / SIEM (security events)
```

---

*END OF PSEUDOCODE — OCI ERP Fusion Microservices Architecture*
