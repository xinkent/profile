from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()