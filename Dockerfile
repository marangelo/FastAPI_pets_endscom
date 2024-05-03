#FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim

LABEL maintainer="Maryan Espinoza <analista.guma@gmail.com>"

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app