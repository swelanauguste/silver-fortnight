#!/bin/sh

# if [ "$DATABASE" = "postgres" ]
# then
#     echo "Waiting for postgres..."

#     while ! nc -z $SQL_HOST $SQL_PORT; do
#       sleep 0.1
#     done

#     echo "PostgreSQL started"
# fi


# python manage.py flush --noinput
python manage.py makemigrations --noinput
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser --email swelanauguste@gmail.com --username superuser --noinput
python manage.py add_categories categories.txt
python manage.py add_tags tags.txt
python manage.py add_departments departments.txt
python manage.py add_positions positions.txt
# # python manage.py collectstatic --noinput


exec "$@"