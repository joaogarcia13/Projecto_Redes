# Projecto_Redes [Orquestrador]

## Environment (venv)
  **CREATE an environment**
  
  ```python -m venv .venv```

##
  
  **ACTIVATE environment**
  
  Linux: 
  ```source .venv/bin/activate```
  
  Windows: 
  ```.venv\Scripts\activate```

##
  **INSTALL requirements**
  ```
   # to install the requirements
   pip install -r requirements.txt

   # to update the requirements
   pip freeze > requirements.txt
   ```
##

## Django

**Create project:**

    django-admin startproject orchestrator

**Run:**
  *manage.py runserver [port] -> the default port is 8000*
  
    manage.py runserver

**Data Base:**
  SQLite3 (need to install SQLiteStudio to edit "db.sqlite3")

**Create model:**
  

    manage.py startapp devices

**Make migrations:**

      manage.py makemigrations orchestrator
      manage.py migrate orchestrator
