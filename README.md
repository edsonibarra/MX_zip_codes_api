# MX_zip_codes_api
Search Mexico zip codes with this API and its settlements
This is an api to get the settlements and details of the zip codes in Mexico.

## Installation with Docker
```
git clone git@github.com:edsonibarra/MX_zip_codes_api.git
cd MX_zip_codes_api
docker build -t doorvel .
docker run -it -p 8000:8000 --name doorvelc doorvel
```

## Installation

```bash
git clone git@github.com:edsonibarra/MX_zip_codes_api.git
cd MX_zip_codes_api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Create .env file inside zip_code_mx/ directory and set environment variables for a remote or local database
```
SECRET_KEY=replaceThisSecretKey
DATABASE_NAME=replaceThisDBNAME
DATABASE_USER=replaceThisDBUSER
DATABASE_PASS=replaceThisDBPASS
DATABASE_HOST=replaceThisDBHOST
DATABASE_PORT=replaceThisDBPORT
```

## If you want to use deafult sqlite3 database update the DATABASES section in zip_code_mx/settings.py for this:
```
DATABASES = {
  'default': {
         'ENGINE': 'django.db.backends.sqlite3',
          'NAME': BASE_DIR / 'db.sqlite3',
      }
 }
```
After you this you can run the server. This will move all the data from the text file to sqlite3 DB. 

## Run the server
```
python3 manage.py runserver
Go to localhost:8000/api/zipCodes/<zip_code>/
```
