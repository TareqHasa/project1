from django.contrib import admin
from .models import Doctor, Patient,Article,Appointment

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Article)
admin.site.register(Appointment)