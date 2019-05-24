from django.shortcuts import render, redirect
from .models import Student, StudentInfo, StudentSkill, StudentDegreeCourse, StudentLanguage
from job_offers.models import JobOffer, DegreeCourse, LanguageLvl, Language, Skill
from django.contrib.auth.decorators import login_required
from employer.views import edit_profile as employer_edit_profile
from django.contrib import messages
from users.models import CustomUser
from django.core.files.storage import FileSystemStorage
from django.conf import settings


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
            image = request.FILES.get('image', 'default.png')
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

            # form validation
            if len(city) < 4:
                messages.error(request, 'Nazwa miasta nie moze byc tak krotka')
            else:
                if len(street) < 4:
                    messages.error(request, 'Nazwa ulicy nie moze byc tak krotka')
                else:
                    if len(str(house_number)) < 1:
                        messages.error(request, 'Podaj całkowity numer budynku')
                    else:
                        _salary_from = string_to_int(salary_from,
                                                     'Podaj całkowity dwucyfrowy dolny przedział zarobkowy na godzinę',
                                                     request,
                                                     2)
                        if _salary_from[0] and _salary_from[2]:
                            salary_from = _salary_from[1]
                            _salary_to = string_to_int(salary_to,
                                                       'Podaj całkowity dwucyfrowy górny przedział zarobkowy na godzinę',
                                                       request,
                                                       2)
                            if _salary_to[0] and _salary_to[2]:
                                salary_to = _salary_to[1]
                                if salary_from > salary_to:
                                    messages.error(request, 'Zarobki "od" nie mogą być wyższe niż zarobi "do"')
                                else:
                                    if len(interest_text) < 5:
                                        messages.error(request, 'Podaj jakieś swoje zainteresowania')
                                    else:
                                        if len(description) < 3:
                                            messages.error(request, 'Powiedz coś o sobie ;)')
                                        else:
                                            # student profile update
                                            student.city = city
                                            student.street = street
                                            student.house_number = house_number
                                            student.flat_number = flat_number
                                            student.salary_from = salary_from
                                            student.salary_to = salary_to
                                            student.document_url = document_url
                                            student.interest_text = interest_text
                                            student.description = description
                                            student.image = image
                                            student.save()

                                            #user profile edit set to done

                                            request.user.doneProfileEdit = 1

                                            StudentDegreeCourse.objects.filter(student=student).delete()
                                            for course in courses:  # szukam czy juz  taki studentdegree bylo dodane, jesli nie to tworze
                                                if not StudentDegreeCourse.objects.filter(student=student,
                                                                                          degree_course__name=course).exists():
                                                    degree_course = DegreeCourse.objects.get(name=course)
                                                    student_degree_course = StudentDegreeCourse(student=student,
                                                                                                degree_course=degree_course)
                                                    student_degree_course.save()

                                            StudentLanguage.objects.filter(student=student).delete()
                                            for index, language in enumerate(languages):
                                                if not StudentLanguage.objects.filter(student=student,
                                                                                      language__name=language).exists():
                                                    language_model = Language.objects.get(name=language)
                                                    languageLvl = LanguageLvl.objects.get(
                                                        level=languagesLvls[index])
                                                    student_language = StudentLanguage(student=student,
                                                                                       language=language_model,
                                                                                       language_lvl=languageLvl)
                                                    student_language.save()

                                            StudentInfo.objects.filter(student=student).delete()
                                            for index, skill in enumerate(skills):
                                                if not StudentInfo.objects.filter(student=student,
                                                                                  skill__skill__name=skill,
                                                                                  text=skillsTexts[index]).exists():
                                                    skill_model = Skill.objects.get(name=skill)
                                                    if not StudentSkill.objects.filter(skill=skill_model).exists():
                                                        student_skill = StudentSkill(skill=skill_model)
                                                        student_skill.save()
                                                    else:
                                                        student_skill = StudentSkill.objects.get(skill=skill_model)
                                                    student_info = StudentInfo(text=skillsTexts[index],
                                                                               student=student, skill=student_skill)
                                                    # , start_date=, end_date=skillsDateTo[index], present=skillsPresent[index],
                                                    if skillsDateFrom[index] is not "":
                                                        student_info.start_date = skillsDateFrom[index]
                                                    if skillsDateTo[index] is not "":
                                                        student_info.end_date = skillsDateTo[index]
                                                    if skillsPresent[index] == "True":
                                                        student_info.present = True
                                                    elif skillsPresent[index] == "False":
                                                        student_info.present = False

                                                    student_info.save()
                    
        
        return render(request, 'student/edit_profile.html', context)
    else:
        return redirect('employer_edit_profile')

def string_to_int(variable, error_message, request, length):
    try:
        variable = (int(variable))
        if len(str(variable)) < length:
            messages.error(request, error_message)
            return False, variable, False
        else:
            return True, variable, True
    except:
        messages.error(request, error_message)
        return True, variable, False


def student_offers(request):
    offers = JobOffer.objects.all()
    context = {
        'offers': offers,
    }
    return render(request, 'student/student_offers.html', context)

@login_required()
def student_profile(request, id):
    try:
        student = Student.objects.get(id=id)
        context = {
        'student' : student,
        'student_info': student.get_matching_info(),
        'isEmployer': request.user.isEmployer,
        }
        return render(request, 'student/student_profile.html', context)
    except:
        messages.error(request, 'Nie znaleziono wybranego studenta')
        return redirect('profile')


@login_required()
def match_offer_with_student(request):
    try:
        student = Student.objects.get(user=request.user)
        offers = JobOffer.objects.all()
        offers_matched = []
        for offer in offers:
            offers_matched.append(offer.match(student))
        
        context = {
            'student': student,
            'offers': offers_matched,
        }
        return render(request, 'student/match.html', context)
        
    except:
        messages.error(request, 'Coś poszło nie tak')
        return redirect('profile')
