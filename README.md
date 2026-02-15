# Personal Expense Insight API

## Description
A RESTful API built with Django and Django REST Framework to manage user expenses and provide spending insights.

## Features
- JWT Authentication
- Expense CRUD
- User-based data isolation

## Tech Stack
- Python
- Django
- Django REST Framework
- Simple JWT

## Setup Instructions

1. Clone the repository
2. Create virtual environment
3. Install dependencies

pip install -r requirements.txt

4. Run migrations

python manage.py migrate

5. Start server

python manage.py runserver

## API Endpoints

POST /api/token/
POST /api/token/refresh/
GET /api/expenses/
POST /api/expenses/
