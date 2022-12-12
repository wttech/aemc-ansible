#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import yaml

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.cli import AEMC, AEMC_arg_spec

DOCUMENTATION = r'''
---
module: osgi_bundle

short_description: Manages OSGi bundles on AEM instance(s)

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
            symbolic_name=dict(type='str'),
            file=dict(type='str'),
        )),
        required_if=[
            ('command', 'list', ['instance_id']),
            ('command', 'read', ['symbolic_name', 'instance_id']),
            ('command', 'save', ['symbolic_name']),
            ('command', 'start', ['symbolic_name']),
            ('command', 'stop', ['symbolic_name']),
            ('command', 'restart', ['symbolic_name']),
            ('command', 'install', ['file']),
            ('command', 'uninstall', ['file', 'symbolic_name'], True),
        ]
    )
    aemc = AEMC(module)
    command = module.params['command']

    args = ['osgi', 'bundle', command]

    instance_id = module.params['instance_id']
    if instance_id:
        args.extend(['--instance-id', instance_id])

    symbolic_name = module.params['symbolic_name']
    if symbolic_name:
        args.extend(['--symbolic-name', symbolic_name])

    aemc.handle_json(args=args)


def main():
    run_module()


if __name__ == '__main__':
    main()
