# Generated by Django 2.1.7 on 2019-05-25 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0005_auto_20190524_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(default='default.png', upload_to='gallery_pics/%Y/%m/%d/'),
        ),
    ]