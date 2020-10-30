import datetime
from .models import Room, Booking

def check_availability(room, check_in, check_out):
    avail_list = []
    booking_list = Booking.objects.filter(room=room)
    for booking in booking_list:
        if booking.check_in > check_out or booking.check_in < check_in:
            avail_list.append(true)
        else:
            avail_list.append(False)