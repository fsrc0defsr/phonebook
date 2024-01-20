FROM python:3.10.12

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD . /app

RUN pip install -r requirements.txt

COPY . /app