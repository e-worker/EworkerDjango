# Generated by Django 2.1.7 on 2019-04-24 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_offers', '0004_auto_20190424_1800'),
        ('student', '0003_remove_student_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentlanguage',
            name='language_lvl',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='job_offers.LanguageLvl'),
            preserve_default=False,
        ),
    ]