#!/bin/sh

export ANSIBLE_CONFIG=./ansible.cfg

ansible-playbook "$@"
