#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.cli import AEMC, AEMC_arg_spec

DOCUMENTATION = r'''
---
module: replication

short_description: Manages content replication on AEM instance(s)

version_added: "1.4.0"

description:
    - Activate, deactivate, and manage content replication between AEM instances.
    - Supports tree activation and various replication filters.

options:
    command:
        description:
            - The replication operation to perform.
            - C(activate) - Activate (publish) content at specified path.
            - C(deactivate) - Deactivate (unpublish) content at specified path.
            - C(tree) - Activate content tree at specified path.
        required: true
        type: str
        choices: ['activate', 'deactivate', 'tree']
    instance_id:
        description: Use only AEM instance with specified ID.
        type: str
    path:
        description: JCR path to replicate.
        type: str
        required: true
    dry_run:
        description: Simulate the operation without making changes.
        type: bool
    ignore_deactivated:
        description: Ignore already deactivated content.
        type: bool
    only_activated:
        description: Only include already activated content.
        type: bool
    only_modified:
        description: Only include modified content.
        type: bool

author:
    - Krystian Panek (krystian.panek@wundermanthompson.com)
'''

EXAMPLES = r'''
- name: Activate content
  wttech.aem.replication:
    command: activate
    instance_id: local_author
    path: /content/mysite/en

- name: Deactivate content
  wttech.aem.replication:
    command: deactivate
    instance_id: local_author
    path: /content/mysite/en/page

- name: Activate content tree
  wttech.aem.replication:
    command: tree
    instance_id: local_author
    path: /content/mysite
    only_modified: true

- name: Dry run tree activation
  wttech.aem.replication:
    command: tree
    instance_id: local_author
    path: /content/mysite
    dry_run: true
'''

RETURN = r'''
'''


def run_module():
    module = AnsibleModule(
        argument_spec=AEMC_arg_spec(dict(
            command=dict(type='str', required=True, choices=['activate', 'deactivate', 'tree']),
            instance_id=dict(type='str'),
            path=dict(type='str', required=True),
            dry_run=dict(type='bool'),
            ignore_deactivated=dict(type='bool'),
            only_activated=dict(type='bool'),
            only_modified=dict(type='bool'),
        )),
    )
    aemc = AEMC(module)
    command = module.params['command']

    args = ['replication', command]

    instance_id = module.params['instance_id']
    if instance_id:
        args.extend(['--instance-id', instance_id])

    path = module.params['path']
    if path:
        args.extend(['--path', path])

    dry_run = module.params['dry_run']
    if dry_run is not None:
        args.extend(['--dry-run', 'true' if dry_run else 'false'])

    ignore_deactivated = module.params['ignore_deactivated']
    if ignore_deactivated is not None:
        args.extend(['--ignore-deactivated', 'true' if ignore_deactivated else 'false'])

    only_activated = module.params['only_activated']
    if only_activated is not None:
        args.extend(['--only-activated', 'true' if only_activated else 'false'])

    only_modified = module.params['only_modified']
    if only_modified is not None:
        args.extend(['--only-modified', 'true' if only_modified else 'false'])

    aemc.handle_json(args=args)


def main():
    run_module()


if __name__ == '__main__':
    main()
