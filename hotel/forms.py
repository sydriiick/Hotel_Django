from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from account.models import User
from .models import Booking, Customer
from .availability import check_availability


class Register(UserCreationForm):
    class Meta:
        model = User
        fields = ['user_email','user_fname','user_lname','user_phone','password1','password2']


class UserAuthForm(forms.ModelForm):
    
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('user_email', 'password')

    def clean(self):
        if self.is_valid():
            user_email = self.cleaned_data['user_email']
            password = self.cleaned_data['password']
            if not authenticate(user_email=user_email, password=password):
                raise forms.ValidationError('Invalid credentials')


class AccountUpdate(forms.ModelForm):

    class Meta:
        model = User
        fields = ('user_email','user_fname','user_lname','user_phone')

    def clean_user_email(self):
        if self.is_valid():
            user_email = self.cleaned_data['user_email']
            try:
                user = User.objects.exclude(pk=self.instance.pk).get(user_email=user_email)
            except User.DoesNotExist:
                return user_email
            raise forms.ValidationError('Email "%s" is already in use.' % user_email)

    def clean_user_phone(self):
        if self.is_valid():
            user_phone = self.cleaned_data['user_phone']
            try:
                user = User.objects.exclude(pk=self.instance.pk).get(user_phone=user_phone)
            except User.DoesNotExist:
                return user_phone
            raise forms.ValidationError('Mobile number "%s" is aready in use.' % user_phone)
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_email','customer_fname','customer_lname','customer_phone']

    def clean(self):
        if self.is_valid():
            customer_email = self.cleaned_data['customer_email']
            customer_fname = self.cleaned_data['customer_fname']
            customer_lname = self.cleaned_data['customer_email']
            customer_phone = self.cleaned_data['customer_phone']
                        