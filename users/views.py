from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from users.models import CustomUser
# Create your views here.
def login(request):
    return render(request, 'users/login.html')

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
                                        messages.success(request, 'Rejestracja przebiegla pomyslnie')
                                        return redirect('login')
        else:
            messages.error(request, 'Hasla nie zgadzaja sie')
            return redirect('register')
    return render(request, 'users/register.html')
    
    
