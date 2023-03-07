#!/bin/sh

# flag '--no-cache' is intentional as file changes from 'src' directory are not causing rebuilding
docker build --no-cache -t wttech/aemc/controller-aws .
