from django.db import models
from datetime import datetime
from job_offers.models import DegreeCourse, Language, Skill, JobOffer
from users.models import CustomUser
from PIL import Image
# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50, default='')
    surname = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=127, default='')
    city = models.CharField(max_length=127, blank=True, null=True, default='')
    street = models.CharField(max_length=127, blank=True, null=True, default='')
    house_number = models.CharField(max_length=20, blank=True, null=True, default='')
    flat_number = models.CharField(max_length=20, blank=True, null=True, default='')
    creation_date = models.DateTimeField(default=datetime.now)
    salary_from = models.IntegerField(blank=True, null=True, default=0)
    salary_to = models.IntegerField(blank=True, null=True, default=0)
    document_url = models.CharField(max_length=255, blank=True, null=True, default='')
    interest_text = models.CharField(max_length=255, blank=True, null=True, default='')
    description = models.CharField(max_length=255, blank=True, null=True, default='')
    image = models.ImageField(upload_to='gallery_pics/%Y/%m/%d/', default = 'default.png')
    user = models.ForeignKey(CustomUser, models.DO_NOTHING)
    def __str__(self):
        return str(self.name)+" "+str(self.surname)

    def save(self, *args, **kwargs):
       super(Student, self).save(*args, **kwargs)
       img = Image.open(self.image.path)
       output_size = (400, 400)
       img.thumbnail(output_size)
       img.save(self.image.path)

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
        skills_fullInfo = StudentInfo.objects.filter(student=self).values('skill__skill__name', 'text', 'start_date', 'end_date', 'present').distinct()
        languages_info = StudentLanguage.objects.filter(student=self).values('language__name', 'language_lvl__level')
        skills = []
        skillsFull = []
        skillsTemp = []
        degree_course = []
        languages = []
        languages_lvl = []
        for skill in skills_info:
            skills.append(skill["skill__skill__name"])
        for skillFull in skills_fullInfo:
            skillsTemp.append(skillFull["skill__skill__name"])
            skillsTemp.append(skillFull["text"])
            skillsTemp.append(skillFull["start_date"])
            skillsTemp.append(skillFull["end_date"])
            skillsTemp.append(skillFull["present"])
            skillsFull.append(skillsTemp)
            skillsTemp = []    
        for degree in degree_course_info:
            degree_course.append(degree["degree_course__name"])
        for language in languages_info:
            languages.append(language["language__name"])
            languages_lvl.append(language["language_lvl__level"])
        salary_from = self.salary_from   
        salary_to = self.salary_to
        #bierz po jednym, pozniej zrob slownik z ofertami i  do kazdej oferty obliczaj dopasowanie
        student_lang=zip(languages, languages_lvl)
        context = {
            'degree_course': degree_course,
            'skills': skills,
            'languages': languages,
            'languages_lvl': languages_lvl,
            'salary_from': salary_from,
            'salary_to': salary_to,
            'student_lang': student_lang,
            'skillsFull': skillsFull,
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
        match = StudentMatchOffer(student=self, percentage=percentage)
        return match

    def filter_student(self, **data):
        student_info = self.get_matching_info()
        print('---------')
        print(student_info)
        print(data)
        print('---------')
        # language_lvl = data['language_lvl']
        filter_required = 0 #nie trzeba wszystkich pól wypełniać(poprawic) liczyc w lepszy sposob filter_required
        filter_student = 0
        print('+++')
        # print(filter_required)
        if data['salary_from']!='':
            salary_from = data['salary_from']
            filter_required+=1
            print("*** salary from")
            print(filter_required)
            print("***")
            if int(salary_from) <= student_info["salary_from"]:
                filter_student+=1
        if data['salary_to']!='':
            salary_to = data['salary_to']
            filter_required+=1
            print("*** salary to")
            print(filter_required)
            print("***")
            if int(salary_to) >= student_info["salary_to"]:
                filter_student+=1
        if data['degree_course'] is not None and data['degree_course']!='':
            degree = data['degree_course']
            print(data['degree_course'])
            filter_required+=1  
            print("*** course")
            print(filter_required)
            print("***")
            for d in student_info["degree_course"]:
                if d in degree:
                    filter_student+=1
        if data['language'] is not None and data['language']!='':
            language = data['language']
            filter_required+=1  
            print("*** language")
            print(filter_required)
            print("***")           
            for l in student_info['languages']:
                if l in language:
                    filter_student+=1
        if data['skills'] is not None and data['skills']!='' :
            skills = data['skills']
            # print("{0}".format(len(skills)))
            filter_required+=1 
            print("*** skills")
            print(filter_required)
            print("***")
            for skill in student_info['skills']:
                if skill in skills:
                    filter_student+=1
        print(filter_required)
        if filter_student>=filter_required:
            print(filter_student)
            return True
        print(filter_student)
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
    student = models.ForeignKey(Student, models.DO_NOTHING)
    percentage = models.FloatField()

    def get_percent(self):
        p = self.percentage * 100
        return '{:.2f}%'.format(p)

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