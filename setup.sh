#!/usr/bin/env sh

COLLECTION_ROOT="${HOME}/.ansible/collections/ansible_collections/wttech"
COLLECTION_DIR="${COLLECTION_ROOT}/aem"

CURRENT_DIR=$(pwd)

echo "Linking Ansible collection from '${CURRENT_DIR}' to '${COLLECTION_DIR}'"
mkdir -p "${COLLECTION_ROOT}"
ln -s "${CURRENT_DIR}" "${COLLECTION_DIR}"
