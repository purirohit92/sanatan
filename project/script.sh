set -m python manage.py migrate && gunicorn ecommerce.wsgi
