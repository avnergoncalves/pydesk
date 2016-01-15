PyDesk
======

Free service desk system

Description
--------------------------------------
PyDesk is a system based on best practices described in the Information Technology Infrastructure Library (ITIL), which provides transparency in the process, increased productivity, aligning expectations with customers, improved quality of services, cost reduction, easy installation and its light version is open source.

Access the demo version [here](https://still-plateau-5016.herokuapp.com/).

User: admin
Password: admin

Heroku Deploy
--------------------------------------
1. Clone project.
    ```shell
    $ git clone https://github.com/avnergoncalves/pydesk.git
    ```
    
2. Create project in heroku (Require Heroku Toolbelt installed download [here](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)).
    ```shell
    $ heroku create
    ```
    
3. Change configuration from the database file at the end of settings.py.
    ```python
    DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'HOST': '<HOST>',
                'NAME': '<NAME>',
                'USER': '<USER>',
                'PASSWORD': '<PASS>',
                'PORT': '5432'
        }
    }
    ```
    
4. Starts build on heroku.
    ```shell
    $ git push heroku master
    ```
    
5. Import database.
    ```shell
    $ heroku run python manage.py syncdb
    ```
