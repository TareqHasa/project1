from users_app.models import Article
from django.urls import path
from . import views
urlpatterns = [
    path('register',views.register,name='register-page'),
    path('rgister/patient',views.patientRegister,name='patient-register'),
    path('rgister/doctor',views.doctorRegister,name='doctor-register'),
    path('profile/<int:id>',views.patientprofile,name='patient-profile'),
    path('login/patient',views.patientLogin,name='patient-login'),
    path('logout',views.logout,name='user-logout'),
    path('details/<int:id>',views.details),
    path('book/<int:id>',views.book),
    path('unbook/<int:id>',views.unbook),
    path('article/<int:id>',views.article)

]