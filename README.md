# Order Man

Lösung / Hilfestellung für die Aufgabe des Faches Verteilte System an der Teko Schweizer Fachschule Olten.

## In Betriebnahme

```
# Interpreter und Libraries installieren
pipenv shell
pipenv install

# Migrate DB
python manage.py migrate

# Erstelle Superuser
python manage.py createsuperuser

# Run Server
python manage.py runserver 0.0.0.0:8000
```

Webgui ist verfügbar unter: 

- http://0.0.0.0:8000/admin

