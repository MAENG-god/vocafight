from django.urls import path
from . import views

urlpatterns = [
    path("", views.study, name="study"),
    path("registration/", views.register, name="registration"),
    path("vocabulary/", views.vocabulary, name="vocabulary"),
    path("vocabulary/<str:date>/", views.vocabulary_daily),
]
