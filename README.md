# Personal Expense Insight API

## Description

Personal Expense Insight API is a RESTful backend application built with **Django** and **Django REST Framework**.  
It allows authenticated users to manage their personal expenses and provides advanced analytical insights into their spending behavior.

The API uses **JWT authentication** and enforces strict **user-based data isolation**, ensuring that each user can only access their own data.

---

## Features

- JWT Authentication (access & refresh tokens)
- Full CRUD operations for expenses
- User-based data isolation
- Monthly spending analytics
- Category-based spending analytics
- Optional date range filtering for analytics
- Total and average spending summary
- Expense categorization
- Consistent API response structure
- Input validation and error handling
- Unit tests for core endpoints
- Production-ready configuration

---

## Tech Stack

- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite (default database, easily replaceable)

---

## Project Structure

personal-expense-insight-api/
├── expense_api/
├── expenses/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── tests.py
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

Mac / Linux:  
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

## Authentication

### Token Endpoints

POST /api/token/  
POST /api/token/refresh/

### Authorization Header

Authorization: Bearer <access_token>

All expense and analytics endpoints require authentication.

---

## Expense Endpoints (CRUD)

GET    /api/expenses/  
POST   /api/expenses/  
GET    /api/expenses/{id}/  
PUT    /api/expenses/{id}/  
PATCH  /api/expenses/{id}/  
DELETE /api/expenses/{id}/  

---

## Analytics Endpoints

### Monthly Insights

GET /api/expenses/monthly-insights/

Optional query parameters:  
?start_date=YYYY-MM-DD  
&end_date=YYYY-MM-DD  

Returns:
- Total spending per month
- Average spending per month
- Number of expenses per month

---

### Category-Based Insights

GET /api/expenses/category-insights/

Returns:
- Total spending per category
- Number of expenses per category

---

### Overall Summary

GET /api/expenses/summary/

Returns:
- Total spending
- Average spending
- Total number of expenses

---

## API Response Format

Success Response:
{
  "success": true,
  "data": {}
}

Error Response:
{
  "success": false,
  "error": "Error message"
}

---

## Running Tests

python manage.py test

Tests cover:
- Authentication
- Expense CRUD operations
- Analytics endpoints
- User data isolation

---

## Security

- JWT-based authentication
- Authentication required for all endpoints
- Expenses filtered by authenticated user
- Secure serializer-level input validation
- No sensitive data exposed in error responses

---

## Deployment

The application is production-ready and can be deployed on platforms such as:
- Render
- Railway
- Fly.io
- DigitalOcean

Deployment considerations:
- Set DEBUG = False
- Use environment variables for secrets
- Configure allowed hosts

---

## Author

Zakaria Radi

---

## Final Notes

This project was built as a capstone backend project, demonstrating:
- Clean architecture
- Secure API design
- Real-world analytics use cases
- Production-ready Django REST practices