###########
# BUILDER #
###########

# pull official base image
FROM python:3.8.3-alpine as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update
RUN apk add postgresql-dev gcc 
RUN apk add python3-dev musl-dev 
RUN apk add libffi-dev openssl-dev
RUN apk add cargo jpeg-dev zlib-dev

# COPY ./requirements.txt .

# lint
RUN pip install --upgrade pip


# install dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########

# pull official base image
FROM python:3.8.3-alpine

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup -S app && adduser -S app -G app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
RUN apk update && apk add libpq gcc musl-dev python3-dev libffi-dev openssl-dev cargo jpeg-dev zlib-dev
RUN pip install --upgrade pip
RUN pip install Pillow
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install /wheels/* --compile --no-cache-dir

# copy entrypoint.sh
COPY ./entrypoint.sh $APP_HOME

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# run entrypoint.prod.sh
ENTRYPOINT ["/home/app/web/entrypoint.sh"]

# FROM python:3.8.3-alpine

# WORKDIR /usr/src/app

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# RUN apk update
# RUN apk add postgresql-dev gcc 
# RUN apk add python3-dev musl-dev 
# RUN apk add libffi-dev 
# RUN apk add cargo jpeg-dev zlib-dev
# COPY ./requirements.txt .


# RUN python3 -m venv venv
# RUN source venv/bin/activate
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# RUN mkdir -p /home/app

# RUN addgroup -S app && adduser -S app -G app

# ENV HOME=/home/app
# ENV APP_HOME=/home/app/web
# RUN mkdir $APP_HOME
# WORKDIR $APP_HOME

# COPY ./entrypoint.sh $APP_HOME

# COPY . $APP_HOME

# RUN chown -R app:app $APP_HOME

# USER app

# ENTRYPOINT ["/home/app/web/entrypoint.sh"]