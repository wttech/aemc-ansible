#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import yaml

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.cli import AEMC, AEMC_arg_spec

DOCUMENTATION = r'''
---
module: repo_node

short_description: Manages repository nodes on AEM instance(s)

version_added: "1.0.0"

author:
    - Krystian Panek (krystian.panek@wundermanthompson.com)
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
            path=dict(type='str', required=True),
            props=dict(type='dict')
        )),
        required_if=[
            ('command', 'read', ['instance_id']),
            ('command', 'save', ['props']),
        ]
    )
    aemc = AEMC(module)

    args = ['repo', 'node', module.params['command']]

    path = module.params['path']
    if path:
        args.extend(['--path', path])

    instance_id = module.params['instance_id']
    if instance_id:
        args.extend(['--instance-id',  instance_id])

    aemc.handle_json(args=args, data=yaml.dump(module.params['props']))


def main():
    run_module()


if __name__ == '__main__':
    main()
