from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from datetime import datetime
import uuid



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    display_name = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(upload_to='users', blank=True, null=True, default='./users/profile_pic2.jpg')
    user_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at= models.DateTimeField(default=datetime.now)
    location = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100, blank=True)
    about_me = models.CharField(max_length=500, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    twitter = models.TextField(max_length=200, blank=True)
    github = models.TextField(max_length=200, blank=True)
    website = models.TextField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        if not self.user_uuid:
            self.user_uuid = uuid.uuid4()
        super().save(*args, **kwargs)

    

    
    

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['display_name']

    

    def __str__(self):
        return self.email
    