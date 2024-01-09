from django.shortcuts import redirect, render
from django.http import HttpResponse
from .form import EmployeeForm
from . models import Employee

from django.conf import settings
from django.core.mail import send_mail



# Create your views here.
def index(request):
    if request.method=="POST":
        form=EmployeeForm(request.POST)
    else:
        form=EmployeeForm()
    if form.is_valid():
        #form.save()
        name=form.cleaned_data['name']
        age=form.cleaned_data['age']
        email=form.cleaned_data['email']
        sql=Employee(name=name,age=age,email=email)
        sql.save()

        subject = 'welcome to qqqqqqqqq'
        message = f'Hi {name}, thank you for registering in fffffs.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )



        return redirect('/')

    
    #return HttpResponse("Hello, what are you doing over there?")
    return render(request,'index.html',{'form':form})
def next(request):
    return render(request,'next.html')
