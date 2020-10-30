from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, user_email, password=None):
        if not user_email:
            raise ValueError('Users must have an email address.')
        
        user = self.model(
                user_email=self.normalize_email(user_email),
            )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_email, password):
        user = self.create_user(
                user_email=self.normalize_email(user_email),
                password = password,
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

class User(AbstractBaseUser):
    user_email      = models.EmailField(max_length=50, unique=True, verbose_name='Email address')
    user_fname      = models.CharField(max_length=50, verbose_name='First name')
    user_lname      = models.CharField(max_length=50, verbose_name='Last name')
    user_phone      = models.CharField(max_length=20, verbose_name='Mobile number')
    date_joined     = models.DateTimeField(auto_now_add=True, verbose_name='Date joined')
    last_login      = models.DateTimeField(auto_now=True, verbose_name='Date Joined')
    is_admin        = models.BooleanField(default=False, verbose_name='Admin')
    is_active       = models.BooleanField(default=True, verbose_name='Active')
    is_staff        = models.BooleanField(default=False, verbose_name='Staff status')
    is_superuser    = models.BooleanField(default=False, verbose_name='Superuser status')

    USERNAME_FIELD = 'user_email'

    objects = MyAccountManager()

    def __str__(self):
        return f'{self.id} | {self.user_email}'

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

