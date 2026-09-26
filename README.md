# College Event Dashboard

A beginner-friendly Django project for managing college events.

## Features
- Dashboard
- Events list
- Add event form
- SQLite database
- Django admin

## Setup on Windows

1. Open this folder in VS Code.
2. Open Terminal.
3. Create a virtual environment:

   python -m venv venv

4. Activate it:

   venv\Scripts\activate

5. Install Django:

   pip install -r requirements.txt

6. Create database tables:

   python manage.py makemigrations
   python manage.py migrate

7. Run:

   python manage.py runserver

8. Open:

   http://127.0.0.1:8000/

## Django admin

Create an admin user:

   python manage.py createsuperuser

Then visit:

   http://127.0.0.1:8000/admin/
