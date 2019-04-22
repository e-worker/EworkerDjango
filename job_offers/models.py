from django.db import models
from datetime import datetime
# Create your models here.



class DegreeCourse(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return str(self.name)

class Department(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 128)
    degree_course = models.ManyToManyField(DegreeCourse)


class Skill(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=40)
    def __str__(self):
        return str(self.name)

class LanguageLvl(models.Model):
    id = models.AutoField(primary_key = True)
    level = models.CharField(max_length = 2)


class Language(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=40)
    language_lvl = models.ForeignKey(LanguageLvl, on_delete = models.CASCADE)
    def __str__(self):
        return str(self.name)



class StudentSkill(models.Model):
    id = models.AutoField(primary_key = True)
    skill = models.ForeignKey(Skill, on_delete = models.CASCADE)
    
    def __str__(self):
        return str(self.skill)
 
class StudentLanguage(models.Model):
    id = models.AutoField(primary_key = True)
    language = models.ForeignKey(Language, on_delete = models.CASCADE)
    
    def __str__(self):
        return str(self.language)


class StudentDegreeCourse(models.Model):
    id = models.AutoField(primary_key = True)
    degree_course = models.ForeignKey(DegreeCourse, on_delete = models.CASCADE)
    
    def __str__(self):
        return str(self.id)
 
class StudentTypeInfo(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 30)

class StudentInfo(models.Model):
    id = models.AutoField(primary_key = True)
    text = models.TextField(max_length = 255)
    student_type_info = models.ForeignKey(StudentTypeInfo, on_delete = models.CASCADE)


class Student(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 30)
    surname = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 12)
    email = models.CharField(max_length = 127)
    city = models.CharField(max_length = 40, blank = True)
    street = models.CharField(max_length = 40, blank = True)
    house_number = models.CharField(max_length = 5, blank = True)
    flat_number = models.CharField(max_length = 5, blank = True)
    creation_date = models.DateTimeField(default = datetime.now)
    salary_from = models.FloatField(blank=True)
    salary_to = models.FloatField(blank=True)
    document_url = models.CharField(max_length = 255, blank = True)
    interest_text = models.TextField(max_length = 500)
    decription = models.TextField(max_length = 500)
    student_info = models.ManyToManyField(StudentInfo)
    student_degree_course = models.ManyToManyField(StudentDegreeCourse)
    student_skill = models.ManyToManyField(StudentSkill)
    student_language = models.ManyToManyField(StudentLanguage)
    
 
 
class JobOfferSkill(models.Model):
    id = models.AutoField(primary_key = True)
    skill = models.ForeignKey(Skill, on_delete = models.CASCADE)
    
    def __str__(self):
        return str(self.skill)
 
 

class JobTypeInfo(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=40)
    def __str__(self):
        return str(self.name)
 
 
 
class JobInfo(models.Model):
    id = models.AutoField(primary_key = True)
    text = models.TextField(max_length=40)
    job_type_info = models.ForeignKey(JobTypeInfo,on_delete = models.CASCADE)
   
    def __str__(self):
        return str(self.job_type_info)
 
 
 
class JobOfferLanguage(models.Model):
    id = models.AutoField(primary_key = True)
    language = models.ForeignKey(Language, on_delete = models.CASCADE)
    
    def __str__(self):
        return str(self.language)




 
 
class OfferDegreeCourse(models.Model):
    id = models.AutoField(primary_key = True)
    degree_course = models.ForeignKey(DegreeCourse, on_delete = models.CASCADE)
    
    def __str__(self):
        return str(self.degree_course)
 
 
 
class JobOffer(models.Model):
    id = models.AutoField(primary_key = True)
    salary_from = models.FloatField()
    salary_to = models.FloatField()
    creation_date = models.DateTimeField(default = datetime.now)
    job_offer_skill = models.ManyToManyField(JobOfferSkill)
    job_info = models.ManyToManyField(JobInfo)
    job_offer_language = models.ManyToManyField(JobOfferLanguage)
    offer_degree_course = models.ManyToManyField(OfferDegreeCourse)
 
 
    def __str__(self):
        return str(self.id)

class Company(models.Model):
    id = models.AutoField(primary_key = True)
    company_name = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 12)
    email = models.CharField(max_length = 127)
    city = models.CharField(max_length = 40, blank = True)
    street = models.CharField(max_length = 40, blank = True)
    house_number = models.CharField(max_length = 5, blank = True)
    flat_number = models.CharField(max_length = 5, blank = True)
    creation_date = models.DateTimeField(default = datetime.now)
    decription = models.TextField(max_length = 500)
    job_offers = models.ManyToManyField(JobOffer)    