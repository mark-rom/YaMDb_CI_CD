![example workflow](https://github.com/mark-rom/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## YaMDb API ##
### Description: ###

YaMDb API is a REST API for content rating service like IMDb. Authenticated users can post reviews on titles, and comment on others' reviews. Moderators can edit or even delete unacceptable content. Every user on the Internet can read reviews.

## Install ##

### Clone the repo: ###
    git clone git@github.com:mark-rom/YaMDb_CI_CD.git

### Go to new dir: ###
    cd YaMDb_CI_CD/infra/
  
### Run docker-compose: ###
    docker-compose up -d
____

## Inside the web container ##

#### Migrate: ####
    docker-compose exec web python3 manage.py migrate

#### Collect static: ####
    docker-compose exec web python3 manage.py collectstatic
  
#### Populate db: ####
    docker-compose exec web python3 manage.py populate_db
  
#### Create superuser: ####
    docker-compose exec web python3 manage.py cratesuperuser

Now the service is available on your local machine at http://localhost/api/v1/, and the admin panel is on http://localhost/admin/.
____

#### How to register ####
  
1. Send POST-request with `email` and `username` parameters to the endpoint `/api/v1/auth/signup/`
2. YaMDB sends a letter with a confirmation code to the email.
3. Send POST-request with `username` and `confirmation_code` to the endpoint `/api/v1/auth/token/`. You will receive a JWT token.
4. You can fill up your profile with PATCH-request to the endpoint `/api/v1/users/me/`
____

## Technologies ##
-Python 3.7
- Django 2.2.19
- Djangorestframework 3.12.4
- JWT
-Docker
- docker-compose
- PostgreSQL
- nginx
- GitHub workflows
____

## CI/CD ##
Set CI/CD to a virtual server. Workflow settings are in `YaMDb_CI_CD/.github/workflows/` directory. Environmental variables are in Actions secrets.
____

##Authors##
[Artem Merkulov](https://github.com/aimerkz), [Artem Fabricov](https://github.com/KitKat-ru), [Pavel Sergeev](https://github.com/mark-rom )
