# Copyright 2026, Adfinis AG
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r'''
---
module: tlsref_facts
short_description: Lookup recommended TLS configuration from tlsref.org.
description:
  - Lookup recommended TLS configuration from tlsref.org (formerly ssl-config.mozilla.org).
  - By default, uses the latest config.  Using a fixed version is recommended.
  - Registers the response as C(ansible_facts.tlsref).
version_added: 1.0.3
author: Adfinis AG
options:
  version:
    description:
      - The version of the TLSRref configuration to fetch, e.g. C(6.0).
      - Defaults to C(latest).
    type: str
    default: latest
attributes:
  check_mode:
    support: full
  diff_mode:
    support: none
  platform:
    platforms: posix
'''


EXAMPLES = r'''
- name: Gather the TLSRef reference configuration
  adfinis.facts.tlsref_facts:
    version: "6.0"

- name: Print the list of TLS ciphers in the intermediate configuration
  ansible.builtin.debug:
    var: ansible_facts.tlsref.configurations.intermediate.ciphers.openssl
'''


RETURN = r'''
ansible_facts:
  description: Facts to add to ansible_facts about the TLSRef reference configuration.
  returned: always
  type: dict
  contains:
    tlsref:
      description:
        - The dictionary returned by tlsref.org.
        - Visit U(https://data.tlsref.org/guidelines/latest.json) for the full contents.
      returned: always
      type: dict
      sample:
        version: 6.0
        href: "https://data.tlsref.org/guidelines/6.0.json"
        configurations:
          modern: ...
          intermediate ...
'''


from ansible.module_utils.basic import AnsibleModule
import json
import urllib.request


def main():
    module = AnsibleModule(
        supports_check_mode=True,
        argument_spec=dict(
            version=dict(type='str', default='latest'),
        )
    )
    version = module.params.get('version')
    url = 'https://data.tlsref.org/guidelines/{}.json'.format(version)
    resp = urllib.request.urlopen(url)
    facts = {
        'ansible_facts': {
            'tlsref': json.load(resp)
        }
    }
    module.exit_json(**facts)


if __name__ == '__main__':
    main()
