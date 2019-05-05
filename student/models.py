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
        languages_info = StudentLanguage.objects.filter(student=self).values('language__name', 'language_lvl__level')
        skills = []
        degree_course = []
        languages = []
        languages_lvl = []
        for skill in skills_info:
            skills.append(skill["skill__skill__name"])
        for degree in degree_course_info:
            degree_course.append(degree["degree_course__name"])
        for language in languages_info:
            languages.append(language["language__name"])
            languages_lvl.append(language["language_lvl__level"])

        
        salary_from = self.salary_from   
        salary_to = self.salary_to
        #bierz po jednym, pozniej zrob slownik z ofertami i  do kazdej oferty obliczaj dopasowanie

        context = {
            'degree_course': degree_course,
            'skills': skills,
            'languages': languages,
            'languages_lvl': languages_lvl,
            'salary_from': salary_from,
            'salary_to': salary_to,
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

    def filter_student(self, **data):
        student_info = self.get_matching_info()
        salary_from = data['salary_from']
        salary_to = data['salary_to']
        degree = data['degree_course']
        language = data['language']
        # language_lvl = data['language_lvl']
        skills = data['skills']
        filter_required = 2 + len(degree) + len(language) + len(skills)
        filter_student = 0
        if salary_from <= student_info["salary_from"]:
            filter_student+=1
        if salary_to <= student_info["salary_to"]:
            filter_student+=1
        for d in student_info["degree_course"]:
            if d in degree:
                filter_student+=1
        for l in student_info['languages']:
            if l in language:
                filter_student+=1
        for skill in student_info['skills']:
            if skill in skills:
                filter_student+=1
        if filter_student>=filter_required:
            return True
        return False

    # def return_dict(self):
    #     salary_from = 2
    #     salary_to = 3
    #     degree = ['Automatyka i Robotyka']
    #     skills = ['Działalność w organizacjach']
    #     language = ['Angielski']
    #     data = {
    #         'salary_from': salary_from,
    #         'salary_to': salary_to,
    #         'degree_course': degree,
    #         'skills': skills,
    #         'language': language,
    #     }
    #     return data


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