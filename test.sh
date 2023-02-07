#!/usr/bin/env sh

# ===== Configuration =====

ROLE=${1:-"instance"}
PLAYBOOK=${2:-"test"}
FLAGS=${3:-"-v"}

# ===== Execution =====

echo ""
echo "===== Building AEM Compose CLI ====="
echo ""

(cd ../aemc && make build)

echo ""
echo "===== Executing AEM Compose Ansible ====="
echo ""
echo "Role: ${ROLE}"
echo "Playbook: ${PLAYBOOK}"
echo ""

(cd "roles/${ROLE}/tests" && ansible-playbook -i "inventory" "${PLAYBOOK}.yml" --connection=local "${FLAGS}")


