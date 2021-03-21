from django.contrib import admin
from .models import CharacterSet, Vocabulary, Meaning

# Register your models here.
admin.site.register(CharacterSet)
admin.site.register(Vocabulary)
admin.site.register(Meaning)