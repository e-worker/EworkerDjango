# Generated by Django 2.1.7 on 2019-04-26 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20190426_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]