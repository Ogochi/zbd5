FROM python:3-alpine

COPY . .
ADD requirements.txt .

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip3 install -r requirements.txt

CMD python3 app.py