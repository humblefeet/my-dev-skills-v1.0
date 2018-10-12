from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Skill(models.Model):
    language = models.CharField(max_length = 50)
    experience = models.IntegerField()
    description = models.TextField(max_length=250)


    def __str__(self):
        return self.language

