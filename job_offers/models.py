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
        languages_info = JobOfferLanguage.objects.filter(job_offer=self).values("language__name")
        skills = []
        degree_course = []
        languages = []
        for skill in skills_info:
            skills.append(skill["job_skill__skill__name"])
        for degree in degree_course_info:
            degree_course.append(degree["degree_course__name"])
        for language in languages_info:
            languages.append(language['language__name'])

        salary_from = self.sallary_from
        salary_to = self.sallary_to
        context = {
            'degree_course': degree_course,
            'skills': skills,
            'salary_from': salary_from,
            'salary_to': salary_to,
            'languages': languages,
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
        match = OfferMatchStudent(offer=self, percentage=percentage)
        return match

    def filter_offer(self, **data):
        offer_info = self.get_info()
        filter_required = 0 
        filter_offer = 0
        print(data)
        if data['salary_from']!='':
            salary_from = data['salary_from']
            filter_required+=1
            if int(salary_from) <= offer_info["salary_from"]:
                filter_offer+=1
                print('ok')
        if data['salary_to']!='':
            salary_to = data['salary_to']
            filter_required+=1
            if int(salary_to) >= offer_info["salary_to"]:
                filter_offer+=1
                print('ok')
        if data['degree_course'] is not None and data['degree_course']!='':
            degree = data['degree_course']
            print(data['degree_course'])
            filter_required+=1  
            for d in offer_info["degree_course"]:
                if d in degree:
                    filter_offer+=1
                    print('ok')
        if data['language'] is not None and data['language']!='':
            language = data['language']
            filter_required+=1  
            for l in offer_info['languages']:
                if l in language:
                    filter_offer+=1
                    print('ok')
        if data['skills'] is not None and data['skills']!='' :
            skills = data['skills']
            filter_required+=1 
            for skill in offer_info['skills']:
                if skill in skills:
                    filter_offer+=1
                    print('**ok**')
        print('{0}/{1}'.format(filter_offer,filter_required))
        print("******")
        print(offer_info)
        print(data)
        print("**********")
        if filter_offer>=filter_required:
            return True
        return False

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
    offer = models.ForeignKey(JobOffer, models.DO_NOTHING)
    percentage = models.FloatField()

    def get_percent(self):
        p = self.percentage * 100
        return int(p)

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
