set -m python manage.py migrate && python manage.py collectstatic && gunicorn ecommerce.wsgi
