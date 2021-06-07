from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300, default="")
    work = models.CharField(max_length=300, default="")
    github = models.CharField(max_length=300, default="")
