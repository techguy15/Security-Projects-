# Security Research Portfolio

Documentation of my penetration testing, vulnerability research, and security projects.

## About Me

Third-year cybersecurity student specializing in web application security, network penetration testing, and embedded systems security. Hands-on practitioner focused on ethical hacking and vulnerability assessment.

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
