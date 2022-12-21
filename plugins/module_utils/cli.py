from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from io import StringIO
from ansible.module_utils.basic import AnsibleModule

import yaml
import json
import os

EXECUTABLE_ENV = 'AEM_CLI_EXECUTABLE'
EXECUTABLE_VAR = 'aem_cli_executable'
EXECUTABLE_PARAM = 'aem_cli_executable'
CONFIG_FILENAME = 'aem.yml'
CONFIG_VAR = 'aem'
CONFIG_PARAM = 'aem_config'


def AEMC_arg_spec(spec):
    spec[CONFIG_PARAM] = dict(type='dict', required=True)
    spec[EXECUTABLE_PARAM] = dict(type='str')
    return spec


class AEMC(object):
    """Delegates execution to AEM CLI"""

    def __init__(self, module: AnsibleModule):
        self.module = module
        self.config_file = os.path.join(self.module.tmpdir, CONFIG_FILENAME)

    def handle_json(self, args, data=None):
        executable = self._get_executable()
        self._write_config()
        args_all = [executable, *['' if v is None else v for v in args]]
        output_yml = self._run_executable(args_all, data)
        self._handle_output(args_all, output_yml)

    def _get_executable(self):
        path_var = self.module.params.get(EXECUTABLE_PARAM, '')
        path_env = os.environ.get(EXECUTABLE_ENV)
        path = path_env or path_var

        if not os.path.isfile(path):
            self.module.fail_json(msg="\n".join([
                "PROBLEM:\n",
                f"Unable to find AEM CLI executable at path '{path}'!",
                f"To fix the problem apply one of actions below:",
                f"1) Set the Ansible variable '{EXECUTABLE_VAR}'",
                f"2) Set the environment variable '{EXECUTABLE_ENV}'",
            ]))
        return path

    def _write_config(self):
        try:
            with open(self.config_file, 'w') as config_file:
                yaml.dump(self.module.params[CONFIG_PARAM], config_file, default_flow_style=False)
        except Exception as e:
            self.module.fail_json(msg="\n".join([
                "PROBLEM:\n",
                f"Unable to save config for AEM CLI command at path '{self.config_file}'",
                "ERROR:\n",
                f"{e}",
            ]))

    def _run_executable(self, args, data):
        json_str = ''
        try:
            (rc, out, err) = self.module.run_command(
                args=args,
                data=data,
                environ_update=dict(
                    AEM_CONFIG_FILE=self.config_file,
                    AEM_INPUT_FILE='STDIN',
                    AEM_INPUT_FORMAT='yml',
                    AEM_OUTPUT_FORMAT='json',
                )
            )
            json_str = out or err
        except Exception as e:
            self.module.fail_json(msg="\n".join([
                "PROBLEM:\n",
                "Unable to run AEM CLI command:",
                ' '.join(args),
                "",
                "ERROR:\n",
                f"{e}",
            ]))
        return json_str

    def _handle_output(self, args, output_json):
        command = ' '.join(args)
        try:
            output = json.load(StringIO(output_json))
            failed = output['failed']
            changed = output['changed']
            log = output['log'].strip()
            result = output['msg'].strip()
            data = output['data']

            if log:
                msg = "\n".join([
                    "COMMAND:\n",
                    command,
                    "",
                    "LOG:\n",
                    log,
                    "",
                    "RESULT:\n",
                    result,
                    "",
                ])
            else:
                msg = "\n".join([
                    "COMMAND:\n",
                    command,
                    "",
                    "RESULT:\n",
                    result,
                    "",
                ])

            if failed:
                self.module.fail_json(msg=msg)
            else:
                self.module.exit_json(**dict(msg=msg, changed=changed, data=data))
        except Exception as e:
            self.module.fail_json(msg="\n".join([
                "Unable to parse JSON output of AEM CLI",
                "",
                "COMMAND:\n",
                command,
                "",
                "OUTPUT:\n",
                output_json,
                "",
                "ERROR:\n",
                f"{e}",
            ]))
