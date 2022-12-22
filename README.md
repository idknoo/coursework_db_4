# Курсовая работа 

## How run the project?

First of all, you must have python and postgresql installed
and to continue ...

##### Clone the repository :
```bash
$ git clone https://github.com/mmdtoorani/online-shop.git
$ cd online-shop
```
##### Create a virtualenv and activate it:
 ```bash
$ python3 -m venv venv
$ . venv/bin/activate
```
##### Or on Windows cmd : 
 ```bash
> py -3 -m venv venv
> venv\Scripts\activate.bat
```

##### Install the requirements :
```bash
$ cd onlineshop
$ pip3 install -r requirements.txt
```

#### In settings.py, set up the database :
for this project i used postgress, you can see the following settings below :
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_user_password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

#### makemigrations :
```bash
python manage.py makemigrations
python manage.py migrate
```

#####  Run the development server :
```bash
python3 manage.py runserver
```
Open http://127.0.0.1:8000 in your browser. 
