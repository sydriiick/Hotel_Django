from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),

    path('logout/', views.logout_view, name='logout'),
    path('account/', views.account_view, name='account'),
    path('booking/', views.booking, name='booking'),


    path('room/<int:room_number>/', views.room, name='room'),
    path('customer/', views.customer, name='customer'),
    path('payment/', views.payment, name='payment'),
    path('book/', views.book, name='book'),

    path('', views.home, name='home'),
]