# Troubleshooting Log

Real issues hit while building this lab, in order encountered. Kept
unedited because the debugging process is part of what this project
demonstrates.

## 1. Case-sensitive mount path (`Nginx` vs `nginx`)
Docker bind mounts are case-sensitive regardless of host filesystem.
`docker-compose.yml` referenced `./nginx/`, the actual folder was `Nginx/`.
Fix: renamed folder to lowercase to match the compose reference.

## 2. Single shared nginx config couldn't target two PHP-FPM backends
Initial config used `fastcgi_pass ${PHP_BACKEND}:9000;` with an
`environment:` variable, assuming nginx would expand it. nginx does not
expand environment variables in config files without `envsubst` templating.
Fix: split into two static config files (`vuln.conf`, `patched.conf`),
each hardcoding its own backend, mounted separately per nginx service.

## 3. Docker daemon permission denied
`permission denied while trying to connect to the docker API at
unix:///var/run/docker.sock`. User wasn't in the `docker` group.
Fix: `sudo usermod -aG docker $USER`, then `newgrp docker` to apply without
a full logout (though group membership is only reliably picked up by new
shells after a full session restart).

## 4. Phantom file from a non-standard slash character
`ls` showed both a `www/` directory and a separate file `www⁄index.php`
at the project root — a fraction-slash character (U+2044) had been typed
instead of a real `/`, likely from a terminal font/autocomplete issue.
The actual `www/` directory was empty; `index.php` never landed inside it.
Fix: `mv "www⁄index.php" www/index.php` (quoted, to handle the odd
character safely).

## 5. `www/` directory owned by root
Docker had auto-created the bind-mount target as root on first container
start. `mv` into it failed with permission denied even as the file owner.
Fix: `sudo chown -R $USER:$USER www/`.

## 6. nginx containers crash-looping: `Permission denied` reading config
```
nginx: [emerg] open() "/etc/nginx/conf.d/default.conf" failed
(13: Permission denied)
```
Host file permissions looked correct (`-rw-r--r--`), but the container
still couldn't read it. Root cause: SELinux mount labeling on Fedora —
Docker bind mounts need an explicit relabel flag for container processes
to access them, even when standard Unix permissions are fine.
Fix: added `:z` to every bind mount in `docker-compose.yml`
(`./nginx/vuln.conf:/etc/nginx/conf.d/default.conf:z`).

## 7. Suricata: rule file not loading at all
Container started clean but logged
`No rule files match the pattern /var/lib/suricata/rules/suricata.rules`
and `0 rules loaded`. The rules file was correctly bind-mounted, just not
at the path Suricata's default config actually scans.
Fix: pointed Suricata explicitly at the mounted file with `-S <path>`
instead of relying on the default rule-directory scan.

## 8. Suricata: same SELinux mount issue as #6, different container
```
chown: changing ownership of '/etc/suricata/rules/php2shell.rules':
Permission denied
```
Same root cause as issue 6, now hit a second time in a different
container. Confirms this is a systemic pattern on this host (Fedora +
SELinux + Docker bind mounts), not a one-off nginx quirk.
Fix: same as #6 — added `:z` to the mount.

## 9. Suricata rules written multi-line — parser requires single-line
Rules were originally formatted across multiple lines for readability.
Suricata's rule parser does not support this; it parsed the opening
`alert http any any -> any any (` as a complete (and invalid) signature.
Fix: rewrote every rule as a single continuous line.

## 10. Suricata and ModSecurity syntax mixed in one file
Original rules file contained both Suricata `alert ...` signatures and
ModSecurity `SecRule ...` directives together. Suricata attempted to parse
the ModSecurity lines as its own syntax and failed with
`no terminating ";" found`.
Fix: split into two separate files — `php2shell_suricata.rules` and
`php2shell_modsecurity.rules` — since they're different engines entirely.

## 11. `dsize` incompatible with `http_client_body` in this rule
```
E: detect-dsize: Parsing '>1000000' failed
```
`dsize` operates on raw packet size; `http_client_body` operates on the
reassembled HTTP body buffer. Mixing them in one signature isn't valid in
this Suricata version/ruleset combination.
Fix: dropped the oversized-body rule rather than chase the exact
compatible syntax under time pressure. Documented as a known gap — the
two remaining rules (field-presence and request-frequency) still cover
the core detection logic.

## Result
After fixing all of the above: lab running correctly (confirmed via
version-split curl checks), scanner validated against both targets with
correct verdicts, and Suricata confirmed firing on a live test request
(`sid:9000001` in `fast.log`).
