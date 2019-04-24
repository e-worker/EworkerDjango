# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=50)
    city = models.CharField(max_length=127)
    street = models.CharField(max_length=127, blank=True, null=True)
    house_number = models.CharField(max_length=20)
    flat_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=127)
    phone = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    creation_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'company'


class DegreeCourse(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    department = models.ForeignKey('Department', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'degree_course'


class Department(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'department'


class JobInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.TextField()
    job_offer = models.ForeignKey('JobOffer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'job_info'


class JobOffer(models.Model):
    id = models.IntegerField(primary_key=True)
    sallary_from = models.IntegerField()
    sallary_to = models.IntegerField()
    creation_date = models.DateTimeField()
    description = models.CharField(max_length=250)
    company = models.ForeignKey(Company, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'job_offer'


class JobOfferLanguage(models.Model):
    id = models.IntegerField(primary_key=True)
    language = models.ForeignKey('Language', models.DO_NOTHING)
    job_offer = models.ForeignKey(JobOffer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_offer_language'


class JobOfferSkill(models.Model):
    id = models.IntegerField(primary_key=True)
    skill = models.ForeignKey('Skill', models.DO_NOTHING)
    job_info = models.ForeignKey(JobInfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'job_offer_skill'


class Language(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'language'


class LanguageLvl(models.Model):
    id = models.IntegerField(primary_key=True)
    level = models.CharField(max_length=50)
    language = models.ForeignKey(Language, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'language_lvl'


class Message(models.Model):
    id = models.IntegerField(primary_key=True)
    header = models.CharField(max_length=50)
    content = models.CharField(max_length=512)
    creation_date = models.DateTimeField()
    student = models.ForeignKey('Student', models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'message'


class OfferDegreeCourse(models.Model):
    id = models.IntegerField(primary_key=True)
    degree_course = models.ForeignKey(DegreeCourse, models.DO_NOTHING)
    job_offer = models.ForeignKey(JobOffer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'offer_degree_course'


class Skill(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'skill'


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=127)
    password = models.CharField(max_length=255)
    city = models.CharField(max_length=127, blank=True, null=True)
    street = models.CharField(max_length=127, blank=True, null=True)
    house_number = models.CharField(max_length=20, blank=True, null=True)
    flat_number = models.CharField(max_length=20, blank=True, null=True)
    creation_date = models.DateTimeField()
    sallary_from = models.IntegerField(blank=True, null=True)
    sallary_to = models.IntegerField(blank=True, null=True)
    document_url = models.CharField(max_length=255, blank=True, null=True)
    interest_text = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class StudentDegreeCourse(models.Model):
    id = models.IntegerField(primary_key=True)
    student = models.ForeignKey(Student, models.DO_NOTHING)
    degree_course = models.ForeignKey(DegreeCourse, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'student_degree_course'


class StudentInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    present = models.FloatField(blank=True, null=True)
    student = models.ForeignKey(Student, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'student_info'


class StudentLanguage(models.Model):
    id = models.IntegerField(primary_key=True)
    student = models.ForeignKey(Student, models.DO_NOTHING)
    language = models.ForeignKey(Language, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'student_language'


class StudentSkill(models.Model):
    id = models.IntegerField(primary_key=True)
    skill = models.ForeignKey(Skill, models.DO_NOTHING)
    student_info = models.ForeignKey(StudentInfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'student_skill'
