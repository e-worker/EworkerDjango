# Generated by Django 2.1.7 on 2019-04-26 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_offers', '0004_auto_20190424_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobofferskill',
            name='job_info',
        ),
        migrations.AddField(
            model_name='jobinfo',
            name='job_skill',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='job_offers.JobOfferSkill'),
            preserve_default=False,
        ),
    ]