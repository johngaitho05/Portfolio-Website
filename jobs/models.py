from django.db import models


class Job(models.Model):
    title= models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    languages= models.CharField(max_length=200)
    github_link = models.CharField(max_length=500)

    def summary(self):
        return self.description[:200]

    def __str__(self):
        return self.title

    def langs(self):
        return self.languages.split(',')




