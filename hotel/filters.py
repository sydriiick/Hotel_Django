import django_filters
from .models import *

class RoomFilter(django_filters.FilterSet):
    class Meta:
        model = Room
        fields = 'room_type','room_bed'

class BookingFilter(django_filters.FilterSet):
    class Meta:
        model = Booking
        fields = 'check_in','check_out'