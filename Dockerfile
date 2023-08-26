FROM python:3.10.12
WORKDIR /api
RUN apt update && apt upgrade -y
RUN apt update
RUN apt update && apt upgrade -y && \
    apt install -y libmariadb-dev-compat gcc
COPY . /api/
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver"]