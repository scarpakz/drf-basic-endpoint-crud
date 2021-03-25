from django.contrib import admin
from .models import (
    Language,
)
class LanguagesTabular(admin.TabularInline):
    model = Language

class LanguagesAdmin(admin.ModelAdmin):
    model = Language
    list_display = ['name', 'paradigm',]

admin.site.register(Language, LanguagesAdmin)