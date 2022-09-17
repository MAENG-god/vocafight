from django.db import models
from datetime import datetime

# Create your models here.

class Voca(models.Model):
    eng = models.CharField(max_length=50)
    kor = models.CharField(max_length=50)
    today = models.DateField(default=datetime.today)