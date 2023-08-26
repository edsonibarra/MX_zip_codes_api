# MX_zip_codes_api
Search Mexico zip codes with this API and its settlements
This is an api to get the settlements and details of the zip codes in Mexico.

## Installation with Docker
```
git clone git@github.com:edsonibarra/MX_zip_codes_api.git
cd MX_zip_codes_api
```
Set SECRET_KEY in a .env file inside root project directory
```
echo "SECRET_KEY=123456" >> zip_code_mx/.env
```
Now you can build the image and run the container
```
docker build -t mx_zip_codes .
docker run -it -p 8000:8000 --name mx_zip_cont mx_zip_codes
```
Go to ```http://localhost:8000/api/zipCodes/01000/```
