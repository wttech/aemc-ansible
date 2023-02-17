#!/bin/bash

export TF_PLUGIN_CACHE_DIR=/root/.terraform.d/plugin-cache

mkdir -p /root/.terraform.d/plugin-cache \
  && terraform init \
  && rm -fr .terraform
