from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Ward)
admin.site.register(Nurse)
admin.site.register(Appointment)
admin.site.register(Department)
