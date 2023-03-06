from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from ansible.plugins.action import ActionBase
from ..module_utils.cli import EXECUTABLE_PARAM, CONFIG_FILE_PARAM, CONFIG_DICT_PARAM, EXECUTABLE_PARAM


class AemActionBase(ActionBase):

    def run(self, tmp=None, task_vars=None):
        result = super(AemActionBase, self).run(tmp, task_vars)

        module_args = self._task.args.copy()
        tpl_vars = self._templar.available_variables

        if EXECUTABLE_PARAM in task_vars:
            module_args[EXECUTABLE_PARAM] = self._templar.template(task_vars[EXECUTABLE_PARAM])
        elif EXECUTABLE_PARAM in tpl_vars:
            module_args[EXECUTABLE_PARAM] = self._templar.template(tpl_vars[EXECUTABLE_PARAM])

        if CONFIG_FILE_PARAM in task_vars:
            module_args[CONFIG_FILE_PARAM] = self._templar.template(task_vars[CONFIG_FILE_PARAM])
        elif CONFIG_FILE_PARAM in tpl_vars:
            module_args[CONFIG_FILE_PARAM] = self._templar.template(tpl_vars[CONFIG_FILE_PARAM])

        module_args[CONFIG_DICT_PARAM] = {}
        if CONFIG_DICT_PARAM in task_vars:
            module_args[CONFIG_DICT_PARAM].update(self._templar.template(task_vars[CONFIG_DICT_PARAM]))
        if CONFIG_DICT_PARAM in tpl_vars:
            module_args[CONFIG_DICT_PARAM].update(self._templar.template(tpl_vars[CONFIG_DICT_PARAM]))

        module_result = self._execute_module(
            module_name=self._task.action,
            module_args=module_args,
            task_vars=task_vars
        )

        result.update(module_result)

        return result
