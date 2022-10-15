from email.policy import default
from tkinter import CASCADE
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.forms import IntegerField

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

class Vocabulary_example(models.Model):
    name = models.CharField(max_length=100, default="example")
    
class Vocabulary_example_deleted(models.Model):
    user = models.CharField(max_length=100)

class Vocas_example(models.Model):
    vocabulary = models.ForeignKey(Vocabulary_example, on_delete=models.CASCADE)
    eng = models.CharField(max_length=50)
    kor = models.CharField(max_length=50)
    today = models.DateField(default=datetime.today)