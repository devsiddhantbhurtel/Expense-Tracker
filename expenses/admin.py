# expenses/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Expense

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("title", "amount", "category", "date", "user")
    list_filter = ("category", "date")
    search_fields = ("title",)
