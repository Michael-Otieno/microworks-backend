
web: gunicorn kot_microworks.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
