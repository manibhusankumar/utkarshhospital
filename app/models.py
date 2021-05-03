from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from datetime import datetime


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

class Select(models.Model):
    select=models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return self.select



class Staff(models.Model):
    staff=models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.staff



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
    mobile = models.CharField(max_length=20,null=True)
    email = models.EmailField(max_length=30, null=True)
    address=models.CharField(max_length=100,null=True)
    date = models.DateTimeField( null=True)
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE, null=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE, null=True)
    select= models.ForeignKey(Select,on_delete=models.CASCADE, null=True)
    message=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.patient_name

####  




class appointment(models.Model):
    
    patient_name = models.CharField(max_length=30, null=True)
    mobile = models.CharField(max_length=20,null=True)
    email = models.EmailField(max_length=30, null=True)
    address=models.CharField(max_length=100,null=True)
    date = models.DateTimeField(default=datetime.now)
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE, null=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE, null=True)
    select=models.ForeignKey(Select,on_delete=models.CASCADE, null=True)
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
    joining_date = models.DateTimeField(default=datetime.now)
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
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE, null=True)
    
    


    def __str__(self):
       return str(self.patient_name)


    
departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]

GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),
)



class Doctorlist(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    resume= models.FileField()
    address = models.CharField(max_length=40)
    email = models.EmailField(max_length=30, null=True)
    mobile = models.CharField(max_length=20,null=True)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
    degree= models.CharField(max_length=100)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)






class Approve_Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    resume= models.FileField()
    address = models.CharField(max_length=40)
    email = models.EmailField(max_length=30, null=True)
    mobile = models.CharField(max_length=20,null=True)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
    degree= models.CharField(max_length=100)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)

