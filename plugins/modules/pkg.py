#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ..module_utils.cli import AEMC, AEMC_arg_spec
from ansible.module_utils.basic import AnsibleModule


DOCUMENTATION = r'''
---
module: pkg

short_description: Manages packages on AEM instance(s)

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
            file=dict(type='str'),
            url=dict(type='str'),
            pid=dict(type='str'),
            path=dict(type='str'),
            force=dict(type='bool'),
        )),
        required_if=[
            ('command', 'read', ['instance_id']),
            ('command', 'read', ['file', 'pid', 'path'], True),
            ('command', 'list', ['instance_id']),
            ('command', 'build', ['instance_id']),
            ('command', 'build', ['file', 'pid', 'path'], True),
            ('command', 'install', ['file', 'pid', 'path'], True),
            ('command', 'uninstall', ['file', 'pid', 'path'], True),
            ('command', 'delete', ['file', 'pid', 'path'], True),
            ('command', 'upload', ['file', 'url'], True),
            ('command', 'deploy', ['file', 'url'], True),
        ]
    )
    aemc = AEMC(module)
    command = module.params['command']
    args = ['pkg', command]

    instance_id = module.params['instance_id']
    if instance_id:
        args.extend(['--instance-id', instance_id])

    file = module.params['file']
    if file:
        args.extend(['--file', file])

    url = module.params['url']
    if url:
        args.extend(['--url', url])

    pid = module.params['pid']
    if pid:
        args.extend(['--pid', pid])

    path = module.params['path']
    if path:
        args.extend(['--path', path])

    force = module.params['force']
    if force is not None:
        args.extend(['--force', "true" if force else "false"])

    aemc.handle_json(args=args)


def main():
    run_module()


if __name__ == '__main__':
    main()
