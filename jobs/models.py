from django.db import models


class Job(models.Model):
    title= models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    description = models.CharField()
    languages= models.CharField(max_length=200)
    github_link = models.CharField()



