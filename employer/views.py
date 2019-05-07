from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import Company
from job_offers.models import JobInfo, JobOfferLanguage, JobOfferSkill, OfferDegreeCourse, Skill, Language, LanguageLvl, DegreeCourse, JobOffer
from student.models import Student

def edit_profile(request):
    if request.user.isEmployer:
        company = Company.objects.get(user__id=request.user.id)

        context = {
            'company': company,
        }

        if request.method == "POST":
            company_name = request.POST['company_name']
            city = request.POST['city']
            street = request.POST['street']
            house_number = request.POST['house_number']
            flat_number = request.POST['flat_number']
            description = request.POST['description']

            if Company.objects.filter(company_name=company_name).exists():
                messages.error(request, 'Nazwa firmy aktualnie wystepuje w naszym systemie')
            else:
                company.city = city
                company.company_name = company_name
                company.street = street
                company.house_number = house_number
                company.flat_number = flat_number
                company.description = description
                company.save()
    return render(request, 'employer/edit_profile.html', context)

def find_students(request):
    if request.method=='POST':
        pass
    return render(request, 'employer/find_student.html')

def offer(request):
    return render(request, 'employer/offer.html')

def add_offer(request):
    if request.user.isEmployer:
        company = Company.objects.get(user__id=request.user.id)
        courses = DegreeCourse.objects.all()
        languages = Language.objects.all()
        languageLvls = LanguageLvl.objects.all()
        skills = Skill.objects.all()
        context = {
            'courses': courses,
            'languages': languages,
            'languageLvls': languageLvls,
            'skills': skills,
            'company': company,
        }
        if request.method == "POST":

            title = request.POST['title']
            salary_from = request.POST['salary_from']
            salary_to = request.POST['salary_to']
            description = request.POST['description']
            courses  = request.POST.getlist('course')
            languages = request.POST.getlist('language')
            languagesLvls = request.POST.getlist('languageLvl')
            skills = request.POST.getlist('skill')
            skillsTexts = request.POST.getlist('skillText')
            skillsDateFrom = request.POST.getlist('date_from')
            skillsDateTo = request.POST.getlist('date_to')
            skillsPresent = request.POST.getlist('present')

            #creating job offer
            job_offer = JobOffer(title=title, sallary_from=salary_from, sallary_to=salary_to, description=description, company=company)
            job_offer.save()

            for course in courses:
                if not OfferDegreeCourse.objects.filter(degree_course__name=course, job_offer=job_offer).exists():
                    degree_course = DegreeCourse.objects.get(name=course)
                    offer_degree_course = OfferDegreeCourse(job_offer=job_offer, degree_course=degree_course)    
                    offer_degree_course.save()

            for index, language in enumerate(languages):
                if not JobOfferLanguage.objects.filter(language__name=language, job_offer=job_offer).exists():
                    language_model = Language.objects.get(name=language)
                    languageLvl = LanguageLvl.objects.get(level=languagesLvls[index])
                    job_offer_language = JobOfferLanguage(language=language_model, language_lvl=languageLvl, job_offer=job_offer)
                    job_offer_language.save()

            for index, skill in enumerate(skills):
                if not JobInfo.objects.filter(job_offer=job_offer, job_skill__skill__name=skill, text=skillsTexts[index]).exists():
                    skill_model = Skill.objects.get(name=skill)
                    if not JobOfferSkill.objects.filter(skill=skill_model).exists():
                        job_offer_skill = JobOfferSkill(skill=skill_model)
                        job_offer_skill.save()
                    else:
                        job_offer_skill = JobOfferSkill.objects.get(skill=skill_model)
                        job_info = JobInfo(text=skillsTexts[index], job_offer=job_offer, job_skill=job_offer_skill)
                        # , start_date=, end_date=skillsDateTo[index], present=skillsPresent[index],
                        if skillsDateFrom[index] is not "":
                            job_info.start_date = skillsDateFrom[index]
                        if skillsDateTo[index] is not "":
                            job_info.end_date = skillsDateTo[index]
                        if skillsPresent[index] == "True":
                            job_info.present = True
                        elif skillsPresent[index] == "False":
                            job_info.present = False

                        job_info.save()


            print(request.body)
        return render(request, 'employer/add_offer.html', context)
    else:
        return redirect("login")