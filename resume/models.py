from django.db import models

from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    profile_photo = models.ImageField(upload_to="Profile_Photos/", null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    adress = models.CharField(max_length=225, null=True, blank=True)
    phone_number = models.CharField(max_length=25,null=True, blank=True)

    def __str__(self):
        return self.username
    

class Experience(models.Model):
    work = models.CharField(max_length=225, blank=True, null=True)
    working_period = models.CharField(max_length=225, null=True, blank=True)
    problem = models.CharField(max_length=225, null=True, blank=True)
    solution = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.work
    

class Education(models.Model):
    education = models.CharField(max_length=225, null=True, blank=True)
    educational_category = models.CharField(max_length=225, null=True, blank=True)
    educational_direction = models.CharField(max_length=225, null=True, blank=True)
    educational_period = models.CharField(max_length=225, null=True, blank=True)
    gpa = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.education
    

class Skill(models.Model):
    work_flow = models.CharField(max_length=225, null=True, blank=True)
    
    def __str__(self):
        return self.work_flow
    

class Interest(models.Model):
    interests = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.interests
    

class AwardCertification(models.Model):
    awards_certifications = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.awards_certifications
