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

echo ""
echo "===== Installing AEM Compose Ansible Collection ====="
echo ""

sh install.sh

# ===== Execution =====

echo ""
echo "===== Executing AEM Compose Ansible ====="
echo ""
echo "Role: ${ROLE}"
echo "Playbook: ${PLAYBOOK}"
echo ""

run_ansible() {
  AEM_HOME_DIR="$(pwd)/roles/${ROLE}/tests/aem/home"
  cd "roles/${ROLE}/tests" && ansible-playbook -i "inventory" "${PLAYBOOK}.yml" --connection=local -e aem_home_dir="$AEM_HOME_DIR" "${FLAGS}"
}
( run_ansible )


