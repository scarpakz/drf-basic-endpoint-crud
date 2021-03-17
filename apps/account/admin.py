from django.contrib import admin
from .models import (
    Profile,
)
class ProfileTable(admin.TabularInline):
    model = Profile

class ProfileDisplay(admin.ModelAdmin):
    model = Profile
    list_display = ['user', 'last_name', 'first_name', 'middle_name', 'type']

# Model Registration
admin.site.register(Profile, ProfileDisplay)