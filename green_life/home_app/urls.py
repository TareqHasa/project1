from django.urls import path
from . import views
urlpatterns = [
    path('',views.home_page,name='home-page'),
    path('about', views.about, name='about-page'),
    path('doctors',views.doctorsShow,name='all-doctors-page'),
]
