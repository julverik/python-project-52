setup:
	make install
	make migrate
	make collectstatic
	make tailwind-build

install:
	uv sync

migrate:
	uv run python manage.py migrate

collectstatic:
	uv run python manage.py collectstatic --noinput

tailwind-build:
	uv run python manage.py tailwind build

build:
	./build.sh

render-start:
	gunicorn hexlet_code.wsgi

dev:
	uv run python manage.py runserver

test:
	PYTHONPATH=./src/hexlet_code uv run python manage.py test users statuses tasks labels

lint:
	uv run ruff check .
	uv run ruff format --check .

format:
	uv run ruff format .
	uv run ruff check --fix .

.PHONY: setup install migrate collectstatic tailwind-build build render-start dev test lint format
