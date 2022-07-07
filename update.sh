#!/bin/bash
set -e -o pipefail

SDDM_GIT=~/git/sddm

git -C "$SDDM_GIT" pull
git -C "$SDDM_GIT" diff v0.19.0.. > update-from-git.patch

git diff --exit-code update-from-git.patch && exit
make autospec
make koji-nowait
