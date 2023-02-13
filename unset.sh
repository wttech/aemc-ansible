#!/usr/bin/env sh

COLLECTION_PATH="${HOME}/.ansible/collections/ansible_collections/wttech/aem"

echo "Unlinking Ansible collection '${COLLECTION_PATH}'"
unlink "${COLLECTION_PATH}"
