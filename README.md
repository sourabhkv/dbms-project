# dbms-project
Cricket dbms project


```powershell
python manage.py runserver
```
Superuser
```
user : sourabh
passwd : Sourabh@dbms@Qwerty123
```

## Workaround
Change database to SQLite
```python
#settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
