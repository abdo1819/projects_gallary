# projects gallary
website to display projects made by student at the collage

## setup
## clone the project
    git clone <project link>

## setup python enviroment


### Create a virtual environment
    python3 -m venv gallary
    source env/bin/activate 
*or use conda*


### install reqiered packages

* Django 
* django-extensions
* djangorestframework
* Markdown
* pydotplus

```
pip install -r requirements.txt
```

## migrate the database and filldata
    python manage.py migrate
    python manage.py runscript fill_data.py

## run server
    python manage.py runserver