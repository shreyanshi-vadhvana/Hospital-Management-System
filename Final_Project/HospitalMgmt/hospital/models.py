from django.db import models

# Create your models here.
class Doctor(models.Model):
    doctor_id=models.IntegerField()
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    skill_name=models.CharField(max_length=30)
    mobile=models.IntegerField()

    def __str__(self):
        return self.fname

class Patient(models.Model):
    patient_id=models.IntegerField()
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    admitted_on=models.DateField()
    mobile=models.IntegerField()

    def __str__(self):
        return self.fname
    
class Nurse(models.Model):
    nurse_id=models.IntegerField()
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    age=models.IntegerField()
    dob=models.DateField()
    mobile=models.IntegerField()     
    doctor_id=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.fname


class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    date1=models.DateField()
    time1=models.TimeField()
    mobile=models.IntegerField()

    def __str__(self):
        return self.doctor.fname+ "--"+self.patient.fname

class Department(models.Model):
    dept_id=models.IntegerField()
    dept_name=models.CharField(max_length=20)

    def __str__(self):
        return self.dept_name

class Ward(models.Model):
    ward_no=models.CharField(max_length=10)
    ward_name=models.CharField(max_length=20)
    doctor_id=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    dept_id=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.ward_name


