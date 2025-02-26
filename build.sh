#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Collect static files for production
python manage.py collectstatic --noinput
