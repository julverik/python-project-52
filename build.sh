#!/usr/bin/env bash
# скачиваем uv
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env

# Устанавливаем Node.js для Render
curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
apt-get install -y nodejs

# Устанавливаем зависимости
make install
npm install

# Собираем стили через Django команду
uv run python manage.py tailwind build

# Собираем статику и миграции
make collectstatic
make migrate