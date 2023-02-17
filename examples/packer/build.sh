#!/bin/sh

if [ -z ${AWS_ACCESS_KEY_ID+x} ]; then
  echo "Requires variable 'AWS_ACCESS_KEY_ID' is not set!"
  exit 1
fi
if [ -z ${AWS_SECRET_ACCESS_KEY+x} ]; then
  echo "Requires variable 'AWS_SECRET_ACCESS_KEY' is not set!"
  exit 1
fi

docker run \
  -v "$(pwd):/controller" \
  -e AWS_ACCESS_KEY_ID \
  -e AWS_SECRET_ACCESS_KEY \
  wttech/aemc/controller-aws \
  packer build "$@" .
