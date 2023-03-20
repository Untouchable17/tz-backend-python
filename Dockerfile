FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install --upgrade pip \
    && pip install psycopg2-binary

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/
