# Generated by Django 2.1.7 on 2019-04-26 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20190426_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='present',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
