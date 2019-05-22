from django.db import models
from django.contrib.auth.models import AbstractUser
from django.apps import apps

class CustomUser(AbstractUser):

    isEmployer = models.BooleanField(default = False)
    doneProfileEdit = models.BooleanField(default = False, blank = True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return str(self.username)
    
    def get_unread_messages(self):
        Model = apps.get_model('message_app', 'Message')
        messages = Model.objects.filter(msg_to=self, seen=False).count()
        print(messages)
        return messages