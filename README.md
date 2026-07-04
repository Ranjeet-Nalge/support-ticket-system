# Support Ticket System

A RESTful Support Ticket Management System built with Django REST Framework.

## Features

- User Authentication using JWT
- CRUD operations for tickets
- PostgreSQL database
- Docker support
- Filtering
- Searching
- Ordering
- Pagination
- Django Admin Panel
- Protected APIs using JWT Authentication

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- Docker
- Simple JWT

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /api/token/ | Login |
| POST | /api/token/refresh/ | Refresh Access Token |
| GET | /api/tickets/ | List Tickets |
| POST | /api/tickets/ | Create Ticket |
| GET | /api/tickets/{id}/ | Retrieve Ticket |
| PUT | /api/tickets/{id}/ | Update Ticket |
| DELETE | /api/tickets/{id}/ | Delete Ticket |

## Authentication

This project uses JWT Authentication.

Add the access token in the Authorization header.

```
Authorization: Bearer <access_token>
```

## Filtering

```
GET /api/tickets/?status=Open
```

## Search

```
GET /api/tickets/?search=login
```

## Ordering

```
GET /api/tickets/?ordering=-created_at
```

## Pagination

```
GET /api/tickets/?page=2
```

## Installation

```bash
git clone <repo>

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

## Environment Variables

Create a `.env` file.

```
SECRET_KEY=

DEBUG=True

DB_NAME=

DB_USER=

DB_PASSWORD=

DB_HOST=

DB_PORT=

```