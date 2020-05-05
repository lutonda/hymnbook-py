from django.db import models

class User (models.Model):
    email = models.CharField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=500, blank=False, null=False)
    fullName = models.CharField(max_length=100)
    isActive = models.BooleanField()
    date = models.DateField()
    #profiles=models.ManyToManyField(Profile)

