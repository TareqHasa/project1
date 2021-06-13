from typing import ContextManager
from users_app.models import create_patient
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
import bcrypt
from .models import *
# Create your views here.
def register(request):
    if 'id' in request.session:
        id=request.session['id']
        return redirect(f'profile/{id}')
    return render(request,'register.html')

def patientRegister(request):

    errors = Patient.objects.patientRegister(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('register-page')
    first_name= request.POST['first_name']
    last_name=request.POST['last_name']
    email=request.POST['email']
    password=request.POST['password']
    confirm_password=request.POST['confirm_password']
    phone=request.POST['phone']

    if password == confirm_password:
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = create_patient(first_name,last_name,email,pw_hash,phone)
    if user:
        request.session['id'] = user.id
        request.session['first_name'] = user.first_name
        request.session['last_name'] = user.last_name
        id=request.session['id']
    return redirect(f'/user/profile/{id}')

def doctorRegister(request):
    pass

def patientprofile(request,id):
    if 'id' in request.session :
        user=Patient.objects.filter(id=id)
        loged_user=user[0]
        mo= Appointment.objects.filter(patient=request.session['id'])
        context={

            'patient':loged_user,
            "app" : Appointment.objects.all(),
            "mo" : mo

        }
        return render(request,'patient.html',context)
    return redirect('home-page')

def patientLogin(request):
    lerrors={}
    user = Patient.objects.filter(email=request.POST['lemail'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['lpassword'].encode(), logged_user.password.encode()):
            request.session['id'] = logged_user.id
            id=logged_user.id
            return redirect(f'/user/profile/{str(id)}')
    lerrors['lpassword']="wrong password"
    if len (lerrors)>0:
        for key, value in lerrors.items():
                messages.error(request, value)
        return redirect('register-page')
    
    return redirect('register-page')

def doctorLogin(request):
    lerrors={}
    user = Doctor.objects.filter(email=request.POST['dlemail'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['dlpassword'].encode(), logged_user.password.encode()):
            request.session['id'] = logged_user.id
            id=logged_user.id
            return redirect(f'/user/profile/{str(id)}')
    lerrors['dlpassword']="wrong password"
    if len (lerrors)>0:
        for key, value in lerrors.items():
                messages.error(request, value)
        return redirect('register-page')
    
    return redirect('register-page')

def logout(request):
    request.session.clear()
    return redirect('home-page')


def details(request,id):
    appe=Appointment.objects.get(id=id)
    user=Patient.objects.get(id=request.session["id"])
    Context={
        'appe': Appointment.objects.get(id=id),
    }
    return render(request,'deatalis.html',Context)

    
def unbook(request,id):
    user= Patient.objects.get(id= request.session['id'])
    Appe = Appointment.objects.get(id=id)
    Appe.patient.remove(user)
    return redirect(f'/user/profile/{str(request.session["id"])}')
def book(request,id):
    user= Patient.objects.get(id= request.session['id'])
    Appe = Appointment.objects.get(id=id)
    Appe.patient.add(user)
    return redirect(f'/user/profile/{str(request.session["id"])}')

def booking(request,id):
    context={
        'bo':Appointment.objects.get(id=id)
    }

def article(request,id):
    ar = Article.objects.get(id=id)
    context = {
        'ar' : ar
    }
    return render(request,'article.html',context)