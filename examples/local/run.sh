#!/usr/bin/env sh

# ===== Configuration =====
PLAYBOOK=${1:-"start"}
FLAGS=${2:-"-v"}

# ===== Prerequisites =====

echo ""
echo "===== Installing AEM Compose CLI ====="
echo ""

(cd ../../../aemc && make install)
export AEM_CLI_EXECUTABLE=$(whereis aem | awk -F': ' '{print $2}')

echo ""
echo "===== Installing AEM Compose Ansible Collection ====="
echo ""

(cd ../../ && sh install.sh)

# ===== Execution =====

echo ""
echo "===== Executing AEM Compose Ansible ====="
echo ""
echo "Playbook: ${PLAYBOOK}"
echo ""

ansible-playbook -i "inventory" "${PLAYBOOK}.yml" --connection=local "${FLAGS}"
