# Hi, I'm Hashir 👋
### Cybersecurity Student | Penetration Tester | Web & Network Security

📍 Rawalpindi/Islamabad, Pakistan  
🎓 **Actively seeking Summer 2026 Cybersecurity Internships**


*Tools of the Trade:* ![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=flat&logo=kali-linux&logoColor=white) 
![Burp Suite](https://img.shields.io/badge/Burp_Suite-FF6633?style=flat&logo=burpsuite&logoColor=white) 
![Metasploit](https://img.shields.io/badge/Metasploit-000000?style=flat&logo=metasploit&logoColor=white) 
![Nmap](https://img.shields.io/badge/Nmap-2B2D31?style=flat&logo=nmap&logoColor=white) 
![Bettercap](https://img.shields.io/badge/Bettercap-FFFFFF?style=flat&logoColor=black) 
![Gobuster](https://img.shields.io/badge/Gobuster-FFB534?style=flat&logoColor=black) 
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) 
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
---

## About Me

Second-year cybersecurity student specializing in **web application security**, **network penetration testing**, and **embedded systems security**. I am a hands-on practitioner focused on ethical hacking and vulnerability assessment with a 3.67 GPA.

I believe that understanding how attacks work is the foundation of building better defenses. All research documented here was conducted in authorized, controlled lab environments.

---

## Skills & Tools

**Penetration Testing:** Web App Security, Network Exploitation, Privilege Escalation, Wireless Security  
**Environments:** Kali Linux, Docker, OWASP Juice Shop, Metasploitable  
**Hardware & IoT:** ESP32, Embedded Systems Security  

*Tools of the Trade:* ![Burp Suite](https://img.shields.io/badge/Burp_Suite-FF6633?style=flat&logo=burpsuite&logoColor=white) ![Metasploit](https://img.shields.io/badge/Metasploit-000000?style=flat&logo=metasploit&logoColor=white) ![Nmap](https://img.shields.io/badge/Nmap-2B2D31?style=flat&logo=nmap&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white) 

---

## Projects

### 🔴 Web Application Security — OWASP Juice Shop
**Tools:** Docker · Burp Suite · Gobuster

Performed a full vulnerability assessment against OWASP Juice Shop in an isolated Docker environment, identifying and exploiting multiple critical vulnerabilities.

* **SQL Injection:** Intercepted login requests with Burp Suite and crafted a payload to bypass authentication entirely, gaining unauthorized admin access. Demonstrated how parameterized queries eliminate this risk.
* **Stored XSS:** Identified unsanitized input fields and injected a persistent script payload, confirming session hijacking and credential theft potential. Remediated via output encoding and Content Security Policy.
* **Directory Enumeration:** Used Gobuster to surface hidden admin panels and sensitive endpoints, illustrating that security through obscurity is not a valid control.

### 🔴 Man-in-the-Middle Attack Analysis — Bettercap
**Tools:** Bettercap · Kali Linux · Wireshark  
**Environment:** Isolated personal test network (Windows + Linux VMs)

Conducted ARP cache poisoning to position as a man-in-the-middle between target VMs and the gateway, demonstrating the full attack chain.

* Executed ARP spoofing with Bettercap to intercept traffic flow.
* Captured cleartext HTTP credentials to demonstrate the risk of unencrypted protocols.
* **Key Takeaway:** Layer 2 trust assumptions remain a relevant threat vector in corporate and IoT environments. Encryption and network monitoring are non-negotiable controls.

### 🔴 Metasploitable 2 — Full Penetration Test
**Tools:** Metasploit Framework · Kali Linux · VMware

Conducted a full penetration test against Metasploitable 2, simulating a real-world black-box assessment.

* Performed host discovery and service enumeration to map the attack surface.
* Gained initial foothold via remote exploits and established reverse shell sessions.
* **Key Takeaway:** Unpatched services and default configurations are highly dangerous. Patch management and service hardening are critical first lines of defense.

### 🔴 Windows 7 Exploitation — EternalBlue
**Tools:** Metasploit Framework · Kali Linux · VMware

Exploited a Windows 7 VM using EternalBlue (MS17-010) in a fully isolated lab environment.

* Scanned target and confirmed SMB vulnerability using Metasploit auxiliary modules.
* Executed the exploit to gain remote code execution without credentials, establishing a Meterpreter reverse shell.
* **Key Takeaway:** EternalBlue remains a critical case study in patch urgency. Legacy systems require strict network segmentation and timely patching.

### 🔴 ESP32 Marauder — Wireless Security Research
**Tools:** ESP32 · ESP32 Marauder firmware · Arduino IDE

Built a portable wireless security research tool to explore the offensive and defensive dimensions of WiFi and Bluetooth.

* Performed passive WiFi scanning to capture SSIDs, BSSIDs, and channel data.
* Demonstrated deauthentication capabilities against test networks to illustrate WiFi disruption risks.
* **Key Takeaway:** Low-cost hardware can be a powerful wireless auditing tool. Organizations must monitor for rogue devices and utilize WPA3.

### 🔴 IoT RC Car — Embedded Systems Security Assessment
**Tools:** ESP32 · L298N Motor Driver · Arduino IDE · Custom firmware

Built and assessed the security of a custom IoT-controlled RC car, evaluating the attack surface in a real embedded system.

* Analyzed the communication layer for potential interception or replay attack vectors.
* Assessed firmware for hardcoded credentials and insecure configurations.
* **Key Takeaway:** Simple embedded systems often prioritize functionality over security, exposing significant attack surfaces through unencrypted communications.

---

## 🚧 Coming Soon

| Project | Description |
|---|---|
| **Honeypot Deployment** | Cowrie & Dionaea implementation to monitor real-world attack patterns. |
| **ESP32 Drone Security** | Building and auditing a custom drone over the summer to assess aerial IoT vulnerabilities and radio communication security. |

---

## ⚖️ Ethics & Methodology

All security testing documented in this portfolio was performed strictly in:
* ✔️ Authorized laboratory environments
* ✔️ Intentionally vulnerable applications built for learning
* ✔️ Controlled, isolated networks I own and operate

*No unauthorized testing has been conducted.*

---

## Let's Connect
Feel free to reach out if you'd like to discuss my projects, cybersecurity trends, or Summer 2026 internship opportunities!

* **LinkedIn:** [Hashir Atiq Hashmi](https://www.linkedin.com/in/hashir-atiq-hashmi-5a96061ab/)
* **Email:** [hashirateeq2005@gmail.com](mailto:hashirateeq2005@gmail.com)
