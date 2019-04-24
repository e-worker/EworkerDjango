from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    return render(request, 'users/login.html')

def register(request):
    if request.method == 'POST':
        return render(request, 'users/register.html')
    return render(request, 'users/register.html')
    
    
