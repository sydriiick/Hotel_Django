from django.urls import path
from . import views



urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),

    path('logout/', views.logout_view, name='logout'),
    path('account/', views.account_view, name='account'),

    path('room/<int:room_number>/', views.room, name='room'),
    path('booking/', views.booking, name='booking'),
    path('payment/', views.payment, name='payment'),

    path('', views.home, name='home'),
]