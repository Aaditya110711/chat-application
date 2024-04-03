from django.contrib import admin
from chatapp.models import (Friend, ChatMessage)
# Register your models here.


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile']

admin.site.register(ChatMessage)