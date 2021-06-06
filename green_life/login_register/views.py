from session_app.models import Appointment, Doctor
from typing import ContextManager
from login_register.models import create_user
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
import bcrypt
from .models import *
from django.http import JsonResponse

def home(request):
    return render(request,'home.html')
def index(request):
    if 'id' in request.session:
        return redirect('/userprofile')
    return render(request,"index.html")

def register(request):
    errors = users.objects.register(request.POST)
    if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
    first_name= request.POST['first_name']
    last_name=request.POST['last_name']
    email=request.POST['email']
    password=request.POST['password']
    confirm_password=request.POST['confirm_password']

    if password == confirm_password:
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = create_user(first_name,last_name,email,pw_hash)
    if user:
        request.session['id'] = user.id
        request.session['first_name'] = user.first_name
        request.session['last_name'] = user.last_name
    return redirect('/userprofile')

def sucsess(request):
    isown = users.objects.get(id = request.session['id'])
    context={
            'myown' : isown.mypost.all(),
            'userpost' : users.objects.get(id = request.session['id'])
         }
    return render(request,'welcome.html',context)

def login(request):
    user = users.objects.filter(email=request.POST['email']) 
    if user:
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['id'] = logged_user.id
            request.session['first_name'] = logged_user.first_name
            request.session['last_name'] = logged_user.last_name

            return redirect('/userprofile')
    return redirect("/")
def userprofile(request):
    if 'id' in request.session :
        user=users.objects.filter(id = request.session['id'])
        loged_user=user[0]
        context={
            "app" : Appointment.objects.all(),
            'user':loged_user
        }

    return render(request,'userprofle.html',context)


def logout(request):
    request.session.clear()
    return redirect('/')

def aboutus(request):
    return render(request,'aboutus.html')



def doctor(request):
    if 'doctor_id' in request.session:
        context={
            'dr':Doctor.objects.get(id=request.session['doctor_id'])
        }
        return render (request,'doctor.html',context)
    return redirect('session/doctorlogin')



# def autocomplete(request):
#     if "term" in request.GET:
#         qs= Doctor.objects.filter(title__isstartwith = request.GET.get("term"))
#         first_name = list()
#         for product in qs :
#             first_name.append(Doctor,first_name)
#         return JsonResponse(first_name, safe = False)
#     return render(request , "")

def doctorlogin(request):
   return redirect ("/session/doctorlogin")


def doclogin1(request):
    doctorlogin = Doctor.objects.filter(email=request.POST['email']) 
    if Doctor:
        logged_user = Doctor[0] 
    
    if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['doctor_id'] = logged_user.id
                request.session['first_name'] = logged_user.first_name
                request.session['last_name'] = logged_user.last_name
                return redirect("/doctor")


