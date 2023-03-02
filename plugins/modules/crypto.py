#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


from ansible.module_utils.basic import AnsibleModule
from ..module_utils.cli import AEMC, AEMC_arg_spec

DOCUMENTATION = r'''
---
module: crypto

short_description: Manages Crypto Support

version_added: "1.0.28"

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
            hmac_file=dict(type='str'),
            master_file=dict(type='str'),
        ))
    )
    aemc = AEMC(module)
    command = module.params['command']

    args = ['crypto', command]

    instance_id = module.params['instance_id']
    if instance_id:
        args.extend(['--instance-id', instance_id])

    hmac_file = module.params['hmac_file']
    if hmac_file:
        args.extend(['--hmac-file', hmac_file])

    master_file = module.params['master_file']
    if hmac_file:
        args.extend(['--master-file', master_file])

    aemc.handle_json(args=args)


def main():
    run_module()


if __name__ == '__main__':
    main()
