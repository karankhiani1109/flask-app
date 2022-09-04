# syntax=docker/dockerfile:1

FROM python:3.8

ENV FLASK_APP=app.py

ENV FLASK_RUN_HOST=0.0.0.0

ENV FLASK_RUN_PORT=5000

RUN pip install --no-cache-dir --upgrade pip

WORKDIR /flask-app

RUN python3 -m venv venv

RUN . venv/bin/activate

COPY flask/requirements.txt .

RUN pip install -r requirements.txt

COPY ./flask ./flask

EXPOSE 5000

CMD ["python3","-m","flask","--app","./flask/app.py", "run"]