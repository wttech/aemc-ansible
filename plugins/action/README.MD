# Actions plugins

Ansible convention assumes having for each module defined the action plugin with the same file name.

AEMC action plugin is simply sharing with module the `aem_config` variable to eliminate a need to pass is separately in each task/playbook definition.
