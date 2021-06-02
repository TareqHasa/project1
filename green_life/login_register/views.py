from typing import ContextManager
from login_register.models import create_user
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
import bcrypt
from .models import *
def index(request):
    if 'id' in request.session:
        return redirect('/thought')
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
    return redirect('/thought')

def sucsess(request):
    isown = users.objects.get(id = request.session['id'])
    context={
            'thoughts' : Thought.objects.all(),
            'myown' : isown.mypost.all(),
            'userpost' : users.objects.get(id = request.session['id'])
         }
    return render(request,'welcome.html',context)

def login(request):
    # see if the username provided exists in the database
    user = users.objects.filter(email=request.POST['email']) # why are we using filter here instead of get?
    if user: # note that we take advantage of truthiness here: an empty list will return false
        logged_user = user[0] 
        # assuming we only have one user with this username, the user would be first in the list we get back
        # of course, we should have some logic to prevent duplicates of usernames when we create users
        # use bcrypt's check_password_hash method, passing the hash from our database and the password from the form
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            # if we get True after checking the password, we may put the user id in session
            request.session['id'] = logged_user.id
            request.session['first_name'] = logged_user.first_name
            request.session['last_name'] = logged_user.last_name

            # never render on a post, always redirect!
            return redirect('/thought')
    # if we didn't find anything in the database by searching by username or if the passwords don't match, 
    # redirect back to a safe route
    return redirect("/")
    return redirect('/')
def welcome(request):
    if 'id' in request.session:
        owner = users.objects.get(id =request.session['id'])
        context={
            "thoughts": Thought.objects.all(),
            'postowner': owner.mypost.all()
         }
        return render(request,"welcome.html",context)


def logout(request):
    request.session.clear()

    return redirect('/')



def addpost(request):
    
    user_id = request.session['id']
    owner = users.objects.get(id =user_id)
    title= request.POST['mypost']
    errors = Thought.objects.addpost(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    post= Thought.objects.create(post=title,own=owner)
    owner.loved.add(post)
    return redirect('/')


def displayinfo(request,id):
    likers = Thought.objects.get(id = id)
    Context={
        'idea' : Thought.objects.get(id = id),
        'who_like': likers.like.all()
    }
    return render(request,'details.html',Context)


def like(request,id):
    if 'id' in request.session:
        likeuser = request.session['id']
        thepost = Thought.objects.get(id =id)
        thepost.like.add(likeuser)
        return redirect('/')
    return redirect('/')


def unlike(request,id):
    likeuser = request.session['id']
    thepost = Thought.objects.get(id =id)
    thepost.like.remove(likeuser)
    return redirect('/')



def deleting(request,id):
    dele= Thought.objects.get(id =id)
    dele.delete()
    return redirect('/')
