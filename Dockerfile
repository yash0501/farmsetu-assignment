FROM python:3.9.12-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y libpq-dev gcc

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD python manage.py runserver

