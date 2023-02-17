#!/bin/sh

pip3 install --upgrade pip && \
pip3 install -r requirements.txt --no-cache-dir && \
ansible-galaxy role install -r requirements.yml --force && \
ansible-galaxy collection install -r requirements.yml --force && \
rm -fr /root/.ansible/tmp
