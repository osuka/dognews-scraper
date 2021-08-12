#!/bin/bash

# This script is called from .devcontainer/devcontainer.json when running
# the project as a Visual Studio Code remote container
. $NVM_DIR/nvm.sh

# there's only one folder
cd /workspaces/*

# install node and packages (version comes from file .nvmrc)
nvm install
nvm use
[ -f package-lock.json ] && npm ci || npm i

# setup python and packages
virtualenv -p python3 .venv
. ./.venv/bin/activate
pip install -r requirements.txt
