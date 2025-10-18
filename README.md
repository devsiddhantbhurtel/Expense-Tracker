# 💰 Expense Tracker (Django)

A simple **Django-based web application** for tracking personal expenses.  
Authenticated users can **add, view, edit, and delete** their own expenses.  
The app includes a **custom user model**, full CRUD functionality, and optional **filters by category and date range**.

---

## 🚀 Features
- User authentication (Login, Logout, Registration)
- Add, Edit, Delete personal expenses
- Only logged-in users can access expense pages
- Users can only view their own expenses
- Display monthly total expenses
- Optional filtering by category or date range
- Success messages on create/edit/delete
- Clean, responsive UI built with minimal CSS

---

## ⚙️ Setup Instructions

### 1. Clone this repository
```bash
git clone https://github.com/<your-username>/Expense-Tracker.git
cd Expense-Tracker/expense_tracker
### 2. Apply migrations
python manage.py makemigrations
python manage.py migrate

### 3.Create a superuser (admin account)
python manage.py createsuperuser

### 4. Run the development server
python manage.py runserver

🗂️ Project Structure
expense_tracker/
├─ expense_tracker/        # Project settings
│  └─ settings.py
├─ expenses/               # Core app
│  ├─ models.py            # Custom User, Expense model
│  ├─ views.py             # CRUD views
│  ├─ forms.py             # Validation and form logic
│  ├─ urls.py              # App routes
│  └─ templates/expenses/  # All templates (list, form, delete, register, login)
├─ manage.py
└─ README.md

