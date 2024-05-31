from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login,logout
# Create your views here.

def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful')
            return redirect('userauth:register')
    context = {
        'form': form
    }
    return render(request, 'userauth/register.html', context)


def login_view(request):
    form = AuthenticationForm
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('info:home')
    context = {
        'form': form
    }
    return render(request, 'userauth/login.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, "Loged out successfully!")
    return redirect('userauth:login')
