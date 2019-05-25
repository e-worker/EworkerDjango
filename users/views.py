from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from users.models import CustomUser
from student.models import Student
from employer.models import Company
from django.contrib.auth.decorators import login_required

from student import views as stud_views

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        messages.error(request, 'Jestes juz zalogowany, nie mozesz sie zalogować drugi raz')
        if request.user.isEmployer == True:
            return redirect('employer_offers')
        else:
            return redirect('student_offers')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Pomyślnie zalogowano')
                if request.user.doneProfileEdit:
                    return redirect('offers')
                else:
                    return redirect('edit_profile')
            else:
                messages.error(request, 'Invalid credentials')
                return render(request, 'users/login.html')
        else:
            return render(request, 'users/login.html')

@login_required(login_url='/')
def logout(request):
    if request.method =='POST':
        auth.logout(request)
        messages.success(request, 'Pomyślnie wylogowano')
        return redirect('login')

def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        isEmployer = request.POST['isEmployer']
        password = request.POST['passwd1']
        password2 = request.POST['passwd2']
        if password == password2:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Ta nazwa uzytkownika jest zajeta, sprobuj innej')
                return redirect('register')
            else:
                if CustomUser.objects.filter(email=email).exists():
                    messages.error(request, 'Ten email akutalnie wystepuje w naszym systemie, sprobuj inny')
                    return redirect('register')
                else:
                    if len(username) > 150 or len(username) < 3:
                        messages.error(request, 'Nazwa uzytkownika powinna byc dluzsza od 3 znakow i krotsza od 150')
                    else:
                        if len(first_name) > 30:
                            messages.error(request, 'Imie powinno zawierac mniej niz 30 znakow')
                        else:
                            if len(last_name) > 150:
                                messages.error(request, 'Nazwisko powinno zawierac mniej niz 150 znakow')
                            else:
                                if len(email) > 254:
                                    messages.error(request, 'Adres email jest za dlugi')
                                else:
                                    if len(phone) > 20:
                                        messages.error(request, 'Numer telefonu jest za dlugo gosciu')
                                    else:
                                        user = CustomUser.objects.create_user(password=password, username=username, first_name=first_name, last_name = last_name, email = email, isEmployer=isEmployer, phone=phone)
                                        user.save()
                                        if isEmployer == 'True':
                                            company = Company(user=user, email=email)
                                            company.save()
                                        else:
                                            student = Student(user=user, name=first_name, surname=last_name, email=email)
                                            student.save()
                                        messages.success(request, 'Rejestracja przebiegla pomyslnie')
                                        return redirect('login')
                                    
        else:
            messages.error(request, 'Hasla nie zgadzaja sie')
            return redirect('register')
    return render(request, 'users/register.html')
    
@login_required()
def profile(request):
    if not request.user.isEmployer:
        student = Student.objects.get(user_id=request.user.id)
        context = {
        'student' : student,
        'student_info': student.get_matching_info(),
        'isEmployer': request.user.isEmployer,
        }
        return render(request, 'student/student_profile.html', context)
    else:
        try:
            company = Company.objects.get(user=request.user)
            return redirect('employer_profile', company.id)
        except:
            return redirect('login')

@login_required()
def offers(request):
    if request.user.isEmployer:
        pass #do something
    else:
        return redirect('student_offers')
