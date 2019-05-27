#!/bin/bash
set -e

python /code/manage.py runserver 0.0.0.0:8000

exec "$@"