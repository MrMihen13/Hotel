#!/bin/sh

python manage.py migrate || exit 1
gunicorn hotel.wsgi:application --bind 0.0.0.0:8000 --reload --log-level DEBUG