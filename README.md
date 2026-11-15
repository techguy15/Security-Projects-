# Hi, I'm Hashir 👋

### Cybersecurity Student | Penetration Tester | Web, Network & IoT Security

📍 Rawalpindi/Islamabad, Pakistan
🎓 Seeking **[ Summer 2027]** cybersecurity internships

![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=flat&logo=kali-linux&logoColor=white)
![Burp Suite](https://img.shields.io/badge/Burp_Suite-FF6633?style=flat&logo=burpsuite&logoColor=white)
![Metasploit](https://img.shields.io/badge/Metasploit-000000?style=flat&logo=metasploit&logoColor=white)
![Nmap](https://img.shields.io/badge/Nmap-2B2D31?style=flat&logo=nmap&logoColor=white)
![Wireshark](https://img.shields.io/badge/Wireshark-1679A7?style=flat&logo=wireshark&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)

---

## About Me

Third-year cybersecurity student at CUST (CGPA 3.61) specializing in **web application security**, **network penetration testing**, and **embedded/IoT security**. I'm a hands-on practitioner: I build the lab, break it, document it, and then work out the defense.

I believe that understanding how attacks work is the foundation of building better defenses. All research documented here was conducted in authorized, controlled lab environments.

---

## 🏆 Achievements

- 🥉 **3rd Place, PKCERT CTF** ([2026]), hosted at CUST. Team of [3]. 
["I personally worked on network,web security,steganography"]

---

## Skills & Tools

**Penetration Testing:** Web App Security, Network Exploitation, Privilege Escalation, Wireless Security
**Network Security:** ARP/DNS spoofing, DoS and mitigation, DHCP attacks and detection, SDN (Mininet/Ryu), Wireshark analysis
**Environments:** Kali Linux, Docker, VMware, OWASP Juice Shop, DVWA, Metasploitable
**Hardware & IoT:** ESP32, embedded systems security, PlatformIO/Arduino

---

## Projects

### 🌐 Network Security

#### 🔴 Network Attacks & Defenses Lab — DoS, DNS, DHCP
**Tools:** Bettercap · Ettercap · Wireshark · hping3 · slowhttptest · dig · dnsmap · Scapy
**Environment:** Kali + Metasploitable2 on VMware, isolated lab

A set of Layer 2–7 attacks, each paired with a tested mitigation.

- **ARP spoofing + sniffing** with Bettercap, confirmed via duplicate ARP replies in Wireshark.
- **Slowloris, SYN flood, UDP flood:** analysed each in Wireshark. Mitigated Slowloris by cutting Apache's timeout from 300 s to 4 s (test ended in ~9 s) and SYN flood with TCP SYN cookies.
- **DNS spoofing** with Ettercap (on-path): redirected a test domain to an attacker-hosted page. Also traced resolution with `dig +trace`, enumerated subdomains with dnsmap, and validated DNSSEC (`ad` flag, RRSIG).
- **DHCP starvation:** captured the DISCOVER flood and ran a detector that alerted on 250–270 unique MACs per 10 s window (baseline ≈ 1).
- **Key Takeaway:** ARP, DNS and DHCP have no built-in authentication. DAI, DNSSEC and DHCP snooping fill that gap.



#### 🔵 Smart Campus SDN Network Redesign — Mininet + Ryu
**Tools:** Mininet · Ryu (OpenFlow 1.3)
**Context:** CY3711 Complex Computing Problem, CUST

- Three-tier topology with five VLANs (10–50) and proxy ARP.
- SDN-based loop prevention that bypasses STP.
- ACL blocking the Student VLAN from the Admin VLAN.
- Resolved STP/OpenFlow conflicts by installing static flows on switch_features events.
- **Key Takeaway:** Segmentation policy can be enforced in the controller, not just on each device.



#### 🔴 Man-in-the-Middle Attack Analysis — Bettercap
**Tools:** Bettercap · Kali Linux · Wireshark
**Environment:** Isolated personal test network (Windows + Linux VMs)

Conducted ARP cache poisoning to position as a man-in-the-middle between target VMs and the gateway, demonstrating the full attack chain.

- Executed ARP spoofing with Bettercap to intercept traffic flow.
- Captured cleartext HTTP credentials to demonstrate the risk of unencrypted protocols.
- **Key Takeaway:** Layer 2 trust assumptions remain a relevant threat vector in corporate and IoT environments. Encryption and network monitoring are non-negotiable controls.

#### 🔴 Metasploitable 2 — Full Penetration Test
**Tools:** Metasploit Framework · Kali Linux · VMware

Conducted a full penetration test against Metasploitable 2, simulating a real-world black-box assessment.

- Performed host discovery and service enumeration to map the attack surface.
- Gained initial foothold via remote exploits and established reverse shell sessions.
- **Key Takeaway:** Unpatched services and default configurations are highly dangerous. Patch management and service hardening are critical first lines of defense.

#### 🔴 Windows 7 Exploitation — EternalBlue
**Tools:** Metasploit Framework · Kali Linux · VMware

Exploited a Windows 7 VM using EternalBlue (MS17-010) in a fully isolated lab environment.

- Scanned target and confirmed SMB vulnerability using Metasploit auxiliary modules.
- Executed the exploit to gain remote code execution without credentials, establishing a Meterpreter reverse shell.
- **Key Takeaway:** EternalBlue remains a critical case study in patch urgency. Legacy systems require strict network segmentation and timely patching.

### 🔴 Web Application Security

#### OWASP Juice Shop
**Tools:** Burp Suite (Proxy, Repeater, Decoder) · Gobuster · Docker · Chromium

Conducted an advanced, manual vulnerability assessment against a modern Node.js/Express/Angular Single Page Application (SPA), successfully exploiting multiple OWASP Top 10 vulnerabilities.

- **[A01:2021] Broken Access Control (IDOR):** Intercepted and manipulated REST API requests in Burp Suite Repeater to bypass authorization checks and access unauthorized database objects (Cart ID manipulation).
- **[A02:2021] Cryptographic Failures:** Identified weak data obfuscation in frontend JavaScript. Extracted and decoded Base64 strings using Burp Decoder to uncover hidden application routes.
- **[A03:2021] Injection (SQLi):** Executed SQL injection payloads (`' OR 1=1 --`) against the authentication mechanism to successfully bypass login controls and hijack administrative access.
- **[A04:2021] Insecure Design (Business Logic Bypass):** Intercepted outbound `POST` requests and manipulated JSON payloads in transit to bypass frontend UI validation constraints (e.g., submitting 0-star ratings).
- **[A05:2021] Security Misconfiguration:** Utilized `gobuster` for aggressive directory enumeration to uncover exposed internal business directories (`/ftp`) and sensitive configuration documents.

#### File Upload to RCE — php2shell-lab
**Tools:** PHP · [add tools used]

[Add 2–3 bullets: the vulnerable setup, how the upload filter was bypassed, what access you got.]

- **Key Takeaway:** [your lesson, e.g. validate file type server-side and store uploads outside the web root]

📁 [php2shell-lab](./php2shell-lab)

### 🔌 Hardware & IoT Security

#### ESP32 Marauder — Wireless Security Research
**Tools:** ESP32 · ESP32 Marauder firmware · Arduino IDE

Built a portable wireless security research tool to explore the offensive and defensive dimensions of WiFi and Bluetooth.

- Performed passive WiFi scanning to capture SSIDs, BSSIDs, and channel data.
- Demonstrated deauthentication capabilities against test networks to illustrate WiFi disruption risks.
- **Key Takeaway:** Low-cost hardware can be a powerful wireless auditing tool. Organizations must monitor for rogue devices and use WPA3.

#### ESP32 WIDS — Wireless Intrusion Detection
**Tools:** ESP32 · SSD1306 OLED · Arduino

- Monitors WiFi traffic in promiscuous mode with ISR-safe interrupt handling.
- Live status shown on an OLED display.
- [Add: what it detects (e.g. deauth frames) and a photo or screenshot.]

#### ESP32 DNS Ad Blocker — Bloom Filter Blocklist
**Tools:** ESP32 · PlatformIO · LittleFS · Python

DNS forwarder running on a plain ESP32 that returns 0.0.0.0 for blocked domains and forwards everything else.

- A Python script builds a Bloom filter blocklist (~466k domains, ~900 KB, ~0.05% false-positive rate) stored in flash, with no SD card needed.
- Lookups take ~8–14 ms for clean domains and ~50 ms for blocked ones.
- Tested on a real iPhone with manual DNS pointed at the board.
- **Known issue:** the brownout detector triggers at WiFi start on this board (power-related).
- **Key Takeaway:** Probabilistic data structures make network-level filtering possible on very constrained hardware.

#### IoT RC Car — Embedded Systems Security Assessment
**Tools:** ESP32 · L298N Motor Driver · Arduino IDE · Custom firmware

Built and assessed the security of a custom IoT-controlled RC car, evaluating the attack surface in a real embedded system.

- Analyzed the communication layer for potential interception or replay attack vectors.
- Assessed firmware for hardcoded credentials and insecure configurations.
- **Key Takeaway:** Simple embedded systems often prioritize functionality over security, exposing significant attack surfaces through unencrypted communications.

---

## 🚧 In Progress & Upcoming

| Project | Description |
|---|---|
| **RF Fingerprinting** | Identifying individual radios from raw I/Q captures using ESP-SDR on ESP32-S3 |
| **WiFi Attack Detection** | Detecting deauth / BLE jamming against a selected target and pinpointing the attacker (ESP32-S3) |
| **WiFi CSI Sensing** | CSI-based gait/motion detection on ESP32 |
| **Air-Gapped Bare-Metal Pentest Lab** | Architecting an isolated, physical LAN using salvaged PC hardware (headless Linux hypervisor) and a dedicated physical router to practice Layer 2/3 network attacks, traffic analysis, and deploy custom Wi-Fi penetration tools. |
| **Honeypot Deployment** | Cowrie & Dionaea implementation to monitor real-world attack patterns. |


---

## ⚖️ Ethics & Methodology

All security testing documented in this portfolio was performed strictly in:

- ✔️ Authorized laboratory environments
- ✔️ Intentionally vulnerable applications built for learning
- ✔️ Controlled, isolated networks I own and operate

*No unauthorized testing has been conducted.*

---

## Let's Connect

Feel free to reach out if you'd like to discuss my projects, cybersecurity trends, or internship opportunities!

- **LinkedIn:** [Hashir Atiq Hashmi](https://www.linkedin.com/in/hashir-atiq-hashmi-5a96061ab/)
- **Email:** [hashirateeq2005@gmail.com](mailto:hashirateeq2005@gmail.com)
