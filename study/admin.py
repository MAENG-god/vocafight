from django.contrib import admin
from .models import Vocas, Vocabulary, Vocabulary_example, Vocabulary_example_deleted, Vocas_example
# Register your models here.

admin.site.register(Vocas)
admin.site.register(Vocabulary)
admin.site.register(Vocabulary_example)
admin.site.register(Vocabulary_example_deleted)
admin.site.register(Vocas_example)
