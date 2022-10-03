from django.urls import path
from . import views

urlpatterns = [
    path("", views.study, name="study"),
    path("entrance/", views.entrance),
    path("registration/", views.register, name="registration"),
    path("vocabulary/", views.vocabulary, name="vocabulary"),
    path("create/", views.createvocabulary),
    path("vocabulary/<int:id>/", views.vocabulary_create),
    path("vocabulary/words/<int:id>/", views.vocabulary_words),
    path("vocabulary/words/<int:vocabulary_id>/delete/<int:voca_id>/", views.vocabulary_words_delete),
    path("vocabulary/words/<int:vocabulary_id>/edit/<int:voca_id>/", views.vocabulary_words_edit),
    
]
