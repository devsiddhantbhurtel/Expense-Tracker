# expenses/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from .models import Expense, User

# Expense Form with validation
class ExpenseForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))

    class Meta:
        model = Expense
        fields = ["title", "amount", "category", "date"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder":"e.g. Lunch at Cafe"}),
            "amount": forms.NumberInput(attrs={"step":"0.01", "min":"0.01"}),
        }
    # Custom validation
    def clean_title(self):
        title = self.cleaned_data.get("title", "").strip()
        if not title:
            raise forms.ValidationError("Title cannot be empty.")
        return title
    
    # Custom validation
    def clean_amount(self):
        amount = self.cleaned_data.get("amount")
        if amount is None or amount <= 0:
            raise forms.ValidationError("Amount must be greater than 0.")
        return amount


class UserCreationForm(BaseUserCreationForm):
    """Custom user creation form for our custom User model."""
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make email field required
        self.fields['email'].required = True
