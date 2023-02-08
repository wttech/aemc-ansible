#!/usr/bin/env sh

VERSION=$1
VERSION_CURRENT=$(git describe --tags --abbrev=0)

if [ -z "$VERSION" ]
then
      echo "Release version is not specified!"
      echo "Last released: ${VERSION_CURRENT}"
      exit 1
fi

GIT_STAT=$(git diff --stat)

if [ "$GIT_STAT" != '' ]; then
  echo "Unable to release. Uncommited changes detected!"
  exit 1
fi

echo "Releasing $VERSION"

echo "Bumping version in files"

GALAXY_FILE="galaxy.yml"

# <https://stackoverflow.com/a/57766728>
if [ "$(uname)" = "Darwin" ]; then
  sed -i '' 's/version: "[^\"]*"/version: "'"$VERSION"'"/g' "$GALAXY_FILE"
else
    sed -i 's/version: "[^\"]*"/version: "'"$VERSION"'"/g' "$GALAXY_FILE"
fi

echo "Pushing version bump"
git commit -a -m "Release $VERSION"
git push

echo "Pushing release tag '$VERSION'"
git tag "$VERSION"
git push origin "$VERSION"
