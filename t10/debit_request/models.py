from django.db import models

# Create your models here.
class Debit(models.Model):
    requester = models.CharField(max_length=244)
    value = models.CharField(max_length=244, default='0')
    target = models.CharField(max_length=14)
    super_user = models.BooleanField()
    is_enable =  models.BooleanField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)