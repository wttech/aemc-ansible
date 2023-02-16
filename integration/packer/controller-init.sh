#!/bin/sh

#pip3 install https://github.com/mitogen-hq/mitogen/archive/refs/tags/v0.3.3.tar.gz
mkdir -p build && wget https://github.com/mitogen-hq/mitogen/archive/refs/tags/v0.3.3.tar.gz -O build/mitogen.tar.gz
tar -xf build/mitogen.tar.gz -C build

ansible-galaxy role install -r controller-requirements.yml --force
ansible-galaxy collection install -r controller-requirements.yml --force
