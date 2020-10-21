FROM python:3.8-alpine
LABEL author='vismoke@yandex.ru' version=2.0 project='study_yp'
WORKDIR /home/app/yamdb
COPY . /home/app/yamdb
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN export SECRET_KEY=test_SECRET_KEY && python manage.py collectstatic --noinput
# CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000