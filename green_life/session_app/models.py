from django.db import models
from django.db.models.deletion import CASCADE
from  login_register.models import *
class Doctor(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    phone_number=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)



class Appointment(models.Model):
    session_about=models.CharField(max_length=255)
    duration=models.CharField(max_length=255)
    desc=models.CharField(max_length=255)
    date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    patient_id= models.ManyToManyField(users, related_name='sessions')
    dr_id=models.ForeignKey(Doctor,related_name='docname' ,on_delete=CASCADE)



class Article (models.Model):
    title=models.CharField(max_length=255)
    article_content=models.TextField()
    doctor_who_wrote=models.ForeignKey(Doctor,related_name="articles",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    