#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import yaml

from ..module_utils.cli import AEMC, AEMC_arg_spec
from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = r'''
---
module: repl_agent

short_description: Manages replication agents on AEM instance(s)

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
            instance_id=dict(type='str', required=True),
            location=dict(type='str', required=True),
            name=dict(type='str', required=True),
            props=dict(type='dict'),
        )),
        required_if=[
            ('command', 'setup', ['props']),
        ]
    )
    aemc = AEMC(module)
    aemc.handle_json(
        args=[
            'repl', 'agent', module.params['command'],
            '--instance-id', module.params['instance_id'],
            '--location', module.params['location'],
            '--name', module.params['name'],
        ],
        data=yaml.dump(module.params['props'])
    )

def main():
    run_module()


if __name__ == '__main__':
    main()
