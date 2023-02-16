#!/bin/bash

# This script prepares managed node (AWS EC2 machine) to be ready before calling Ansible

sudo yum install -y unzip python3 python3-pip && \
sudo pip3 install -r /tmp/requirements.txt
