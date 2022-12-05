Environment
  # to create an environment
  python -m venv .venv
  
  # to activate environment
  Linux: source .venv/bin/activate
  Windows: .venv\Scripts\activate


Create project:
  django-admin startproject orquestrador .

Run:
  # manage.py runserver [port] -> the default port is 8000
  manage.py runserver 8000

Data Base:
  SQLite3 (need to install SQLiteStudio to edit "db.sqlite3")

Create model:
  manage.py startapp devices

Make migrations:
  manage.py makemigrations orquestrador
  manage.py migrate orquestrador
