#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.cli import AEMC, AEMC_arg_spec

DOCUMENTATION = r'''
---
module: auth_user_key

short_description: Manage AEM user private keys in the keystore

version_added: "1.6.10"

author:
    - Piotr Andruszkiewicz (piotr.andruszkiewicz@vml.com)
'''

EXAMPLES = r'''
'''

RETURN = r'''
'''


def run_module():
    module = AnsibleModule(
        argument_spec=AEMC_arg_spec(dict(
            command=dict(type='str', required=True),
            instance_id=dict(type='str'),
            id=dict(type='str'),
            scope=dict(type='str'),
            keystore_file=dict(type='path'),
            keystore_password=dict(type='str', no_log=True),
            key_alias=dict(type='str'),
            key_password=dict(type='str', no_log=True),
            new_key_alias=dict(type='str', default=None),
        )),
        required_if=[
            ('command', 'add', ['instance_id', 'id', 'key_alias', 'keystore_file', 'keystore_password']),
            ('command', 'delete', ['instance_id', 'id', 'key_alias']),
        ]
    )

    aemc = AEMC(module)
    command = module.params['command']

    args = ['auth', 'user', 'key', command]

    instance_id = module.params['instance_id']
    if instance_id:
        args.extend(['--instance-id', instance_id])


    user_id = module.params['id']
    if user_id:
        args.extend(['--id', user_id])

    scope = module.params['scope']
    if scope:
        args.extend(['--scope', scope])

    keystore_file = module.params['keystore_file']
    if keystore_file:
        args.extend(['--keystore-file', keystore_file])

    keystore_password = module.params['keystore_password']
    if keystore_password:
        args.extend(['--keystore-password', keystore_password])

    key_alias = module.params['key_alias']
    if key_alias:
        args.extend(['--key-alias', key_alias])

    key_password = module.params['key_password']
    if key_password:
        args.extend(['--key-password', key_password])

    new_key_alias = module.params['new_key_alias']
    if new_key_alias:
        args.extend(['--new-alias', new_key_alias])

    aemc.handle_json(args=args)


def main():
    run_module()


if __name__ == '__main__':
    main()
