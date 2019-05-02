from django.db import models
from datetime import datetime
from users.models import CustomUser
from django.forms.models import model_to_dict

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

    def received_messages(CustomUser: CustomUser):

        if not CustomUser.isEmployer:
            messages_from_me_to = Message.objects.filter(msg_from=CustomUser.id).values_list('msg_to_id', 'msg_to__company__company_name')
            messages_to_me = Message.objects.filter(msg_to=CustomUser.id).values_list('msg_from_id', 'msg_from__company__company_name')
        else:
            messages_from_me_to = Message.objects.filter(msg_from=CustomUser.id).values_list('msg_to_id', 'msg_to__student__name')
            messages_to_me = Message.objects.filter(msg_to=CustomUser.id).values_list('msg_from_id', 'msg_from__student__name')

        msg_from_me = set()
        for messages in messages_from_me_to:
            msg_from_me.add(messages[1])

        msg_to_me = set()
        for messages in messages_to_me:
            msg_to_me.add(messages[1])

        user_type = CustomUser.isEmployer

        return msg_from_me, msg_to_me, user_type