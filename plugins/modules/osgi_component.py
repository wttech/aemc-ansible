#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


from ansible.module_utils.basic import AnsibleModule
from ..module_utils.cli import AEMC, AEMC_arg_spec

DOCUMENTATION = r'''
---
module: osgi_component

short_description: Manages OSGi components on AEM instance(s)

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
        )),
        required_if=[
            ('command', 'list', ['instance_id']),
            ('command', 'read', ['pid', 'instance_id']),
            ('command', 'enable', ['pid']),
            ('command', 'disable', ['pid']),
            ('command', 'reenable', ['pid']),
        ]
    )
    aemc = AEMC(module)
    command = module.params['command']

    args = ['osgi', 'component', command]

    instance_id = module.params['instance_id']
    if instance_id:
        args.extend(['--instance-id', instance_id])

    pid = module.params['pid']
    if pid:
        args.extend(['--pid', pid])

    aemc.handle_json(args=args)


def main():
    run_module()


if __name__ == '__main__':
    main()
