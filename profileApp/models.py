from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from datetime import datetime
import uuid




class Badge(models.Model):
    title = models.CharField(max_length=50, default="Bronze Badge Title")
    description = models.TextField(blank=True, default="Bronze Badge Description")
    image = models.ImageField(upload_to='badges/', blank=True, null=True, default=None)
    
    def __str__(self):
        return self.title
     


        





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
    user_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    created_at= models.DateTimeField(default=datetime.now)
    location = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100, blank=True)
    about_me = models.CharField(max_length=500, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    twitter = models.TextField(max_length=200, blank=True)
    github = models.TextField(max_length=200, blank=True)
    website = models.TextField(max_length=200, blank=True)
    badge = models.ManyToManyField(Badge, related_name="Badges")

    def save(self, *args, **kwargs):
        if not self.user_uuid:
            self.user_uuid = uuid.uuid4()
        super().save(*args, **kwargs)

    
    def follow(self, user_to_follow):
        if user_to_follow != self and not self.is_following(user_to_follow):
            Follow.objects.create(follower=self, following=user_to_follow)

    def unfollow(self, user_to_unfollow):
        Follow.objects.filter(follower=self, following=user_to_unfollow).delete()

    def is_following(self, user):
        return self.following.filter(following=user).exists()    
    
    

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['display_name']

    

    def __str__(self):
        return self.email
    
    
class Follow(models.Model):
    follower = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')    





