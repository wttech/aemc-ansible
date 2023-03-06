#!/bin/sh

{{ ansible_managed | comment }}

aem_start() {
  su - "{{ aem_system_user }}" -c ". /etc/profile && cd {{ aem_root_dir }} && {{ aem_cli_executable }} instance up"
}

aem_stop() {
  su - "{{ aem_system_user }}" -c ". /etc/profile && cd {{ aem_root_dir }} && {{ aem_cli_executable }} instance down"
}

aem_status() {
  su - "{{ aem_system_user }}" -c ". /etc/profile && cd {{ aem_root_dir }} && {{ aem_cli_executable }} instance status"
}

case "$1" in
  start)
    aem_start
  ;;
  stop)
    aem_stop
  ;;
  status)
    aem_status
  ;;
  restart)
    aem_stop
    aem_start
  ;;
  *)
  echo "Usage: {start|stop|status|restart}"
  exit 1
  ;;
esac
