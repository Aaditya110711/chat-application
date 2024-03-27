from django.contrib import admin
from chatapp.models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    readonly_fields = ['preview']