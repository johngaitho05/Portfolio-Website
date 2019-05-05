from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=500)
    message = models.TextField(default=' ')

    def __str__(self):
        return self.email

