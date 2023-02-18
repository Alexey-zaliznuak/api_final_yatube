# Yatube Api
### Describe
Api for
[Yatube](https://github.com/Alexey-zaliznuak/Yatube)
created by
[redoc documentation](/yatube_api/static/redoc.yaml)

Also you can see Swagger Yatube Api on `/api/` or `/api/swagger/`

### Technology
Python 3.11

Django 3.2.16

DRF 3.12.4
### Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`

### Start in dev mode
- Install and set environment
- Install dependencies from requirements.txt
```
pip install -r requirements.txt
```

- In the folder with manage.py run next command:
```
python manage.py runserver
```

## API Reference example

#### Get JWT token

```http
  POST /api/v1/jwt/create/
```

|Json parameter | Type     | Description                  |
| :------------ | :------- | :--------------------------- |
| `username`    | `string` | **Required**. Your username  |
| `password`    | `string` | **Required**. Your password  |

#### Get all posts

```http
  GET /api/v1/posts/
```

| Header      | Type     | Description                  |
| :---------- | :------- | :--------------------------- |
| `JWT token` | `string` | **Required**. Your JWT token |

More information on `/api/`