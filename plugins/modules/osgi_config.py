#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import yaml

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.cli import AEMC, AEMC_arg_spec

DOCUMENTATION = r'''
---
module: osgi_config

short_description: Manages OSGi configuration on AEM instance(s)

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
            pid=dict(type='str'),
            props=dict(type='dict'),
        )),
        required_if=[
            ('command', 'read', ['instance_id', 'pid']),
            ('command', 'list', ['instance_id']),
            ('command', 'read', ['pid']),
            ('command', 'save', ['pid']),
            ('command', 'delete', ['pid']),
            ('command', 'save', ['pid', 'props']),
        ]
    )
    aemc = AEMC(module)
    command = module.params['command']

    args = ['osgi', 'config', command]

    instance_id = module.params['instance_id']
    if instance_id:
        args.extend(['--instance-id', instance_id])

    pid = module.params['pid']
    if pid:
        args.extend(['--pid', pid])

    aemc.handle_json(args=args, data=yaml.dump(module.params['props']))


def main():
    run_module()


if __name__ == '__main__':
    main()
