web: gunicorn run:APP
web: python manage.py runserver --host 0.0.0.0 --port ${PORT}
init: python migrations.py db init
migrate: python migrations.py db migrate
upgrade: python migrations.py db upgrade