#!/usr/bin/env bash
/usr/local/bin/wait-for-postgres.sh postgres:5432 -t 30 && python /code/manage.py collectstatic --noinput && python /code/manage.py makemigrations --noinput && python /code/manage.py migrate --noinput && uvicorn home.asgi:application --reload --host 0.0.0.0 --port 8000
