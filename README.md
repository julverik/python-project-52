# Менеджер задач (Python)

[![hexlet-check](https://github.com/julverik/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/julverik/python-project-52/actions)

[![Quality gate status](https://sonarcloud.io/api/project_badges/measure?project=julverik_python-project-52&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=julverik_python-project-52)

[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=julverik_python-project-52&metric=coverage)](https://sonarcloud.io/summary/new_code?id=julverik_python-project-52)

На практике узнаете о проектировании баз данных, PaaS, мониторинге ошибок, ORM, фреймворке Django, шаблонизации и Tailwind CSS.

Учебный проект Хекслета: https://ru.hexlet.io/programs/python
Как это должно работать: https://files.hexlet.app/a/0rkpse

## Демо

Приложение доступно по адресу: **https://python-project-52-new.onrender.com**

## Стек

- **Python** 3.14
- **Django** 6.1 — ORM, шаблонизатор, формы, аутентификация и авторизация
- **PostgreSQL** — в продакшене 
- **SQLite** — для локальной разработки
- **django-filter** — фильтрация списка задач
- **Tailwind CSS** — через django-tailwind-cli
- **Whitenoise** — раздача статики
- **Gunicorn** — WSGI-сервер
- **Render.com** — PaaS для деплоя
- **python-dotenv** — управление переменными окружения
- **uv** — пакетный менеджер

## Установка

### Требования
- Python 3.10 или выше
- uv (пакетный менеджер)

### Клонирование репозитория

## Установка и запуск

```bash
git clone https://github.com/julverik/python-project-52.git
cd python-project-52
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env
make install
npm install
cp .env.example .env 2>/dev/null || echo "SECRET_KEY=$(uv run python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')\nDEBUG=True\nDATABASE_URL=sqlite:///db.sqlite3" > .env
uv run python manage.py tailwind build
uv run python manage.py migrate
uv run python manage.py createsuperuser
make dev


---

<details>
<summary>Автоматические тесты Хекслета</summary>

Тесты запускаются на каждый коммит. За запуск отвечает файл `.github/workflows/hexlet-check.yml` — не удаляйте и не переименовывайте ни его, ни репозиторий.

</details>

## О Хекслете

[Хекслет](https://ru.hexlet.io/) — школа программирования: авторские программы обучения с практикой, поддержкой наставников и реальными проектами, которые остаются в резюме. Этот репозиторий — один из таких проектов.
