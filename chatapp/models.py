from django.db import models

# Create your models here.


class Friend(models.Model):
    profile = models.OneToOneField("account.Profile", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.profile.name

class ChatMessage(models.Model):
    body = models.TextField()
    msg_sender = models.ForeignKey("account.Profile", on_delete=models.CASCADE, related_name="msg_sender")
    msg_receiver = models.ForeignKey("account.Profile", on_delete=models.CASCADE, related_name="msg_receiver")
    seen = models.BooleanField(default=False)

    def __str__(self):
        return self.body
    