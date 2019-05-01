from django.db import models
import django


class Blog(models.Model):
    title = models.CharField(max_length=255)
    Author = models.CharField(max_length=255)
    pub_date = models.DateField(("Date"), default=django.utils.timezone.now)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
