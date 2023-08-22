FROM python:3.11-slim-bullseye

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Update Linux
RUN apt-get update \
    && apt-get -y install libpq-dev gcc

# Instalar dependencias
COPY . /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt