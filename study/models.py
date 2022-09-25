from tkinter import CASCADE
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Vocabulary(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Vocas(models.Model):
    vocabulary = models.ForeignKey(Vocabulary, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    eng = models.CharField(max_length=50)
    kor = models.CharField(max_length=50)
    today = models.DateField(default=datetime.today)