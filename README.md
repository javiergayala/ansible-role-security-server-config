# `ansible-role-security-server-config`

This role applies generic security-related server configuration changes.  These
may be resulting from TVA security scans of our environment, or best
practices.

## Requirements

None

## Role Variables

From the `defaults/main.yml` file:

```yaml
# Disable ICMP Redirects
rax_svr_cfg_icmp_redirect: 0
```

## Dependencies

None

## Example Playbook

```yaml
    - hosts: servers
      roles:
         - { role: rswebteam.security-server-config, rax_svr_cfg_icmp_redirect: 1 }
```

## Author Information

Javier Ayala
