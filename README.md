# api_final
## Описание
REST API для проекта Yatube.
Содержит набор эндпоинтов, которые позволяют управлять публикациями и комментариями.

* api/v1/posts/ - CRUD для публикаций.
* api/v1/posts/{post_id}/comments/ - CRUD для комментариев к публикации
* api/v1/groups/ - Получение списка сообществ или подробной информации о сообществе
* api/v1/follow/ - GET/POST для получения информации о подписках/подписке на пользователя.

Пользователю необходимо зарегистрироваться и все запросы осуществлять с использованием JWT-токена:
* api/v1/jwt/create/ - Получение JWT-токена
* api/v1/jwt/refresh/ - Обновление JWT-токена
* api/v1/jwt/verify/ - Проверка JWT-токена
## Установка
Клонировать репозиторий:

```bash
git clone https://github.com/timur-nagimov/api_final_yatube
```

Перейти в папку с проектом:

```bash
cd api_final_yatube
```

Создание/актиавация виртуального окружения

```bash
py -m venv venv
```
  
```bash
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```bash
python3 -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

Выполнить миграции:

```bash
python3 manage.py migrate
```

Запустить проект:

```bash
python3 manage.py runserver
```

## Примеры
api/v1/posts/ - При отправке GET-запроса на эндпоинт

Результат будет примерно следующим:\
```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
При POST-запросе на этот же эндпоинт обязательно надо передать поле `text`, остальные поля - необязательные:
```json
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
----
api/v1/groups/ - Поддерживает только GET-запросы и выдает информацию вида:
```json
[
  {
    "id": 0,
    "title": "string",
    "slug": "^-$",
    "description": "string"
  }
]
```
----
api/v1/follow/ - Поддерживает только GET-запросы и выдает информацию вида:
```json
[
  {
    "user": "string",
    "following": "string"
  }
]
```
----
api/v1/posts/{post_id}/comments/ - CRUD для комментариев. Для отправки комментария необходимо передать текст:
```json
{
  "text": "string"
}
```
Сами комментарии имеют следующий формат:
```json
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```

## Использованные технологии
Использовался фреймворк Django с надстройкой в виде DRF (Django Rest Framework).
Дополнительно для генерации и взаимодействия с токенами использовалась библиотека djoser.