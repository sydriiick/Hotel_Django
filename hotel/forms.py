from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from account.models import User


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
        user_email = self.cleaned_data['user_email']
        password = self.cleaned_data['password']
        if not authenticate(user_email=user_email, password=password):
            raise forms.ValidationError('Invalid Login')