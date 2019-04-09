from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    isEmployer = models.BooleanField(default = False)
    doneProfileEdit = models.BooleanField(default = False, blank = True)
    def __str__(self):
        return self.username