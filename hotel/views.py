from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, logout, login
from .forms import Register, UserAuthForm, AccountUpdate
from .models import Room
# Create your views here.

def home(request):
    context = {}
    room_list = Room.objects.all()
    context['room_list'] = room_list
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

def account_view(request):

    if not request.user.is_authenticated:
        return redirect("login")

    context = {}

    if request.POST:
        form = AccountUpdate(request.POST, instance=request.user)
        if form.is_valid():
            form.initial ={
                'user_email': request.POST['user_email'],
                'user_fname': request.POST['user_fname'],
                'user_lname': request.POST['user_lname'],
                'user_phone': request.POST['user_phone'],
            }
            form.save()
            context['success_message'] = 'Changes saved successfully'
    else:
        form = AccountUpdate(
                initial={
                    'user_email': request.user.user_email,
                    'user_fname': request.user.user_fname,
                    'user_lname': request.user.user_lname,
                    'user_phone': request.user.user_phone,
                }
            )
    context['account_form'] = form
    return render(request, 'user/account.html', context)

def room(request, room_number):
    context = {}
    room = get_object_or_404(Room, room_number=room_number)
    context['room'] = room

    return render(request, 'hotel/room.html', context)



def booking(request):
    context = {}
    return render(request, 'hotel/booking.html', context)

def payment(request):
    context = {}
    return render(request, 'hotel/payment.html', context)