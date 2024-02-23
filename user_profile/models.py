from django.db import models
from django.contrib.auth.models import User
from core.models import BaseModel
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Account(BaseModel):
    user = models.OneToOneField(User, related_name='account_user', on_delete=models.CASCADE, primary_key=True)
    promotional_point = models.IntegerField(default=0)
    phone = models.CharField(max_length=15)
    is_verified = models.BooleanField(default=False)
    receive_announcement = models.BooleanField(default=False)
    keywords = ArrayField(models.CharField(max_length=20), default=[], blank=True)


    

