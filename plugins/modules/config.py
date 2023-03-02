#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.cli import AEMC, AEMC_arg_spec


DOCUMENTATION = r'''
---
module: config

short_description: Manages AEM configuration

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
            file=dict(type='str'),
        )),
        required_if=[
            ('command', 'export', ['file']),
        ]
    )
    aemc = AEMC(module)
    command = module.params['command']

    args = ['config', command]

    file = module.params['file']
    if file:
        args.extend(['--file', file])

    aemc.handle_json(args=args)


def main():
    run_module()


if __name__ == '__main__':
    main()
