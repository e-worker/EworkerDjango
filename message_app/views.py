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


def dashboard(request):

    query_result = Message.received_messages(request.user)
    context = {
        'from_list': query_result[0],
        'to_list': query_result[1],
        'all_messages': query_result[2],
        'isEmployer': query_result[3],
    }
    return render(request, 'users/messages.html', context)

def viewMessages(request, user_id):
    messages = Message.chat(request.user, user_id)
    context = {
        'messages': messages
    }
    return render(request, 'users/chat.html', context)