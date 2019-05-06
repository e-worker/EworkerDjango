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

    def received_messages(user: CustomUser):

        user_type = user.isEmployer
        user_id = user.id

        if not user_type:
            messages_from_me_to = Message.objects.filter(msg_from=user_id).values_list('msg_to_id', 'msg_to__company__company_name')
            messages_to_me = Message.objects.filter(msg_to=user_id).values_list('msg_from_id', 'msg_from__company__company_name')
        else:
            messages_from_me_to = Message.objects.filter(msg_from=user_id).values_list('msg_to_id', 'msg_to__student__name', 'msg_to__student__surname')
            messages_to_me = Message.objects.filter(msg_to=user_id).values_list('msg_from_id', 'msg_from__student__name', 'msg_from__student__surname')

        msg_from_me = set()
        msg_to_me = set()
        all_messages = set()
        for messages in messages_from_me_to:
            msg_from_me.add(messages)
            all_messages.add(messages)

        for messages in messages_to_me:
            msg_to_me.add(messages)
            all_messages.add(messages)

        return msg_from_me, msg_to_me, all_messages, user_type

    def chat(user: CustomUser, number_id: int):
        user_type = user.isEmployer
        user_id = user.id

        messages = Message.objects.filter(msg_from=user_id, msg_to=number_id)
        messages2 = Message.objects.filter(msg_from=number_id, msg_to=user_id)
        all_messages = messages.union(messages2)
        all_messages.order_by('-creation_date')
        # all_messages = zip(messages, messages2).sort(key=['creation_date'])

        return all_messages