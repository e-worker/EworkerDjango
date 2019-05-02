from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from message_app.models import Message
from employer.models import Company
from student.models import Student

# Create your views here.

@login_required()
def new_message(request):
    if request.method == 'POST':
        header = request.POST['header']
        content = request.POST['content']
        if request.user.isEmployer:
            student = request.POST['email-adresat']
            company = request.user.email
        else:
            student = request.user.email
            company = request.POST['email-adresat']
        if not Company.objects.filter(email=company).exists() or not Student.objects.filter(email=student).exists():
            messages.error(request, 'Podany adresat nie istnieje w bazie, sprawdz email')
        else:
            company_id = Company.objects.get(email__exact=company).id
            student_id = Student.objects.get(email__exact=student).id
            message = Message(header=header, content=content, student=student,company=company)
            message.save()
            return redirect('messages')
    return render(request, 'users/new_message.html')


def dashboard(request):
    
    if request.user.isEmployer:
        id = Company.objects.get(user_id=request.user.id)
        query_result = Message.objects.filter(company_id=id)
        students = query_result.values_list('student_id', flat = True)
        senders = Student.objects.filter(id__in=students)
        mylist = zip(senders, query_result)
        context = {
           'messages_list': mylist,
        }
        return render(request, 'users/messages.html', context)

    return render(request, 'users/messages.html')

def viewMessages(request):
    # todo generate all messages beeing sent to receiver in separate window
    xd