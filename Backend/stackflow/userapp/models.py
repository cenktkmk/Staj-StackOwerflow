from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

from profileApp.models import CustomUser



class Tags(models.Model):
    tagler = models.CharField(("Tagler"), max_length=10)

    def __str__(self):
        return self.tagler

class Post(models.Model):
    title = models.CharField(("Başlık"), max_length=50, null=True)
    description = models.TextField(("Açıklama"), max_length=500, null=True)
    createdAt = models.DateTimeField(("Oluşturma tarihi"), auto_now=True)
    viewed = models.IntegerField(("Görüntülenme Sayısı"), default=0)
    like = models.IntegerField(("Beğeni Sayısı"), default=0)
    comment = models.IntegerField(("Yorum Sayısı"), default=0)
    user = models.ForeignKey(CustomUser, verbose_name=("Yazarı"), on_delete=models.CASCADE)
    tagleri = models.ManyToManyField(Tags,("Tagleri"))
    kodalanı = RichTextField("Kod Bloğu", max_length=1500, null=True)

    


