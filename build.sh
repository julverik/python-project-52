#!/usr/bin/env bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env

curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
apt-get install -y nodejs

make install
npm install

uv run python manage.py tailwind build
make collectstatic

# Миграции
uv run python manage.py migrate users
uv run python manage.py migrate