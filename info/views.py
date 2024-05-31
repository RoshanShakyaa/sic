from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from .models import Notice
from lms.models import Course

# Create your views here.
def homeview(request):
    courses = Course.objects.all().order_by('-id')
    context = {'courses': courses}
    return render(request, 'info/home.html', context)

def noticeview(request):
    return render(request, 'info/notice.html')

def contactview(request):
    if request.method == "POST":
        contactform = ContactForm(request.POST)   #data get garcha
        if contactform.is_valid():
            contactform.save()
            messages.success(request, 'Your form was submitted successfully!!')
            return redirect('info:contact') #urls ko app_name ko url ko name    
    else:
        form = ContactForm     
        
    context ={
        'form':form
        }
    return render(request, 'info/contact.html', context)


def noticeview(request):
    notices = Notice.objects.all().order_by('-id')
    context = {"notices": notices}
    return render(request, 'info/notice.html', context)