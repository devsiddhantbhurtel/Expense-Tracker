# expenses/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    pass # Custom user model will extend later if needed

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Food','Food'),
        ('Transport','Transport'),
        ('Rent','Rent'),
        ('Utilities','Utilities'),
        ('Other','Other'),
    ]

    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')
    date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='expenses')

    created_at = models.DateTimeField(auto_now_add=True)

    # Meta options
    class Meta:
        ordering = ["-date", "-created_at"]

    # String representation of the model
    def __str__(self):
        return f"{self.title} - {self.amount}"
