
# JWT (JSON Web Token) – Complete Interview Cheat Sheet

JWT (JSON Web Token) is a compact, secure, stateless token standard used for authentication and authorization in web applications, APIs, microservices, cloud-native systems, and distributed architectures.

JWT allows users to securely access APIs without storing session data on the server.

---

# JWT Architecture Flow

```text id="a4v8q2"
User Login
    ↓
Authentication Server
    ↓
JWT Token Generated
    ↓
Client Stores Token
    ↓
Client Sends Token in API Request
    ↓
API Gateway / Spring Security Validates JWT
    ↓
Access Granted to Microservice
```

---

# JWT Structure

JWT contains 3 parts separated by dots:

```text id="o4k1uv"
Header.Payload.Signature
```

Example:

```text id="h9lz8x"
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

---

# JWT Components

| Component | Purpose                                      |
| --------- | -------------------------------------------- |
| Header    | Contains token type and encryption algorithm |
| Payload   | Contains user data/claims                    |
| Signature | Verifies token integrity and authenticity    |

---

# JWT Payload (Claims)

| Claim | Meaning           |
| ----- | ----------------- |
| sub   | User ID/subject   |
| role  | User role         |
| exp   | Expiration time   |
| iss   | Token issuer      |
| aud   | Intended audience |
| iat   | Issued time       |

---

# JWT Authentication Flow in Microservices

```text id="g3m8yf"
Frontend / Mobile App
          ↓
Login API
          ↓
Authentication Service
          ↓
JWT Token
          ↓
API Gateway
          ↓
Microservices
          ↓
Database
```

---

# JWT with Spring Boot Components

| Component          | Purpose                        |
| ------------------ | ------------------------------ |
| Spring Security    | Authentication & authorization |
| JWT Library        | Token generation/validation    |
| REST Controller    | Login APIs                     |
| User Service       | User validation                |
| Filter/Interceptor | Validate JWT on every request  |
| API Gateway        | Centralized token validation   |

---

# Java JWT Example

## Generate JWT

```java id="epzrvr"
String token = Jwts.builder()
   .setSubject("rahul")
   .claim("role", "ADMIN")
   .setExpiration(new Date(System.currentTimeMillis()+3600000))
   .signWith(SignatureAlgorithm.HS256, secretKey)
   .compact();
```

---

## Validate JWT

```java id="l37lpa"
Claims claims = Jwts.parser()
   .setSigningKey(secretKey)
   .parseClaimsJws(token)
   .getBody();
```

---

# JWT Security Components

| Security Area     | Implementation  |
| ----------------- | --------------- |
| Authentication    | OAuth2 + JWT    |
| Authorization     | RBAC/roles      |
| Encryption        | HTTPS/TLS       |
| Secret Management | Vault/KMS       |
| Token Expiration  | exp claim       |
| Refresh Token     | Token renewal   |
| API Protection    | API Gateway/WAF |

---

# JWT Tools & Technologies

| Category         | Tools                        |
| ---------------- | ---------------------------- |
| Java Framework   | Spring Boot                  |
| Security         | Spring Security              |
| JWT Libraries    | jjwt, Nimbus JOSE            |
| API Testing      | Postman                      |
| API Gateway      | Kong, NGINX, OCI API Gateway |
| Monitoring       | Prometheus, Grafana          |
| Logging          | ELK Stack                    |
| Containerization | Docker                       |
| Orchestration    | Kubernetes                   |

---

# JWT with Cloud Platforms

| Area         | OCI             | AWS             | Azure          | GCP              |
| ------------ | --------------- | --------------- | -------------- | ---------------- |
| Identity     | OCI IAM         | AWS IAM/Cognito | Azure AD       | Cloud IAM        |
| Secrets      | OCI Vault       | Secrets Manager | Key Vault      | Secret Manager   |
| API Security | OCI API Gateway | API Gateway     | API Management | API Gateway      |
| Monitoring   | OCI Monitoring  | CloudWatch      | Azure Monitor  | Cloud Monitoring |

---

# JWT Scalability Design

| Area                     | Solution                |
| ------------------------ | ----------------------- |
| Stateless Authentication | No session storage      |
| Horizontal Scaling       | Kubernetes scaling      |
| Load Balancing           | API Gateway/LB          |
| Distributed Systems      | Shared token validation |
| Caching                  | Redis token cache       |

---

# JWT Monitoring & Observability

| Monitoring Area     | Tools            |
| ------------------- | ---------------- |
| API Metrics         | Prometheus       |
| Dashboard           | Grafana          |
| Log Analysis        | ELK / Splunk     |
| Distributed Tracing | Jaeger / OCI APM |
| Security Alerts     | SIEM tools       |

---

# JWT Use Cases

| Use Case             | Example                     |
| -------------------- | --------------------------- |
| Single Sign-On (SSO) | Enterprise login            |
| API Security         | Secure REST APIs            |
| Microservices        | Service authentication      |
| Mobile Apps          | Token-based login           |
| Banking Systems      | Secure transactions         |
| E-Commerce           | User session management     |
| SaaS Platforms       | Multi-tenant authentication |

---

# Real-Time Enterprise Use Case

## Banking Application

```text id="5z0mte"
Customer Login
      ↓
Authentication Service
      ↓
JWT Generated
      ↓
API Gateway Validates JWT
      ↓
Transaction Service
      ↓
Fraud Detection Service
```

### Features

* Secure stateless login
* Role-based authorization
* Microservices communication
* Kubernetes deployment
* Centralized monitoring

---

# Advantages of JWT

| Benefit               | Description             |
| --------------------- | ----------------------- |
| Stateless             | No server-side session  |
| Scalable              | Easy cloud scaling      |
| Secure                | Digitally signed tokens |
| Lightweight           | Compact format          |
| Cross-Platform        | Works across systems    |
| Faster Authentication | Reduced DB lookups      |

---

# JWT Challenges

| Challenge        | Solution                 |
| ---------------- | ------------------------ |
| Token Theft      | HTTPS + short expiry     |
| Secret Leakage   | Vault/KMS                |
| Token Revocation | Blacklist/refresh tokens |
| Large Payload    | Keep claims minimal      |

---

# JWT vs Session Authentication

| JWT                      | Session-Based              |
| ------------------------ | -------------------------- |
| Stateless                | Stateful                   |
| Better for microservices | Better for monolith        |
| Easy scaling             | Session replication needed |
| Stored client-side       | Stored server-side         |

---

# Interview Answer (2–3 Lines)

“JWT is a stateless authentication mechanism used to securely authorize users and APIs using digitally signed tokens. In Java Spring Boot microservices, I implement JWT with Spring Security, API Gateway, OAuth2, Kubernetes, OCI/AWS cloud services, and monitoring tools like Prometheus and Grafana for scalable and secure enterprise applications.”

===============

# JWT Supporting Code Snippets (Java Spring Boot)

---

# 1. Maven Dependencies

```xml id="z5n1xq"
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt</artifactId>
    <version>0.9.1</version>
</dependency>

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

---

# 2. JWT Utility Class

## Generate & Validate JWT Token

```java id="ggpd1w"
@Component
public class JwtUtil {

    private String SECRET_KEY = "mysecretkey";

    // Generate Token
    public String generateToken(String username) {

        return Jwts.builder()
                .setSubject(username)
                .claim("role", "ADMIN")
                .setIssuedAt(new Date())
                .setExpiration(
                   new Date(System.currentTimeMillis() + 3600000)
                )
                .signWith(SignatureAlgorithm.HS256, SECRET_KEY)
                .compact();
    }

    // Extract Username
    public String extractUsername(String token) {

        return Jwts.parser()
                .setSigningKey(SECRET_KEY)
                .parseClaimsJws(token)
                .getBody()
                .getSubject();
    }

    // Validate Token
    public boolean validateToken(String token, String username) {

        String extractedUser = extractUsername(token);

        return extractedUser.equals(username);
    }
}
```

---

# 3. Authentication Controller

## Login API

```java id="q0m0e8"
@RestController
@RequestMapping("/auth")
public class AuthController {

    @Autowired
    private JwtUtil jwtUtil;

    @PostMapping("/login")
    public String login(@RequestParam String username,
                        @RequestParam String password) {

        // Dummy validation
        if(username.equals("admin")
            && password.equals("admin123")) {

            return jwtUtil.generateToken(username);
        }

        return "Invalid Credentials";
    }
}
```

---

# 4. JWT Filter

## Validate JWT on Every Request

```java id="9q2nx6"
@Component
public class JwtFilter extends OncePerRequestFilter {

    @Autowired
    private JwtUtil jwtUtil;

    @Override
    protected void doFilterInternal(HttpServletRequest request,
                                    HttpServletResponse response,
                                    FilterChain filterChain)
                                    throws ServletException, IOException {

        String authHeader = request.getHeader("Authorization");

        if(authHeader != null && authHeader.startsWith("Bearer ")) {

            String token = authHeader.substring(7);

            String username = jwtUtil.extractUsername(token);

            System.out.println("Authenticated User: " + username);
        }

        filterChain.doFilter(request, response);
    }
}
```

---

# 5. Spring Security Configuration

```java id="tclo5n"
@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Autowired
    private JwtFilter jwtFilter;

    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http)
            throws Exception {

        http.csrf().disable()
            .authorizeHttpRequests()
            .requestMatchers("/auth/login").permitAll()
            .anyRequest().authenticated();

        http.addFilterBefore(
            jwtFilter,
            UsernamePasswordAuthenticationFilter.class
        );

        return http.build();
    }
}
```

---

# 6. Secure REST API

```java id="zq28j4"
@RestController
@RequestMapping("/api")
public class UserController {

    @GetMapping("/users")
    public String getUsers() {

        return "Secure User Data";
    }
}
```

---

# 7. Sample API Request

## Login Request

```http id="jjk3lu"
POST /auth/login

username=admin
password=admin123
```

---

## JWT Response

```text id="9jhh9h"
eyJhbGciOiJIUzI1NiJ9...
```

---

## Access Secure API

```http id="g9uxqn"
GET /api/users

Authorization: Bearer eyJhbGciOiJIUzI1NiJ9...
```

---

# 8. JWT with API Gateway Architecture

```text id="klv8ob"
Frontend / Mobile App
          ↓
API Gateway
          ↓
JWT Validation
          ↓
Spring Boot Microservices
          ↓
Oracle DB / Redis / Kafka
```

---

# 9. Kubernetes Deployment YAML

```yaml id="q3r0gv"
apiVersion: apps/v1
kind: Deployment
metadata:
  name: jwt-service

spec:
  replicas: 3

  selector:
    matchLabels:
      app: jwt-service

  template:
    metadata:
      labels:
        app: jwt-service

    spec:
      containers:
      - name: jwt-container
        image: jwt-app:latest

        ports:
        - containerPort: 8080
```

---

# 10. Dockerfile

```dockerfile id="q0zljx"
FROM openjdk:17

COPY target/jwt-app.jar jwt-app.jar

ENTRYPOINT ["java","-jar","/jwt-app.jar"]
```

---

# 11. Prometheus Monitoring Example

```yaml id="6xv79v"
scrape_configs:
  - job_name: 'spring-boot-app'

    static_configs:
      - targets: ['localhost:8080']
```

---

# 12. OCI / AWS / Azure Components

| Area           | Services                                                          |
| -------------- | ----------------------------------------------------------------- |
| Cloud Platform | Oracle Cloud Infrastructure, Amazon Web Services, Microsoft Azure |
| API Gateway    | OCI API Gateway, AWS API Gateway                                  |
| Secrets        | OCI Vault, AWS Secrets Manager                                    |
| Kubernetes     | OKE, EKS, AKS                                                     |
| Monitoring     | OCI Monitoring, CloudWatch, Azure Monitor                         |

---

# 13. Real-Time Enterprise Use Case

## Banking Transaction Service

```text id="bzw9kk"
User Login
    ↓
JWT Token Generated
    ↓
API Gateway Validates JWT
    ↓
Transaction Microservice
    ↓
Kafka Notification Service
    ↓
Monitoring & Logging
```

---

# 14. Interview Summary (2–3 Lines)

“I implement JWT authentication in Java Spring Boot using Spring Security, JWT filters, and API Gateway for stateless authentication and authorization. The application is containerized using Docker, deployed on Kubernetes/OKE, integrated with OCI/AWS cloud services, and monitored using Prometheus, Grafana, and centralized logging solutions.”
