# Personal Expense Insight API

## Description

Personal Expense Insight API is a RESTful backend application built with Django and Django REST Framework.
It allows authenticated users to manage their personal expenses and access analytical insights about their spending.

The API uses JWT authentication and ensures that each user can only access their own data.

---

## Features

- JWT Authentication (access & refresh tokens)
- Full CRUD operations for expenses
- User-based data isolation
- Monthly spending analytics
- Total and average spending summary
- Expense categorization
- Input validation and error handling
- Unit tests for core endpoints
- Production-ready configuration

---

## Tech Stack

- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite (default database)

---

## Project Structure

personal-expense-insight-api/
├── expense_api/
├── expenses/
├── venv/
├── manage.py
├── requirements.txt
└── README.md

---

## Setup Instructions

### 1. Clone the repository

git clone <repository-url>
cd personal-expense-insight-api

---

### 2. Create and activate a virtual environment

python -m venv venv

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

---

### 3. Install dependencies

pip install -r requirements.txt

---

### 4. Apply database migrations

python manage.py migrate

---

### 5. Run the development server

python manage.py runserver

Server will start at:
http://127.0.0.1:8000/

---

## Authentication Endpoints

POST /api/token/
POST /api/token/refresh/

Authorization Header:
Authorization: Bearer <access_token>

---

## Expense Endpoints

GET /api/expenses/
POST /api/expenses/
GET /api/expenses/{id}/
PUT /api/expenses/{id}/
DELETE /api/expenses/{id}/

---

## Analytics Endpoints

### Monthly Insights

GET /api/expenses/monthly-insights/

Returns:
- Total spending per month
- Average spending per month
- Number of expenses per month

---

### Overall Summary

GET /api/expenses/summary/

Returns:
- Total spending
- Average spending
- Total number of expenses

---

## Running Tests

python manage.py test

---

## Security

- JWT-based authentication
- Authentication required for all endpoints
- Expenses filtered by authenticated user
- Serializer-level input validation

---

## Deployment

The project is ready for deployment and can be hosted on:
- Render
- Railway
- Fly.io
- DigitalOcean

---

## Future Improvements

- Category-based analytics
- Date range filtering
- Pagination and filtering
- API versioning
- Swagger / OpenAPI documentation

---

## Author

Zakaria Radi
