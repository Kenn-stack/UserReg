from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ('firstname', 'lastname', 'middlename', 'date_of_birth')


