# Book Management System (Django)

## Features
- User Authentication (Login / Logout)
- Book CRUD Operations
- Borrow & Return Books
- Quantity Management
- Admin Panel
- Login protected views

## Tech Stack
- Python
- Django
- SQLite
- HTML, CSS (Bootstrap)

## How to Run Project

```bash
git clone <repo-url>
cd bookmanagement
python -m venv venv
venv\Scripts\activate
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
