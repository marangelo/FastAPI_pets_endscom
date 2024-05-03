#FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim

LABEL maintainer="Maryan Espinoza <analista.guma@gmail.com>"

# COPY ./requirements.txt /app/requirements.txt
# RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
# COPY ./app /app

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]