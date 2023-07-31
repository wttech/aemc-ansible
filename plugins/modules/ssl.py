#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


from ansible.module_utils.basic import AnsibleModule
from ..module_utils.cli import AEMC, AEMC_arg_spec

DOCUMENTATION = r'''
---
module: ssl

short_description: Manages SSL by Default setup

version_added: "1.2.2"

author:
    - Piotr Andruszkiewicz (piotr.andruszkiewicz@wundermanthompson.com)
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
            keystore_password=dict(type='str', no_log=True),
            truststore_password=dict(type='str', no_log=True),
            certificate_file=dict(type='str'),
            private_key_file=dict(type='str'),
            https_hostname=dict(type='str'),
            https_port=dict(type='str'),
        ))
    )
    aemc = AEMC(module)
    command = module.params['command']

    args = ['ssl', command]

    instance_id = module.params['instance_id']
    if instance_id:
        args.extend(['--instance-id', instance_id])

    keystore_password = module.params['keystore_password']
    if keystore_password:
        args.extend(['--keystore-password', keystore_password])

    truststore_password = module.params['truststore_password']
    if truststore_password:
        args.extend(['--truststore-password', truststore_password])

    certificate_file = module.params['certificate_file']
    if certificate_file:
        args.extend(['--certificate-file', certificate_file])

    private_key_file = module.params['private_key_file']
    if private_key_file:
        args.extend(['--private-key-file', private_key_file])

    https_hostname = module.params['https_hostname']
    if https_hostname:
        args.extend(['--https-hostname', https_hostname])

    https_port = module.params['https_port']
    if https_port:
        args.extend(['--https-port', https_port])

    aemc.handle_json(args=args)


def main():
    run_module()


if __name__ == '__main__':
    main()
