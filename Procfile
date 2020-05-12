web: gunicorn motorhome_root.motorhome_site.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
