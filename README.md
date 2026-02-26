# Security Research Portfolio

Documentation of my penetration testing, vulnerability research, and security projects.

## About Me

Second year cybersecurity student specializing in web application security, network penetration testing, and embedded systems security. Hands-on practitioner focused on ethical hacking and vulnerability assessment.
## Completed Projects

### 🔴 Web Application Security - OWASP Juice Shop

**Objective:** Identify and exploit web vulnerabilities in controlled environment

**Environment:** Docker, OWASP Juice Shop, Burp Suite, Gobuster

**Vulnerabilities Exploited:**

**1. SQL Injection - Authentication Bypass**
- Intercepted login requests using Burp Suite
- Tested SQL injection payloads
- Successfully bypassed authentication: `' OR 1=1--`
- Gained unauthorized admin access
- **Impact:** Complete authentication bypass
- **OWASP:** A03:2021 - Injection

**2. Cross-Site Scripting (XSS)**
- Identified unsanitized input fields
- Injected payload: `<script>alert('XSS')</script>`
- Confirmed stored XSS vulnerability
- **Impact:** Session hijacking, credential theft potential
- **OWASP:** A03:2021 - Injection

**3. Directory Enumeration**
- Used Gobuster for directory discovery
- Found hidden admin panels and sensitive endpoints
- **Impact:** Information disclosure, unauthorized access points

**Key Takeaways:**
- Input validation is critical for security
- Parameterized queries prevent SQL injection
- Output encoding prevents XSS attacks
- Security through obscurity is not security
### 🔴 Man-in-the-Middle Attack Analysis - Bettercap

**Background:** Discovered this as an optional lab exercise at the end of my network security lab manual. Got curious and decided to explore it hands-on.

**Objective:** Understand network-layer attack vectors and ARP spoofing in controlled environment

**Environment:**
- Personal test network (isolated)
- Bettercap framework
- Kali Linux
- Target machines: Windows and Linux VMs

**What I Did:**

**1. Network Reconnaissance**
- Identified active hosts on network
- Mapped network topology
- Selected target for demonstration

**2. ARP Spoofing Attack**
- Positioned myself as man-in-the-middle between target and gateway
- Used Bettercap to poison ARP caches
- Successfully intercepted network traffic flow

**3. Traffic Analysis**
- Captured HTTP requests and responses
- Observed cleartext credential transmission
- Demonstrated vulnerability of unencrypted protocols
- Analyzed packet structure and data flow

**Attack Mechanics:**
- **Technique:** ARP cache poisoning
- **Tool:** Bettercap
- **Result:** Complete visibility into target's network communication

**Impact & Implications:**
- HTTP traffic completely visible
- Credentials transmitted in cleartext can be captured
- Users unaware of interception
- Demonstrates critical importance of encryption

**Defense Mechanisms Explored:**
- Static ARP entries
- ARP spoofing detection tools
- Network segmentation
- Mandatory HTTPS/TLS
- VPN usage for sensitive communications

**Key Learnings:**
- Network protocols operate on trust (ARP has no authentication)
- Encryption is essential, not optional
- Even "secure" networks can be compromised at layer 2
- Monitoring and detection are critical defensive layers
- Understanding attacks is key to building better defenses

**Why This Matters:**
This attack vector is still relevant today - coffee shop WiFi, corporate networks, IoT devices all vulnerable without proper security controls.

**Ethics:** All testing conducted on personal network infrastructure with full authorization. No unauthorized interception performed.

---
---
## Current Skills

**Penetration Testing:**
- Web application security testing
- Network exploitation
- System compromise and privilege escalation
- Wireless security assessment

**Tools & Frameworks:**
- Burp Suite, Metasploit Framework, Bettercap
- Docker, Kali Linux
- ESP32/Arduino for hardware security
- Python and Bash scripting

---

## Projects

### 🔴 SQL Injection - OWASP Juice Shop

**Environment:** Docker, OWASP Juice Shop, Burp Suite

**What I Did:**
1. Deployed Juice Shop application in isolated Docker environment
2. Used Burp Suite to intercept and analyze HTTP requests
3. Identified SQL injection vulnerability in login form
4. Crafted payload: `' OR 1=1--` to bypass authentication
5. Successfully gained unauthorized admin access

**Impact:** 
- Authentication bypass
- Unauthorized access to administrative functions
- Potential data exposure

**Mitigation:**
- Use parameterized queries/prepared statements
- Input validation and sanitization
- Principle of least privilege

**OWASP:** A03:2021 - Injection

---

### 🔴 Cross-Site Scripting (XSS) - OWASP Juice Shop

**Environment:** OWASP Juice Shop, Browser Developer Tools, Burp Suite

**What I Did:**
1. Identified user input fields that display content without proper sanitization
2. Tested basic XSS payload: `<script>alert('XSS')</script>`
3. Confirmed stored XSS vulnerability
4. Demonstrated script execution in victim's browser context

**Impact:**
- Session token theft
- Credential harvesting
- Page defacement
- Malicious redirects

**Mitigation:**
- Output encoding/escaping
- Content Security Policy (CSP)
- Input validation
- HttpOnly and Secure cookie flags

**OWASP:** A03:2021 - Injection

---

### 🔴 Directory Enumeration

**Tool Used:** Gobuster

**What I Did:**
- Performed directory and file enumeration on Juice Shop
- Discovered hidden endpoints and administrative panels
- Identified sensitive files and directories

**Key Learning:** 
- Importance of proper access controls
- Hidden doesn't mean secure
- Regular security audits catch these issues

---

## Coming Soon

Working on documenting these completed projects:

- **Metasploitable 2 Penetration Test** - Full assessment of vulnerable Linux system
- **Windows 7 Exploitation** - Metasploit Framework exploitation
- **Man-in-the-Middle Attack** - Bettercap ARP spoofing and traffic interception
- **ESP32 Marauder** - Wireless security research and WiFi penetration testing
- **IoT RC Car Security** - Embedded systems security assessment
- **Honeypot Deployment** - Cowrie & Dionaea implementation

---

## Learning Resources

**Currently Studying:**
- "Web Hacking 101" by Peter Yaworski
- OWASP documentation and guidelines
- TryHackMe and HackTheBox platforms
- Active participation in the cybersecurity community

---

## Ethics Statement

All security testing and research documented here was conducted in:
- Authorized laboratory environments
- Intentionally vulnerable applications designed for learning
- Controlled networks with proper permission
- Compliance with ethical hacking guidelines

No unauthorized testing or malicious activity has been performed.

---

**GPA:** 3.67 | **Status:** Actively seeking Summer 2026 cybersecurity internships

*Portfolio last updated: [2-26-2026]*
