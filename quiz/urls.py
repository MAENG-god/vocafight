from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.quiz, name="quiz"),
    path("all/", views.quiz_all),
    path("start/", views.start, name="start"),
]