#!/bin/sh

docker run \
  -v "$(pwd):/controller" \
  -e AWS_ACCESS_KEY_ID \
  -e AWS_SECRET_ACCESS_KEY \
  --rm -it --entrypoint bash \
  wttech/aemc/controller-aws
