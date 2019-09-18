from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    
    email = models.EmailField(max_length=200)
    # name = models.CharField(max_length=200)

    def __str__(self):
        return self.email