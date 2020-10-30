from django.contrib import admin
from django.contrib import messages
from .models import User, Room, Booking

# Register your models here.
admin.site.site_header = "Hotel Admin"
admin.site.site_title ="Hotel Admin Area"
admin.site.index_title ="Welcome to Hotel Admin Area"



class HotelAdmin(admin.ModelAdmin):
    search_fields = ['room_number']

admin.site.register(Room, HotelAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ['booking_user','booking_room','check_in','check_out','booking_date']
    search_fields = ['booking_user','booking_room','check_in','check_out','booking_date']

admin.site.register(Booking, BookingAdmin)