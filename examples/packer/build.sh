#!/bin/sh

if [ -z ${AWS_ACCESS_KEY_ID+x} ]; then
  echo "Requires variable 'AWS_ACCESS_KEY_ID' is not set!"
  exit 1
fi
if [ -z ${AWS_SECRET_ACCESS_KEY+x} ]; then
  echo "Requires variable 'AWS_SECRET_ACCESS_KEY' is not set!"
  exit 1
fi

ACTION=${1:-test}
AEM_INSTANCE_KIND=${2:-classic}

ANSIBLE_EXTRA_VARS="aem_instance_kind='${AEM_INSTANCE_KIND}'"

if [ "$ACTION" = "debug" ] ; then
  touch packer.log

  docker run -i -t \
    -v "$(pwd):/controller" \
    -e PACKER_LOG=1 \
    -e PACKER_LOG_PATH="packer.log" \
    -e AWS_ACCESS_KEY_ID \
    -e AWS_SECRET_ACCESS_KEY \
    wttech/aemc/controller-aws \
    packer build -var ansible_extra_vars="$ANSIBLE_EXTRA_VARS" -debug .
else
  docker run \
    -v "$(pwd):/controller" \
    -e AWS_ACCESS_KEY_ID \
    -e AWS_SECRET_ACCESS_KEY \
    wttech/aemc/controller-aws \
    packer build -var ansible_extra_vars="$ANSIBLE_EXTRA_VARS" .
fi
