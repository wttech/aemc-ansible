#!/bin/sh

{{ ansible_managed | comment }}

aem_launch() {
  su - "{{ aem_system_user }}" -c ". /etc/profile && cd {{ aem_root_dir | dirname }} && {{ aem_cli_executable }} instance launch"
}

aem_terminate() {
  su - "{{ aem_system_user }}" -c ". /etc/profile && cd {{ aem_root_dir | dirname }} && {{ aem_cli_executable }} instance terminate"
}

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
  launch)
    aem_launch
  ;;
  terminate)
    aem_terminate
  ;;
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
  echo "Usage: {launch|terminate|start|stop|restart|status}"
  exit 1
  ;;
esac
