from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    frase = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to='users/', default='users/default.jpg')
    profile_color = models.CharField(max_length=30, blank=True)
    adult_content = models.BooleanField(default=False)