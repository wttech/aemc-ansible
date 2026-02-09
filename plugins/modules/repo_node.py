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
            path=dict(type='str'),
            props=dict(type='dict'),
            source_path=dict(type='str'),
            target_path=dict(type='str'),
            replace=dict(type='bool'),
        )),
        required_if=[
            ('command', 'read', ['path', 'instance_id']),
            ('command', 'save', ['path', 'props']),
            ('command', 'copy', ['source_path', 'target_path']),
            ('command', 'move', ['source_path', 'target_path']),
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

    source_path = module.params['source_path']
    if source_path:
        args.extend(['--source-path', source_path])

    target_path = module.params['target_path']
    if target_path:
        args.extend(['--target-path', target_path])

    replace = module.params['replace']
    if replace is not None:
        args.extend(['--replace', 'true' if replace else 'false'])

    aemc.handle_json(args=args, data=yaml.dump(module.params['props']))


def main():
    run_module()


if __name__ == '__main__':
    main()
