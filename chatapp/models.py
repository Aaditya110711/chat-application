from django.db import models

# Create your models here.


class Friend(models.Model):
    profile = models.OneToOneField("account.Profile", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.profile.name
