###########
# BUILDER #
###########

# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
RUN && apk add gcc postgresql-dev musl-dev python3-dev libffi-dev openssl-dev cargo python3-dev jpeg-dev zlib-dev libpq

# lint
RUN pip install --upgrade pip
RUN pip install flake8
COPY . .

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt


# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup -S app && adduser -S app -G app


RUN mkdir /home/app/web
RUN mkdir /home/app/web/staticfiles
RUN mkdir /home/app/web/mediafiles
WORKDIR /home/app/web

# copy entrypoint.sh
COPY ./entrypoint.sh /home/app/web

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app /home/app/web

# change to the app user
USER app

# run entrypoint.sh
ENTRYPOINT ["/home/app/web/entrypoint.sh"]