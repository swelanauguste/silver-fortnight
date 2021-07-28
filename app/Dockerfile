# pull official base image
FROM python:3.10-rc-buster as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install libpq-dev postgresql postgresql-contrib ncat -y

# RUN useradd -ms /bin/bash app
# RUN usermod -a -G app app
# RUN chown -R app:app /usr/src/app
# USER app

# create and activate virtual environment
RUN python -m venv venv
RUN . venv/bin/activate

# install dependencies
RUN python -m pip install --upgrade pip --no-warn-script-location
COPY ./requirements.txt .
# RUN pip install -r requirements.txt --no-warn-script-location
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

FROM python:3.10-rc-buster

RUN mkdir -p /home/app

RUN useradd -ms /bin/bash app && usermod -a -G app app

RUN apt-get update && apt-get install ncat -y
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME

COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy entrypoint.sh
COPY ./entrypoint.sh $APP_HOME

RUN chown -R app:app $APP_HOME
RUN chown -R app:app /home/app/web/staticfiles

# copy project
COPY . $APP_HOME

USER app

# run entrypoint.sh
ENTRYPOINT ["/home/app/web/entrypoint.sh"]