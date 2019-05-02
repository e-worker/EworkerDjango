from django.db import models
from datetime import datetime
from users.models import CustomUser
# Create your models here.

class Message(models.Model):
    id = models.AutoField(primary_key = True)
    header = models.CharField(max_length=50)
    content = models.CharField(max_length=512)
    creation_date = models.DateTimeField(default=datetime.now)
    msg_from = models.ForeignKey(CustomUser, related_name='sender', on_delete=models.DO_NOTHING)
    msg_to = models.ForeignKey(CustomUser, related_name='receiver', on_delete=models.DO_NOTHING)
    def __str__(self):
        return str(self.header)