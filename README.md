# PNAI_2023_LAB1
A simple Python + Django project carried out as a part of the subject "Programowanie Nowoczesnych Aplikacji Internetowych""

## Visual Studio Code addons
### Python pack
_NOTE: make sure you install the proper package. Correct one should contain Pylance, Linting, Jupyter Notebooks etc._
```
Name: Python
Id: ms-python.python
Description: IntelliSense (Pylance), Linting, Debugging (multi-threaded, remote), Jupyter Notebooks, code formatting, refactoring, unit tests, and more.
Version: 2022.20.2
Publisher: Microsoft
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-python.python
```

### Django snippets
```
Name: Djaneiro - Django Snippets
Id: thebarkman.vscode-djaneiro
Description: A collection of snippets for django templates, models, views, fields & forms. Ported from Djaneiro for SublimeText
Version: 1.4.2
Publisher: Scott Barkman
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=thebarkman.vscode-djaneiro
```

## Install required dependencies 
### Python
This project is based on Python 3.10.7. Please consider to use mentioned version or higher.
### Django
Use `pip install django` in your terminal to install the newest version of Django. If you want to install the one used in this project (4.2.1) use `pip install django=4.2.1` to specify.
### Check setup
Make sure, that Python and Django are installed. Run `python --version` and `python -m django --version` to check that.

## Run project
To run this project:
+ Open terminal and go to the directory with `manage.py` script
  + `cd biblioteka`
+ Make migration of your models to a database
  + `python manage.py makemigrations`
  + then `python manage.py migrate`
+ If migration ended succesfully (you should have `migrations` folder in your `katalog` app)
  + `python manage.py runserver`

After running your app it should be available in `https:localhost:8000/admin/`
