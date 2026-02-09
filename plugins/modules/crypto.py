#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


from ansible.module_utils.basic import AnsibleModule
from ..module_utils.cli import AEMC, AEMC_arg_spec

DOCUMENTATION = r'''
---
module: crypto

short_description: Manages AEM Crypto Support

version_added: "1.0.28"

description:
    - Manage AEM crypto keys and encrypt/decrypt values.
    - Supports key generation, protection, and file-based key management.

options:
    command:
        description:
            - The crypto operation to perform.
            - C(key) - Generate or manage crypto keys.
            - C(protect) - Protect (encrypt) a plain text value.
        required: true
        type: str
        choices: ['key', 'protect']
    instance_id:
        description: Use only AEM instance with specified ID.
        type: str
    hmac_file:
        description: Path to HMAC key file.
        type: str
    master_file:
        description: Path to master key file.
        type: str
    value:
        description: Plain text value to protect (encrypt). Required for protect command.
        type: str
        no_log: true

author:
    - Krystian Panek (krystian.panek@wundermanthompson.com)
'''

EXAMPLES = r'''
- name: Generate crypto keys
  wttech.aem.crypto:
    command: key
    instance_id: local_author

- name: Protect a plain text value
  wttech.aem.crypto:
    command: protect
    instance_id: local_author
    value: "my-secret-password"
'''

RETURN = r'''
'''


def run_module():
    module = AnsibleModule(
        argument_spec=AEMC_arg_spec(dict(
            command=dict(type='str', required=True, choices=['key', 'protect']),
            instance_id=dict(type='str'),
            hmac_file=dict(type='str'),
            master_file=dict(type='str'),
            value=dict(type='str', no_log=True),
        )),
        required_if=[
            ('command', 'protect', ['value']),
        ],
    )
    aemc = AEMC(module)
    command = module.params['command']

    args = ['crypto', command]

    instance_id = module.params['instance_id']
    if instance_id:
        args.extend(['--instance-id', instance_id])

    hmac_file = module.params['hmac_file']
    if hmac_file:
        args.extend(['--hmac-file', hmac_file])

    master_file = module.params['master_file']
    if master_file:
        args.extend(['--master-file', master_file])

    value = module.params['value']
    if value:
        args.extend(['--value', value])

    aemc.handle_json(args=args)


def main():
    run_module()


if __name__ == '__main__':
    main()
