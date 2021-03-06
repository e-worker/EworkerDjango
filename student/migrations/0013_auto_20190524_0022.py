# Generated by Django 2.1.7 on 2019-05-24 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_auto_20190524_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='city',
            field=models.CharField(blank=True, default='', max_length=127, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='description',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='document_url',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(default='', max_length=127),
        ),
        migrations.AlterField(
            model_name='student',
            name='flat_number',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='house_number',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to='gallery_pics/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='interest_text',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='street',
            field=models.CharField(blank=True, default='', max_length=127, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='surname',
            field=models.CharField(default='', max_length=50),
        ),
    ]
