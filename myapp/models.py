from django import forms
from django.db import models
from django.db.models import Model
# Create your models here.

# models.py

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    

