"""HospitalMgmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from hospital.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', About,name='about'),
    path('', Index,name='home'),
    path('index/', Home,name='index'),
    path('admin_login/', Login,name='login'),
    path('logout/', Logout_admin,name='logout'),
    path('contact/', Contact,name='contact'),
    path('view_doctor/', View_Doctor, name='view_doctor'),
    path('view_patient/', View_Patient, name='view_patient'),
    path('view_appointment/', View_Appointment, name='view_appointment'),
    path('view_nurse/', View_Nurse, name='view_nurse'),
    path('view_ward/', View_Ward, name='view_ward'),
    path('view_department/', View_Department, name='view_department'),
    path('add_doctor/', Add_Doctor, name='add_doctor'),
    path('add_appointment/', Add_Appointment, name='add_appointment'),
    path('add_patient/', Add_Patient, name='add_patient'),
    path('add_nurse/', Add_Nurse, name='add_nurse'),
    path('add_department/', Add_Department, name='add_department'),
    path('add_ward/', Add_Ward, name='add_ward'),
]
