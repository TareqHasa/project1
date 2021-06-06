from typing import ValuesView
from django.urls import path
from . import views
urlpatterns = [
    path('book/<int:id>', views.booking),
    path('createsession/<int:id>',views.addsession),
    path('doctorlogin',views.doctorlogin),
    path('doclogin',views.doclogin),
    path('session/doctor',views.showdr),
    path('session',views.display),
    path('confirm/<bo.id>',views.confirm),
    path('articles',views.arti),
    path('book/<id>',views.booking),

]

