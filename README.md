# API для Yatube

API для социальной сети Yatube. Сервис позволяет читать публикации,
создавать посты и комментарии, получать список сообществ и управлять
подписками на авторов. Для аутентификации используются JWT-токены.

## Технологии

- Python 3
- Django 3.2
- Django REST Framework
- Simple JWT
- SQLite

## Установка

Клонируйте репозиторий и перейдите в директорию проекта:

```bash
git clone <адрес_репозитория>
cd api-final-yatube-ad
```

Создайте и активируйте виртуальное окружение:

```bash
python3 -m venv venv
source venv/bin/activate
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

Выполните миграции:

```bash
cd yatube_api
python manage.py migrate
```

Запустите сервер:

```bash
python manage.py runserver
```

Документация API доступна по адресу:

```text
http://127.0.0.1:8000/redoc/
```

## Примеры запросов

Получить JWT-токен:

```http
POST /api/v1/jwt/create/
Content-Type: application/json

{
  "username": "user",
  "password": "password"
}
```

Создать публикацию:

```http
POST /api/v1/posts/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "text": "Новая публикация",
  "group": 1
}
```

Получить список комментариев к публикации:

```http
GET /api/v1/posts/1/comments/
```

Подписаться на автора:

```http
POST /api/v1/follow/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "following": "author_username"
}
```
