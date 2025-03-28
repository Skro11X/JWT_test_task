#!/bin/bash
set -e

python manage.py migrate
python manage.py init_groups

exec "$@"