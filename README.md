# `ansible-role-security-server-config`

This role applies generic security-related server configuration changes.

## Requirements

None

## Role Variables

From the `defaults/main.yml` file:

```yaml
# Disable ICMP Redirects
sec_svr_cfg_icmp_redirect: 0

# Whether to disable root console logins
# False: no do not disable, True: yes disable
sec_svr_cfg_disable_anon_root_login: "False"
```

## Dependencies

None

## Example Playbook

```yaml
- hosts: servers
  roles:
    - {
        role: javiergayala.security-server-config,
        sec_svr_cfg_icmp_redirect: 1,
      }
```

## Author Information

Javier Ayala
