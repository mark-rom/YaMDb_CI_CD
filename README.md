![example workflow](https://github.com/mark-rom/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## YaMDb API ##
### Описание: ###

Проект YaMDb (REST API) собирает отзывы пользователей на различные произведения. Читать контент могут все, вносить и изменять только аутентифицированные пользователи.  
Предоставляет ответы от сервера в формате JSON для последующей сериалиализации на стороне фронта. 

#### Алгоритм регистрации пользователей ####
  
1. Пользователь отправляет POST-запрос на добавление нового пользователя с параметрами `email` и `username` на эндпоинт `/api/v1/auth/signup/`.  
2. YaMDB отправляет письмо с кодом подтверждения `confirmation_code` на адрес `email`. В проекте реализован бэкенд почтового сервиса, папка - `sent_emails`.  
3. Пользователь отправляет POST-запрос с параметрами `username` и `confirmation_code` на эндпоинт `/api/v1/auth/token/`, в ответе на запрос ему приходит token (JWT-токен).  
4. При желании пользователь отправляет PATCH-запрос на эндпоинт `/api/v1/users/me/` и заполняет поля в своём профайле. 
____

## Технологии ##
- Python 3.7
- Django 2.2.19
- Djangorestframework 3.12.4
- JWT
- Docker
- Docker-compose
- PostgreSQL
- Nginx
- Github workflows
____

## Установка ##

### Клонируйте репозиторий: ###
    git clone git@github.com:mark-rom/infra_sp2.git

### Перейдите в репозиторий в командной строке: ###
    cd infra_sp2/infra/
  
### Запустите docker-compose в detach-режиме: ###
    docker-compose up -d
____

## Внутри контейнера web ##

#### Выполните миграции: ####
    docker-compose exac web python3 manage.py migrate
  
#### Заполните базу данных из csv файлов: ####
    docker-compose exac web python3 manage.py populate_db
  
#### Создайте суперюзера: ####
    docker-compose exac web python3 manage.py cratesuperuser

#### Соберите статику: ####
    docker-compose exac web python3 manage.py collectstatic

Теперь сервис доступен для работы на вашем компьютере по адресу http://localhost/api/v1/, а админка – http://localhost/admin/.
____

## Авторы ##
[Артем Меркулов](https://github.com/aimerkz), [Артем Фабриков](https://github.com/KitKat-ru), [Павел Сергеев](https://github.com/mark-rom)
