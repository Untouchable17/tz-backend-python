#!/bin/sh

python manage.py collectstatic --no-input --clear

if [ "$DJANGO_ENVIRONMENT" = "production" ]; then
    gunicorn config.wsgi:application --bind 0.0.0.0:8000
else
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver 0.0.0.0:8000
fi
