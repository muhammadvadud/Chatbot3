from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    img = models.ImageField(upload_to="avatar", default="avatar/default.jpg")
    phone = models.IntegerField(null=True,blank=True)
