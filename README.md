# 🎓 Student Management System

A **Django-based Student Management System** with REST API support.  
This project provides secure student record management with authentication and CRUD operations, and is designed following real-world backend practices.

---

## 🚀 Key Features

- Secure admin authentication
- Student CRUD operations
- Search by name or roll number
- REST APIs using Django REST Framework
- SQLite (development) and PostgreSQL (production) support
- Clean and secure project structure

---

## 🛠 Tech Stack

- Python, Django, Django REST Framework
- SQLite / PostgreSQL
- HTML, CSS, Bootstrap
- Git & GitHub

---

## 📂 Project Structure
# 🎓 Student Management System

A **Django-based Student Management System** with REST API support.  
This project provides secure student record management with authentication and CRUD operations, and is designed following real-world backend practices.

---

## 🚀 Key Features

- Secure admin authentication
- Student CRUD operations
- Search by name or roll number
- REST APIs using Django REST Framework
- SQLite (development) and PostgreSQL (production) support
- Clean and secure project structure

---

## 🛠 Tech Stack

- Python, Django, Django REST Framework
- SQLite / PostgreSQL
- HTML, CSS, Bootstrap
- Git & GitHub

---

## 📂 Project Structure
student_management/
├── student_management/ # Project settings
├── students/ # Student app (models, views, APIs)
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore


---

## ⚙️ Setup (Local)

git clone https://github.com/USERNAME/student-management-django.git
cd student-management-django
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

## 🔗 API Endpoints

- `GET /api/students/` – Get all students  
- `GET /api/students/?search=name` – Search students  
- `POST /api/students/` – Add new student (Admin only)  
- `PUT /api/students/{id}/` – Update student  
- `DELETE /api/students/{id}/` – Delete student

👤 Author
Famesh Vilash Katre
MCA | Python & Django Developer
