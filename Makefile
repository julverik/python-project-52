install:
	uv sync

migrate:
	uv run python manage.py migrate

collectstatic:
	uv run python manage.py collectstatic --noinput

build:
	./build.sh

render-start:
	gunicorn hexlet_code.wsgi

dev:
	uv run python manage.py runserver

test:
	uv run python manage.py test
