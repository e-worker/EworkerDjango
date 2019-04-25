from django.shortcuts import render
from .models import Student, StudentInfo, StudentSkill, StudentDegreeCourse, StudentLanguage
from job_offers.models import DegreeCourse, LanguageLvl, Language, Skill
# Create your views here.

def edit_profile(request):
    courses = DegreeCourse.objects.all()
    languages = Language.objects.all()
    languageLvls = LanguageLvl.objects.all()
    skills = Skill.objects.all()
    context = {
        'courses': courses,
        'languages': languages,
        'languageLvls': languageLvls,
        'skills': skills,
    }
    if request.method == "POST":
        print(request.body)
    return render(request, 'student/edit_profile.html', context)