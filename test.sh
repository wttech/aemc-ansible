#!/usr/bin/env sh

# ===== Configuration =====

ROLE=${1:-"instance"}
PLAYBOOK=${2:-"extensive"}
FLAGS=${3:-"-v"}

# ===== Prerequisites =====

if [ -z ${AEM_CLI_EXECUTABLE+x} ]; then
  echo ""
  echo "===== Building AEM Compose CLI ====="
  echo ""

  (cd ../aemc && make install)
fi

# ===== Execution =====

echo ""
echo "===== Executing AEM Compose Ansible ====="
echo ""
echo "Role: ${ROLE}"
echo "Playbook: ${PLAYBOOK}"
echo ""

run_ansible() {
  cd "roles/${ROLE}/tests" && ansible-playbook -i "inventory" "${PLAYBOOK}.yml" --connection=local "${FLAGS}"
}
( run_ansible )


