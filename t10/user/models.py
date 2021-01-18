from django.db import models

# Create your models here.
class User():
    login = models.CharField(max_length=11, blank=False)
    password = models.CharField(max_length=8, blank=False)
    