from django.contrib import admin
from django.contrib import messages
from .models import Room, Booking, Customer, Comment
from django.contrib.contenttypes.admin import GenericTabularInline
# Register your models here.
admin.site.site_header = "Hotel Admin"
admin.site.site_title ="Hotel Admin Area"
admin.site.index_title ="Welcome to Hotel Admin Area"


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class HotelAdmin(admin.ModelAdmin):
    search_fields = ['room_number']
    inlines = [CommentInline]

admin.site.register(Room, HotelAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ['booking_user','booking_room','check_in','check_out']
    search_fields = ['booking_user','booking_room__room_number','check_in','check_out','booking_date']

admin.site.register(Booking, BookingAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_email','customer_fname','customer_lname','customer_phone','customer_date']
    search_fields = ['customer_email','customer_fname','customer_lname','customer_phone','customer_date']

admin.site.register(Customer, CustomerAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','name','room','rate','created_on','status']
    list_filter = ['rate','status','created_on']
    search_fields = ['user__booking_user','room__room_number','rate']
    actions = ['approve_comments', 'disapprove_comments']

    def approve_comments(self, request, queryset):
        queryset.update(status=True)
    def disapprove_comments(self, request, queryset):
        queryset.update(status=False)

admin.site.register(Comment, CommentAdmin)