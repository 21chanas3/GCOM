# GCOM

TODO: Make this better

This project uses `poetry`

To run without Socket.IO, use `python manage.py runserver`
To run with Socket.IO, use `gunicorn -b :8000 --threads 100 --access-logfile - gcom.wsgi:application`.
You must use WSL if on Windows