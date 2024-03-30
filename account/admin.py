from django.contrib import admin
from account.models import (Profile, OtpCode)

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    readonly_fields = ['preview']


@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'code']
