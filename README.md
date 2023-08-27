# Bitpin

## Getting started
This project is dockerized, and to deploy, just run the following commands
```
git clone git@github.com:amirhosseindehghan1/Bitpin.git
cd Bitpin
docker-compose up -d
```
Three containers are created that run the Django project with gonicorn

## Create Superuser
For createsuperuser you can login django containet shell with this command:
```
docker exec -it django_container_name_or_id bash sh
python manage.py createsuperuser
```
After Create Superuser just exit the shell:
```
exit
```
Now Restart or rebuild the project with these command:

```
docker-compose restart
```
Or
```
docker-compose up --build
```