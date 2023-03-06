#!/usr/bin/env sh

# ===== Configuration =====

ROLE=${1:-"instance"}
PLAYBOOK=${2:-"extensive"}
FLAGS=${3:-"-v"}

# ===== Prerequisites =====

echo ""
echo "===== Installing AEM Compose Ansible Collection ====="
echo ""

(cd ../aemc && make install)
export AEM_CLI_EXECUTABLE=$(whereis aem | awk -F': ' '{print $2}')

sh install.sh

# ===== Execution =====

echo ""
echo "===== Executing AEM Compose Ansible ====="
echo ""
echo "Role: ${ROLE}"
echo "Playbook: ${PLAYBOOK}"
echo ""

run_ansible() {
  AEM_ROOT_DIR="$(pwd)/roles/${ROLE}/tests/aem"
  cd "roles/${ROLE}/tests" && ansible-playbook -i "inventory" "${PLAYBOOK}.yml" --connection=local -e aem_root_dir="$AEM_ROOT_DIR" "${FLAGS}"
}
( run_ansible )


