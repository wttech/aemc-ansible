#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.cli import AEMC, AEMC_arg_spec

DOCUMENTATION = r'''
---
module: gts_certificate

short_description: Manage certificates in Global Trust Store

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
            alias=dict(type='str'),
            path=dict(type='str'),
        )),
        required_if=[
            ('command', 'add', ['instance_id','path']),
            ('command', 'remove', ['instance_id','alias']),
            ('command', 'read', ['instance_id','alias']),
        ]
    )

    aemc = AEMC(module)
    command = module.params['command']

    args = ['gts', 'certificate', command]

    instance_id = module.params['instance_id']
    if instance_id:
        args.extend(['--instance-id', instance_id])

    alias = module.params['alias']
    if alias:
        args.extend(['--alias', alias])

    path = module.params['path']
    if path:
        args.extend(['--path', path])

    aemc.handle_json(args=args)


def main():
    run_module()


if __name__ == '__main__':
    main()
