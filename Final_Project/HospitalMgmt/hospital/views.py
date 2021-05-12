from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,logout,login

# Create your views here.

def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'index.html')   

def Home(request):
    return render(request,'index.html')
    
def Login(request):
    error=""
    if request.method=='POST':
        u=request.POST['uname']
        p=request.POST['pwd']
        user=authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d={'error':error}
    return render(request,'login.html',d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)    
    return redirect('login')

def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc= Doctor.objects.all()  
    d={'doc': doc } 
    return render(request, 'view_doctor.html', d)

def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat= Patient.objects.all()  
    p={'pat': pat } 
    return render(request, 'view_patient.html', p)

def View_Nurse(request):
    if not request.user.is_staff:
        return redirect('login')
    nur= Nurse.objects.all()  
    n={'nur': nur } 
    return render(request, 'view_nurse.html', n)

def View_Ward(request):
    if not request.user.is_staff:
        return redirect('login')
    war= Ward.objects.all()  
    w={'war': war } 
    return render(request, 'view_ward.html', w)

def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    app= Appointment.objects.all()  
    a={'app': app } 
    return render(request, 'view_appointment.html', a)

def View_Department(request):
    if not request.user.is_staff:
        return redirect('login')
    dept= Department.objects.all()  
    dp={'dept': dept } 
    return render(request, 'view_department.html', dp)

def Add_Doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        d_id=request.POST['doctor_id']
        f=request.POST['fname']
        l=request.POST['lname']
        sn=request.POST['skill_name']
        m=request.POST['mobile']
        
        try:
            Doctor.objects.create(doctor_id=d_id,fname=f,lname=l,skill_name=sn,mobile=m)
            error="no"
        except:
            error="yes"

    d={'error':error}
    return render(request,'add_doctor.html',d)

def Add_Patient(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        p=request.POST['patient_id']
        f=request.POST['fname']
        l=request.POST['lname']
        a=request.POST['admitted_on']
        m=request.POST['mobile']

        try:
            Patient.objects.create(patient_id=p,fname=f,lname=l,admitted_on=a,mobile=m)
            error="no"
        except:
            error="yes"

    pa={'error':error}
    return render(request,'add_patient.html',pa)

def Add_Appointment(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    doct=Doctor.objects.all()
    pat=Patient.objects.all()
    if request.method=='POST':
        d=request.POST['doctor']
        f=request.POST['patient']
        l=request.POST['date']
        sn=request.POST['time']
        m=request.POST['mobile']
        app=Doctor.objects.filter(fname=d).first()
        ap=Patient.objects.filter(fname=f).first()
        try:
            Appointment.objects.create(doctor=app,patient=ap,date1=l,time1=sn,mobile=m)
            error="no"
        except:
            error="yes"

    d={'error':error,'doctor':doct,'patient':pat}
    return render(request,'add_appointment.html',d)

def Add_Nurse(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    doct=Doctor.objects.all()
    if request.method=='POST':
        n=request.POST['nurse_id']
        f=request.POST['fname']
        l=request.POST['lname']
        sn=request.POST['age']
        db=request.POST['dob']
        m=request.POST['mobile']
        d=request.POST['doctor']

        app=Doctor.objects.filter(fname=d).first()
        try:
            Nurse.objects.create(nurse_id=n,fname=f,lname=l,age=sn,dob=db,mobile=m,doctor_id=app)
            error="no"
        except:
            error="yes"

    d={'error':error,'doctor':doct}
    return render(request,'add_nurse.html',d)

def Add_Department(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        di=request.POST['dept_id']
        n=request.POST['dept_name']
        
        try:
            Department.objects.create(dept_id=di,dept_name=n)
            error="no"
        except:
            error="yes"

    d={'error':error}
    return render(request,'add_department.html',d)

def Add_Ward(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    doct=Doctor.objects.all()
    dep=Department.objects.all()
    if request.method=='POST':
        wn=request.POST['ward_no']
        n=request.POST['ward_name']
        do=request.POST['doctor']
        de=request.POST['dept']
        app=Doctor.objects.filter(fname=do).first()
        ap=Department.objects.filter(dept_name=de).first()
        try:
            Ward.objects.create(ward_no=wn,ward_name=n,doctor_id=app,dept_id=ap)
            error="no"
        except:
            error="yes"

    d={'error':error,'doctor':doct,'dept':dep}
    return render(request,'add_ward.html',d)
