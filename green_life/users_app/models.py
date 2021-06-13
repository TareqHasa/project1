from django.db import models
from django.utils import timezone
import re
class PatientManager(models.Manager):
    def patientRegister(self, postData):
        errors = {}
        if len(postData['first_name']) < 2 or not postData['first_name'].isalpha():
            errors["first_name"] = "first name should be at least 2 characters and contains only characters"
        if len(postData['last_name']) < 2 or not postData['last_name'].isalpha():
            errors["last_name"] = "last name should be at least 2 characters and contains only characters"
        if len(postData['password']) < 8:
            errors["password"] = "password should be more than 8 characters atleast"
        if len(postData['phone'])<9:
            errors['phone']="Phone Number should be more than 9 number"
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if Patient.objects.filter(email=postData['email']):
            errors['Email']= "This email is already used"
        return errors

    def patientLogin(self,postData):
        errors = {}
        email = postData['email']
        if len(postData['password']) < 8:
            errors["password"] = "password should be more than 8 characters atleast"
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"

        return errors
# Create your models here.
class DoctorManager(models.Manager):
    def DoctorLogin(self,postData):
        errors = {}
        email = postData['email']
        if len(postData['password']) < 8:
            errors["password"] = "password should be more than 8 characters atleast"
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        return errors

class Patient(models.Model):
    first_name= models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password= models.CharField(max_length=255)
    phone=models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=PatientManager()
    def __str__(self) :
        return  (f'{self.first_name}  {self.last_name}')

class Doctor(models.Model):
    first_name= models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password= models.CharField(max_length=255)
    phone=models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) :
        return (f'{self.first_name}  {self.last_name}')

class Article(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    written_by=models.ForeignKey(Doctor,related_name='articles',on_delete=models.CASCADE)
    post_time=models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) :
        return self.title

class Appointment(models.Model):
    session_about=models.CharField(max_length=255)
    duration=models.CharField(max_length=255)
    desc=models.TextField()
    date=models.DateTimeField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    patient= models.ManyToManyField(Patient, related_name='doctors')
    doctor=models.ForeignKey(Doctor,related_name='patients' ,on_delete=models.CASCADE)
    def __str__(self) :
        return self.session_about

def create_patient(fname,lname,email,passwd,phone):
    user =Patient.objects.create(first_name=fname,last_name=lname,email=email,password=passwd,phone=phone)
    return user