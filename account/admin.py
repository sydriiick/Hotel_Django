from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from account.models import User
# Register your models here.

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('user_email', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]
    


class UserAdmin(UserAdmin):
    list_display = ('user_email','user_fname','user_lname','user_phone','is_active','is_admin')
    readonly_fields = ('date_joined','last_login')
    
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('user_email', 'password')}),
        ('Personal info', {'fields': ('user_fname','user_lname','user_phone')}),
        ('Permissions', {'fields': ('is_active','is_admin','is_staff','is_superuser')}),
        (None, {'fields': ('date_joined', 'last_login')}),)
    add_fieldsets = (
        (None,  {'classes': ('wide',),'fields': ('user_email', 'password1','password2')}),
        ('Personal info', {'fields': ('user_fname','user_lname','user_phone')}),
        ('Permissions', {'fields': ('is_active','is_admin','is_staff','is_superuser')}),)

    search_fields = ('user_fname','user_lname','user_email')
    ordering = ('user_email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)