# PHP2Shell (CVE-2026-109618 / CVE-2026-109619) — Lab, Scanner & Detection

Analysis, patch-verification tooling, and network detection rules for the
critical PHP engine RCE vulnerabilities disclosed October 21, 2026. Built
within days of public disclosure, from the official advisory and researcher
writeups — no walkthrough existed yet.

## What this is

Two critical vulnerabilities (CVSS 9.2) were found in the PHP engine itself
— not in any specific application — so WordPress, Drupal, Joomla, and
effectively any PHP-based site running an affected version is exposed
regardless of the app layer. This repo contains:

1. **A controlled lab** — vulnerable (8.3.35) and patched (8.3.36) PHP
   running side by side via Docker, to study and verify patch behavior.
2. **A patch-verification scanner** — Python tool that fingerprints a
   target's PHP version and flags exposure against the advisory's
   patched-version table.
3. **Detection rules** — Suricata and ModSecurity signatures built from
   the publicly described attack surface, to catch exploitation *attempts*
   in logs/traffic.

This project deliberately does **not** include exploit code. The goal is
understanding the bug class and building defensive tooling around it, not
weaponizing it.

## The vulnerability, briefly

Both CVEs are flaws in the PHP engine itself, not in any application. Both
allow unauthenticated remote code execution and are rated CVSS 9.2 by the
PHP project. They affect PHP serving web requests in general (PHP-FPM,
Apache mod_php, CGI, FrankenPHP, LiteSpeed), not just FPM.

- **CVE-2026-109618: memory-exhaustion corruption.** If memory runs out
  while a request is being set up, PHP can be interrupted with internal
  request data only partly initialised. Request cleanup then treats that
  invalid data as valid.
- **CVE-2026-109619: stale global state.** Request-owned data can stay
  referenced after its backing memory has been freed (use-after-free), and
  a later request handled by the same worker can use it before it is reset.
  The advisory highlights PHP's session upload progress feature, which is
  on by default, as a way to produce and consume this stale state. That is
  why the detection rules here look for `PHP_SESSION_UPLOAD_PROGRESS`.

Because both bugs live in the engine, patching application code (e.g.
WordPress plugins) does nothing — the fix has to be at the PHP version
level. Patched versions: **8.2.35 / 8.3.36 / 8.4.27 / 8.5.12**.

A separate, related session-upload-progress condition (CVE-2026-115560) was
covered in an informational advisory on October 23. This repo does not
cover it.

## Repo structure

```
docker-compose.yml       Vulnerable + patched PHP, each behind its own nginx
nginx/                   Separate configs per backend (vuln.conf / patched.conf)
www/                     Test app served to both backends
scanner/                 Python version-fingerprinting scanner
detection/               Suricata + ModSecurity rules
docs/                    Troubleshooting log (TROUBLESHOOTING.md)
```

## Running the lab

```bash
docker compose up -d
curl -s localhost:8081 | grep "PHP Version"   # vulnerable: 8.3.35
curl -s localhost:8082 | grep "PHP Version"   # patched:    8.3.36
```

## Running the scanner

```bash
pip install requests
python3 scanner/php2shell_scanner.py http://localhost:8081 http://localhost:8082
```

```
Scanning 2 target(s) for CVE-2026-109618 / CVE-2026-109619 exposure...

[VULNERABLE]   http://localhost:8081          PHP 8.3.35     Below patched version 8.3.36 for the 8.3 branch
[OK]           http://localhost:8082          PHP 8.3.36     Meets or exceeds the patched version for its branch

1 of 2 target(s) flagged vulnerable.
```

## Running the detection rules (Suricata)

```bash
docker run -d --name suricata-test \
  --cap-add net_admin --cap-add sys_nice \
  -v "$(pwd)/detection/php2shell_suricata.rules:/etc/suricata/rules/php2shell.rules:z" \
  --net=host \
  jasonish/suricata:latest \
  -i lo -S /etc/suricata/rules/php2shell.rules -l /var/log/suricata
```

Trigger a request matching the known attack surface and confirm detection:

```bash
curl -F "PHP_SESSION_UPLOAD_PROGRESS=test123" -F "file=@www/index.php" http://localhost:8081
docker exec suricata-test cat /var/log/suricata/fast.log
```

Confirmed firing:
```
[**] [1:9000001:1] PHP2Shell - PHP_SESSION_UPLOAD_PROGRESS field present in multipart upload [**]
[Classification: Web Application Attack] [Priority: 1] {TCP} ... -> ...:8081
```

## Limitations (stated honestly, not hidden)

- These rules detect *request shape* matching the publicly known attack
  surface, not confirmed exploitation. `PHP_SESSION_UPLOAD_PROGRESS` is a
  legitimate PHP feature — expect false positives on apps using real
  upload-progress bars. Tune against real traffic baselines before
  deploying.
- Only the Suricata rule has been tested (it fires on a test request, see
  `fast.log` above). The ModSecurity rules are included but untested.
- The ModSecurity oversized-body rule (`id:9000102`) blocks any multipart
  request over 1 MB, which will also block legitimate uploads. Tune the
  threshold to your application before enabling it in blocking mode.
- The precise memory-corruption trigger conditions are not publicly
  detailed at request-shape granularity, and this repo does not attempt
  to reconstruct them. Detection here works off what researchers
  responsibly disclosed as the attack surface — that's the honest ceiling
  of what this kind of project should produce.
- Patching PHP is the only complete fix. Detection rules are a
  stopgap/visibility layer for environments mid-patch-rollout, not a
  substitute.

## If you can't patch yet

PHP's advisory lists mitigations that reduce exposure but do not make an
installation safe. Check the advisory for the exact settings. In summary:

- **CVE-2026-109619:** disable session upload progress in a configuration
  applied before request parsing, then restart every PHP worker.
- **CVE-2026-109618:** tighten limits on request body size and complexity,
  and review the advisory's memory-limit guidance (set at a level
  applications can't override).

Patching remains the only complete fix.

## Troubleshooting log

See [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md) for the real
debugging trail — SELinux bind-mount permission issues (hit twice, in two
different containers), Suricata's single-line rule requirement, a
ModSecurity/Suricata syntax collision, and a `dsize` + `http_client_body`
incompatibility. Kept in because the debugging process is as much the
point of this repo as the final working state.

## Sources

- PHP Foundation security advisory and release announcement, October 21, 2026
- GitHub Security Advisories: GHSA-w8hw-w9fx-j79w (CVE-2026-109618) and GHSA-6wmf-4rv5-p3rp (CVE-2026-109619)
- NCSC-NL, "php2shell" operational information (affected products, detection, mitigations)
- Wiz / watchTowr technical writeups on PHP2Shell exploitation
