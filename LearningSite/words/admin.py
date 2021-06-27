from django.contrib import admin
from .models import CharacterSet, Vocabulary, Meaning, Score

# Register your models here.
admin.site.register(CharacterSet)
admin.site.register(Vocabulary)
admin.site.register(Meaning)
admin.site.register(Score)