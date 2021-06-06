from django.shortcuts import redirect, render
from django.http import JsonResponse

from datetime import date # عملنا امبورت للتاريخ 
from .models import * 
import bcrypt

def booking(request,id):
    context={
        'bo':Appointment.objects.get(id=id)
    }
    return render(request,'confirmation.html',context)
    #     #أول إشي جبنا السيشن للحجز والمستخدم الذي يريد الحجز 
    #  sessname=Appointment.objects.get(id=id)
    # user_id=User.objects.get(id=request.session['id'])
    # time=date.today()#فنكشن جاهزة بالبايثون للتاريخ 
    # tim=sessname.date()
    # now=tim.split(":")#فنكشن جاهزة عشان تحط الوقت بمصفوفة 
    # Tnow=time.split(":")#بدنا نفحص أنه اذا الجلسة اليوم محجوزة ولا لا فعشان هيك بنجيب اول اشي تاريخ اليوم بعدين بنجيب الجلسات المحجوزة في ذلك اليوم 
    # if now [1]<Tnow[1] and now [0]<Tnow[0] : #لفحص شهر الجلسة 
    #     return redirect()
    # sessname.patient_id.add(user_id)
    #     return redirect()#راجعيييييييييييييين

def addsession(request,id):
    #لإضافة جلسة إلى النظام #
        dr=Doctor.objects.get(id=request.session['doctor_id'] )
        date=request.POST['date']
        time=request.POST['time']
        desc=request.POST['desc']
        sessionname=request.POST['sessionname']
        Appointment.objects.create(session_about=sessionname,duration=time,date=date,desc=desc,dr_id=dr)
        return redirect("/userprofile")
def userprofile(request):
    return render(request,'userprofile.html')

def doctorlogin(request):
    return render(request,"doctorlogin.html")



def doclogin(request):
    doctorlogin = Doctor.objects.filter(email=request.POST['email']) 
    if Doctor:
        logged_user = Doctor[0] 
    
    if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['doctor_id'] = logged_user.id
                request.session['first_name'] = logged_user.first_name
                request.session['last_name'] = logged_user.last_name
                return redirect()

def showdr(request,id):
    thisA = Appointment.object.get(id=id)
    print(thisA.date)
    context={
        'appointment':Appointment.object.get(id=id),
        'displaydoctor':Doctor.objects.all(),
    }
    return render(request,'reservationsession.html',context)

    
def display(request):
    context={
        'docinfo':Appointment.objects.all()
    }

    return render(request,'session.html' ,context)

def confirm(request,id):
    user_id=users.objects.get(id=request.session['id'])
    appoin=Appointment.objects.get(id=id)
    appoin.patient_id.add(user_id)
    return redirect('/userprofle')


def autocomplete(request):
    if "term" in request.GET:
        qs= Doctor.objects.filter(title__isstartwith = request.GET.get("term"))
        first_name = list()
        for product in qs :
            first_name.append(Doctor,first_name)
        return Jsonresponse(first_name, safe = False)
    return render(request , "")

def arti(request):
    context ={
        'arti' :Article.objects.all()
    }
    return render(request,'articles.html',context)
    
def booking(request,id):
    user= users.objects.get(id= request.session['id'])
    Appe = Appointment.objects.get(id=id)
    Appe.patient_id.add(user)
    return redirect('/userprofile')
