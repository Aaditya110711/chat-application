from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    pic = models.ImageField(upload_to="profile_pic/", null=True, blank=True)

    def preview(self):
        return mark_safe(f'<img src="{self.pic.url}" width="150" height="150" />')

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

