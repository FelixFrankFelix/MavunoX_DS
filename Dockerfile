FROM python:3.12.0-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirement.txt

 