#!/bin/sh

{{ ansible_managed | comment }}

# TODO export AEM_INSTANCE_LOCAL_SERVICE_MODE=true

aem_start() {
  su - "{{ aem_system_user }}" -c ". /etc/profile && cd {{ aem_root_dir | dirname }} && {{ aem_cli_executable }} instance start"
}

aem_stop() {
  su - "{{ aem_system_user }}" -c ". /etc/profile && cd {{ aem_root_dir | dirname }} && {{ aem_cli_executable }} instance stop"
}

aem_status() {
  su - "{{ aem_system_user }}" -c ". /etc/profile && cd {{ aem_root_dir | dirname }} && {{ aem_cli_executable }} instance status"
}

case "$1" in
  start)
    aem_start
  ;;
  stop)
    aem_stop
  ;;
  restart)
    aem_stop
    aem_start
  ;;
  status)
    aem_status
  ;;
  *)
  echo "Usage: {start|stop|restart|status}"
  exit 1
  ;;
esac
