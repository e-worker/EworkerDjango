# Generated by Django 2.1.7 on 2019-04-24 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='phone',
        ),
    ]