# PaaS Microservices ↔ OCI ERP Fusion SaaS
# Complete Architecture Pseudocode
# GL · AP · AR · Tax · SharePoint · AI Agent Studio · WebLogic

═══════════════════════════════════════════════════════════════════════════════
TABLE OF CONTENTS
═══════════════════════════════════════════════════════════════════════════════
 01. Architecture Overview & Topology
 02. Cloud Infrastructure (OCI PaaS)
 03. DNS Resolution & Traffic Routing
 04. WAF — Web Application Firewall
 05. LBaaS — Load Balancer as a Service
 06. API Gateway (OCI + Kong)
 07. OAuth 2.0 / JWT — Identity & Token Management
 08. Kubernetes (OKE) — Container Orchestration
 09. WebLogic Server (OCI WLS) — Integration Runtime
 10. OCI ERP Fusion SaaS Integration Layer
     10a. General Ledger (GL)
     10b. Accounts Payable (AP)
     10c. Accounts Receivable (AR)
     10d. Tax
 11. Microservices — Spring Boot
 12. AI Agent Studio — Intelligent Automation
 13. React Frontend
 14. REST API Contracts
 15. Kafka — Event Streaming
 16. Redis — Caching & State
 17. Database Layer (PaaS)
 18. Azure SharePoint Integration
 19. DevSecOps / CI / CD Pipeline
 20. Monitoring & Observability
 21. Security & Secrets Management
 22. End-to-End Request Flow
 23. Component Map
═══════════════════════════════════════════════════════════════════════════════


────────────────────────────────────────────────────────────────────────────
01. ARCHITECTURE OVERVIEW & TOPOLOGY
────────────────────────────────────────────────────────────────────────────

TOPOLOGY paas_to_saas_architecture:

  ZONE internet:
    - end_users (browser, mobile)
    - partner_systems (B2B)

  ZONE oci_paas (PaaS runtime — customer controlled):
    - OCI DNS
    - OCI WAF
    - OCI LBaaS
    - OCI API Gateway / Kong Gateway
    - OCI Container Engine for Kubernetes (OKE)
    - OCI WebLogic Server (WLS on OCI)
    - OCI Streaming (Kafka-compatible)
    - OCI Cache (Redis-compatible)
    - OCI Autonomous Database (ATP + ADW)
    - OCI Vault
    - OCI AI Platform / AI Agent Studio
    - OCI Object Storage
    - OCI Logging Analytics

  ZONE oci_saas (SaaS — Oracle managed):
    - OCI ERP Cloud Fusion (GL, AP, AR, Tax modules)
    - OCI Identity Cloud Service (IDCS)
    - OCI ERP REST/SOAP APIs
    - OCI ERP BIP Reports (BI Publisher)
    - OCI ERP FBDI (File-Based Data Import)
    - OCI ERP HDL (HCM Data Loader, if HCM used)

  ZONE azure (external SaaS):
    - Azure Active Directory (AAD)
    - Microsoft SharePoint Online
    - Microsoft Graph API

  CONNECTIVITY paas ↔ saas:
    - OCI ERP Fusion REST APIs (HTTPS/TLS 1.3)
    - ERP Fusion SOAP Web Services (legacy modules)
    - ERP Fusion BIP Report REST API (scheduled extracts)
    - ERP Fusion Business Events (UCM / Oracle Integration Cloud)
    - OAuth 2.0 Client Credentials (ERP Fusion → IDCS)

  KEY PRINCIPLE:
    PaaS layer NEVER stores ERP source-of-truth data permanently.
    PaaS layer CACHES ERP data in Redis (short TTL) and
    replicates events via Kafka to ADW for analytics.
    All write-back to ERP goes through ERP Integration Service.


────────────────────────────────────────────────────────────────────────────
02. CLOUD INFRASTRUCTURE (OCI PaaS)
────────────────────────────────────────────────────────────────────────────

INFRASTRUCTURE oci_paas_foundation:

  TENANCY:
    region_primary   = ap-mumbai-1       // or us-phoenix-1
    region_dr        = ap-hyderabad-1
    tenancy_id       = <oci_tenancy_ocid>

  COMPARTMENTS:
    /erp-paas-prod
    /erp-paas-staging
    /erp-paas-dev
    /erp-paas-shared-services
    /erp-paas-security

  VCN: erp-paas-vcn (10.0.0.0/16)

    SUBNETS:
      dmz_subnet          10.0.1.0/24   PUBLIC    (WAF, LBaaS endpoints)
      gateway_subnet      10.0.2.0/24   PRIVATE   (API Gateway, Kong)
      app_subnet          10.0.3.0/24   PRIVATE   (OKE pods, WebLogic)
      data_subnet         10.0.4.0/24   PRIVATE   (DB, Redis, Kafka)
      integration_subnet  10.0.5.0/24   PRIVATE   (ERP connectors, outbound)
      monitoring_subnet   10.0.6.0/24   PRIVATE   (Prometheus, Grafana, Jaeger)

    INTERNET_GATEWAY:    attached to dmz_subnet
    NAT_GATEWAY:         for private subnets (outbound only → ERP Fusion SaaS)
    SERVICE_GATEWAY:     OCI services (Object Storage, Vault, ADW) without NAT
    DYNAMIC_ROUTING_GATEWAY (DRG):
      FastConnect / VPN to on-premise if hybrid needed

    SECURITY_LISTS:
      dmz_subnet:
        INGRESS: 0.0.0.0/0  port=443
        EGRESS:  gateway_subnet port=443,8080
      gateway_subnet:
        INGRESS: dmz_subnet  port=443,8080
        EGRESS:  app_subnet  port=8080,8443
      app_subnet:
        INGRESS: gateway_subnet port=8080,8443
        EGRESS:  data_subnet   port=5432,6379,9092
        EGRESS:  0.0.0.0/0    port=443   (ERP Fusion HTTPS outbound)
      data_subnet:
        INGRESS: app_subnet  port=5432,6379,9092
        DENY all else

  OCI_SERVICES:
    object_storage:
      - erp-paas-artifacts       (CI/CD build artifacts)
      - erp-paas-erp-extracts    (BIP report downloads from ERP Fusion)
      - erp-paas-sharepoint-sync (SharePoint document staging)
      - erp-paas-ai-models       (AI Agent model artifacts)
      - erp-paas-backups         (DB + Kafka snapshots)

    vault: erp-paas-vault
      secrets:
        ERP_FUSION_CLIENT_ID
        ERP_FUSION_CLIENT_SECRET
        ERP_FUSION_BASE_URL
        DB_PASSWORD_PROD
        REDIS_AUTH_TOKEN
        KAFKA_SASL_PASSWORD
        JWT_PRIVATE_KEY_PEM
        JWT_PUBLIC_KEY_PEM
        SHAREPOINT_TENANT_ID
        SHAREPOINT_CLIENT_ID
        SHAREPOINT_CLIENT_SECRET
        AI_AGENT_STUDIO_API_KEY
        WEBLOGIC_ADMIN_PASSWORD
        SONARQUBE_TOKEN
        SLACK_WEBHOOK_URL

    certificates_service:
      - erp.company.com      (wildcard TLS cert, auto-renewed)
      - api.erp.company.com
      - sharepoint.erp.company.com


────────────────────────────────────────────────────────────────────────────
03. DNS RESOLUTION & TRAFFIC ROUTING
────────────────────────────────────────────────────────────────────────────

COMPONENT dns (OCI DNS + Traffic Management):

  ZONES:
    public_zone:  erp.company.com
    private_zone: erp.internal  (for pod-to-pod, VCN-private)

  PUBLIC DNS RECORDS:
    A     erp.company.com                → LBaaS_public_IP
    CNAME api.erp.company.com            → lbaas.erp.company.com
    CNAME app.erp.company.com            → lbaas.erp.company.com
    CNAME sharepoint.erp.company.com     → lbaas.erp.company.com
    CNAME ai.erp.company.com             → lbaas.erp.company.com
    CNAME admin.erp.company.com          → weblogic-admin-lb.internal
    TTL   = 300

  PRIVATE DNS RECORDS (VCN-internal):
    A  api-gateway.erp.internal          → API_gateway_cluster_ip
    A  finance-svc.erp.internal          → finance-service ClusterIP
    A  erp-connector.erp.internal        → erp-integration-service ClusterIP
    A  redis.erp.internal                → Redis cluster endpoint
    A  kafka.erp.internal                → Kafka bootstrap endpoint
    A  atp.erp.internal                  → ATP DB endpoint (private)

  TRAFFIC_MANAGEMENT_POLICY:
    strategy  = GEOLOCATION + FAILOVER
    primary   = ap-mumbai-1    (LBaaS_IP_primary)
    secondary = ap-hyderabad-1 (LBaaS_IP_dr)

    HEALTH_CHECK:
      url      = "https://api.erp.company.com/health"
      interval = 30s
      timeout  = 10s
      threshold = 3 failures → failover

  FUNCTION dns_failover_trigger():
    IF health_check(primary) FAILS 3 consecutive times:
      UPDATE A record → LBaaS_IP_dr
      NOTIFY ops via PagerDuty + Slack
      LOG failover_event → OCI Logging
    IF primary RECOVERS:
      REVERT A record → LBaaS_IP_primary after 5 consecutive passes
      NOTIFY recovery


────────────────────────────────────────────────────────────────────────────
04. WAF — WEB APPLICATION FIREWALL
────────────────────────────────────────────────────────────────────────────

COMPONENT waf (OCI WAF):

  MODE: Detection + Prevention

  RULE_GROUPS:
    owasp_core_ruleset:
      ENABLE SQL_INJECTION_PROTECTION     level=HIGH
      ENABLE XSS_PROTECTION               level=HIGH
      ENABLE COMMAND_INJECTION_PROTECTION level=HIGH
      ENABLE PATH_TRAVERSAL_PROTECTION    level=HIGH
      ENABLE CSRF_PROTECTION              level=MEDIUM
      ENABLE XXE_PROTECTION               level=HIGH
      ENABLE SSRF_PROTECTION             level=HIGH  // critical for SaaS proxy pattern

    custom_rules:
      RULE block_erp_scraping:
        IF request.path MATCHES "/api/v1/erp/*"
        AND request.headers["X-API-Key"] IS MISSING:
          ACTION = BLOCK, RETURN 403

      RULE rate_limit_erp_endpoints:
        per_ip:     200  req/min  on /api/v1/erp/*   // ERP data is expensive
        per_token:  1000 req/min  on /api/v1/*
        per_global: 50000 req/min global ceiling
        ON breach:  RETURN 429 + Retry-After header

      RULE block_tor_and_vpn:
        IF client_ip IN threat_intelligence_feed:
          ACTION = BLOCK

      RULE allow_erp_fusion_callbacks:
        IF source_ip IN erp_fusion_known_ips[]  // ERP business event webhooks
          AND request.path == "/api/v1/erp/events/callback":
          ACTION = BYPASS_WAF_CHECKS
          FORWARD directly to API Gateway

    ddos_protection:
      threshold_rps      = 20000
      burst_threshold    = 50000
      mitigation         = scrubbing_center_activation
      alert_channel      = PagerDuty + Slack #security-alerts

  FUNCTION inspect_request(request):
    FOR each rule_group IN [owasp_core_ruleset, custom_rules]:
      FOR each rule IN rule_group:
        result = rule.evaluate(request)
        IF result.action == BLOCK:
          LOG waf_block_event(request, rule.id) → OCI Logging + Splunk
          RETURN http_response(403, { code: "WAF_BLOCKED", rule: rule.id })
        IF result.action == CHALLENGE:
          RETURN captcha_response()
    LOG waf_pass_event(request) → OCI Logging (sampled 10%)
    RETURN PASS → LBaaS


────────────────────────────────────────────────────────────────────────────
05. LBaaS — LOAD BALANCER AS A SERVICE
────────────────────────────────────────────────────────────────────────────

COMPONENT lbaas (OCI Load Balancer):

  TYPE: Public (flexible shape, 10 Mbps – 8 Gbps)

  LISTENERS:
    https_listener:
      port         = 443
      protocol     = HTTPS
      ssl_cert     = oci_certificates.erp.company.com
      ssl_policy   = TLS_1_2_and_1_3
      ciphers      = [TLS_AES_256_GCM_SHA384, TLS_CHACHA20_POLY1305_SHA256]
      default_backend_set = api_gateway_pool

    http_listener:
      port     = 80
      protocol = HTTP
      rule     = REDIRECT 301 → https://{host}{path}

  BACKEND_SETS:

    api_gateway_pool:
      algorithm          = ROUND_ROBIN
      session_persistence = NONE (stateless JWT)
      health_check:
        protocol         = HTTPS
        url_path         = "/health"
        interval_ms      = 10000
        timeout_ms       = 3000
        retries          = 3
        return_code      = 200
      backends:
        - kong-gateway-pod-1.app_subnet:8443  weight=1
        - kong-gateway-pod-2.app_subnet:8443  weight=1
        - kong-gateway-pod-3.app_subnet:8443  weight=1

    frontend_pool:
      algorithm           = IP_HASH   // consistent hashing for React SPA
      health_check:
        url_path          = "/"
        return_code       = 200
      backends:
        - react-frontend-pod-1:3000
        - react-frontend-pod-2:3000

    weblogic_console_pool:
      algorithm = LEAST_CONNECTIONS
      backends:
        - weblogic-admin-server:7002   // HTTPS admin port

  RULE_SETS:
    routing_rules:
      IF path STARTS_WITH "/api/"    → api_gateway_pool
      IF path STARTS_WITH "/console" → weblogic_console_pool
      ELSE                           → frontend_pool

    request_headers:
      ADD X-Request-ID    = {uuid()}  // unique per request
      ADD X-Forwarded-For = {client_ip}
      ADD X-Real-IP       = {client_ip}

    response_headers:
      ADD Strict-Transport-Security = max-age=31536000; includeSubDomains
      ADD X-Content-Type-Options    = nosniff
      ADD X-Frame-Options           = DENY
      ADD Content-Security-Policy   = default-src 'self'
      REMOVE Server
      REMOVE X-Powered-By


────────────────────────────────────────────────────────────────────────────
06. API GATEWAY (OCI API Gateway + Kong Gateway on OKE)
────────────────────────────────────────────────────────────────────────────

COMPONENT api_gateway:

  LAYER_1: OCI API Gateway (edge, public-facing)
    PURPOSE: TLS termination, initial auth, WAF bypass routing, DDoS guard

    ROUTES:
      /api/v1/erp/*          → Kong Gateway (ERP integration routes)
      /api/v1/finance/*      → Kong Gateway (internal finance service)
      /api/v1/procurement/*  → Kong Gateway (procurement service)
      /api/v1/sharepoint/*   → Kong Gateway (SharePoint proxy)
      /api/v1/ai/*           → Kong Gateway (AI Agent Studio proxy)
      /api/v1/reports/*      → Kong Gateway (reporting service)
      /health                → health-check-service (no auth)
      /api/v1/erp/events/callback → erp-event-listener (ERP webhook)

  LAYER_2: Kong Gateway (OKE-deployed, internal)
    PURPOSE: Fine-grained routing, plugin pipeline, service discovery

    PLUGINS_PIPELINE (ordered):
      1. jwt-keycloak          (validate JWT signature, expiry, claims)
      2. oci-vault-secrets     (inject ERP credentials from vault)
      3. rate-limiting-advanced(Redis-backed sliding window)
      4. request-id            (propagate X-Request-ID)
      5. correlation-id        (add X-Correlation-ID if missing)
      6. request-transformer   (inject X-Tenant-ID, X-User-ID from JWT claims)
      7. response-transformer  (strip internal headers before client response)
      8. opentelemetry         (emit spans to Jaeger)
      9. prometheus            (metrics endpoint for Prometheus scrape)
      10. acl                  (role-based access: CONSUMER_GROUPS per route)
      11. http-log             (async log to Kafka topic: api-gateway-logs)

    SERVICES AND ROUTES:

      SERVICE erp_gl_service:
        url = http://erp-integration-svc.erp-services:8090
        ROUTES:
          GET  /api/v1/erp/gl/journal-entries        → getJournalEntries
          GET  /api/v1/erp/gl/trial-balance          → getTrialBalance
          GET  /api/v1/erp/gl/account-balances       → getAccountBalances
          POST /api/v1/erp/gl/journal-entries/import → importJournalEntries
          GET  /api/v1/erp/gl/periods                → getAccountingPeriods
        CONSUMER_GROUPS: [FINANCE_READ, FINANCE_WRITE, ADMIN]

      SERVICE erp_ap_service:
        url = http://erp-integration-svc.erp-services:8090
        ROUTES:
          GET  /api/v1/erp/ap/invoices               → getAPInvoices
          GET  /api/v1/erp/ap/invoices/{id}          → getAPInvoiceById
          POST /api/v1/erp/ap/invoices               → createAPInvoice
          GET  /api/v1/erp/ap/payments               → getAPPayments
          GET  /api/v1/erp/ap/suppliers              → getSuppliers
        CONSUMER_GROUPS: [AP_READ, AP_WRITE, FINANCE_READ]

      SERVICE erp_ar_service:
        url = http://erp-integration-svc.erp-services:8090
        ROUTES:
          GET  /api/v1/erp/ar/invoices               → getARInvoices
          POST /api/v1/erp/ar/invoices               → createARInvoice
          GET  /api/v1/erp/ar/receipts               → getARReceipts
          GET  /api/v1/erp/ar/customers              → getARCustomers
          GET  /api/v1/erp/ar/aging-report           → getAgingReport
        CONSUMER_GROUPS: [AR_READ, AR_WRITE, FINANCE_READ]

      SERVICE erp_tax_service:
        url = http://erp-integration-svc.erp-services:8090
        ROUTES:
          GET  /api/v1/erp/tax/rates                 → getTaxRates
          GET  /api/v1/erp/tax/configurations        → getTaxConfig
          POST /api/v1/erp/tax/calculate             → calculateTax
          GET  /api/v1/erp/tax/returns               → getTaxReturns
        CONSUMER_GROUPS: [TAX_READ, TAX_WRITE, FINANCE_READ]

      SERVICE ai_agent_service:
        url = http://ai-agent-svc.erp-services:8095
        ROUTES:
          POST /api/v1/ai/query                      → naturalLanguageQuery
          POST /api/v1/ai/reconcile                  → triggerReconciliation
          POST /api/v1/ai/anomaly-detect             → detectAnomalies
          GET  /api/v1/ai/suggestions/{context}      → getAISuggestions
        CONSUMER_GROUPS: [AI_USER, ADMIN]

  FUNCTION route_request(request):
    // Layer 1: OCI API Gateway
    strip_tls(request)
    validate_ssl_certificate()
    route_to_kong(request)

    // Layer 2: Kong plugin pipeline
    jwt_claims = jwt_plugin.validate(request.headers.Authorization)
    IF jwt_claims.invalid:
      RETURN 401 { error: "INVALID_TOKEN" }

    acl_plugin.check(jwt_claims.roles, request.route.consumer_groups)
    IF acl.denied:
      RETURN 403 { error: "INSUFFICIENT_PERMISSIONS" }

    rate_limiter.check(jwt_claims.client_id)
    IF rate_limited:
      RETURN 429 { error: "RATE_LIMIT_EXCEEDED", retry_after: N }

    request = request_transformer.enrich(request, jwt_claims)
    otel.start_span(request)

    FORWARD → upstream_service
    otel.end_span(response)
    response = response_transformer.clean(response)
    RETURN response


────────────────────────────────────────────────────────────────────────────
07. OAUTH 2.0 / JWT — IDENTITY & TOKEN MANAGEMENT
────────────────────────────────────────────────────────────────────────────

COMPONENT identity_platform (OCI IDCS / Keycloak on OKE):

  REALMS:
    erp_employees_realm:    (internal enterprise users)
    erp_partners_realm:     (external vendors, customers)
    erp_systems_realm:      (service-to-service M2M)
    erp_agents_realm:       (AI agents — scoped, minimal permissions)

  CLIENTS (OAuth 2.0 Client Registrations):

    react_spa:
      grant_type        = AUTHORIZATION_CODE + PKCE (S256)
      redirect_uris     = ["https://app.erp.company.com/callback"]
      scopes            = [openid, profile, erp:read, erp:write, ai:use]
      access_token_ttl  = 15 minutes
      refresh_token_ttl = 8 hours
      token_binding     = httpOnly cookie for refresh token

    spring_microservices:
      grant_type        = CLIENT_CREDENTIALS
      scopes            = [erp:read, erp:write, kafka:publish]
      access_token_ttl  = 10 minutes

    weblogic_integration:
      grant_type        = CLIENT_CREDENTIALS
      scopes            = [erp:fusion:read, erp:fusion:write]
      access_token_ttl  = 5 minutes  // short-lived for ERP calls

    ai_agent_client:
      grant_type        = CLIENT_CREDENTIALS
      scopes            = [erp:read, ai:query]  // read-only + AI
      access_token_ttl  = 5 minutes

    erp_fusion_callback:
      grant_type        = CLIENT_CREDENTIALS  // ERP calls back to PaaS
      scopes            = [events:write]
      ip_restriction    = erp_fusion_known_ips[]

  JWT_TOKEN_STRUCTURE:
    header:
      alg = RS256
      kid = key_id (for key rotation without downtime)
      typ = JWT

    payload:
      iss  = "https://idcs.erp.company.com"
      sub  = user_uuid
      aud  = ["api.erp.company.com"]
      exp  = now + 900 (15 min)
      iat  = now
      jti  = uuid()  // unique token ID (for revocation)
      claims:
        tenant_id    = tenant_uuid
        roles        = ["FINANCE_MANAGER", "AP_APPROVER"]
        permissions  = ["erp:read", "erp:write"]
        department   = "Finance"
        cost_center  = "CC-001"
        email        = user@company.com

    signature: RS256(base64url(header) + "." + base64url(payload), private_key)

  FUNCTION authorize_code_flow(request):
    validate(client_id, redirect_uri, code_challenge, state)
    IF NOT authenticated:
      REDIRECT → login_page (SAML SSO to corporate IdP if federated)
    ISSUE authorization_code (single-use, 5min TTL)
    REDIRECT → redirect_uri?code={auth_code}&state={state}

  FUNCTION token_exchange(auth_code, code_verifier):
    VERIFY code_challenge == base64url(sha256(code_verifier))  // PKCE
    VERIFY auth_code not expired and not already used
    MARK auth_code as USED in Redis
    GENERATE access_token (JWT, RS256, 15min)
    GENERATE refresh_token (opaque, 8h, stored in Redis)
    RETURN { access_token, refresh_token, token_type: Bearer, expires_in: 900 }

  FUNCTION validate_jwt(token):
    // Kong / API Gateway calls this
    header  = base64decode(token.header)
    payload = base64decode(token.payload)

    FETCH public_key from JWKS endpoint (cached in Redis, refreshed hourly)
      url = "https://idcs.erp.company.com/.well-known/jwks.json"

    VERIFY signature(token, public_key)
    VERIFY payload.exp > now()
    VERIFY payload.iss == expected_issuer
    VERIFY payload.aud CONTAINS "api.erp.company.com"

    revoked = redis.get("token:revoked:" + payload.jti)
    IF revoked:
      THROW TokenRevokedException

    RETURN payload.claims

  FUNCTION revoke_token(jti, exp):
    ttl = exp - now()
    redis.setex("token:revoked:" + jti, ttl, "1")

  FUNCTION refresh_access_token(refresh_token):
    stored = redis.get("token:refresh:" + refresh_token)
    IF stored == nil OR stored.expired:
      RETURN 401 { error: "REFRESH_TOKEN_EXPIRED" }
    user = stored.user_data
    GENERATE new_access_token
    ROTATE refresh_token (old → deleted, new → Redis)
    RETURN new_tokens

  ERP_FUSION_TOKEN_MANAGEMENT:
    // Separate OAuth flow to ERP Fusion SaaS
    FUNCTION get_erp_fusion_token():
      cached = redis.get("erp:fusion:token")
      IF cached AND valid:
        RETURN cached

      token = HTTP POST https://login.oracle.com/oam/server/obrareq.cgi
        body:
          grant_type    = client_credentials
          client_id     = ERP_FUSION_CLIENT_ID (from vault)
          client_secret = ERP_FUSION_CLIENT_SECRET (from vault)
          scope         = "https://erp.oracle.com/.default"

      redis.setex("erp:fusion:token", token.expires_in - 60, token.access_token)
      RETURN token.access_token


────────────────────────────────────────────────────────────────────────────
08. KUBERNETES (OKE) — CONTAINER ORCHESTRATION
────────────────────────────────────────────────────────────────────────────

COMPONENT kubernetes (OCI Container Engine for Kubernetes):

  VERSION: Kubernetes 1.29+

  NODE_POOLS:
    system_pool:
      nodes  = 3
      shape  = VM.Standard.E4.Flex (4 OCPU, 16GB)
      labels = { role: system }
      taints = [{ key: node-role, value: system, effect: NoSchedule }]
      purpose: Ingress controller, cert-manager, Vault agent, Istio control

    app_pool:
      nodes    = 6 (auto-scale 4–20)
      shape    = VM.Standard.E4.Flex (8 OCPU, 32GB)
      labels   = { role: app }
      purpose  = Spring Boot microservices, Kong Gateway, React

    data_pool:
      nodes    = 4
      shape    = VM.Standard.E4.Flex (8 OCPU, 64GB)
      labels   = { role: data }
      purpose  = Kafka brokers, Redis cluster

    weblogic_pool:
      nodes    = 2
      shape    = VM.Standard.E4.Flex (16 OCPU, 128GB)
      labels   = { role: weblogic }
      purpose  = WebLogic Server managed servers (or WLS runs on OCI WLS PaaS)

    ai_pool:
      nodes    = 2
      shape    = BM.GPU.A10.4 (GPU-backed)
      labels   = { role: ai }
      purpose  = AI Agent Studio inference pods

    monitoring_pool:
      nodes    = 2
      shape    = VM.Standard.E4.Flex (4 OCPU, 16GB)
      labels   = { role: monitoring }

  NAMESPACES:
    erp-system         (ingress-nginx, cert-manager, vault-agent-injector, istio)
    erp-gateway        (Kong Gateway, OCI API Gateway proxy)
    erp-services       (all Spring Boot microservices)
    erp-integration    (ERP Fusion connectors, WebLogic JCA adapter pods)
    erp-data           (Kafka, Redis, ZooKeeper operators)
    erp-ai             (AI Agent Studio pods)
    erp-monitoring     (Prometheus, Grafana, Jaeger, Loki, AlertManager)
    erp-cicd           (Tekton pipelines, ArgoCD)

  FUNCTION deploy_microservice(name, image, config, secrets):

    CREATE Deployment in erp-services:
      metadata:
        name      = name
        namespace = erp-services
        labels    = { app: name, version: config.version, tier: backend }
        annotations:
          vault.hashicorp.com/agent-inject: "true"
          vault.hashicorp.com/role: name

      spec:
        replicas = 3
        strategy:
          type = RollingUpdate
          maxSurge         = 1
          maxUnavailable   = 0

        pod_spec:
          serviceAccountName = name + "-sa"
          containers:
            - name:  name
              image: ocir.io/tenancy/erp/{name}:{config.tag}
              ports: [8080]
              envFrom:
                - configMapRef:  name + "-config"
                - secretRef:     name + "-secrets"   // injected by Vault agent
              env:
                - SPRING_PROFILES_ACTIVE = production
                - JAVA_OPTS = -Xms512m -Xmx1g -XX:+UseG1GC
              resources:
                requests: { cpu: 500m, memory: 1Gi }
                limits:   { cpu: 2,    memory: 2Gi }
              livenessProbe:
                httpGet: { path: /actuator/health/liveness, port: 8080 }
                initialDelaySeconds = 60
                periodSeconds       = 15
                failureThreshold    = 3
              readinessProbe:
                httpGet: { path: /actuator/health/readiness, port: 8080 }
                initialDelaySeconds = 30
                periodSeconds       = 10
              lifecycle:
                preStop: { exec: sleep 10 }   // drain connections before kill

          topologySpreadConstraints:
            maxSkew           = 1
            topologyKey       = kubernetes.io/hostname
            whenUnsatisfiable = DoNotSchedule   // spread across nodes

    CREATE HorizontalPodAutoscaler:
      minReplicas = 2
      maxReplicas = 30
      metrics:
        - type: Resource, cpu,       averageUtilization = 70
        - type: External, kafka_lag, target = 1000 messages
        - type: Pods,     rps,       target = 500 rps/pod

    CREATE PodDisruptionBudget:
      minAvailable = 2  // always keep 2 pods alive during drain/upgrades

    CREATE NetworkPolicy:
      podSelector:  { app: name }
      ingress:
        - from: [ namespaceSelector: { name: erp-gateway } ]
          ports: [8080]
      egress:
        - to:   [ namespaceSelector: { name: erp-data } ]
          ports: [6379, 9092]         // Redis + Kafka
        - to:   [ namespaceSelector: { name: erp-integration } ]
          ports: [8090]               // ERP integration service
        - to:   ipBlock: { cidr: 0.0.0.0/0, except: [10.0.0.0/8] }
          ports: [443]                // ERP Fusion HTTPS outbound

  SERVICE_MESH (Istio):
    ENABLE auto mTLS between all pods in erp-services namespace
    DEFINE PeerAuthentication: mode = STRICT (no plain-text traffic)
    DEFINE DestinationRule per service:
      trafficPolicy:
        connectionPool:
          http: { http2MaxRequests: 1000, h2UpgradePolicy: UPGRADE }
        outlierDetection:
          consecutiveErrors    = 5
          interval             = 30s
          baseEjectionTime     = 30s
          maxEjectionPercent   = 50
    DEFINE VirtualService for canary:
      route:
        - destination: { host: name, subset: stable } weight=90
        - destination: { host: name, subset: canary } weight=10


────────────────────────────────────────────────────────────────────────────
09. WEBLOGIC SERVER (OCI WLS PaaS)
────────────────────────────────────────────────────────────────────────────

COMPONENT weblogic_server (OCI WebLogic Suite on OCI):

  PURPOSE:
    - Host legacy J2EE EJBs being migrated to microservices
    - Run Oracle ADF-based admin UIs connecting to ERP Fusion
    - JCA adapter for ERP Fusion SOAP web services (legacy integration)
    - Oracle SOA Suite / OSB orchestration for complex ERP workflows
    - Gradual strangler-fig migration to Spring Boot microservices

  TOPOLOGY:
    admin_server:
      host    = weblogic-admin.app_subnet
      port    = 7002 (HTTPS)
      purpose = Administration Console, deployment orchestration

    managed_servers:
      cluster = erp-wls-cluster
      servers:
        - wls-managed-1  (host BPEL processes, ADF apps)
        - wls-managed-2  (host JCA adapters, OSB proxies)
      port  = 8443
      jvm:  -Xms2g -Xmx8g -XX:+UseG1GC

    data_sources:
      erp_paas_ds:
        jndi_name = jdbc/erpPaasDS
        url       = jdbc:oracle:thin:@atp.erp.internal:1521/erppaas_high
        user      = erp_app_user
        password  = from vault
        pool:     minCapacity=5, maxCapacity=50

  WLS_MODULES:

    MODULE erp_soap_adapter:
      PURPOSE: Call ERP Fusion SOAP Web Services for legacy operations
      FUNCTION call_erp_fusion_soap(service_name, payload):
        wsdl_url = ERP_FUSION_BASE_URL + "/soa-infra/services/default/" + service_name
        token    = get_erp_fusion_token()
        client   = jax_ws_client(wsdl_url)
        client.set_header("Authorization", "Bearer " + token)
        client.set_header("X-Correlation-ID", correlationId)
        response = client.invoke(payload)
        RETURN response

    MODULE erp_event_listener:
      PURPOSE: Receive business events from ERP Fusion (UCM / Oracle Events)
      ENDPOINT: POST /api/v1/erp/events/callback
      FUNCTION handle_erp_event(event):
        VALIDATE event.signature (HMAC-SHA256 with shared secret)
        DESERIALIZE event
        PUBLISH event → Kafka topic: erp.fusion.events.inbound
        RETURN 200 OK (async processing by Kafka consumers)

    MODULE bpel_process_manager:
      PURPOSE: Long-running approval workflows spanning ERP Fusion + PaaS
      PROCESSES:
        three_way_match_process:
          RECEIVE: purchase_order + goods_receipt + ap_invoice
          COMPARE: PO amount vs GR amount vs Invoice amount
          IF match:
            CALL erp_fusion.ap.approve_invoice(invoice_id)
            PUBLISH kafka_event("ap.invoice.approved")
          ELSE:
            CREATE exception_workflow → notify finance team
            PUBLISH kafka_event("ap.invoice.exception")

    MODULE osb_proxy_service:
      PURPOSE: Mediation and transformation between PaaS and ERP Fusion APIs
      TRANSFORMS:
        JSON → SOAP (for legacy ERP endpoints)
        SOAP → JSON (normalize ERP responses to REST contract)
        XSLT transforms for ERP XML → domain objects
      ROUTING:
        IF erp_fusion_api AVAILABLE:
          ROUTE → live ERP Fusion REST/SOAP
        ELSE (circuit_breaker OPEN):
          ROUTE → cached_data_service (serve from Redis/ADW)
          EMIT circuit_breaker_open event → monitoring


────────────────────────────────────────────────────────────────────────────
10. OCI ERP FUSION SAAS INTEGRATION LAYER
────────────────────────────────────────────────────────────────────────────

COMPONENT erp_integration_service (Spring Boot, port 8090):

  PURPOSE: Single integration hub for all ERP Fusion SaaS data access.
           PaaS microservices NEVER call ERP Fusion directly.
           All ERP access goes through this service.

  PATTERNS:
    - Cache-Aside: check Redis → if miss → call ERP Fusion → populate Redis
    - Circuit Breaker: Resilience4j wrapping all ERP Fusion HTTP calls
    - Retry with exponential backoff: 3 retries, 1s/2s/4s delays
    - Timeout: 30s for ERP API calls (ERP Fusion can be slow)
    - Idempotency: dedup write-back operations using Redis keys
    - Pagination: auto-handle ERP Fusion paginated responses (limit=500)

  ERP_FUSION_BASE_CONFIG:
    base_url       = ERP_FUSION_BASE_URL   (from OCI Vault)
    auth_url       = "https://login.oracle.com/oam/..."
    api_version    = "11.13.22.12"
    timeout_ms     = 30000
    max_retries    = 3
    circuit_breaker:
      failure_rate_threshold    = 50%
      wait_duration_open_state  = 60s
      permitted_calls_half_open = 3

  ──────────────────────────────────────────
  10a. GENERAL LEDGER (GL) INTEGRATION
  ──────────────────────────────────────────

  FUNCTION getGLJournalEntries(params):
    // params: { ledger_id, period_name, account_segment, page, limit }

    cache_key = "gl:journals:" + hash(params)
    cached    = redis.get(cache_key)
    IF cached: RETURN cached

    token    = get_erp_fusion_token()
    all_data = []
    offset   = 0

    LOOP:
      response = HTTP GET
        url     = ERP_BASE + "/fscmRestApi/resources/11.13.22.12/glJournals"
        headers = { Authorization: Bearer {token}, Content-Type: application/json }
        params  = {
          q:        "PeriodName='{params.period_name}';LedgerId={params.ledger_id}",
          limit:    500,
          offset:   offset,
          fields:   "JournalHeaderId,JournalName,PeriodName,Status,TotalAccounted
                     DebitAccounted,CreditAccounted,BatchName,CreationDate"
        }

      all_data.append(response.items)
      IF response.hasMore == false: BREAK
      offset += 500

    result = map_to_domain_gl_journals(all_data)
    redis.setex(cache_key, 300, result)  // 5min TTL
    PUBLISH kafka_event("erp.gl.journals.fetched", { count: result.size, params })
    RETURN result

  FUNCTION getGLTrialBalance(ledger_id, period_name, currency):
    cache_key = "gl:trial_balance:" + ledger_id + ":" + period_name
    cached    = redis.get(cache_key)
    IF cached: RETURN cached

    // Use BIP Report REST API for complex reports
    token    = get_erp_fusion_token()
    response = HTTP POST
      url     = ERP_BASE + "/xmlpserver/services/rest/v1/reports"
      headers = { Authorization: Bearer {token} }
      body    = {
        reportAbsolutePath: "/Custom/Finance/TrialBalance.xdo",
        parameterNameValues: {
          ledger_id:   ledger_id,
          period_name: period_name,
          currency:    currency
        },
        byPassCache: false,
        reportOutputPath: null,  // inline response
        flattenXML: true
      }

    data  = parse_bip_xml_response(response)
    redis.setex(cache_key, 600, data)   // 10min TTL
    RETURN data

  FUNCTION getGLAccountBalances(account_combination, period_range):
    cache_key  = "gl:balances:" + account_combination + ":" + period_range
    cached     = redis.get(cache_key)
    IF cached: RETURN cached

    token     = get_erp_fusion_token()
    response  = HTTP GET
      url     = ERP_BASE + "/fscmRestApi/resources/11.13.22.12/glBalances"
      params  = {
        q:      "AccountCombination='{account_combination}'",
        fields: "LedgerId,PeriodName,AccountCombination,Currency,
                 BeginningBalance,PeriodActivity,EndingBalance"
      }

    result   = map_to_domain_balances(response.items)
    redis.setex(cache_key, 120, result)  // 2min TTL (balances change)
    RETURN result

  FUNCTION importGLJournalEntries(journal_batch):
    // Write-back to ERP Fusion GL
    idempotency_key = "gl:import:" + journal_batch.reference
    IF redis.get(idempotency_key):
      THROW DuplicateImportException("Already submitted: " + idempotency_key)

    token    = get_erp_fusion_token()
    response = HTTP POST
      url     = ERP_BASE + "/fscmRestApi/resources/11.13.22.12/glJournals"
      headers = { Authorization: Bearer {token}, Content-Type: application/json }
      body    = {
        JournalName:       journal_batch.name,
        LedgerId:          journal_batch.ledger_id,
        PeriodName:        journal_batch.period,
        Currency:          journal_batch.currency,
        JournalLines:      journal_batch.lines.map(l → {
          AccountCombination: l.account,
          EnteredDebit:       l.debit,
          EnteredCredit:      l.credit,
          Description:        l.description
        })
      }

    IF response.status == 201:
      redis.setex(idempotency_key, 86400, response.JournalHeaderId)  // 24h dedup
      PUBLISH kafka_event("erp.gl.journal.imported", response)
      RETURN response
    ELSE:
      LOG error(response) with correlationId
      THROW ERPFusionWriteException(response.detail)

  ──────────────────────────────────────────
  10b. ACCOUNTS PAYABLE (AP) INTEGRATION
  ──────────────────────────────────────────

  FUNCTION getAPInvoices(params):
    // params: { supplier_id, status, date_from, date_to, page, limit }

    cache_key = "ap:invoices:" + hash(params)
    cached    = redis.get(cache_key)
    IF cached AND params.status != "NEEDS_REVALIDATION":
      RETURN cached

    token    = get_erp_fusion_token()
    response = HTTP GET
      url    = ERP_BASE + "/fscmRestApi/resources/11.13.22.12/invoices"
      params = {
        q:      build_ap_query(params),
        fields: "InvoiceId,InvoiceNumber,InvoiceDate,SupplierName,SupplierId,
                 InvoiceAmount,AmountPaid,PaymentStatus,DueDate,Description,
                 InvoiceCurrency,LegalEntity",
        limit:  params.limit ?: 100,
        offset: params.page * (params.limit ?: 100)
      }

    result = map_to_domain_ap_invoices(response.items)
    redis.setex(cache_key, 60, result)    // 1min TTL (AP data changes frequently)
    RETURN { data: result, total: response.totalResults, hasMore: response.hasMore }

  FUNCTION createAPInvoice(invoice_data):
    VALIDATE invoice_data (required fields, amount > 0, valid supplier)
    idempotency_key = "ap:create:" + invoice_data.invoice_number

    IF redis.get(idempotency_key):
      RETURN redis.get(idempotency_key + ":result")

    token    = get_erp_fusion_token()
    response = HTTP POST
      url    = ERP_BASE + "/fscmRestApi/resources/11.13.22.12/invoices"
      body   = map_to_erp_ap_invoice(invoice_data)

    IF response.status == 201:
      redis.setex(idempotency_key, 86400, "submitted")
      redis.setex(idempotency_key + ":result", 86400, response)
      INVALIDATE cache("ap:invoices:*")   // bust AP list caches
      PUBLISH kafka_event("erp.ap.invoice.created", response)
      RETURN response

  FUNCTION getAPPayments(params):
    cache_key = "ap:payments:" + hash(params)
    cached    = redis.get(cache_key)
    IF cached: RETURN cached

    token    = get_erp_fusion_token()
    response = HTTP GET
      url    = ERP_BASE + "/fscmRestApi/resources/11.13.22.12/payments"
      params = {
        q:      "PaymentDate >= '{params.date_from}' AND PaymentDate <= '{params.date_to}'",
        fields: "PaymentId,PaymentNumber,PaymentDate,PaymentAmount,
                 PaymentCurrency,SupplierName,BankAccountName,PaymentStatus"
      }

    result = map_to_domain_payments(response.items)
    redis.setex(cache_key, 120, result)
    RETURN result

  ──────────────────────────────────────────
  10c. ACCOUNTS RECEIVABLE (AR) INTEGRATION
  ──────────────────────────────────────────

  FUNCTION getARInvoices(params):
    cache_key = "ar:invoices:" + hash(params)
    cached    = redis.get(cache_key)
    IF cached: RETURN cached

    token    = get_erp_fusion_token()
    response = HTTP GET
      url    = ERP_BASE + "/fscmRestApi/resources/11.13.22.12/receivablesInvoices"
      params = {
        q:      build_ar_query(params),
        fields: "CustomerTrxId,TrxNumber,TrxDate,CustomerName,CustomerId,
                 InvoiceAmount,AmountDue,DueDate,Status,TrxType,Currency"
      }

    result = map_to_domain_ar_invoices(response.items)
    redis.setex(cache_key, 60, result)
    RETURN result

  FUNCTION getARAgingReport(as_of_date, customer_id):
    cache_key = "ar:aging:" + as_of_date + ":" + (customer_id ?: "ALL")
    cached    = redis.get(cache_key)
    IF cached: RETURN cached

    // Aging reports → BIP REST API (complex report)
    token    = get_erp_fusion_token()
    response = HTTP POST
      url    = ERP_BASE + "/xmlpserver/services/rest/v1/reports"
      body   = {
        reportAbsolutePath: "/Custom/AR/AgingReport.xdo",
        parameterNameValues: {
          p_as_of_date:  as_of_date,
          p_customer_id: customer_id ?: "ALL"
        }
      }

    aging_buckets = parse_bip_aging_report(response)
    // buckets: current, 1-30d, 31-60d, 61-90d, 91-120d, 120d+
    redis.setex(cache_key, 1800, aging_buckets)   // 30min (aging is a snapshot)
    RETURN aging_buckets

  FUNCTION createARReceipt(receipt_data):
    idempotency_key = "ar:receipt:" + receipt_data.reference_number
    IF redis.get(idempotency_key): RETURN redis.get(idempotency_key + ":result")

    token    = get_erp_fusion_token()
    response = HTTP POST
      url    = ERP_BASE + "/fscmRestApi/resources/11.13.22.12/receivablesCreditMemos"
      body   = map_to_erp_ar_receipt(receipt_data)

    IF response.status == 201:
      redis.setex(idempotency_key, 86400, "submitted")
      INVALIDATE cache("ar:invoices:*")
      PUBLISH kafka_event("erp.ar.receipt.created", response)
      RETURN response

  ──────────────────────────────────────────
  10d. TAX INTEGRATION
  ──────────────────────────────────────────

  FUNCTION getTaxRates(params):
    // params: { tax_regime_code, tax_type, effective_date, country }
    cache_key = "tax:rates:" + hash(params)
    cached    = redis.get(cache_key)
    IF cached: RETURN cached

    token    = get_erp_fusion_token()
    response = HTTP GET
      url    = ERP_BASE + "/fscmRestApi/resources/11.13.22.12/taxRates"
      params = {
        q:      "TaxRegimeCode='{params.tax_regime_code}'
                 AND EffectiveFrom <= '{params.effective_date}'
                 AND (EffectiveTo IS NULL OR EffectiveTo >= '{params.effective_date}')",
        fields: "TaxRateId,TaxRateCode,TaxRate,TaxRegimeCode,TaxType,
                 EffectiveFrom,EffectiveTo,CountryCode"
      }

    result = map_to_domain_tax_rates(response.items)
    redis.setex(cache_key, 3600, result)  // 1h TTL (tax rates rarely change)
    RETURN result

  FUNCTION calculateTax(transaction):
    // Real-time tax calculation via ERP Fusion Tax Service
    token    = get_erp_fusion_token()
    response = HTTP POST
      url    = ERP_BASE + "/fscmRestApi/resources/11.13.22.12/taxCalculations"
      body   = {
        TransactionType:    transaction.type,           // PURCHASE | SALE
        TransactionDate:    transaction.date,
        ShipToCountry:      transaction.ship_to_country,
        ShipFromCountry:    transaction.ship_from_country,
        CustomerClass:      transaction.customer_class,
        SupplierClass:      transaction.supplier_class,
        Lines:              transaction.lines.map(l → {
          LineNumber:       l.number,
          Amount:           l.amount,
          ProductCategory:  l.product_category,
          ProductFiscalClassification: l.fiscal_class
        })
      }

    tax_result = {
      total_tax:    response.TotalTax,
      tax_lines:    response.TaxLines,
      tax_regime:   response.TaxRegimeCode,
      jurisdiction: response.JurisdictionCode
    }
    // Tax calculations NOT cached (real-time, context-dependent)
    RETURN tax_result

  FUNCTION getTaxConfiguration(legal_entity_id):
    cache_key = "tax:config:" + legal_entity_id
    cached    = redis.get(cache_key)
    IF cached: RETURN cached

    token    = get_erp_fusion_token()
    response = HTTP GET
      url    = ERP_BASE + "/fscmRestApi/resources/11.13.22.12/taxConfigurations"
      params = { q: "LegalEntityId={legal_entity_id}" }

    result = map_to_domain_tax_config(response.items)
    redis.setex(cache_key, 3600, result)
    RETURN result


────────────────────────────────────────────────────────────────────────────
11. MICROSERVICES — SPRING BOOT
────────────────────────────────────────────────────────────────────────────

// ─── SHARED BASE PATTERN ───────────────────────────────────────────────

PATTERN spring_boot_microservice:

  BOOTSTRAP:
    LOAD config: spring.config.import = vault://erp-paas-vault/data/{service-name}
    LOAD config: spring.cloud.oci.config.*  (OCI Config Service)
    CONFIGURE datasource: HikariCP (min=5, max=20, connectionTimeout=30s)
    CONFIGURE redis_template (Lettuce driver, cluster mode)
    CONFIGURE kafka_producer (acks=all, idempotence=true)
    CONFIGURE resilience4j: circuit_breaker, retry, bulkhead per ERP endpoint
    CONFIGURE opentelemetry_agent (auto-instrument HTTP, JDBC, Kafka, Redis)
    REGISTER actuator: /health, /metrics, /info, /prometheus

  MDC_FILTER (servlet filter, order=1):
    FOR every request:
      correlationId = request.header("X-Request-ID") ?: uuid()
      userId        = jwt.claims("sub")
      tenantId      = jwt.claims("tenant_id")
      SET MDC["correlationId"] = correlationId
      SET MDC["userId"]        = userId
      SET MDC["tenantId"]      = tenantId
      SET MDC["service"]       = SERVICE_NAME
      response.setHeader("X-Correlation-ID", correlationId)

  GLOBAL_EXCEPTION_HANDLER:
    ConstraintViolationException    → 400 + validation_details
    AuthenticationException         → 401 + message
    AccessDeniedException           → 403 + required_permission
    ResourceNotFoundException       → 404 + resource_id
    DuplicateImportException        → 409 + existing_id
    ERPFusionWriteException         → 502 + erp_error_detail
    CircuitBreakerOpenException     → 503 + retry_after
    Throwable (catch-all)           → 500 + correlationId (NEVER leak stack trace)

// ─── FINANCE ORCHESTRATION SERVICE ────────────────────────────────────

SERVICE finance_orchestration_service (port 8080):

  FUNCTION getFinancialDashboard(tenant_id, period):
    // Fan-out: fetch GL + AP + AR + Tax concurrently
    PARALLEL EXECUTE:
      gl_summary    = erp_integration_client.getGLAccountBalances("ALL", period)
      ap_summary    = erp_integration_client.getAPInvoices({ status: UNPAID, period })
      ar_summary    = erp_integration_client.getARInvoices({ status: OUTSTANDING })
      tax_summary   = erp_integration_client.getTaxConfiguration(tenant_id)

    dashboard = merge(gl_summary, ap_summary, ar_summary, tax_summary)
    ENRICH dashboard WITH ai_agent_client.getAISuggestions("FINANCE_DASHBOARD")
    RETURN dashboard

  FUNCTION initiateThreeWayMatch(po_id, gr_id, invoice_id):
    po      = procurement_service_client.getPO(po_id)
    gr      = inventory_service_client.getGoodsReceipt(gr_id)
    invoice = erp_integration_client.getAPInvoiceById(invoice_id)

    tolerance = 0.02  // 2% variance allowed

    IF ABS(po.amount - invoice.amount) / po.amount > tolerance:
      CREATE exception: THREE_WAY_MISMATCH
      PUBLISH kafka_event("ap.three_way_match.exception", { po, gr, invoice })
      NOTIFY finance_team via notification_service
      RETURN { status: EXCEPTION, mismatch: calculate_variance(po, invoice) }

    erp_integration_client.approveAPInvoice(invoice_id)
    PUBLISH kafka_event("ap.three_way_match.approved", { po, gr, invoice })
    RETURN { status: APPROVED }

// ─── PROCUREMENT SERVICE ───────────────────────────────────────────────

SERVICE procurement_service (port 8081):

  FUNCTION createPurchaseOrder(request):
    VALIDATE budget → erp_integration_client.checkGLBudget(request.dept, request.amount)
    VALIDATE supplier → erp_integration_client.getSupplier(request.supplier_id)

    po = {
      po_number:   generate_po_number(),
      supplier_id: request.supplier_id,
      line_items:  request.line_items,
      total:       SUM(line_items.amount),
      currency:    request.currency,
      status:      DRAFT
    }
    SAVE po → ATP database
    PUBLISH kafka_event("procurement.po.created", po)

    IF po.total > approval_threshold:
      SEND approval_request → notification_service

    RETURN po

// ─── REPORTING SERVICE ────────────────────────────────────────────────

SERVICE reporting_service (port 8084):

  FUNCTION generateFinancialReport(report_type, params):
    MATCH report_type:
      CASE TRIAL_BALANCE:
        data = erp_integration_client.getGLTrialBalance(params.ledger, params.period, params.currency)
      CASE AP_AGING:
        data = erp_integration_client.getAPInvoices({ ...params, include_aging: true })
      CASE AR_AGING:
        data = erp_integration_client.getARAgingReport(params.as_of_date, params.customer_id)
      CASE TAX_SUMMARY:
        data = erp_integration_client.getTaxReturns(params.period)
      CASE CASH_FLOW:
        gl   = erp_integration_client.getGLAccountBalances(params.cash_accounts, params.period)
        ap   = erp_integration_client.getAPPayments(params)
        ar   = erp_integration_client.getARReceipts(params)
        data = compute_cash_flow(gl, ap, ar)

    report_id = uuid()
    SAVE report → ADW (analytics warehouse)
    UPLOAD PDF → sharepoint_proxy_service (erp-reports library)
    PUBLISH kafka_event("report.generated", { report_id, report_type })
    RETURN { report_id, download_url }


────────────────────────────────────────────────────────────────────────────
12. AI AGENT STUDIO — INTELLIGENT AUTOMATION
────────────────────────────────────────────────────────────────────────────

COMPONENT ai_agent_studio (OCI AI Agent Studio + custom agents):

  PURPOSE:
    - Natural language query over ERP Fusion data (GL, AP, AR, Tax)
    - Anomaly detection on financial transactions
    - Automated reconciliation suggestions
    - Invoice exception classification
    - Tax compliance risk scoring
    - Predictive cash flow forecasting

  INFRASTRUCTURE:
    DEPLOY on: erp-ai namespace (GPU-backed nodes: BM.GPU.A10.4)
    MODELS:
      - Base LLM:        OCI Generative AI (Cohere Command / Llama 3)
      - Embedding model: OCI Generative AI Embeddings
      - Custom model:    fine-tuned on ERP Fusion data schema (OCI Data Science)
    VECTOR_DB: Oracle DB 23ai (vector search extension) or OpenSearch

  AGENT_DEFINITIONS:

    AGENT gl_analysis_agent:
      TOOLS:
        - get_gl_journal_entries(period, account_filter)
        - get_trial_balance(ledger_id, period)
        - get_account_balances(account, period_range)
        - search_erp_docs(query)          // vector search on ERP documentation
      FUNCTION query(user_question, context):
        prompt = build_erp_prompt(user_question, context, erp_schema_context)
        CALL OCI_GenAI_API (model: cohere-command-r-plus):
          system: "You are an ERP Finance analyst with access to GL data.
                   Always cite journal entry IDs and account codes in answers.
                   Do not hallucinate ERP data — use only tool results."
          messages: conversation_history + [{ role: user, content: prompt }]
          tools: gl_analysis_agent.tools
        EXECUTE tool_calls returned by model
        RETURN synthesized_answer

    AGENT ap_reconciliation_agent:
      TOOLS:
        - get_ap_invoices(filters)
        - get_ap_payments(date_range)
        - get_purchase_orders(filters)
        - flag_exception(invoice_id, reason)
      FUNCTION reconcile(period):
        invoices = get_ap_invoices({ period, status: UNPAID })
        payments = get_ap_payments({ period })
        unmatched = find_unmatched(invoices, payments)
        FOR each item IN unmatched:
          classification = classify_exception(item)  // LLM call
          IF classification.confidence > 0.85:
            AUTO flag_exception(item.id, classification.reason)
          ELSE:
            QUEUE for human_review with classification.suggestion

    AGENT tax_risk_agent:
      TOOLS:
        - get_tax_configurations(legal_entity)
        - get_transactions_for_review(filters)
        - calculate_tax_for_transaction(transaction)
      FUNCTION assess_risk(transactions):
        FOR each tx IN transactions:
          calculated_tax = calculate_tax_for_transaction(tx)
          IF ABS(tx.applied_tax - calculated_tax.total_tax) > threshold:
            EMIT risk_alert(tx, calculated_tax, risk_score)
            PUBLISH kafka_event("tax.risk.detected", risk_alert)

    AGENT cash_flow_forecast_agent:
      TOOLS:
        - get_ar_aging(as_of_date)
        - get_ap_payments_due(date_range)
        - get_gl_balances(cash_accounts)
      FUNCTION forecast(horizon_days=90):
        ar_expected   = model_ar_collections(ar_aging)
        ap_due        = get_ap_payments_due({ days: horizon_days })
        current_cash  = get_gl_balances(CASH_ACCOUNTS)
        forecast_data = time_series_forecast(current_cash, ar_expected, ap_due)
        RETURN { daily_forecast, weekly_summary, risk_days: days_below_threshold }

  AI_AGENT_SERVICE (Spring Boot wrapper, port 8095):

    FUNCTION natural_language_query(request):
      // request: { question, context_module, user_id, conversation_id }
      history = redis.get("ai:conv:" + request.conversation_id) ?: []

      agent = select_agent(request.context_module):
        GL    → gl_analysis_agent
        AP    → ap_reconciliation_agent
        AR    → ar_reconciliation_agent  (similar to AP)
        TAX   → tax_risk_agent
        DEFAULT → general_erp_agent

      result = agent.query(request.question, history)
      history.append({ role: user, content: request.question })
      history.append({ role: assistant, content: result })
      redis.setex("ai:conv:" + request.conversation_id, 3600, history)
      RETURN { answer: result, sources: result.citations }

    FUNCTION detect_anomalies(module, period):
      data      = erp_integration_client.get_module_data(module, period)
      anomalies = statistical_anomaly_detection(data):
        method   = Isolation Forest + LLM explanation
        threshold = 3 sigma
      FOR each anomaly IN anomalies:
        PUBLISH kafka_event("ai.anomaly.detected", anomaly)
      RETURN anomalies


────────────────────────────────────────────────────────────────────────────
13. REACT FRONTEND
────────────────────────────────────────────────────────────────────────────

COMPONENT react_frontend (React 18 + TypeScript):

  STACK:
    - React 18 + TypeScript
    - Redux Toolkit + RTK Query (server + global state)
    - React Router v6 (navigation)
    - Axios (HTTP with interceptors)
    - TanStack Table (GL / AP / AR data grids)
    - Recharts / D3 (financial charts)
    - AG Grid (large data tabular views)
    - React Hook Form + Zod (form validation)
    - i18next (internationalization)

  BOOTSTRAP:
    INIT oauth_pkce_client:
      authority     = IDCS_URL
      client_id     = react_spa
      redirect_uri  = APP_URL + "/callback"
      scope         = "openid profile erp:read erp:write ai:use"
    SETUP RTK Query base:
      baseUrl        = API_BASE_URL
      prepareHeaders = (headers) → { attach Bearer token; RETURN headers }
      401 handler    = auto_refresh_token() then retry
      403 handler    = navigate("/unauthorized")
    SETUP WebSocket for real-time notifications:
      url = WSS_URL + "/ws/notifications?token=" + access_token

  ROUTING:
    /login                   → LoginPage (OAuth redirect)
    /callback                → OAuthCallbackHandler
    /dashboard               → FinancialDashboard    [FINANCE_READ]
    /gl/journals             → GLJournalList         [FINANCE_READ]
    /gl/journals/new         → GLJournalForm         [FINANCE_WRITE]
    /gl/trial-balance        → TrialBalanceReport    [FINANCE_READ]
    /ap/invoices             → APInvoiceList         [AP_READ]
    /ap/invoices/:id         → APInvoiceDetail       [AP_READ]
    /ap/invoices/new         → APInvoiceForm         [AP_WRITE]
    /ar/invoices             → ARInvoiceList         [AR_READ]
    /ar/aging                → ARAgingReport         [AR_READ]
    /tax/calculator          → TaxCalculator         [TAX_READ]
    /tax/configurations      → TaxConfigView         [TAX_READ]
    /reports                 → ReportCenter          [FINANCE_READ]
    /ai/assistant            → AIAssistantChat       [AI_USE]
    /sharepoint/documents    → SharePointDocViewer   [DOC_READ]
    /admin                   → AdminPanel            [ADMIN]

  COMPONENT FinancialDashboard:
    ON mount (PARALLEL fetch via RTK Query):
      glSummary      = useGetGLAccountBalancesQuery({ period: currentPeriod })
      apSummary      = useGetAPInvoicesQuery({ status: 'UNPAID', limit: 5 })
      arSummary      = useGetARInvoicesQuery({ status: 'OUTSTANDING', limit: 5 })
      taxAlerts      = useGetTaxRiskAlertsQuery()
      aiSuggestions  = useGetAISuggestionsQuery({ context: 'DASHBOARD' })

    RENDER:
      <DashboardGrid>
        <GLSummaryCard    data={glSummary}   loading={glSummary.isLoading} />
        <APSummaryCard    data={apSummary}   onViewAll={() → navigate("/ap")} />
        <ARAgingWidget    data={arSummary}   chartType="donut" />
        <TaxAlertBanner   alerts={taxAlerts} />
        <CashFlowChart    data={glSummary}   range="90d" />
        <AIInsightPanel   suggestions={aiSuggestions} />
        <RealtimeNotifications socket={ws} />
      </DashboardGrid>

  COMPONENT AIAssistantChat:
    state: { messages[], conversationId, isLoading }

    FUNCTION sendMessage(userMessage):
      ADD { role: user, content: userMessage } to messages
      SET isLoading = true
      response = await API.post("/api/v1/ai/query", {
        question:        userMessage,
        context_module:  currentModule,
        conversation_id: conversationId
      })
      ADD { role: assistant, content: response.answer, sources: response.sources }
      SET isLoading = false

    RENDER:
      <ChatContainer>
        <ModuleSelector onChange={setCurrentModule} modules=[GL, AP, AR, TAX] />
        <MessageList>
          FOR each message IN messages:
            <MessageBubble role={message.role} content={message.content}>
              IF message.sources:
                <SourceCitations sources={message.sources} />
            </MessageBubble>
        </MessageList>
        <MessageInput onSend={sendMessage} loading={isLoading}
                      placeholder="Ask anything about GL, AP, AR or Tax..." />
      </ChatContainer>

  COMPONENT GLJournalList:
    state: { filters, pagination }
    data = useGetGLJournalsQuery({ ...filters, ...pagination })
    RENDER:
      <FilterBar>
        <PeriodPicker />  <LedgerSelector />  <StatusFilter />
      </FilterBar>
      <AGGrid
        columnDefs = [JournalName, Period, Debit, Credit, Status, Actions]
        rowData    = {data.items}
        pagination = { page, pageSize, total }
        onRowClick = (row) → navigate("/gl/journals/" + row.JournalHeaderId)
      />
      <ExportButton onClick={exportToExcel} />
      <SharePointUploadButton onClick={uploadToSharePoint} />


────────────────────────────────────────────────────────────────────────────
14. REST API CONTRACTS
────────────────────────────────────────────────────────────────────────────

REST_API_CONTRACTS:

  STANDARD_RESPONSE_ENVELOPE:
    {
      success:       boolean,
      data:          object | array | null,
      error:         { code: string, message: string, details: [] } | null,
      meta: {
        correlationId: string,
        timestamp:     ISO8601,
        page:          int | null,
        size:          int | null,
        total:         int | null,
        erp_source:    "OCI_ERP_FUSION_LIVE" | "CACHE" | "FALLBACK"
      }
    }

  ERP GL ENDPOINTS:
    GET  /api/v1/erp/gl/journal-entries
         ?ledger_id&period_name&account_segment&page&limit&sort
    GET  /api/v1/erp/gl/journal-entries/{id}
    POST /api/v1/erp/gl/journal-entries/import    (body: JournalBatch)
    GET  /api/v1/erp/gl/trial-balance
         ?ledger_id&period_name&currency
    GET  /api/v1/erp/gl/account-balances
         ?account_combination&period_range
    GET  /api/v1/erp/gl/periods
         ?ledger_id&status=OPEN

  ERP AP ENDPOINTS:
    GET  /api/v1/erp/ap/invoices
         ?supplier_id&status&date_from&date_to&page&limit
    GET  /api/v1/erp/ap/invoices/{id}
    POST /api/v1/erp/ap/invoices                  (body: APInvoice)
    GET  /api/v1/erp/ap/payments
         ?date_from&date_to&supplier_id
    GET  /api/v1/erp/ap/suppliers
         ?name&status&page&limit

  ERP AR ENDPOINTS:
    GET  /api/v1/erp/ar/invoices
         ?customer_id&status&date_from&date_to&page&limit
    POST /api/v1/erp/ar/invoices                  (body: ARInvoice)
    GET  /api/v1/erp/ar/receipts
         ?customer_id&date_from&date_to
    GET  /api/v1/erp/ar/customers
         ?name&status&page&limit
    GET  /api/v1/erp/ar/aging-report
         ?as_of_date&customer_id

  ERP TAX ENDPOINTS:
    GET  /api/v1/erp/tax/rates
         ?tax_regime_code&tax_type&effective_date&country
    GET  /api/v1/erp/tax/configurations
         ?legal_entity_id
    POST /api/v1/erp/tax/calculate               (body: TaxableTransaction)
    GET  /api/v1/erp/tax/returns
         ?period&legal_entity_id

  AI ENDPOINTS:
    POST /api/v1/ai/query                         (body: { question, context_module, conversation_id })
    POST /api/v1/ai/anomaly-detect               (body: { module, period })
    POST /api/v1/ai/reconcile                    (body: { module, period })
    GET  /api/v1/ai/suggestions/{context}
    GET  /api/v1/ai/cash-flow-forecast
         ?horizon_days&legal_entity_id

  SHAREPOINT ENDPOINTS:
    POST /api/v1/sharepoint/documents/upload     (multipart/form-data)
    GET  /api/v1/sharepoint/documents
         ?site&library&folder&page&limit
    GET  /api/v1/sharepoint/documents/{id}
    DELETE /api/v1/sharepoint/documents/{id}

  PAGINATION_STANDARD:
    request:  ?page=0&limit=50&sort=createdAt,desc
    response meta: { page:0, size:50, total:1250, totalPages:25 }

  CACHING_HEADERS:
    GL journal entries:   Cache-Control: max-age=300
    Tax rates:            Cache-Control: max-age=3600
    AP/AR invoices:       Cache-Control: max-age=60, must-revalidate
    Tax calculation:      Cache-Control: no-store  (real-time)


────────────────────────────────────────────────────────────────────────────
15. KAFKA — EVENT STREAMING
────────────────────────────────────────────────────────────────────────────

COMPONENT kafka_cluster (OCI Streaming / Confluent on OKE):

  CONFIGURATION:
    brokers           = 3 (multi-AZ)
    replication_factor = 3
    min.insync.replicas = 2
    retention.ms      = 604800000  // 7 days
    compression.type  = snappy
    schema_registry   = Confluent Schema Registry (Avro schemas)

  TOPICS:
    erp.fusion.events.inbound     partitions=6   // ERP → PaaS business events
    erp.gl.journals.fetched       partitions=3   // GL data fetch events
    erp.ap.invoice.created        partitions=6   // AP write-back confirmations
    erp.ap.invoice.approved       partitions=3
    erp.ar.invoice.created        partitions=6
    erp.ar.receipt.created        partitions=3
    erp.tax.risk.detected         partitions=3
    procurement.po.created        partitions=6
    procurement.po.approved       partitions=3
    ap.three_way_match.approved   partitions=3
    ap.three_way_match.exception  partitions=3
    ai.anomaly.detected           partitions=3
    notifications.outbound        partitions=6
    audit.events                  partitions=12  // immutable audit stream
    api-gateway-logs              partitions=6
    erp.cache.invalidation        partitions=3   // distributed cache busting
    sharepoint.upload.queue       partitions=3   // async SharePoint uploads
    report.generation.queue       partitions=3

  PRODUCER_CONFIG (all Spring Boot services):
    acks             = all
    retries          = 3
    retry.backoff.ms = 1000
    enable.idempotence = true
    max.in.flight.requests.per.connection = 1

  CONSUMER_GROUPS:

    erp-event-processor:
      SUBSCRIBE: erp.fusion.events.inbound
      FUNCTION process(erp_event):
        MATCH erp_event.type:
          "oracle.apps.financials.payables.invoices.approve":
            UPDATE local ap_invoice cache (invalidate Redis)
            PUBLISH audit_event
          "oracle.apps.financials.receivables.receipt.apply":
            INVALIDATE ar_invoice cache
            TRIGGER ar_reconciliation_agent.reconcile()
          "oracle.apps.generalLedger.journalEntries.post":
            INVALIDATE gl_journal cache
            UPDATE reporting_warehouse

    cache-invalidation-consumer:
      SUBSCRIBE: erp.cache.invalidation
      FUNCTION process(event):
        FOR each pattern IN event.cache_patterns:
          redis.delete_pattern(pattern)

    reporting-consumer:
      SUBSCRIBE: erp.gl.journals.fetched, erp.ap.invoice.created,
                 erp.ar.invoice.created, erp.tax.risk.detected
      FUNCTION process(event):
        UPSERT → Oracle ADW (analytics warehouse)
        REFRESH materialized_views affected

    notification-consumer:
      SUBSCRIBE: ap.three_way_match.exception, ai.anomaly.detected,
                 erp.tax.risk.detected, procurement.po.created
      FUNCTION process(event):
        recipients = resolve_recipients(event.type, event.payload)
        channel    = user_preferences.get_channel(recipients)  // email | Slack | in-app
        CALL notification_service.send({ recipients, channel, event })

    sharepoint-upload-consumer:
      SUBSCRIBE: sharepoint.upload.queue
      FUNCTION process(event):
        file = generate_document(event.template, event.data)
        sharepoint_proxy_service.upload(file, event.metadata)

    audit-consumer:
      SUBSCRIBE: audit.events
      FUNCTION process(event):
        PERSIST → audit_log table (append-only, never update/delete)
        IF event.severity == HIGH:
          FORWARD → Splunk SIEM immediately


────────────────────────────────────────────────────────────────────────────
16. REDIS — CACHING & STATE
────────────────────────────────────────────────────────────────────────────

COMPONENT redis_cluster (OCI Cache with Redis):

  TOPOLOGY: Redis Cluster (6 nodes: 3 masters + 3 replicas, multi-AZ)
  SECURITY: TLS + AUTH token (from OCI Vault), IP whitelist (data_subnet only)
  PERSISTENCE: AOF (appendonly yes) + RDB snapshot every 60s

  KEY_NAMESPACES AND TTLs:

    Authentication & Authorization:
      "token:refresh:{user_id}"           TTL = 28800  (8h)
      "token:revoked:{jti}"               TTL = 900    (15min, matches JWT expiry)
      "erp:fusion:token"                  TTL = token.expires_in - 60
      "sp:graph:token"                    TTL = 3500   (SharePoint token)
      "jwks:public_keys"                  TTL = 3600   (JWKS cache)
      "auth_code:{code}"                  TTL = 300    (PKCE auth code, single-use)

    ERP Fusion Data Cache:
      "gl:journals:{hash(params)}"        TTL = 300
      "gl:trial_balance:{l}:{p}"          TTL = 600
      "gl:balances:{account}:{period}"    TTL = 120
      "ap:invoices:{hash(params)}"        TTL = 60
      "ap:payments:{hash(params)}"        TTL = 120
      "ar:invoices:{hash(params)}"        TTL = 60
      "ar:aging:{date}:{customer}"        TTL = 1800
      "tax:rates:{hash(params)}"          TTL = 3600
      "tax:config:{legal_entity}"         TTL = 3600

    Idempotency Keys (write-back dedup):
      "gl:import:{reference}"             TTL = 86400
      "ap:create:{invoice_number}"        TTL = 86400
      "ar:receipt:{reference}"            TTL = 86400

    AI Conversations:
      "ai:conv:{conversation_id}"         TTL = 3600

    Rate Limiting:
      "rate:{client_id}:{window}"         TTL = 60

    Distributed Locks:
      "lock:{resource_id}"                TTL = 30

    Sessions:
      "session:{user_id}"                 TTL = 28800

  FUNCTION cache_aside(cache_key, ttl, supplier_fn):
    result = redis.get(cache_key)
    IF result IS NOT NULL:
      metrics.increment("cache.hit", tags=[cache_key.namespace])
      RETURN deserialize(result)
    metrics.increment("cache.miss", tags=[cache_key.namespace])
    data = supplier_fn()   // fetch from ERP Fusion API
    redis.setex(cache_key, ttl, serialize(data))
    RETURN data

  FUNCTION distributed_lock(resource, ttl=30):
    lock_key = "lock:" + resource
    lock_val = instance_id + ":" + uuid()
    acquired = redis.set(lock_key, lock_val, NX=true, EX=ttl)
    IF NOT acquired:
      THROW ResourceLockedException(resource)
    TRY
      YIELD  // execute critical section
    FINALLY
      script = "if redis.call('get',KEYS[1])==ARGV[1] then return redis.call('del',KEYS[1]) else return 0 end"
      redis.eval(script, [lock_key], [lock_val])  // atomic check-and-delete


────────────────────────────────────────────────────────────────────────────
17. DATABASE LAYER (PaaS)
────────────────────────────────────────────────────────────────────────────

COMPONENT database_layer:

  OLTP: Oracle Autonomous Transaction Processing (ATP)
    service_level = HIGH (OLTP)
    auto_scaling  = TRUE
    backup        = automatic (daily, 60-day retention)
    encryption    = TDE (AES-256)
    data_guard    = ENABLED (standby in DR region)
    private_endpoint = TRUE (no public access)
    connection_pool:
      driver       = JDBC thin (wallet-based)
      pool_library = HikariCP
      min_pool     = 5, max_pool = 20

  ANALYTICS: Oracle Autonomous Data Warehouse (ADW)
    service_level = MEDIUM (analytics)
    purpose       = Kafka → ADW for reporting, dashboards, AI training data
    auto_indexing = TRUE
    materialized_views:
      mv_gl_monthly_summary   (refreshed: hourly)
      mv_ap_aging_buckets     (refreshed: every 15min)
      mv_ar_collection_trends (refreshed: every 15min)
      mv_tax_liability_summary (refreshed: daily)
      mv_cash_flow_weekly     (refreshed: hourly)

  SCHEMA (key tables in ATP):

    TABLE erp_sync_log:
      id UUID PK, module ENUM(GL,AP,AR,TAX), operation ENUM(FETCH,WRITE),
      erp_entity_id VARCHAR, status ENUM(SUCCESS,FAILED,RETRY),
      correlation_id UUID, tenant_id UUID, payload_hash VARCHAR,
      created_at TIMESTAMP, duration_ms INT
      PURPOSE: Track all ERP Fusion API calls for audit + retry

    TABLE procurement_orders:
      po_number VARCHAR PK, supplier_id UUID, total_amount DECIMAL(18,2),
      currency CHAR(3), status ENUM(DRAFT,APPROVED,RECEIVED,CANCELLED),
      erp_po_id VARCHAR (ERP Fusion PO ID after write-back),
      tenant_id UUID, created_by UUID, created_at TIMESTAMP
      INDEX: (tenant_id, status), (erp_po_id)

    TABLE sharepoint_document_map:
      id UUID PK, erp_entity_type VARCHAR, erp_entity_id VARCHAR,
      sharepoint_item_id VARCHAR, sharepoint_drive_id VARCHAR,
      site_name VARCHAR, library_name VARCHAR, file_name VARCHAR,
      tenant_id UUID, uploaded_at TIMESTAMP
      INDEX: (erp_entity_type, erp_entity_id), (tenant_id)

    TABLE notification_log:
      id UUID PK, event_type VARCHAR, recipient_id UUID,
      channel ENUM(EMAIL,SLACK,IN_APP,SMS), status ENUM(SENT,FAILED,PENDING),
      payload CLOB, attempts INT, last_attempt TIMESTAMP,
      tenant_id UUID, created_at TIMESTAMP

    TABLE audit_log:
      id UUID PK, entity_type VARCHAR, entity_id UUID,
      action VARCHAR, performed_by UUID, tenant_id UUID,
      before_state CLOB, after_state CLOB, ip_address VARCHAR,
      correlation_id UUID, timestamp TIMESTAMP
      PARTITION BY: timestamp (monthly partitions)
      // IMMUTABLE: no UPDATE, no DELETE ever

    TABLE ai_query_log:
      id UUID PK, user_id UUID, module VARCHAR,
      question CLOB, answer CLOB, tokens_used INT,
      model_version VARCHAR, latency_ms INT,
      tenant_id UUID, created_at TIMESTAMP

  MULTI_TENANCY:
    STRATEGY: Row-Level Security (RLS) with tenant_id
    IMPLEMENTATION:
      VPD (Virtual Private Database) policy on all tables:
        POLICY: WHERE tenant_id = SYS_CONTEXT('USERENV','CLIENT_INFO')
      Spring: @TenantFilter Hibernate interceptor
        ON session open: SET CLIENT_INFO = current_tenant_id

  MIGRATIONS (Flyway):
    location = classpath:db/migration/
    naming   = V{version}__{description}.sql
    baseline = V1__initial_schema.sql
    VALIDATE on startup, FAIL_FAST on checksum mismatch


────────────────────────────────────────────────────────────────────────────
18. AZURE SHAREPOINT INTEGRATION
────────────────────────────────────────────────────────────────────────────

COMPONENT sharepoint_proxy_service (Spring Boot, port 8085):

  PURPOSE:
    - Upload ERP-generated documents (AP invoices, GL reports, tax returns)
    - Retrieve documents for React frontend display
    - Sync ERP Fusion BIP report outputs → SharePoint document libraries
    - Provide unified document management across ERP + PaaS + SharePoint

  AZURE_AD_AUTHENTICATION:
    tenant_id     = SHAREPOINT_TENANT_ID   (from vault)
    client_id     = SHAREPOINT_CLIENT_ID   (from vault)
    client_secret = SHAREPOINT_CLIENT_SECRET (from vault)
    scope         = "https://graph.microsoft.com/.default"
    grant_type    = client_credentials

  FUNCTION get_sharepoint_token():
    cached = redis.get("sp:graph:token")
    IF cached: RETURN cached

    response = HTTP POST
      url  = "https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
      body = { grant_type, client_id, client_secret, scope }

    redis.setex("sp:graph:token", response.expires_in - 60, response.access_token)
    RETURN response.access_token

  FUNCTION upload_document(file_bytes, metadata):
    // metadata: { site_name, library, folder_path, file_name, erp_entity_type, erp_entity_id }

    idempotency_key = "sp:upload:" + metadata.erp_entity_type + ":" + metadata.erp_entity_id
    IF redis.get(idempotency_key):
      RETURN redis.get(idempotency_key + ":result")

    token   = get_sharepoint_token()
    site_id = resolve_site_id(metadata.site_name, token)
    drive_id = resolve_drive_id(site_id, metadata.library, token)

    // For files > 4MB, use resumable upload session
    IF file_bytes.size > 4_000_000:
      upload_url = create_upload_session(site_id, drive_id, metadata, token)
      item_id    = chunked_upload(upload_url, file_bytes, chunk_size=3_276_800)
    ELSE:
      response = HTTP PUT
        url     = "https://graph.microsoft.com/v1.0/sites/{site_id}/drives/{drive_id}/items/{folder_path}:/{file_name}:/content"
        headers = { Authorization: Bearer {token}, Content-Type: application/octet-stream }
        body    = file_bytes
      item_id = response.id

    // Set metadata fields on the SharePoint item
    HTTP PATCH
      url  = "https://graph.microsoft.com/v1.0/sites/{site_id}/drives/{drive_id}/items/{item_id}/listItem/fields"
      body = {
        ERPEntityType: metadata.erp_entity_type,
        ERPEntityId:   metadata.erp_entity_id,
        TenantId:      metadata.tenant_id,
        UploadedBy:    metadata.uploaded_by
      }

    SAVE sharepoint_document_map → ATP database
    redis.setex(idempotency_key, 86400, "uploaded")
    redis.setex(idempotency_key + ":result", 86400, { item_id, webUrl: response.webUrl })
    INVALIDATE cache("sp:docs:" + metadata.site_name + ":" + metadata.library + ":*")
    PUBLISH kafka_event("sharepoint.document.uploaded", metadata + { item_id })
    RETURN { item_id, webUrl: response.webUrl }

  FUNCTION list_documents(site_name, library, folder, filters):
    cache_key = "sp:docs:" + site_name + ":" + library + ":" + folder + ":" + hash(filters)
    cached    = redis.get(cache_key)
    IF cached: RETURN cached

    token   = get_sharepoint_token()
    site_id = resolve_site_id(site_name, token)
    drive_id = resolve_drive_id(site_id, library, token)

    response = HTTP GET
      url     = "https://graph.microsoft.com/v1.0/sites/{site_id}/drives/{drive_id}/items/{folder_id}/children"
      params  = { $select: "id,name,webUrl,size,createdDateTime,lastModifiedDateTime,file", $top: 50 }
      headers = { Authorization: Bearer {token} }

    items = response.value.map(map_to_domain_document)
    redis.setex(cache_key, 120, items)
    RETURN items

  KAFKA_CONSUMER (sharepoint-upload-consumer):
    SUBSCRIBE: sharepoint.upload.queue
    ON event:
      MATCH event.trigger:
        "ap.invoice.approved":
          file = pdf_generator.generate_ap_invoice_pdf(event.invoice)
          upload_document(file, {
            site:     "erp-accounts-payable",
            library:  "Approved Invoices",
            folder:   event.period,
            filename: "INV_" + event.invoice.number + ".pdf",
            erp_entity_type: "AP_INVOICE",
            erp_entity_id:   event.invoice.id
          })
        "report.generated":
          file = object_storage.get(event.report_path)
          upload_document(file, {
            site:     "erp-finance-reports",
            library:  "Period Reports",
            folder:   event.period,
            filename: event.report_name + ".pdf",
            erp_entity_type: "REPORT",
            erp_entity_id:   event.report_id
          })


────────────────────────────────────────────────────────────────────────────
19. DEVSECOPS / CI / CD PIPELINE
────────────────────────────────────────────────────────────────────────────

COMPONENT devsecops_pipeline:

  VCS:      GitHub Enterprise
  CI:       GitHub Actions + Tekton Pipelines (on OKE)
  CD:       ArgoCD (GitOps) on OKE
  IaC:      Terraform (OCI provider) + OCI Resource Manager
  REGISTRY: OCI Container Registry (OCIR)
  SECRETS:  OCI Vault (never in code, never in env files)

  GITFLOW_BRANCHING:
    main        → production  (protected, require 2 approvals + status checks)
    release/*   → staging
    develop     → development (auto-deploy)
    feature/*   → PR target: develop
    hotfix/*    → PR target: main + develop
    dependabot/ → auto-PR for dependency updates

  CI_PIPELINE (GitHub Actions + Tekton):

    TRIGGER: push to any branch, PR opened/updated

    STAGE 1 — Pre-flight Checks:
      CHECKOUT code
      DETECT changed_modules (only build affected microservices)
      VALIDATE commit_message follows conventional commits
      CHECK branch_name matches naming convention

    STAGE 2 — SAST & Dependency Security:
      RUN Checkstyle + SpotBugs (Java code quality)
      RUN ESLint + TypeScript strict check (React)
      RUN SonarQube analysis:
        coverage threshold     > 80%
        code_smells            = 0 blocker, < 10 critical
        security_hotspots      = must review all
        duplications           < 3%
      RUN OWASP Dependency Check (Java CVE scan)
      RUN Snyk (npm + Maven vulnerability scan)
      RUN Semgrep (custom security rules for ERP data handling):
        RULE: no_hardcoded_erp_credentials
        RULE: no_plaintext_jwt_logging
        RULE: no_sensitive_data_in_cache_key
      IF any_critical_vulnerability:
        BLOCK pipeline
        CREATE GitHub issue with vulnerability details
        NOTIFY security_team via Slack #security-alerts

    STAGE 3 — Build:
      BUILD Spring Boot:
        mvn clean package -DskipTests -Pprod
        OUTPUT: target/{service}-{version}.jar
      BUILD React:
        npm ci
        npm run build:prod
        OUTPUT: build/ (minified, hashed assets)
      BUILD Docker images:
        FROM eclipse-temurin:21.0.3_9-jre-alpine   // pinned, minimal
        RUN addgroup -S appgroup && adduser -S appuser -G appgroup
        COPY --chown=appuser:appgroup {service}.jar /app/
        USER appuser                                // non-root mandatory
        EXPOSE 8080
        ENTRYPOINT ["java","-XX:+UseContainerSupport","-jar","/app/{service}.jar"]
      TAG image: ocir.io/{tenancy}/erp/{service}:{git_sha}-{semver}
      SCAN image with Trivy:
        severity = CRITICAL,HIGH
        IF found: BLOCK pipeline

    STAGE 4 — Tests:
      RUN unit_tests:
        Spring: JUnit 5 + Mockito + AssertJ
        React:  Jest + React Testing Library
      RUN integration_tests (Testcontainers):
        SPIN UP: Oracle DB (ATP-compatible), Redis, Kafka
        MOCK: ERP Fusion API (WireMock stubs with real response shapes)
        TEST all ERP integration service methods end-to-end
        TEST cache-aside pattern (hit + miss)
        TEST circuit_breaker opens after 5 failures
      RUN contract_tests (Pact):
        VERIFY React → API Gateway contract
        VERIFY microservice → ERP integration service contract
      RUN DAST (OWASP ZAP) against staging:
        ACTIVE scan on /api/v1/* endpoints
        ALERT on HIGH+ findings
      PUBLISH coverage → SonarQube
      PUBLISH test results → GitHub Checks

    STAGE 5 — Artifact Promotion:
      PUSH Docker image → OCIR (immutable tag)
      PUSH Helm chart → OCI Helm Registry
      SIGN image + chart (Cosign / Notary)
      UPDATE GitOps manifest repo:
        FILE: gitops-repo/overlays/{env}/kustomization.yaml
        CHANGE: image tag → new build tag
        COMMIT + PUSH (triggers ArgoCD sync)
      CREATE GitHub Release (semver + changelog)

  CD_PIPELINE (ArgoCD GitOps):

    ArgoCD watches gitops-repo for manifest changes

    ENVIRONMENT: development
      TRIGGER:   push to develop
      SYNC:      ArgoCD app: erp-dev (auto-sync, 1min poll)
      POST_SYNC: run smoke_test suite
      NOTIFY:    Slack #erp-dev-deploys

    ENVIRONMENT: staging
      TRIGGER:   push to release/*
      STRATEGY:  Canary deployment (Argo Rollouts)
        STEP 1: deploy canary at 10% traffic
        STEP 2: wait 5min, monitor error_rate + latency
        STEP 3: IF metrics OK → promote to 25% → 50% → 100%
                IF metrics BAD → auto rollback in < 60s
      GATE: manual approval required (tech lead + QA)
      POST_GATE: run full integration test suite
      NOTIFY: Slack #erp-staging-deploys

    ENVIRONMENT: production
      TRIGGER:   merge to main (after staging approval)
      STRATEGY:  Blue/Green deployment
        PROVISION: green environment (new version, isolated)
        HEALTH:    run readiness checks on all green pods
        SMOKE:     run production smoke tests on green (via internal URL)
        SWITCH:    update LBaaS backend_set → green (atomic, < 5s)
        MONITOR:   15-minute burn-in period (auto-rollback threshold: error_rate > 1%)
        STABLE:    decommission blue after 30min
      GATES:
        - change_management ticket approved (ServiceNow)
        - deploy window: Mon-Thu 10:00-15:00 IST (no Friday deploys)
        - no open P1 incidents
      POST_DEPLOY:
        RUN production smoke tests
        UPDATE JIRA tickets as DEPLOYED
        POST release_notes → Confluence
        NOTIFY Slack #erp-prod-deploys + email stakeholders
        START 30min observation period alert

  INFRASTRUCTURE_AS_CODE (Terraform):
    STRUCTURE:
      /terraform
        /modules/
          oci-vcn, oci-oke, oci-atp, oci-adw, oci-lbaas
          oci-api-gateway, oci-streaming, oci-cache, oci-vault
          oci-wls, oci-ai-platform, oci-object-storage
        /environments/
          dev.tfvars, staging.tfvars, production.tfvars

    WORKFLOW:
      PR: terraform fmt -check && terraform validate && terraform plan → post plan as PR comment
      MERGE to main: terraform apply (dev auto, staging/prod require manual approval in OCI Resource Manager)
      STATE: stored in OCI Object Storage (locking via OCI Object Storage metadata)
      DRIFT: daily terraform plan; alert if diff detected

  SECRET_ROTATION (automated):
    DB_PASSWORD:           rotate every 90 days (OCI Vault + Kubernetes Secret auto-sync)
    ERP_FUSION_SECRET:     rotate every 30 days (manual coordination with ERP admin)
    JWT_KEY_PAIR:          rotate every 180 days (zero-downtime via kid in JWT header)
    TLS_CERTS:             auto-renew (cert-manager + OCI Certificates, 60d before expiry)
    REDIS_AUTH_TOKEN:      rotate every 90 days
    SHAREPOINT_SECRET:     rotate every 30 days


────────────────────────────────────────────────────────────────────────────
20. MONITORING & OBSERVABILITY
────────────────────────────────────────────────────────────────────────────

COMPONENT observability_stack:

  FRAMEWORK: OpenTelemetry (unified instrumentation across all services)

  ── METRICS (Prometheus + Grafana) ──────────────────────────────────────

  PROMETHEUS scrape targets (every 15s):
    - All Spring Boot pods:     /actuator/prometheus
      Metrics: http_requests_total, http_request_duration_seconds,
               erp_fusion_api_calls_total, erp_fusion_api_duration,
               cache_hits_total, cache_misses_total,
               kafka_producer_record_send_total, kafka_consumer_lag,
               jvm_memory_used_bytes, jvm_gc_pause_seconds,
               hikaricp_connections_active, hikaricp_connections_pending
    - Kong Gateway:             /metrics
    - Redis Exporter:           redis_connected_clients, redis_memory_used,
                                redis_cache_hit_ratio, redis_evicted_keys
    - Kafka Exporter:           kafka_consumergroup_lag, kafka_topic_throughput
    - OKE Node Exporter:        node_cpu, node_memory, node_disk_io
    - WebLogic Exporter:        wls_active_sessions, wls_heap_used,
                                wls_request_duration

  GRAFANA DASHBOARDS:
    1. ERP Integration Health:
       - ERP Fusion API call rate, error rate, latency p50/p95/p99
       - Circuit breaker state per ERP module (GL/AP/AR/Tax)
       - Cache hit rate per ERP data type
       - ERP API quota consumption

    2. Service Health Overview:
       - Golden signals per service: Latency, Traffic, Errors, Saturation
       - SLO/SLA compliance (99.9% availability target)

    3. Kafka Lag Dashboard:
       - Consumer group lag per topic/partition
       - Throughput (msgs/sec produce + consume)

    4. Business KPIs:
       - GL journal entries processed/hour
       - AP invoices fetched + created
       - AR receipts processed
       - Tax calculations/hour
       - AI agent queries/hour

    5. WebLogic Dashboard:
       - JVM heap, thread count, active sessions
       - BPEL process instances (active, completed, faulted)

    6. Infrastructure:
       - OKE node CPU/memory/disk
       - Pod restart count, OOMKill events

  ALERTING RULES (AlertManager → PagerDuty + Slack):
    P1 (page immediately):
      - ERP Fusion API circuit_breaker OPEN for > 2min
      - Service error_rate > 5% for 2min
      - DB connection pool saturation > 90%
      - Any pod restart > 3 in 5min (possible crash loop)
      - Kafka consumer lag > 50000 messages (stuck consumer)
      - LBaaS health check failing

    P2 (Slack alert, respond within 30min):
      - ERP Fusion API latency p99 > 30s
      - Cache hit rate < 50% for 10min
      - API Gateway error_rate > 1%
      - JWT validation failures spike (possible attack)
      - Kafka consumer lag > 10000 messages

    P3 (Slack alert, resolve within 4h):
      - Disk usage > 80%
      - WebLogic heap > 85%
      - Unused ERP API quota < 20% remaining

  ── LOGS (Loki + Fluent Bit + OCI Logging Analytics) ────────────────────

  LOG_FORMAT: Structured JSON (all services)
    {
      "@timestamp":  ISO8601,
      "level":       INFO|WARN|ERROR,
      "service":     "erp-integration-service",
      "version":     "2.1.4",
      "correlationId": "uuid",
      "userId":      "uuid",
      "tenantId":    "uuid",
      "message":     "...",
      "duration_ms": 245,
      "http_method": "GET",
      "http_path":   "/api/v1/erp/gl/journals",
      "http_status": 200,
      "erp_module":  "GL",          // for ERP calls
      "cache_hit":   false,         // for ERP calls
      "exception":   null,          // or { type, message, correlationId }
    }

  LOG_PIPELINE:
    Fluent Bit DaemonSet → collect from all OKE pod stdout/stderr
      → PARSE: structured JSON
      → ENRICH: add node_name, namespace, pod_name
      → ROUTE:
          level=ERROR → OCI Logging Analytics + Loki + Splunk (immediate)
          erp_module≠null → OCI Logging Analytics (ERP audit trail)
          DEFAULT → Loki (7-day retention) + OCI Logging Analytics (90-day)

  SECURITY_LOG_RULES (→ Splunk SIEM):
    - JWT validation failures (> 10/min per IP → potential attack)
    - WAF block events
    - 403 response spikes
    - ERP Fusion write-back failures (potential data integrity issue)
    - Admin console access events
    - Vault secret access events

  ── TRACES (Jaeger + OpenTelemetry) ─────────────────────────────────────

  OTEL_INSTRUMENTATION (auto via Java agent):
    - Inbound HTTP (Kong → Spring Boot)
    - Outbound HTTP (Spring Boot → ERP Fusion, SharePoint, AI Studio)
    - JDBC queries (SQL text + duration, sanitize bind params)
    - Redis operations (command + key prefix, NOT value)
    - Kafka produce/consume (with baggage propagation)
    - Inter-service calls

  TRACE_CONTEXT_PROPAGATION:
    PROTOCOL: W3C Trace Context (traceparent, tracestate)
    BAGGAGE:  X-Tenant-ID, X-Correlation-ID carried in all spans

  SAMPLING:
    head_based: 10%       (normal traffic)
    tail_based: 100%      (all traces containing errors)
    forced:     header "X-Force-Trace: true" → 100% (for debugging)

  JAEGER FEATURES:
    - Cross-service trace visualization
    - ERP Fusion API call span details (URL, status, duration)
    - Service dependency graph (auto-generated)
    - Latency histograms per operation

  ── SYNTHETIC MONITORING (OCI Synthetics) ────────────────────────────────

  MONITORS (every 1min from Mumbai + Hyderabad):
    - GET https://app.erp.company.com → expect 200, < 2s
    - GET https://api.erp.company.com/health → expect { status: UP }
    - GET https://api.erp.company.com/api/v1/erp/gl/periods (with canary token)
    - POST https://api.erp.company.com/api/v1/erp/tax/calculate (synthetic payload)
    IF any monitor fails:
      ALERT PagerDuty + Slack immediately
      TRIGGER incident_response runbook

  ── ERP FUSION SaaS MONITORING ───────────────────────────────────────────

  MONITORS:
    - Poll ERP Fusion /fscmRestApi/resources/.../health every 5min
    - Track ERP API quota: ALERT at 80% of daily limit
    - Monitor BPEL scheduled processes (payroll, GL posting batches)
    - Detect ERP Fusion maintenance windows (pre-announced → trigger circuit breaker early)

  FUNCTION erp_fusion_health_check():
    response = HTTP GET ERP_BASE + "/fscmRestApi/resources/11.13.22.12/fnd/health"
    IF response.status != 200 OR response.time > 30s:
      OPEN circuit_breaker (erp_integration_service)
      ENABLE fallback_mode:
        SERVE data from Redis cache (stale but available)
        SERVE data from ADW snapshot (last synced)
        ADD response header "X-Data-Source: FALLBACK"
      ALERT PagerDuty + Slack #erp-integration-alerts
    ELSE IF circuit_breaker == OPEN AND response.status == 200 for 3 consecutive:
      CLOSE circuit_breaker (half-open → healthy)
      NOTIFY recovery


────────────────────────────────────────────────────────────────────────────
21. SECURITY & SECRETS MANAGEMENT
────────────────────────────────────────────────────────────────────────────

COMPONENT security_framework:

  ZERO_TRUST PRINCIPLES:
    - Every service call authenticated (mTLS via Istio)
    - Every API call authorized (JWT + RBAC in Kong)
    - Principle of least privilege (minimal OCI IAM policies)
    - Assume breach: full audit trail, SIEM, anomaly detection

  OCI_VAULT:
    - All secrets stored in OCI Vault (no exceptions)
    - Vault Agent Injector (Kubernetes): injects secrets as env vars at pod startup
    - No secret ever touches disk, log, or code
    - Vault dynamic secrets for DB (auto-rotate credentials)

  OCI_IAM_POLICIES:
    erp-integration-service:
      Allow group erp-integration to use secret-family in vault erp-paas-vault
      Allow group erp-integration to use object-family in bucket erp-paas-erp-extracts
    erp-monitoring:
      Allow group erp-monitoring to read log-content in compartment erp-paas-prod
    erp-cicd:
      Allow group erp-cicd to manage repos in registry

  NETWORK_SECURITY:
    - OKE pods: NetworkPolicy (zero-trust, deny-all default, explicit allows)
    - Istio mTLS: STRICT mode in erp-services namespace
    - No pod has public IP (all behind LBaaS + API Gateway)
    - ERP Fusion API calls: NAT Gateway (outbound only, known IP for ERP allowlist)
    - Database: private endpoint only, no internet access

  COMPLIANCE:
    - SOC 2 Type II alignment
    - ISO 27001 controls mapping
    - Audit logs: immutable, 7-year retention (financial records)
    - Data encryption: AES-256 at rest, TLS 1.2+ in transit
    - PII masking in logs (user names, account numbers redacted)
    - GDPR: right to erasure supported via data classification tags


────────────────────────────────────────────────────────────────────────────
22. END-TO-END REQUEST FLOW
────────────────────────────────────────────────────────────────────────────

SCENARIO: Finance Manager queries GL Trial Balance via React dashboard

STEP 1  — Browser
  User opens https://app.erp.company.com/gl/trial-balance
  Browser checks local token store → access_token valid

STEP 2  — DNS
  app.erp.company.com resolves to LBaaS_public_IP
  OCI Traffic Management confirms primary region healthy

STEP 3  — WAF
  HTTPS request inspected: no SQL injection, XSS, rate limit OK
  X-Request-ID injected
  PASS → LBaaS

STEP 4  — LBaaS
  TLS terminated, HTTPS redirected if plain HTTP
  Security response headers added (HSTS, CSP, X-Frame-Options)
  Routed → Kong Gateway pod via ROUND_ROBIN

STEP 5  — Kong Gateway
  Plugin pipeline executes:
    jwt_plugin:             validates JWT (signature + expiry + revocation check in Redis)
    acl_plugin:             verifies FINANCE_READ role for /api/v1/erp/gl/* route
    rate_limiting_plugin:   increments Redis counter (within limits)
    request_transformer:    injects X-Tenant-ID, X-User-ID from JWT claims
    opentelemetry_plugin:   starts distributed trace span
  FORWARD → erp-integration-service:8090

STEP 6  — ERP Integration Service (Spring Boot)
  MDC populated: correlationId, userId, tenantId
  cache_key = "gl:trial_balance:{ledger_id}:{period}"
  Redis.get(cache_key) → CACHE MISS (first request of the day)

  ERP Fusion token fetched:
    Redis.get("erp:fusion:token") → MISS
    HTTP POST Oracle IDCS → access_token
    Redis.setex("erp:fusion:token", 3440, token)

  Circuit breaker: CLOSED (ERP Fusion healthy)
  HTTP POST ERP Fusion BIP REST API:
    URL: /xmlpserver/services/rest/v1/reports
    Auth: Bearer {erp_token}
    Body: { reportPath: TrialBalance.xdo, params: { ledger_id, period_name } }
    Latency: ~8 seconds (BIP report generation)

  Response received:
    parse_bip_xml_response(response) → domain_object
    redis.setex(cache_key, 600, domain_object)   // cache for 10min
    LOG: { level: INFO, message: "GL trial balance fetched from ERP",
           cache_hit: false, duration_ms: 8240, erp_module: GL }
  PUBLISH kafka_event("erp.gl.journals.fetched")
  RETURN trial_balance_data

STEP 7  — Response path
  erp-integration-service → Kong (response_transformer strips internal headers)
  Kong → LBaaS → Browser
  Total latency: ~8.5s (ERP call is bottleneck, acceptable for report generation)
  Response header: X-Correlation-ID (for support tracing)

STEP 8  — React
  RTK Query receives response
  Trial balance data rendered in AGGrid
  Cache-Control header (max-age=600) respected by browser cache

STEP 9  — Observability auto-captured:
  Prometheus: http_request_duration_seconds bucket updated
  Jaeger: full trace (Kong → Spring Boot → Redis miss → ERP Fusion BIP)
  Loki: structured JSON log with all context
  Grafana dashboard: ERP API call rate + latency updated in real time

STEP 10 — Same request 2 minutes later:
  Redis CACHE HIT → return in < 10ms (no ERP Fusion call)
  Response header: X-Data-Source: CACHE


# 23. COMPONENT MAP


```MAP

INTERNET
  └─► OCI DNS (erp.company.com) + Traffic Management (failover)
        └─► OCI WAF (OWASP, DDoS, rate-limit, SSRF protection)
              └─► OCI LBaaS (TLS termination, security headers, routing)
                    ├─► OCI API Gateway (Layer 1: edge auth, routing)
                    │     └─► Kong Gateway on OKE (Layer 2: plugins, RBAC, traces)
                    │           ├─► erp-integration-service (ERP SaaS hub)
                    │           │     ├─► OCI ERP Fusion (GL/AP/AR/Tax REST + BIP + SOAP)
                    │           │     ├─► Redis (cache-aside, tokens, locks)
                    │           │     └─► Kafka (event publish)
                    │           ├─► finance-orchestration-service
                    │           ├─► procurement-service
                    │           ├─► reporting-service
                    │           ├─► ai-agent-service ──► OCI Generative AI
                    │           ├─► sharepoint-proxy-service ──► Azure AD + MS Graph
                    │           └─► notification-service
                    │
                    └─► React Frontend (OKE pods / CDN)
                          └─► OAuth2 PKCE ──► OCI IDCS / Keycloak

OCI PaaS Data Layer:
  ├─ Oracle ATP (OLTP: procurement, audit, sharepoint map, notification log)
  ├─ Oracle ADW (analytics: Kafka-fed, materialized views, AI training)
  ├─ Redis Cluster (ERP data cache, tokens, rate-limit, distributed locks)
  └─ Kafka Cluster (event streaming, async decoupling, audit stream)

OCI ERP Fusion SaaS (Oracle-managed):
  ├─ GL Module (journals, balances, trial balance, BIP reports)
  ├─ AP Module (invoices, payments, suppliers)
  ├─ AR Module (invoices, receipts, customers, aging)
  ├─ Tax Module (rates, config, real-time calculation)
  └─ Business Events (webhooks → ERP event listener on WLS)

WebLogic (OCI WLS PaaS):
  ├─ BPEL Process Manager (3-way match workflow)
  ├─ Oracle Service Bus (JSON↔SOAP mediation)
  ├─ JCA ERP Adapter (legacy SOAP calls)
  └─ ERP Event Listener (receive ERP business event callbacks)

Azure (external):
  ├─ Azure Active Directory (OAuth2 for Graph API)
  └─ SharePoint Online (document libraries for ERP artifacts)

DevSecOps:
  ├─ GitHub Enterprise (VCS + Actions CI)
  ├─ Tekton (CI pipelines on OKE)
  ├─ ArgoCD (GitOps CD)
  ├─ SonarQube + Snyk + Semgrep + Trivy (security scanning)
  ├─ Terraform + OCI Resource Manager (IaC)
  └─ OCI Vault + cert-manager (secrets + TLS auto-rotation)

Observability:
  ├─ Prometheus (metrics scrape)
  ├─ Grafana (dashboards + alerting)
  ├─ AlertManager → PagerDuty + Slack
  ├─ Loki + Fluent Bit (log aggregation)
  ├─ Jaeger + OpenTelemetry (distributed tracing)
  ├─ OCI Logging Analytics (90-day log retention)
  ├─ OCI Synthetics (synthetic monitoring)
  └─ Splunk SIEM (security events, audit, compliance)

```

# END — PaaS ↔ OCI ERP Fusion SaaS Microservices Pseudocode Architecture
