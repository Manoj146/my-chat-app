#!/usr/bin/env bash
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files into staticfiles/ directory
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate
