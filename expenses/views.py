# expenses/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum
from .forms import UserCreationForm
from django.shortcuts import redirect
from django.utils import timezone

# List View with filtering and total calculation
class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expense
    template_name = "expense_list.html"
    context_object_name = "expenses"
    paginate_by = 20

    def get_queryset(self):
        qs = Expense.objects.filter(user=self.request.user)
        # optional filters via query params
        category = self.request.GET.get("category")
        start_date = self.request.GET.get("start_date")
        end_date = self.request.GET.get("end_date")
        if category:
            qs = qs.filter(category=category)
        if start_date:
            qs = qs.filter(date__gte=start_date)
        if end_date:
            qs = qs.filter(date__lte=end_date)
        return qs

# Add total calculation to context
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # total for current month
        today = timezone.localdate()
        month_total = Expense.objects.filter(
            user=self.request.user,
            date__year=today.year,
            date__month=today.month
        ).aggregate(total=Sum("amount"))["total"] or 0
        ctx["month_total"] = month_total
        ctx["categories"] = [c for c, _ in Expense.CATEGORY_CHOICES]
        return ctx

# Mixin to ensure only the owner can edit/delete an expense
class ExpenseOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        expense = self.get_object()
        return expense.user == self.request.user

# Create, Update, Delete Views
class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = "expense_form.html"
    success_url = reverse_lazy("expenses:list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, "Expense added successfully.")
        return response

# Update and Delete Views with ownership check
class ExpenseUpdateView(LoginRequiredMixin, ExpenseOwnerMixin, UpdateView):
    model = Expense
    form_class = ExpenseForm
    template_name = "expense_form.html"
    success_url = reverse_lazy("expenses:list")

    def form_valid(self, form):
        messages.success(self.request, "Expense updated successfully.")
        return super().form_valid(form)

class ExpenseDeleteView(LoginRequiredMixin, ExpenseOwnerMixin, DeleteView):
    model = Expense
    template_name = "expense_confirm_delete.html"
    success_url = reverse_lazy("expenses:list")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Expense deleted successfully.")
        return super().delete(request, *args, **kwargs)

# Optional: simple registration view
class RegisterView(FormView):
    template_name = "registration/registration.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Registration successful. You can log in now.")
        return super().form_valid(form)

    
