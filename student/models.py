from django.db import models
from datetime import datetime
from job_offers.models import DegreeCourse, Language, Skill
from users.models import CustomUser
# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=127)
    city = models.CharField(max_length=127, blank=True, null=True)
    street = models.CharField(max_length=127, blank=True, null=True)
    house_number = models.CharField(max_length=20, blank=True, null=True)
    flat_number = models.CharField(max_length=20, blank=True, null=True)
    creation_date = models.DateTimeField(default=datetime.now)
    sallary_from = models.IntegerField(blank=True, null=True)
    sallary_to = models.IntegerField(blank=True, null=True)
    document_url = models.CharField(max_length=255, blank=True, null=True)
    interest_text = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(CustomUser, models.DO_NOTHING)

class StudentDegreeCourse(models.Model):
    id = models.AutoField(primary_key = True)
    student = models.ForeignKey(Student, models.DO_NOTHING)
    degree_course = models.ForeignKey(DegreeCourse, models.DO_NOTHING)



class StudentInfo(models.Model):
    id = models.AutoField(primary_key = True)
    text = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    present = models.FloatField(blank=True, null=True)
    student = models.ForeignKey(Student, models.DO_NOTHING)



class StudentLanguage(models.Model):
    id = models.AutoField(primary_key = True)
    student = models.ForeignKey(Student, models.DO_NOTHING)
    language = models.ForeignKey(Language, models.DO_NOTHING)



class StudentSkill(models.Model):
    id = models.AutoField(primary_key = True)
    skill = models.ForeignKey(Skill, models.DO_NOTHING)
    student_info = models.ForeignKey(StudentInfo, models.DO_NOTHING)
