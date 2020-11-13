import datetime
from datetime import datetime
from .models import Room, Booking

def check_availability(room, check_in, check_out):
    avail_list = []
    booking_list = Booking.objects.filter(booking_room=room)
    for booking in booking_list:
        book2 = booking.check_in
        if booking.check_in > datetime.strptime(check_out, "%m/%d/%Y %I:%M %p") or booking.check_out < datetime.strptime(check_in, "%m/%d/%Y %I:%M %p"):
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)