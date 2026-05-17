# Django React E-commerce (Modernized)

A modernized full-stack ecommerce project built using:

- Django
- Django REST Framework
- React
- SQLite
- Docker

This project originally started from the tutorial project by JustDjango and is now being rebuilt and modernized into a scalable backend-focused ecommerce architecture.

---

# Inspiration

Original project inspiration:

https://github.com/justdjango/django-react-ecommerce

This repository is now evolving independently with:

- modern DRF architecture
- custom authentication system
- modular apps
- Dockerized backend
- API-first development
- scalable backend structure

---

# Project Structure

```text
E-commerce/
│
├── frontend/                     # Existing React frontend
│
├── modern_backend/               # New DRF backend
│   │
│   ├── apps/
│   │   ├── users/
│   │   ├── products/
│   │   └── common/
│   │
│   ├── config/
│   │
│   ├── manage.py
│   ├── requirements.txt
│   └── db.sqlite3
│
├── legacy_backend/               # Original Django backend reference
│
└── README.md
```

---

# Current Features

## Backend

- Django REST Framework setup
- Custom User Model
- Modular app architecture
- User Registration API
- SQLite database
- Dockerized backend
- JWT-ready structure

## Frontend

- React ecommerce UI
- Cart & checkout UI
- Product pages
- Existing frontend workflow

---

# Tech Stack

## Backend

- Python
- Django
- Django REST Framework
- SimpleJWT
- SQLite
- Docker

## Frontend

- React
- Axios
- Bootstrap

---

# Backend Setup

## 1. Clone Repository

```bash
git clone https://github.com/h4tz/E-commerce.git
cd E-commerce
```

---

## 2. Navigate to Backend

```bash
cd modern_backend
```

---

## 3. Create Virtual Environment

```bash
python3 -m venv venv
```

Activate virtual environment:

### Linux / WSL

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install django djangorestframework djangorestframework-simplejwt python-decouple
```

Or:

```bash
pip install -r requirements.txt
```

---

## 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 6. Run Server

```bash
python manage.py runserver
```

Backend runs on:

```text
http://127.0.0.1:8000/
```

---

# Frontend Setup

Navigate to frontend directory:

```bash
cd frontend
```

Install packages:

```bash
npm install
```

Run frontend:

```bash
npm start
```

Frontend runs on:

```text
http://localhost:3000/
```

---

# Docker Setup

## Build Backend Container

```bash
docker build -t modern-backend .
```

---

## Run Backend Container

```bash
docker run -p 8000:8000 modern-backend
```

---

# API Endpoints

## Authentication

### Register User

```http
POST /api/users/register/
```

### Example Request

```json
{
    "email": "test@test.com",
    "username": "testuser",
    "password": "12345678"
}
```

---

# Current Backend Architecture

## Apps

### users

Handles:

- authentication
- user management
- JWT auth
- profiles

### products

Handles:

- products
- categories
- inventory

### common

Shared utilities:

- base models
- helpers
- permissions
- constants

---

# Goals / Roadmap

## Phase 1

- DRF setup
- Custom user model
- Registration API
- JWT authentication

## Phase 2

- Product APIs
- Category APIs
- Pagination
- Filtering
- Search

## Phase 3

- Cart system
- Order management
- Checkout flow

## Phase 4

- Stripe integration
- Payment workflows
- Webhooks

## Phase 5

- Redis
- Celery
- Background tasks

## Phase 6

- Swagger/OpenAPI docs
- CI/CD
- Production deployment
- Nginx + Gunicorn
- PostgreSQL

---

# Learning Goals

This project is part of my backend engineering journey focused on:

- scalable Django architecture
- DRF best practices
- authentication systems
- API design
- Docker & DevOps
- production backend workflows
- system design fundamentals

---

# Current Status

## Completed

- Modern backend initialized
- Custom user model
- DRF installed
- Users app setup
- Registration API
- Docker backend setup

## In Progress

- JWT authentication
- Product APIs
- Frontend integration

---

# Future Improvements

- PostgreSQL
- Redis caching
- Celery workers
- Docker Compose
- Kubernetes experimentation
- API versioning
- Unit testing
- Monitoring & logging
- Role-based permissions

---

# Author

GitHub:

https://github.com/h4tz

---

# License

This project is for learning and educational purposes.