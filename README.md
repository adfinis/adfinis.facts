# Adfinis facts Collection for Ansible

Collection for custom Adfinis ansible facts plugins

## Included content

* timer_facts: slightly modified `service_facts` plugin to support timer units

## Using this collection

Usage examples for the individual fact plugins included:

### timer_facts

```yaml
- name: Populate timer facts
  adfinis.facts.timer_facts:

- name: Print timer facts
  ansible.builtin.debug:
    var: ansible_facts.timers
```

### Installing the Collection from Ansible Galaxy

Before using this collection, you need to install it with the Ansible Galaxy command-line tool:
```bash
ansible-galaxy collection install adfinis.facts
```

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:
```yaml
---
collections:
  - name: adfinis.facts
```

Note that if you install the collection from Ansible Galaxy, it will not be upgraded automatically when you upgrade the `ansible` package. To upgrade the collection to the latest available version, run the following command:
```bash
ansible-galaxy collection install adfinis.facts
```

You can also install a specific version of the collection, for example, if you need to downgrade when something is broken in the latest version (please report an issue in this repository). Use the following syntax to install version `0.1.0`:

```bash
ansible-galaxy collection install adfinis.facts:==0.1.0
```

See [Ansible Using collections](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html) for more details.

### Contributing to this collection

Once you have done some work, please test the collection locally using molecule.
To install it locally, use `ansible-galaxy collection build` and install the resulting `tar.gz` file.
