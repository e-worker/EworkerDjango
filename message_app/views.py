from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from message_app.models import Message
from employer.models import Company
from student.models import Student
from users.models import CustomUser

# Create your views here.

@login_required(login_url='/')
def new_message(request, id=0):
    context ={    }
    if request.method == 'POST':
        header = request.POST['header']
        content = request.POST['content']
        if len(header) < 3:
            messages.error(request, 'Temat wiadomości jest za kró†ki')
        else:
            if len(content) < 5:
                messages.error(request, 'Wiadomość jest zbyt krótka')
            else:
                if request.user.isEmployer:
                    student_email = request.POST['email-adresat']
                    company = request.user
                    if Student.objects.filter(email=student_email).exists():
                        student = CustomUser.objects.get(email=student_email)
                        message = Message(header=header, content=content, msg_from=company, msg_to=student)
                        message.save()
                        return redirect('messages')
                    else:
                        messages.error(request, 'Podany student nie istnieje w bazie, sprawdz email')
                else:
                    student = request.user
                    company_email = request.POST['email-adresat']
                    if Company.objects.filter(email=company_email).exists():
                        company = CustomUser.objects.get(email=company_email)
                        message = Message(header=header, content=content, msg_from=student, msg_to=company)
                        message.save()
                        return redirect('messages')
                    else:
                        messages.error(request, 'Podany pracodawca nie istnieje w bazie, sprawdz email')
        return render(request, 'users/new_message.html')
    else:
        if id != 0:
            if request.user.isEmployer:
                student_direct_email = Student.objects.get(id=id).email
                context = {
                    'direct_email': student_direct_email
                }
            else:
                employer_direct_email = Company.objects.get(id=id).email
                context = {
                    'direct_email': employer_direct_email
                }
    return render(request, 'users/new_message.html', context)

@login_required(login_url='/')
def dashboard(request):
    query_result = Message.received_messages(request.user)

    context = {
        'all_messages': query_result[0],
        'isEmployer': query_result[1],
    }
    return render(request, 'users/messages.html', context)

@login_required(login_url='/')
def viewMessages(request, user_id):
    messages = Message.chat(request.user, user_id)
    for message in messages:
        if message.msg_to == request.user:
            message.seen = True
            message.save()

    if request.user.isEmployer:
        request_name = Company.objects.get(user_id=request.user.id).company_name
    else:
        request_name = Student.objects.get(user_id=request.user.id).name

    if Company.objects.filter(user_id=user_id).exists():
        user_name = Company.objects.get(user_id=user_id).company_name
        opposite_email = Company.objects.get(user_id=user_id).email
    else:
        first_name = Student.objects.get(user_id=user_id).name
        last_name = Student.objects.get(user_id=user_id).surname
        user_name = first_name +" "+ last_name
        opposite_email = Student.objects.get(user_id=user_id).email

    context = {
        'messages': messages,
        'user_id': request.user.id,
        'request_user_name': request_name,
        'opposite_user_name': user_name,
        'opposite_email': opposite_email,
    }
    return render(request, 'users/chat.html', context)