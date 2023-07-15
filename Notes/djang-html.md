## To get html emmet in django html

- Go to the setting
 ~/.config/Code/User/settings.json
 - Edit settings.json
 - Add files.associations:

 ``"files.associations": {
        "**/templates/*.html": "django-html",
        "**/templates/*": "django-txt",
        "**/requirements{/**,*}.{txt,in}": "pip-requirements",
        "*.html": "html"
      },
      "emmet.includeLanguages": { "django-html": "html" }
``
