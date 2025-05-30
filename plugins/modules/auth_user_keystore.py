#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.cli import AEMC, AEMC_arg_spec

DOCUMENTATION = r'''
---
module: auth_user_keystore

short_description: Manage AEM user keystore

version_added: "1.4.2"

author:
    - Jan Kowalczyk (jan.kowalczyk@wundermanthompson.com)
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
            keystore_password=dict(type='str', no_log=True),
        )),
        required_if=[
            ('command', 'create', ['instance_id', 'id', 'scope', 'keystore_password']),
            ('command', 'status', ['instance_id', 'id', 'scope']),
        ]
    )

    aemc = AEMC(module)
    command = module.params['command']

    args = ['auth', 'user', 'keystore', command]

    instance_id = module.params['instance_id']
    if instance_id:
        args.extend(['--instance-id', instance_id])


    user_id = module.params['id']
    if user_id:
        args.extend(['--id', user_id])

    scope = module.params['scope']
    if scope:
        args.extend(['--scope', scope])

    keystore_password = module.params['keystore_password']
    if keystore_password:
        args.extend(['--keystore-password', keystore_password])

    aemc.handle_json(args=args)


def main():
    run_module()


if __name__ == '__main__':
    main()
