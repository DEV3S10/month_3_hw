from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class BlogUser(AbstractUser):
    age = models.IntegerField()
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'age']
