# MX_zip_codes_api
Search Mexico zip codes with this API and its settlements
This is an api to get the settlements and details of the zip codes in Mexico.

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

## Run the server
```
python3 manage.py runserver
Go to localhost:8000/api/zipCodes/<zip_code>/
```
