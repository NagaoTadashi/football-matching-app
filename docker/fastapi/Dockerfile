FROM python:3.9

WORKDIR /code

COPY ./backend/requirements.txt /code/requirements.txt

COPY ./backend/serviceAccountKey.json /code/serviceAccountKey.json

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

