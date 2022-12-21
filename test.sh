#!/usr/bin/env sh

# ===== Utilities =====

# 'realpath' is not OOTB installed on Mac
rp()
{
    f=$@;
    if [ -d "$f" ]; then
        base="";
        dir="$f";
    else
        base="/$(basename "$f")";
        dir=$(dirname "$f");
    fi;
    dir=$(cd "$dir" && /bin/pwd);
    echo "$dir$base"
}

# ===== Configuration =====

ROLE=${1:-instance}
PLAYBOOK=${2:-test}

# ===== Execution =====

echo ""
echo "===== Building AEM Compose CLI ====="
echo ""

(cd ../aemc && make build)

AEM_CLI_EXECUTABLE="$(rp "../aemc/bin/aem")"
export AEM_CLI_EXECUTABLE # TODO comment out to test auto-downloading of CLI via 'base' role

echo ""
echo "===== Executing AEM Compose Ansible ====="
echo ""
echo "Role: ${ROLE}"
echo "Playbook: ${PLAYBOOK}"
echo ""

(cd "roles/${ROLE}/tests" && ansible-playbook -i "inventory" "${PLAYBOOK}.yml" --connection=local --verbose)


