FROM python:3.11-slim-bullseye

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Update Linux
RUN apt-get update \
    && apt-get upgrade -y

# Instalar dependencias
COPY . /app
RUN pip install -r requirements.txt