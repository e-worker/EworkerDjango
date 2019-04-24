from django.db import models
from datetime import datetime
from employer.models import Company

class DegreeCourse(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=255)
    department = models.ForeignKey('Department', models.DO_NOTHING)
    def __str__(self):
        return str(self.name)+", "+str(self.department)

class Department(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return str(self.name)

class JobInfo(models.Model):
    id = models.AutoField(primary_key = True)
    text = models.TextField()
    job_offer = models.ForeignKey('JobOffer', models.DO_NOTHING)
    def __str__(self):
        return str(self.job_offer)    

class JobOffer(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=50)
    sallary_from = models.IntegerField()
    sallary_to = models.IntegerField()
    creation_date = models.DateTimeField(default=datetime.now)
    description = models.CharField(max_length=250)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    def __str__(self):
        return str(self.title)

class JobOfferLanguage(models.Model):
    id = models.AutoField(primary_key = True)
    language = models.ForeignKey('Language', models.DO_NOTHING)
    language_lvl = models.ForeignKey('LanguageLvl', models.DO_NOTHING)
    job_offer = models.ForeignKey(JobOffer, models.DO_NOTHING, blank=True, null=True)
    def __str__(self):
        return str(self.language)+" : "+str(self.language_lvl)

class JobOfferSkill(models.Model):
    id = models.AutoField(primary_key = True)
    skill = models.ForeignKey('Skill', models.DO_NOTHING)
    job_info = models.ForeignKey(JobInfo, models.DO_NOTHING)
    def __str__(self):
        return str(self.skill)


class LanguageLvl(models.Model):
    id = models.AutoField(primary_key = True)
    level = models.CharField(max_length=50)
    def __str__(self):
        return str(self.level)

class Language(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return str(self.name)

class OfferDegreeCourse(models.Model):
    id = models.AutoField(primary_key = True)
    degree_course = models.ForeignKey(DegreeCourse, models.DO_NOTHING)
    job_offer = models.ForeignKey(JobOffer, models.DO_NOTHING)
    def __str__(self):
        return str(self.degree_course)

class Skill(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return str(self.name)
