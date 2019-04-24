from django.db import models
from datetime import datetime
from users.models import CustomUser

# Create your models here.
class Company(models.Model):
    id = models.AutoField(primary_key = True)
    company_name = models.CharField(max_length=50)
    city = models.CharField(max_length=127)
    street = models.CharField(max_length=127, blank=True, null=True)
    house_number = models.CharField(max_length=20)
    flat_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=127)
    description = models.CharField(max_length=255)
    creation_date = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(CustomUser, models.DO_NOTHING)

    def __str__(self):
        return str(self.company_name)
