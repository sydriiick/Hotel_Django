from django.db import models
from datetime import datetime
from django.utils import timezone
from account.models import User 
# Create your models here.

now = timezone.now()


class Room(models.Model):
    CATEGORY = [
        ('STA','Standard'),
        ('DEL','Delux')
    ]

    room_number = models.IntegerField(verbose_name='Room Number')
    room_type = models.CharField(max_length=3, choices=CATEGORY, verbose_name='Type')
    room_bed = models.IntegerField(verbose_name='Number of Bed(s)')
    room_capacity = models.IntegerField(verbose_name='Capacity')
    room_desc = models.TextField(max_length=400, verbose_name='Description')

    def __str__(self):
        return f'{self.room_number}'

class Booking(models.Model):
    booking_user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='User')
    booking_room = models.ForeignKey(Room, on_delete = models.CASCADE, verbose_name='Room Number')
    check_in = models.DateTimeField(verbose_name='Check In')
    check_out = models.DateTimeField(verbose_name='Check Out')
    booking_date = models.DateTimeField(default=now, verbose_name='Booking Date')
    
