web: python manage.py collectstatic --no-input \
    && python manage.py migrate \
    && gunicorn pbandkamp.wsgi --log-level debug