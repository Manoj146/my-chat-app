#!/usr/bin/env bash
export DJANGO_SETTINGS_MODULE=backend.settings

set -o errexit

daphne -b 0.0.0.0 -p 10000 backend.asgi:application
