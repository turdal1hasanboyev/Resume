from django.db import models

from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    profile_photo = models.ImageField(upload_to="Profile_Photos/", null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    adress = models.CharField(max_length=225, null=True, blank=True)
    phone_number = models.CharField(max_length=25,null=True, blank=True)

    def __str__(self):
        return self.username
    