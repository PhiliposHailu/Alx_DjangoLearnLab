from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(max_length=200)
    profile_picture = models.ImageField(null=True)
    followers = models.ManyToManyField('self', symmetrical=False)
