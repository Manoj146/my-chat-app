#!/usr/bin/env bash
set -o errexit

daphne -b 0.0.0.0 -p 10000 backend.asgi:application
