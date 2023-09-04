#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


from ansible.module_utils.basic import AnsibleModule
from ..module_utils.cli import AEMC, AEMC_arg_spec

DOCUMENTATION = r'''
---
module: gts_certificate

short_description: Communicate with Global Trust Store

version_added: "1.3.6"

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
            password=dict(type='str', no_log=True),
        )),
        required_if=[
            ('command', 'create', ['instance_id','password']),
            ('command', 'status', ['instance_id']),
        ]
    )
    aemc = AEMC(module)
    command = module.params['command']

    args = ['gts', command]

    instance_id = module.params['instance_id']
    if instance_id:
        args.extend(['--instance-id', instance_id])

    password = module.params['password']
    if password:
        args.extend(['--password', password])

    aemc.handle_json(args=args)


def main():
    run_module()


if __name__ == '__main__':
    main()
