from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_worker = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
