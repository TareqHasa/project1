from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('doclogin1',views.doclogin1),
    path('doctorlogin',views.doctorlogin),
    path('registration', views.index), #show main page
    path('register',views.register), #for the regiseration
    path('login',views.login), #for the login page
    path('logout',views.logout),
    path('userprofile',views.userprofile),
    path('aboutus', views.aboutus),
    path('doctor',views.doctor),
    path('home',views.home),
    

]
