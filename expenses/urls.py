# expenses/urls.py
from django.urls import path
from .views import ExpenseListView, ExpenseCreateView, ExpenseUpdateView, ExpenseDeleteView, RegisterView

app_name = "expenses"

urlpatterns = [
    path("", ExpenseListView.as_view(), name="list"),
    path("create/", ExpenseCreateView.as_view(), name="create"),
    path("<int:pk>/edit/", ExpenseUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", ExpenseDeleteView.as_view(), name="delete"),
    path("register/", RegisterView.as_view(), name="register"),  # optional simple registration
]
