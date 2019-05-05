from django.db import models
from datetime import datetime
from job_offers.models import DegreeCourse, Language, Skill, JobOffer
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
    salary_from = models.IntegerField(blank=True, null=True)
    salary_to = models.IntegerField(blank=True, null=True)
    document_url = models.CharField(max_length=255, blank=True, null=True)
    interest_text = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(CustomUser, models.DO_NOTHING)
    def __str__(self):
        return str(self.name)+" "+str(self.surname)
    def get_info(self):
        salary_from = self.salary_from
        salary_to = self.salary_to
        degree_course = StudentDegreeCourse.objects.filter(student=self)
        skills = StudentInfo.objects.filter(student=self) #poprawka (wez tylko skillsy)
        language = StudentLanguage.objects.filter(student=self)
        context={
            'salary_from': salary_from,
            'salary_to': salary_to,
            'degree_course': degree_course,
            'skills': skills,
            'language': language,
        }
        return context


    def get_matching_info(self):
        """matching categories
            degree course
            experience
            internship
            organizations
            courses
            ca$h
        """
        degree_course_info = StudentDegreeCourse.objects.filter(student=self).values("degree_course__name")
        skills_info = StudentInfo.objects.filter(student=self).values('skill__skill__name').distinct()
        skills = []
        degree_course = []
        for skill in skills_info:
            skills.append(skill["skill__skill__name"])
        for degree in degree_course_info:
            degree_course.append(degree["degree_course__name"])
        salary_from = self.salary_from   

        #bierz po jednym, pozniej zrob slownik z ofertami i  do kazdej oferty obliczaj dopasowanie

        context = {
            'degree_course': degree_course,
            'skills': skills,
            'salary_from': salary_from,
        }
        return context

    def match(self, job_offer: JobOffer):
        student_matching_info = self.get_matching_info()
        job_offer_matching_info = job_offer.get_info()
        job_req_skills = len(job_offer_matching_info["skills"]) + 2 # skills + (salary & degree)
        student_matched_skills = 0
        for skill in student_matching_info["skills"]:
            print(skill)
            if skill in job_offer_matching_info["skills"]:
                print("added")
                student_matched_skills+=1
        if job_offer_matching_info["salary_from"] >= student_matching_info["salary_from"]:
            print("salary matching")
            student_matched_skills+=1
        for degree in student_matching_info["degree_course"]:
            if degree in job_offer_matching_info["degree_course"]:
                student_matched_skills+=1
                print(degree)
            
                
        percentage = student_matched_skills/job_req_skills
        match = StudentMatchOffer(offer=job_offer, percentage=percentage)
        return match


class StudentDegreeCourse(models.Model):
    id = models.AutoField(primary_key = True)
    student = models.ForeignKey(Student, models.DO_NOTHING)
    degree_course = models.ForeignKey(DegreeCourse, models.DO_NOTHING)
    def __str__(self):
        return str(self.student)+" : "+str(self.degree_course)


class StudentInfo(models.Model):
    id = models.AutoField(primary_key = True)
    text = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    present = models.BooleanField(blank=True, null=True, default=False)
    skill = models.ForeignKey('StudentSkill', models.DO_NOTHING)
    student = models.ForeignKey(Student, models.DO_NOTHING)
    def __str__(self):
        return str(self.student)

class StudentMatchOffer(models.Model):
    id = models.AutoField(primary_key = True)
    offer = models.ForeignKey(JobOffer, models.DO_NOTHING)
    percentage = models.FloatField()

class StudentLanguage(models.Model):
    id = models.AutoField(primary_key = True)
    student = models.ForeignKey(Student, models.DO_NOTHING)
    language = models.ForeignKey(Language, models.DO_NOTHING)
    language_lvl = models.ForeignKey('job_offers.LanguageLvl', models.DO_NOTHING)
    def __str__(self):
        return str(self.student)+": "+str(self.language)+" "+str(self.language_lvl)


class StudentSkill(models.Model):
    id = models.AutoField(primary_key = True)
    skill = models.ForeignKey(Skill, models.DO_NOTHING)
    # student_info = models.ForeignKey(StudentInfo, models.DO_NOTHING)
    def __str__(self):
        return str(self.skill)