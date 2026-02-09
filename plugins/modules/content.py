#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.cli import AEMC, AEMC_arg_spec

DOCUMENTATION = r'''
---
module: content

short_description: Manages JCR content on AEM instance(s)

version_added: "1.4.0"

description:
    - Clean, download, pull, push, and copy JCR content between AEM instances.
    - Supports Vault filter files and filter roots for selective content operations.

options:
    command:
        description:
            - The content operation to perform.
            - C(clean) - Normalize content files.
            - C(download) - Download content from instance to local file.
            - C(pull) - Pull content from instance and unpack to JCR root directory.
            - C(push) - Push content from JCR root directory to instance.
            - C(copy) - Copy content between instances.
        required: true
        type: str
        choices: ['clean', 'download', 'pull', 'push', 'copy']
    instance_id:
        description: Use only AEM instance with specified ID.
        type: str
    dir:
        description: JCR root directory path.
        type: str
    file:
        description: Local file path.
        type: str
    path:
        description: JCR root path or local file path.
        type: str
    filter_roots:
        description: Vault filter root paths.
        type: list
        elements: str
    filter_file:
        description: Vault filter file path.
        type: str
    target_file:
        description: File path for downloaded package.
        type: str
    target_pid:
        description: Package ID (group:name:version) for downloaded package.
        type: str
    clean:
        description: Normalize content during operation.
        type: bool
    replace:
        description: Replace content after downloading (for pull command).
        type: bool
    filter_mode:
        description: Override default filter mode (for push command).
        type: str
    instance_target_url:
        description: Destination instance URL(s) for copy command.
        type: list
        elements: str
    instance_target_id:
        description: Destination instance ID(s) for copy command.
        type: list
        elements: str

author:
    - Krystian Panek (krystian.panek@wundermanthompson.com)
'''

EXAMPLES = r'''
- name: Clean content directory
  wttech.aem.content:
    command: clean
    path: /path/to/jcr_root/content/mysite

- name: Download content from instance
  wttech.aem.content:
    command: download
    instance_id: local_author
    filter_roots:
      - /content/mysite
      - /content/dam/mysite
    target_file: /tmp/content.zip

- name: Pull content from instance
  wttech.aem.content:
    command: pull
    instance_id: local_author
    dir: /path/to/jcr_root/content/mysite
    filter_roots:
      - /content/mysite
    clean: true

- name: Push content to instance
  wttech.aem.content:
    command: push
    instance_id: local_author
    dir: /path/to/jcr_root/content/mysite

- name: Copy content between instances
  wttech.aem.content:
    command: copy
    instance_id: local_author
    instance_target_id:
      - local_publish
    filter_roots:
      - /content/mysite
'''

RETURN = r'''
'''


def run_module():
    module = AnsibleModule(
        argument_spec=AEMC_arg_spec(dict(
            command=dict(type='str', required=True, choices=['clean', 'download', 'pull', 'push', 'copy']),
            instance_id=dict(type='str'),
            dir=dict(type='str'),
            file=dict(type='str'),
            path=dict(type='str'),
            filter_roots=dict(type='list', elements='str'),
            filter_file=dict(type='str'),
            target_file=dict(type='str'),
            target_pid=dict(type='str'),
            clean=dict(type='bool'),
            replace=dict(type='bool'),
            filter_mode=dict(type='str'),
            instance_target_url=dict(type='list', elements='str'),
            instance_target_id=dict(type='list', elements='str'),
        )),
        required_if=[
            ('command', 'clean', ['dir', 'file', 'path'], True),
            ('command', 'download', ['target_file']),
            ('command', 'download', ['filter_roots', 'filter_file'], True),
            ('command', 'pull', ['dir', 'file', 'path'], True),
            ('command', 'push', ['dir', 'file', 'path'], True),
            ('command', 'copy', ['filter_roots', 'filter_file'], True),
            ('command', 'copy', ['instance_target_url', 'instance_target_id'], True),
        ],
        mutually_exclusive=[
            ['dir', 'file', 'path'],
            ['filter_roots', 'filter_file'],
            ['instance_target_url', 'instance_target_id'],
        ]
    )
    aemc = AEMC(module)
    command = module.params['command']

    args = ['content', command]

    instance_id = module.params['instance_id']
    if instance_id:
        args.extend(['--instance-id', instance_id])

    dir_param = module.params['dir']
    if dir_param:
        args.extend(['--dir', dir_param])

    file_param = module.params['file']
    if file_param:
        args.extend(['--file', file_param])

    path = module.params['path']
    if path:
        args.extend(['--path', path])

    filter_roots = module.params['filter_roots']
    if filter_roots:
        for root in filter_roots:
            args.extend(['--filter-roots', root])

    filter_file = module.params['filter_file']
    if filter_file:
        args.extend(['--filter-file', filter_file])

    target_file = module.params['target_file']
    if target_file:
        args.extend(['--target-file', target_file])

    target_pid = module.params['target_pid']
    if target_pid:
        args.extend(['--target-pid', target_pid])

    clean = module.params['clean']
    if clean is not None:
        args.extend(['--clean', 'true' if clean else 'false'])

    replace = module.params['replace']
    if replace is not None:
        args.extend(['--replace', 'true' if replace else 'false'])

    filter_mode = module.params['filter_mode']
    if filter_mode:
        args.extend(['--filter-mode', filter_mode])

    instance_target_url = module.params['instance_target_url']
    if instance_target_url:
        for url in instance_target_url:
            args.extend(['--instance-target-url', url])

    instance_target_id = module.params['instance_target_id']
    if instance_target_id:
        for target_id in instance_target_id:
            args.extend(['--instance-target-id', target_id])

    aemc.handle_json(args=args)


def main():
    run_module()


if __name__ == '__main__':
    main()
