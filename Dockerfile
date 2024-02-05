FROM python:3.11-slim

COPY requirements.txt /

RUN pip3 install --upgrade pip

RUN pip3 install -r /requirements.txt

COPY . /app

WORKDIR /app

EXPOSE 6868

CMD ["gunicorn","--config", "gunicorn_config.py", "app:app"]