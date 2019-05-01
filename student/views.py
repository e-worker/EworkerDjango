from django.shortcuts import render, redirect
from .models import Student, StudentInfo, StudentSkill, StudentDegreeCourse, StudentLanguage
from job_offers.models import DegreeCourse, LanguageLvl, Language, Skill
from django.contrib.auth.decorators import login_required
from employer.views import edit_profile as employer_edit_profile


# Create your views here.
@login_required()
def edit_profile(request):
    if not request.user.isEmployer:
        student = Student.objects.get(user__id=request.user.id)
        student_courses = StudentDegreeCourse.objects.filter(student=student)
        student_languages = StudentLanguage.objects.filter(student=student)
        student_skills = StudentInfo.objects.filter(student=student)

        courses = DegreeCourse.objects.all()
        languages = Language.objects.all()
        languageLvls = LanguageLvl.objects.all()
        skills = Skill.objects.all()
        context = {
            'courses': courses,
            'languages': languages,
            'languageLvls': languageLvls,
            'skills': skills,
            'student': student,
            'student_courses': student_courses,
            'student_languages': student_languages,
            'student_skills': student_skills,
        }
        if request.method == "POST":

            city = request.POST['city']
            street = request.POST['street']
            house_number = request.POST['house_number']
            flat_number = request.POST['flat_number']
            salary_from = request.POST['salary_from']
            salary_to = request.POST['salary_to']
            document_url = request.POST['document_url']
            interest_text = request.POST['interest_text']
            description = request.POST['description']
            
            courses  = request.POST.getlist('course')
            languages = request.POST.getlist('language')
            languagesLvls = request.POST.getlist('languageLvl')
            skills = request.POST.getlist('skill')
            skillsTexts = request.POST.getlist('skillText')
            skillsDateFrom = request.POST.getlist('date_from')
            skillsDateTo = request.POST.getlist('date_to')
            skillsPresent = request.POST.getlist('present')

            #student profile update
            student.city = city
            student.street = street
            student.house_number = house_number
            student.flat_number = flat_number
            student.salary_from = salary_from
            student.salary_to = salary_to
            student.document_url = document_url
            student.interest_text = interest_text
            student.description = description
            student.save()

            StudentDegreeCourse.objects.filter(student=student).delete()
            for course in courses: # szukam czy juz  taki studentdegree bylo dodane, jesli nie to tworze 
                if not StudentDegreeCourse.objects.filter(student = student, degree_course__name = course).exists():
                    degree_course = DegreeCourse.objects.get(name=course)
                    student_degree_course = StudentDegreeCourse(student=student, degree_course = degree_course)
                    student_degree_course.save()               
            
            StudentLanguage.objects.filter(student=student).delete()
            for index, language in enumerate(languages):
                if not StudentLanguage.objects.filter(student=student, language__name=language).exists():
                    language_model = Language.objects.get(name=language)
                    languageLvl = LanguageLvl.objects.get(level=languagesLvls[index])
                    student_language = StudentLanguage(student=student, language=language_model, language_lvl=languageLvl)
                    student_language.save()

            StudentInfo.objects.filter(student=student).delete()
            for index, skill in enumerate(skills):
                if not StudentInfo.objects.filter(student=student, skill__skill__name=skill, text=skillsTexts[index]).exists():
                    skill_model = Skill.objects.get(name=skill)
                    if not StudentSkill.objects.filter(skill=skill_model).exists():
                        student_skill = StudentSkill(skill=skill_model)
                        student_skill.save()
                    else:
                        student_skill = StudentSkill.objects.get(skill=skill_model)
                    student_info = StudentInfo(text=skillsTexts[index], student=student, skill=student_skill)
                    # , start_date=, end_date=skillsDateTo[index], present=skillsPresent[index],
                    if skillsDateFrom[index] is not "":
                        student_info.start_date=skillsDateFrom[index]
                    if skillsDateTo[index] is not "":
                        student_info.end_date=skillsDateTo[index]
                    if skillsPresent[index] == "True":
                        student_info.present=True
                    elif skillsPresent[index] == "False":
                        student_info.present=False    
                    
                    student_info.save()
                    
        
        return render(request, 'student/edit_profile.html', context)
    else:
        return employer_edit_profile(request)

def student_offers(request):
    return render(request, 'student/student_offers.html')