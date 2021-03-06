from django.db import models

# Create your models here.
class User(models.Model):
    name =  models.CharField(max_length=140)
    email = models.CharField(max_length=140)
    password = models.CharField(max_length=32)
    is_super = models.BooleanField()
    is_enable = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)