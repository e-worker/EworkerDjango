from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    isEmployer = models.BooleanField(default = False)
    doneProfileEdit = models.BooleanField(default = False, blank = True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return str(self.username)