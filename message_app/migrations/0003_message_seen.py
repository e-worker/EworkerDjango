# Generated by Django 2.1.7 on 2019-05-22 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_app', '0002_auto_20190502_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='seen',
            field=models.BooleanField(default=False),
        ),
    ]
