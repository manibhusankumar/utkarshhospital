from django.db import models
# Create your models here.

class Gender(models.Model):
    gender=models.CharField(max_length=70, null=True)
    
    def __str__(self):
        return self.gender



class Department(models.Model):
    department=models.CharField(max_length=70, null=True)   

    def __str__(self):
        return self.department


class Doctor(models.Model):
    doctor=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.doctor


class Admin_Addinfo(models.Model):
    image=models.ImageField()
    doctor_name = models.CharField(max_length=100)
    specilization=models.CharField(max_length=100)
    educational_qualifications=models.CharField(max_length=100)
    experience=models.CharField(max_length=50)
    language=models.CharField(max_length=50)
    fees=models.IntegerField(null=True)
    opd_shift=models.CharField(max_length=100)

    def __str__(self):
    		return self.doctor_name

	
class Approved(models.Model):
    patient_name = models.CharField(max_length=30, null=True)
    phone_number = models.BigIntegerField( null=True)
    email = models.EmailField(max_length=30, null=True)
    address=models.CharField(max_length=100,null=True)
    date = models.DateTimeField( null=True)
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE, null=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE, null=True)
    message=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.patient_name

    	


class appointment(models.Model):
    
    patient_name = models.CharField(max_length=30, null=True)
    phone_number = models.BigIntegerField( null=True)
    email = models.EmailField(max_length=30, null=True)
    address=models.CharField(max_length=100,null=True)
    date = models.DateTimeField( null=True)
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE, null=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE, null=True)
    message=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.patient_name
#------------------------------------------------------

class Shift(models.Model):
    shift = models.CharField(max_length=50)
    def __str__(self):
        return self.shift



class Nurse(models.Model):
    name = models.CharField(max_length=50)
    phone_number=models.IntegerField(null=True)
    email = models.EmailField(max_length=30, null=True)
    address=models.CharField(max_length=100)
    state=models.CharField(max_length=20)
    experience=models.CharField(max_length=50)
    department = models.CharField(max_length=100, null=True)
    age = models.IntegerField()
    shift = models.ForeignKey(Shift,on_delete=models.CASCADE)
    image=models.ImageField()
    
    

    def __str__(self):
        return self.name


#===========================================
#compounder

class Compounder(models.Model):
    name = models.CharField(max_length=50)
    phone_number=models.IntegerField(null=True)
    email = models.EmailField(max_length=30, null=True)
    address=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=20)
    experience=models.CharField(max_length=50)
    department = models.CharField(max_length=100, null=True)
    age = models.IntegerField()
    shift = models.ForeignKey(Shift,on_delete=models.CASCADE)
    joining_date = models.DateField(null=True)
    image=models.ImageField()


    def __str__(self):
        return self.name 


class Feedback(models.Model):
    name=models.CharField(max_length=40,null=True)
    email=models.EmailField(max_length=40,null=True)
    message=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name

# Room service
class Room_Service(models.Model):
    room_number = models.IntegerField(null=True)
    bed_number = models.IntegerField(null=True)
    patient_name=models.CharField(max_length=100, null=True)
    patient_age=models.IntegerField(null=True)
    patient_gender=models.ForeignKey(Gender,on_delete=models.CASCADE, null=True)
    staff_name=models.CharField(max_length=100,null=True)
    
    


    def __str__(self):
       return str(self.patient_name)