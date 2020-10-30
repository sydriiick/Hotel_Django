from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from .forms import Register, UserAuthForm
from .models import Room
# Create your views here.

def home(request):
    room_list = Room.objects.order_by('room_number')
    context = {'room_list': room_list}
    return render(request, 'home.html', context)


def register(request):
    context = {}

    if request.POST:
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            user_email = form.cleaned_data.get('user_email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(user_email=user_email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = Register()
    context['registration_form'] = form   
    return render(request, 'user/register.html', context)



def login_view(request):
    context = {}
    user = request.user
    
    if user.is_authenticated:
        returnredirect('home')
    
    if request.POST: 
        form = UserAuthForm(request.POST)
        
        if form.is_valid():
            user_email = request.POST['user_email']
            password = request.POST['password']
            user = authenticate(user_email=user_email, password = password)

            if user:
                login(request, user)
                return redirect('home')

    else:
        form = UserAuthForm()

    context['login_form'] = form
    return render(request, 'user/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')