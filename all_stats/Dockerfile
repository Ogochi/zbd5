FROM python:3-alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

ADD requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .
CMD python3 app.py