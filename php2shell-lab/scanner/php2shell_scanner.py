#!/usr/bin/env python3
"""
php2shell_scanner.py

Patch-verification scanner for CVE-2026-109618 / CVE-2026-109619 ("PHP2Shell").
Fingerprints the PHP version a target server is running and flags whether
it falls inside the vulnerable range, based on the PHP Foundation's
October 21, 2026 security advisory.

This tool does NOT exploit anything. It identifies version exposure only,
the same way a vulnerability scanner or asset-inventory tool would.

Usage:
    python3 php2shell_scanner.py http://localhost:8081
    python3 php2shell_scanner.py http://localhost:8081 http://localhost:8082
    python3 php2shell_scanner.py --list targets.txt
"""

import argparse
import re
import sys
from dataclasses import dataclass

import requests

# Minimum PATCHED version per branch, per the PHP Foundation advisory.
# Anything strictly below the patched version on a given branch is vulnerable.
PATCHED_VERSIONS = {
    (8, 5): (8, 5, 12),
    (8, 4): (8, 4, 27),
    (8, 3): (8, 3, 36),
    (8, 2): (8, 2, 35),
}

VERSION_RE = re.compile(r"(\d+)\.(\d+)\.(\d+)")


@dataclass
class ScanResult:
    target: str
    version: str | None
    status: str  # "vulnerable" | "patched" | "unsupported" | "unknown"
    detail: str


def parse_version(raw: str) -> tuple[int, int, int] | None:
    m = VERSION_RE.search(raw)
    if not m:
        return None
    return tuple(int(g) for g in m.groups())  # type: ignore


def fingerprint(target: str, timeout: float = 5.0) -> str | None:
    """
    Try to extract a PHP version string from a target.
    Checks, in order:
      1. X-Powered-By response header (most common, if not stripped)
      2. A phpinfo()-style HTML body (fallback for lab/dev targets)
    """
    try:
        resp = requests.get(target, timeout=timeout)
    except requests.RequestException as exc:
        print(f"[!] Could not reach {target}: {exc}", file=sys.stderr)
        return None

    header = resp.headers.get("X-Powered-By", "")
    if "PHP" in header:
        v = parse_version(header)
        if v:
            return ".".join(map(str, v))

    # Fallback: look for phpinfo()-style "PHP Version X.Y.Z" in the body.
    # Real-world targets rarely expose this -- it's here for lab/dev use
    # where X-Powered-By may be suppressed but phpinfo() is still reachable.
    body_match = re.search(r"PHP Version\s*</td><td[^>]*>\s*([\d.]+)", resp.text)
    if not body_match:
        body_match = re.search(r"PHP Version\s+([\d.]+)", resp.text)
    if body_match:
        return body_match.group(1)

    return None


def classify(version_str: str) -> tuple[str, str]:
    v = parse_version(version_str)
    if not v:
        return "unknown", "Could not parse version string"

    branch = (v[0], v[1])
    if branch not in PATCHED_VERSIONS:
        return "unsupported", f"PHP {v[0]}.{v[1]} is not in the tracked branch list (likely EOL or unreleased)"

    patched = PATCHED_VERSIONS[branch]
    if v < patched:
        patched_str = ".".join(map(str, patched))
        return "vulnerable", f"Below patched version {patched_str} for the {branch[0]}.{branch[1]} branch"
    return "patched", "Meets or exceeds the patched version for its branch"


def scan(target: str) -> ScanResult:
    version = fingerprint(target)
    if not version:
        return ScanResult(target, None, "unknown", "No PHP version could be fingerprinted")
    status, detail = classify(version)
    return ScanResult(target, version, status, detail)


def print_result(r: ScanResult) -> None:
    icon = {
        "vulnerable": "[VULNERABLE]",
        "patched": "[OK]",
        "unsupported": "[?]",
        "unknown": "[?]",
    }[r.status]
    ver = r.version or "unknown"
    print(f"{icon:14} {r.target:30} PHP {ver:10} {r.detail}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("targets", nargs="*", help="One or more target URLs")
    parser.add_argument("--list", help="File with one target URL per line")
    args = parser.parse_args()

    targets = list(args.targets)
    if args.list:
        with open(args.list) as f:
            targets += [line.strip() for line in f if line.strip() and not line.startswith("#")]

    if not targets:
        parser.error("No targets given. Pass URLs directly or use --list.")

    print(f"Scanning {len(targets)} target(s) for CVE-2026-109618 / CVE-2026-109619 exposure...\n")
    results = [scan(t) for t in targets]
    for r in results:
        print_result(r)

    vulnerable_count = sum(1 for r in results if r.status == "vulnerable")
    print(f"\n{vulnerable_count} of {len(results)} target(s) flagged vulnerable.")


if __name__ == "__main__":
    main()
