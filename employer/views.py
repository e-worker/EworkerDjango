from django.shortcuts import render
from django.contrib import messages, auth
from .models import Company
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
