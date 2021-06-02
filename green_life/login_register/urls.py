from django.urls import path
from . import views
urlpatterns = [
    path('', views.index), #show main page
    path('register',views.register), #for the regiseration
    path('thought',views.sucsess),
    path('login',views.login), #for the login page
    path('welcome',views.welcome),
    path('logout',views.logout),
    path('addthought',views.addpost),
    path('thought/<int:id>',views.displayinfo),
    path('like/<int:id>', views.like),
    path('unlike/<int:id>', views.unlike),
    path('delet/<int:id>',views.deleting)


]
