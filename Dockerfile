FROM ubuntu:20.04

ENV LC_ALL=C.UTF-8

EXPOSE 8000

RUN apt-get update && apt-get install -y vim && apt-get install -y python3-pip && apt-get install -y postgresql-client

RUN apt-get install -y iputils-ping && apt-get install -y curl && apt-get install -y telnet

RUN pip3 install Django==4.0.2 && pip3 install psycopg2-binary==2.9.3

RUN pip3 install tzdata

WORKDIR /home/

COPY . .

WORKDIR /home/mytestsite/

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000", "--settings", "mytestsite.settings.docker"]
