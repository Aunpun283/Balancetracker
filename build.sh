#!/usr/bin/env bash

set -o errexit

pip install -r reqs.txt

python3 manage.py collectstatic --no-input
python3 manage.py migrate
