from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserModel(AbstractUser):
    city = models.CharField(("City"), max_length=50, null=True)
    isBanned = models.BooleanField(("Banlı m?"), default=False)
    avatar = models.FileField(verbose_name="Avatar Yükleyin", upload_to='uploads', default='default_avatar.jpg')
    about = models.CharField(("Hakkımızda"), max_length=150, null=True )
    link1 = models.URLField(blank=True, null=True, verbose_name="Github", default="Link Bulunamadı")
    link2 = models.URLField(blank=True, null=True, verbose_name="Website", default="Link Bulunamadı")
    link3 = models.URLField(blank=True, null=True, verbose_name="Twitter", default="Link Bulunamadı")

    def __str__(self):
        return self.username

