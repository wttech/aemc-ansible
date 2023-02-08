#!/usr/bin/env sh

VERSION=$1
VERSION_TAG="v$VERSION"

VERSION_CURRENT_TAG=$(git describe --tags --abbrev=0)
VERSION_CURRENT_TAG="${VERSION_CURRENT_TAG:1}"

if [ -z "$VERSION" ]
then
      echo "Release version is not specified!"
      echo "Last released: ${VERSION_CURRENT_TAG}"
      exit 1
fi

GIT_STAT=$(git diff --stat)

if [ "$GIT_STAT" != '' ]; then
  echo "Unable to release. Uncommited changes detected!"
  exit 1
fi

echo "Releasing $VERSION_TAG"

echo "Bumping version in files"

ROLE_BASE_DEFAULTS_FILE="roles/base/defaults/main.yml"

# <https://stackoverflow.com/a/57766728>
if [ "$(uname)" = "Darwin" ]; then
  sed -i '' 's/aem_cli_version: "[^\"]*"/aem_cli_version: "'"$VERSION"'"/g' "$ROLE_BASE_DEFAULTS_FILE"
else
    sed -i 's/aem_cli_version: "[^\"]*"/aem_cli_version: "'"$VERSION"'"/g' "$ROLE_BASE_DEFAULTS_FILE"
fi

echo "Pushing version bump"
git commit -a -m "Release $VERSION_TAG"
git push

echo "Pushing release tag '$VERSION_TAG'"
git tag "$VERSION_TAG"
git push origin "$VERSION_TAG"
