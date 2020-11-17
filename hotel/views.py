from django.shortcuts import render, redirect, get_object_or_404, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.views.generic import FormView
from .forms import Register, UserAuthForm, AccountUpdate, CustomerForm
from account.models import User
from .models import Room, Booking, Customer, Comment
from .availability import check_availability
from datetime import datetime
from .filters import RoomFilter, BookingFilter
from django.db.models import Q

# Create your views here.

def home(request):
    context = {}

    if request.GET:
        check_in =  datetime.strptime(request.GET.get('check_in'), "%m/%d/%Y %I:%M %p")
        check_out = datetime.strptime(request.GET.get('check_out'), "%m/%d/%Y %I:%M %p")
        room_list = Room.objects.all().filter(~Q(booking__check_in__gte = check_in),~Q(booking__check_out__gte = check_out))
    else:
        room_list = Room.objects.all()
    roomfilter = RoomFilter(request.GET, queryset=room_list)
    room_list = roomfilter.qs
    context = {
        'room_list': room_list,
        'roomfilter': roomfilter,
        }

    return render(request, 'home.html', context)

def booking(request):
    context = {}
    if request.user.is_authenticated:
        user = request.user
        
    book_list = Booking.objects.filter(booking_user=user)
    
    context['book_list'] = book_list
    return render(request, 'user/booking.html', context)


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
    room = get_object_or_404(Room, room_number = room_number)
    comment_list = Comment.objects.filter(room = room , status=True)

    if request.user.is_authenticated:
        user = request.user
        book_list = Booking.objects.filter(booking_room = room , booking_user = user)
        if book_list:
            book_user  =  Booking.objects.filter(booking_room = room , booking_user = user)[0]
        context = {
            'room': room,
            'comment_list': comment_list,
            'book_list': book_list,
        }

    else:
        context = {
            'room': room,
            'comment_list': comment_list,
        }
    
        
    if request.POST:
        comment = request.POST.get('comment')
        rate = request.POST.get('rate')
        name = user.user_fname + ' ' + user.user_lname[:1] + '.'
        comments = Comment.objects.create(
            user = book_user,
            room = room,
            name = name,
            comment = comment,
            rate = rate,
            )
        comments.save()
    return render(request, 'hotel/room.html', context)


def customer(request):
    context = {}
    if request.user.is_authenticated:
        user = request.user
    else:
        user = []
    
    check_in = request.POST.get('check_in')
    check_out = request.POST.get('check_out')
    
    nights = datetime.strptime(check_out, "%m/%d/%Y %I:%M %p") - datetime.strptime(check_in, "%m/%d/%Y %I:%M %p")

    room_list = Room.objects.filter(room_number=request.POST.get('room'))
    
    if check_in[:-9] >= check_out[:-9]:
        messages.error(request, 'Minimum of one night. Try another date.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else :
        available_rooms = []
        for room in room_list:  
            if check_availability(room, check_in, check_out):
                available_rooms.append(room)

        if len(available_rooms) > 0:
            rooms = available_rooms[0]   
            context = {
                'user': user,
                'room': room,
                'check_in': check_in,
                'check_out': check_out,
                'nights': int(nights.total_seconds() / 86400)+1,
                }
            return render(request, 'hotel/customer.html', context)
        else:
            messages.error(request, 'This date is already reserved. Try another one.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def payment(request):
    context = {}

    if request.POST:
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()    
    else:
        form = CustomerForm()

    room = request.POST.get('room')
    check_in = request.POST.get('check_in')
    check_out = request.POST.get('check_out')
    email = request.POST.get('customer_email')
    fname =  request.POST.get('customer_fname')
    lname =  request.POST.get('customer_lname')

    nights = datetime.strptime(check_out, "%m/%d/%Y %I:%M %p") - datetime.strptime(check_in, "%m/%d/%Y %I:%M %p")

    context = {
        'user': email,
        'room': Room.objects.get(room_number=room),
        'check_in': check_in,
        'check_out': check_out,
        'fname': fname,
        'lname': lname,
        'nights': int(nights.total_seconds() / 86400)+1,
        }
    
    return render(request, 'hotel/payment.html', context)

def book(request):
    context = {}
    
    room = request.POST.get('room')
    email = request.POST.get('email')
    check_in = request.POST.get('check_in')
    check_out = request.POST.get('check_out')

    book = Booking.objects.create(
        booking_user =  email,
        booking_room = Room.objects.get(room_number=room),
        check_in = datetime.strptime(check_in, "%m/%d/%Y %I:%M %p"),
        check_out = datetime.strptime(check_out, "%m/%d/%Y %I:%M %p"),
        )
    book.save()
    messages.error(request, 'Successfully Booked!')
    return redirect("home")
