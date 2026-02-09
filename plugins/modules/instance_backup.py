#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.cli import AEMC, AEMC_arg_spec

DOCUMENTATION = r'''
---
module: instance_backup

short_description: Manages AEM instance backups

version_added: "1.4.0"

description:
    - Create, list, and restore backups of AEM instances.
    - Supports backup operations on local and remote instances.

options:
    command:
        description:
            - The backup operation to perform.
            - C(list) - List available backups.
            - C(make) - Create a new backup.
            - C(use) - Use/restore a specific backup.
            - C(perform) - Perform backup (create and potentially delete old ones).
            - C(restore) - Restore from the latest or specified backup.
        required: true
        type: str
        choices: ['list', 'make', 'use', 'perform', 'restore']
    instance_id:
        description: Use only AEM instance with specified ID.
        type: str
    file:
        description: Backup file path.
        type: str
    delete_created:
        description: Delete backup file after restoring.
        type: bool

author:
    - Krystian Panek (krystian.panek@wundermanthompson.com)
'''

EXAMPLES = r'''
- name: List available backups
  wttech.aem.instance_backup:
    command: list
    instance_id: local_author

- name: Create a backup
  wttech.aem.instance_backup:
    command: make
    instance_id: local_author

- name: Restore from a specific backup
  wttech.aem.instance_backup:
    command: use
    instance_id: local_author
    file: /path/to/backup.zip

- name: Perform backup with cleanup
  wttech.aem.instance_backup:
    command: perform
    instance_id: local_author

- name: Restore from latest backup
  wttech.aem.instance_backup:
    command: restore
    instance_id: local_author
    delete_created: true
'''

RETURN = r'''
'''


def run_module():
    module = AnsibleModule(
        argument_spec=AEMC_arg_spec(dict(
            command=dict(type='str', required=True, choices=['list', 'make', 'use', 'perform', 'restore']),
            instance_id=dict(type='str'),
            file=dict(type='str'),
            delete_created=dict(type='bool'),
        )),
    )
    aemc = AEMC(module)
    command = module.params['command']

    args = ['instance', 'backup', command]

    instance_id = module.params['instance_id']
    if instance_id:
        args.extend(['--instance-id', instance_id])

    file_param = module.params['file']
    if file_param:
        args.extend(['--file', file_param])

    delete_created = module.params['delete_created']
    if delete_created is not None:
        args.extend(['--delete-created', 'true' if delete_created else 'false'])

    aemc.handle_json(args=args)


def main():
    run_module()


if __name__ == '__main__':
    main()
