from django.db import models
from datetime import datetime
from django.utils import timezone
from account.models import User 
# Create your models here.

now = timezone.now

class Customer(models.Model):
    customer_email      = models.EmailField(max_length=50, verbose_name='Email address')
    customer_fname      = models.CharField(max_length=50, verbose_name='First name')
    customer_lname      = models.CharField(max_length=50, verbose_name='Last name')
    customer_phone      = models.CharField(max_length=20, verbose_name='Mobile number')
    customer_date       = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')

    def __str__(self):
        return self.customer_email

class Room(models.Model):
    CATEGORY = [
        ('STA','Standard'),
        ('DEL','Delux')
    ]
    room_number     = models.IntegerField(verbose_name='Room Number')
    room_type       = models.CharField(max_length=3, choices=CATEGORY, verbose_name='Type')
    room_bed        = models.IntegerField(verbose_name='Number of Bed(s)')
    room_capacity   = models.IntegerField(verbose_name='Capacity')
    room_desc       = models.TextField(max_length=400, verbose_name='Description')
    room_price      = models.FloatField(null=True)
    room_image      = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.room_number)

class Booking(models.Model):
    booking_user    = models.EmailField(max_length=50, verbose_name='Customer email')
    booking_room    = models.ForeignKey(Room, on_delete = models.CASCADE, verbose_name='Room Number')
    check_in        = models.DateTimeField(blank=True, null=True,verbose_name='Check In')
    check_out       = models.DateTimeField(blank=True, null=True,verbose_name='Check Out')
    booking_date    = models.DateTimeField(auto_now_add=True, verbose_name='Booking Date')
    
    def __str__(self):
        return self.booking_user

class Comment(models.Model):
    user = models.ForeignKey(Booking, on_delete=models.CASCADE, verbose_name='Customer email')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Room number')
    name = models.CharField(max_length=20, null=True)
    comment = models.TextField(max_length=250, blank=True, verbose_name='Comment')
    rate = models.IntegerField(default=1, verbose_name='Rate')
    status = models.BooleanField(default=False, verbose_name='Status')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Created on')

    def __str__(self):
        return str(self.id)