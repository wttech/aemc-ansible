#!/bin/sh

{{ ansible_managed | comment }}

# TODO export AEM_INSTANCE_LOCAL_SERVICE_MODE=true
# TODO export AEM_OUTPUT_LOG_MODE=both

su - "{{ aem_system_user }}" -c ". /etc/profile && cd {{ aem_root_dir | dirname }} && {{ aem_cli_executable }} $*"
