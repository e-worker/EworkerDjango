# Generated by Django 2.1.7 on 2019-05-22 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0003_remove_company_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='image',
            field=models.CharField(blank=True, max_length=511),
        ),
    ]
