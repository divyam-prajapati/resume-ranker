from django.db import models
# Create your models here.

class myUploadFile(models.Model):
    myfiles = models.FileField(upload_to="")

class Data(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=64, null=True)
    collegeName = models.CharField(max_length=100, null=True) 
    degree = models.CharField(max_length=200, null=True)
    graduationYear = models.CharField(max_length=200, null=True)
    yearsOfExperience = models.CharField(max_length=200, null=True)
    companiesWorkedAt = models.CharField(max_length=200, null=True)
    designation = models.CharField(max_length=200, null=True)
    skills = models.TextField(max_length=255, null=True)
    Location = models.TextField(max_length=200, null=True)
    emailAddress = models.EmailField(null=True)