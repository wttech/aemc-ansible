#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.cli import AEMC, AEMC_arg_spec

DOCUMENTATION = r'''
---
module: oak

short_description: Manages Oak operations on AEM instance(s)

version_added: "1.4.0"

description:
    - Manage Oak operations including compaction and index management.
    - Supports segment compaction and Lucene index operations.

options:
    command:
        description:
            - The Oak operation to perform.
            - C(compact) - Run segment store compaction offline.
            - C(index-list) - List all Oak indexes.
            - C(index-read) - Read index definition and statistics.
            - C(index-reindex) - Trigger reindexing for a single index.
            - C(index-reindex-batch) - Trigger batch reindexing.
        required: true
        type: str
        choices: ['compact', 'index-list', 'index-read', 'index-reindex', 'index-reindex-batch']
    instance_id:
        description: Use only AEM instance with specified ID.
        type: str
    name:
        description: Index name (required for index-read and index-reindex).
        type: str
    batch_id:
        description: Batch reindex ID.
        type: str
    name_pattern:
        description: Index name pattern for batch operations.
        type: str
    force:
        description: Force the operation.
        type: bool

author:
    - Krystian Panek (krystian.panek@wundermanthompson.com)
'''

EXAMPLES = r'''
- name: Compact segment store
  wttech.aem.oak:
    command: compact
    instance_id: local_author

- name: List all indexes
  wttech.aem.oak:
    command: index-list
    instance_id: local_author

- name: Read index statistics
  wttech.aem.oak:
    command: index-read
    instance_id: local_author
    name: lucene

- name: Reindex a specific index
  wttech.aem.oak:
    command: index-reindex
    instance_id: local_author
    name: lucene
    force: true

- name: Batch reindex by pattern
  wttech.aem.oak:
    command: index-reindex-batch
    instance_id: local_author
    name_pattern: "lucene*"
'''

RETURN = r'''
'''


def run_module():
    module = AnsibleModule(
        argument_spec=AEMC_arg_spec(dict(
            command=dict(type='str', required=True, choices=['compact', 'index-list', 'index-read', 'index-reindex', 'index-reindex-batch']),
            instance_id=dict(type='str'),
            name=dict(type='str'),
            batch_id=dict(type='str'),
            name_pattern=dict(type='str'),
            force=dict(type='bool'),
        )),
        required_if=[
            ('command', 'index-read', ['name']),
            ('command', 'index-reindex', ['name']),
        ],
    )
    aemc = AEMC(module)
    command = module.params['command']

    # Map command names with dashes
    command_map = {
        'compact': 'compact',
        'index-list': 'index-list',
        'index-read': 'index-read',
        'index-reindex': 'index-reindex',
        'index-reindex-batch': 'index-reindex-batch',
    }

    args = ['oak', command_map[command]]

    instance_id = module.params['instance_id']
    if instance_id:
        args.extend(['--instance-id', instance_id])

    name = module.params['name']
    if name:
        args.extend(['--name', name])

    batch_id = module.params['batch_id']
    if batch_id:
        args.extend(['--batch-id', batch_id])

    name_pattern = module.params['name_pattern']
    if name_pattern:
        args.extend(['--name-pattern', name_pattern])

    force = module.params['force']
    if force is not None:
        args.extend(['--force', 'true' if force else 'false'])

    aemc.handle_json(args=args)


def main():
    run_module()


if __name__ == '__main__':
    main()
