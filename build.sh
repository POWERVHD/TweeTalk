#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e  

echo "🚀 Installing dependencies..."
pip install -r requirements.txt

echo "⚡ Applying database migrations..."
python manage.py migrate --noinput

echo "🎨 Collecting static files..."
python manage.py collectstatic --noinput

# Optional: Create a superuser (only if required)
# echo "👤 Creating superuser..."
# python manage.py createsuperuser --noinput --username admin --email admin@example.com

echo "✅ Build process completed!"
