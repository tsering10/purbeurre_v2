# Django Project PurBeurre

This app lets a user search for a product and suggests similar healthier products. Users can save their favorite product in their account. The product data are collected from OpenFoodFacts(https://fr.openfoodfacts.org/). This app is available both in English and French. 

### French language
![Pur Beurre French](https://github.com/tsering10/purbeurre_v2/blob/main/static/purbeurre/img/fr.png)
### English language
![Pur Beurre English](https://github.com/tsering10/purbeurre_v2/blob/main/static/purbeurre/img/en.png)

### Setting up Django internationalisation
Add english language via internationalisation settings by this way:

#### settings.py :
* import **unittext_lazy** translation method;
* set **LocaleMiddleware** between CommonMiddleware and SessionMiddleware;
* add supported english language code **'en',_ ('English');**
* add LOCALE_PATHS **local** as a folder where find translations.

#### urls.py :
* import **i18n_patterns** function;
* divid admin urls from others;
* add language codes in PurBeurre website URLs.

#### views.py :
* import **unittext_lazy** translation method;
* mark all wanted items to translate;

#### html files :
* import label tag **{% load i18n %}** to activate translation;
* mark all wanted items by **{% trans "" %}** label tag.

#### create django.po / django.mo files :
* run `django-admin makemessages -l en` command from application root folder;
* make translations in **django.po** file;
* run `django-admin compilemessages` command from project root to create optimized **django.mo** file.

## 1. Requirements :

* Python 3.x (you can install [python](https://www.python.org/downloads/))
* Django  (you can install [Django](https://docs.djangoproject.com/en/3.2/topics/install/)) 
* **pip** package management system -
* Using a virtual environment is highly recommended - Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io)
* Dependencies in **requirements.txt** (use `pip install -r requirements.txt` to install them)

## 2. Database :
* PostgreSQL is used for this project 
* Database structure implementation : use `manage.py migrate` command
* To update the database use `manage.py db_loading`

In your Django settings.py

```bash
   'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'YOUR DB NAME',
        'USER': 'YOUR DB USERNAME',
        'PASSWORD': 'YOUR DB PASSWORD', 
        'HOST': 'YOUR DB HOST',
        'PORT': '5432',
    }
}
```
## 3. Configure Gmail SMTP server:
* under your settings.py file you need to add the following settings

```bash
EMAIL_BACKEND = ‘django.core.mail.backends.smtp.EmailBackend’
EMAIL_HOST = ‘smtp.gmail.com’
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = ‘your_account@gmail.com’
EMAIL_HOST_PASSWORD = ‘your account’s password’
```

## 4. Getting Started

1. Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).
2. you can clone or fork the git repo

```bash
$ virtualenv {your virtual env name}
$ source {your virtual env name}/bin/activate
$ pip install -r requirements.txt
$ cd projectname/
$ python manage.py migrate
$ python manage.py runserver

```
Then go to localhost:8000 or 127.0.0.1:8000, and the app should be launched and usable there.

## 5. Tests

To run the tests, cd into the directory where manage.py is:

```bash
$ ./manage.py test 

```
If you want to know the test coverage:


```bash
$ coverage run ./manage.py test 

```
To get test report and generate report in html file:


```bash
$ coverage report -m

$ coverage html
```
## Acknowledgment
I would like to thank my mentor Dimitri Ségard, for all the help and advices he gave to me to accomplish this project.
