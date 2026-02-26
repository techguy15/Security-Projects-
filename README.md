# Security-Projects-
Documented security projects and penetration testing projects
# Security Projects Portfolio

A collection of my security research, penetration testing, and vulnerability assessment projects.

## About Me
Cybersecurity student specializing in:
- Web Application Security
- Network Penetration Testing
- Embedded Systems & IoT Security
- Hardware Hacking

## Projects

### 1. SQL Injection - OWASP Juice Shop

**Objective:** Identify and exploit SQL injection vulnerabilities in a vulnerable web application

**Environment:**
- OWASP Juice Shop (Docker)
- Burp Suite Community Edition
- Kali Linux

**What I Did:**
1. Deployed Juice Shop in Docker container
2. Intercepted login request using Burp Suite
3. Tested for SQL injection vulnerability
4. Successfully bypassed authentication using payload: `' OR 1=1--`
5. Gained unauthorized admin access

**Vulnerability Details:**
- Type: SQL Injection
- Location: Login form
- Impact: Authentication bypass, unauthorized access to admin functionality
- OWASP Category: A03:2021 - Injection

**Key Takeaways:**
- Input validation is critical for security
- Parameterized queries prevent SQL injection
- Never trust user input directly in SQL queries

**Tools Used:** Docker, Burp Suite, OWASP Juice Shop

---

### 2. Cross-Site Scripting (XSS) - OWASP Juice Shop

**Objective:** Find and exploit XSS vulnerabilities

**What I Did:**
1. Identified input fields that display user content
2. Tested with basic XSS payload: `<script>alert('XSS')</script>`
3. Successfully triggered script execution
4. Demonstrated stored XSS vulnerability

**Impact:** 
- Can steal user session tokens
- Can redirect users to malicious sites
- Can modify page content

**Mitigation:**
- Input sanitization
- Output encoding
- Content Security Policy (CSP)

**Tools Used:** Burp Suite, Browser Developer Tools

---

### More Projects Coming Soon
- Metasploitable 2 Penetration Test
- ESP32 Security Research
- Man-in-the-Middle Attack Analysis
- IoT Device Security Assessment

## Skills & Tools
- **Penetration Testing:** Metasploit, Burp Suite, Bettercap
- **Web Security:** SQL Injection, XSS, CSRF, OWASP Top 10
- **Hardware:** ESP32, Arduino, Wireless Security
- **Programming:** Python, Bash
- **Operating Systems:** Kali Linux, Windows, Docker

## Learning Resources
Currently studying:
- Web Hacking 101 by Peter Yaworski
- Hands-on practice with TryHackMe and HackTheBox
- OWASP resources and documentation

---

*All security testing conducted in authorized lab environments for educational purposes.*
