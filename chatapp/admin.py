from django.contrib import admin
from chatapp.models import Friend
# Register your models here.


# class FriendAdmin(admin.ModelAdmin):
#     list_display = ['id', 'profile.name']
admin.site.register(Friend)