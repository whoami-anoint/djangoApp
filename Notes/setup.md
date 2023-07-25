## App setup

-  Specific subcommand. 
``python manage.py``

- To change port number:
- `888 to 5555 `
- `` python manage.py runserver 5555``

- `python manage.py startapp home `
- Create <b>urls.py</b> at home
- Create your views here in views.py
    -  ``from django.shortcuts import render,HttpResponse``
- Added two folders
    - static
    - templates

- Added Manually in settings.py : 

``STATICFILES_DIRS = [
    BASE_DIR / "static",
    "/var/www/static/",
]
``

- To get secret key; ``grep -Inr SECRET_KEY *``
