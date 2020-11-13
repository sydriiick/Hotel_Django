import django_filters

from .models import *

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Room
        fields = 'room_type','room_bed'