from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from message_app.models import Message
from employer.models import Company
from student.models import Student
from users.models import CustomUser

# Create your views here.

@login_required()
def new_message(request):
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
                    if Student.objects.get(email=student_email):
                        student = CustomUser.objects.get(email=student_email)
                        message = Message(header=header, content=content, msg_from=company, msg_to=student)
                        message.save()
                        return redirect('messages')
                    else:
                        messages.error(request, 'Podany student nie istnieje w bazie, sprawdz email')
                else:
                    student = request.user
                    company_email = request.POST['email-adresat']
                    if Company.objects.get(email=company_email):
                        company = CustomUser.objects.get(email=company_email)
                        message = Message(header=header, content=content, msg_from=student, msg_to=company)
                        message.save()
                        return redirect('messages')
                    else:
                        messages.error(request, 'Podany pracodawca nie istnieje w bazie, sprawdz email')
    return render(request, 'users/new_message.html')


def dashboard(request):
    
    # if request.user.isEmployer:
    #     id = Company.objects.get(user_id=request.user.id)
    #     query_result = Message.objects.filter(company_id=id)
    #     students = query_result.values_list('student_id', flat = True)
    #     senders = Student.objects.filter(id__in=students)
    #     mylist = zip(senders, query_result)
    #     context = {
    #        'messages_list': mylist,
    #     }
    #     return render(request, 'users/messages.html', context)
    # else:
    #     id = Student.objects.get(user_id=request.user.id)
    #     query_result = Message.objects.filter(student_id=id)
    #     companies = query_result.values_list('company_id', flat = True)
    #     senders = Company.objects.filter(id__in=companies)
    #     mylist = zip(senders, query_result)
    #     context = {
    #         'messages_list': mylist,
    #     }
    #     return render(request, 'users/messages.html', context)


    return render(request, 'users/messages.html')

def viewMessages(request):
    # todo generate all messages beeing sent to receiver in separate window
    xd