from django.contrib import admin
from .models import CharacterSet, Character, Meaning

# Register your models here.
admin.site.register(CharacterSet)
admin.site.register(Character)
admin.site.register(Meaning)