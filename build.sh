#!/usr/bin/env bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env

curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
apt-get install -y nodejs

make install
npm install

./node_modules/.bin/tailwindcss -i task_manager/static/css/input.css -o task_manager/static/css/output.css

make collectstatic && make migrate