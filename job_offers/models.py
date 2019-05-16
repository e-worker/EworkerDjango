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
    job_skill = models.ForeignKey('JobOfferSkill', models.DO_NOTHING)
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

    def get_info(self):
        degree_course_info = OfferDegreeCourse.objects.filter(job_offer=self).values("degree_course__name")
        skills_info = JobInfo.objects.filter(job_offer=self).values('job_skill__skill__name').distinct() 
        skills = []
        degree_course = []
        for skill in skills_info:
            skills.append(skill["job_skill__skill__name"])
        for degree in degree_course_info:
            degree_course.append(degree["degree_course__name"])
        
        salary_from = self.sallary_from
        
        context = {
            'degree_course': degree_course,
            'skills': skills,
            'salary_from': salary_from,
        }
        return context

    def match(self, student: 'student.Student'):
        student_matching_info = student.get_matching_info()
        job_offer_matching_info = self.get_info()
        job_req_skills = len(job_offer_matching_info["skills"]) + 2 # skills + (salary & degree)
        student_matched_skills = 0
        for skill in student_matching_info["skills"]:
            if skill in job_offer_matching_info["skills"]:
                student_matched_skills+=1
        if job_offer_matching_info["salary_from"] >= student_matching_info["salary_from"]:
            student_matched_skills+=1
        for degree in student_matching_info["degree_course"]:
            if degree in job_offer_matching_info["degree_course"]:
                student_matched_skills+=1
                 
                
        percentage = student_matched_skills/job_req_skills
        match = OfferMatchStudent(student=student, percentage=percentage)
        return match

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
    # job_info = models.ForeignKey(JobInfo, models.DO_NOTHING)
    def __str__(self):
        return str(self.skill)

class OfferMatchStudent(models.Model):
    id = models.AutoField(primary_key = True)
    student = models.ForeignKey('student.Student', models.DO_NOTHING)
    percentage = models.FloatField()

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
