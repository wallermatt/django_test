FROM ubuntu:20.04

ENV LC_ALL=C.UTF-8

EXPOSE 8000

RUN apt-get update && apt-get install -y vim && apt-get install -y python3-pip && apt-get install -y postgresql-client

RUN apt-get install -y iputils-ping && apt-get install -y curl && apt-get install -y telnet

RUN apt-get install -y libpq-dev

RUN pip3 install Django && pip3 install psycopg2-binary

RUN pip3 install tzdata

WORKDIR /home/

COPY . .

WORKDIR /home/mytestsite/

ARG SETTINGS
ENV envSettings=$SETTINGS

CMD ["sh", "-c", "python3 manage.py runserver 0.0.0.0:8000 --settings ${envSettings}"]
