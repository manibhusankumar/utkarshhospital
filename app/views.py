from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from app.models import appointment
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from app.forms import AppointmentForm
from . forms import SignUpForm
from django.conf import settings
from app.forms import Add_DoctorForm
from app.models import Admin_Addinfo
from .models import Approved
from . forms import *


# Create your views here.
def Home(request):
    return render(request,'base.html')


	

def Appointment(request):
    if request.method=="POST":
        form = AppointmentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,' your Appointment book successfully!!! please wait for confirmations')
            return redirect("Appointment")

    else:
        form = AppointmentForm(request.FILES)
    return render(request,"bookappoitment.html",{"form":form})



def Admin(request):
	return render(request,'verticalnavbar.html')

def Admin_login(request):
    if request.method =="POST":
        form =AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            uname =form.cleaned_data["username"]
            upass =form.cleaned_data["password"]
            user = authenticate(username=uname,password=upass)
            messages.success(request,' successfully Login!!')
            if user is not None:
                login(request,user)
                return redirect('Admin')
    else:							
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})


def user_login(request):
    if request.method =="POST":
        form =AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            uname =form.cleaned_data["username"]
            upass =form.cleaned_data["password"]
            user = authenticate(username=uname,password=upass)
            messages.success(request,' successfully Login!!')
            if user is not None:
                login(request,user)
                return redirect('Appointment')
    else:							
        form=AuthenticationForm()
    return render(request,'Userlogin.html',{'form':form})


def SignUp(request):
    if request.method=="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for'+ user)
            return redirect("user_login")
    else:
        form = SignUpForm()
    return render(request,"signup.html",{"form":form})


def Logout_user(request):
	logout(request)
	return redirect("Home")



def Admin_logout(request):
	logout(request)
	return redirect("Admin")

def Admin_base(request):
	return render(request,'admin_base.html')


def Read_Appointment(request):
    read = appointment.objects.all()
    return render(request,"read_appointment.html",{"read":read})


def Actions_Appointment(request):
    read = appointment.objects.all()
    messages.success(request,' actions perform')
    return render(request,"actions.html",{"read":read})


# def Update(request,id):
#     upd=appointment.objects.get(id=id)
#     update=AppointmentForm(request.POST or None,request.FILES or None,instance=upd)
#     if update.is_valid():
#         update.save()
#         return redirect('Read_Appointment')
#     return render(request,"update.html",{"update":update})    

def Delete(request,id):
    del_t=appointment.objects.get(id=id)    
    del_t.delete()

    return redirect("Actions_Appointment")


def Send_Email(request,id):
    a=[appointment.objects.get(id=id).email]

    send_mail(
        subject = "greetings",
        message = "hello your appoint has been confirmed",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=a,
        
        fail_silently=False

    )
    # a = recipient_list
    # for i in recipient_list:
    #     print(i)

        
    # print(recipient_list)

    return render(request,"actions.html")



#cancel appointment
def Reject_Email(request,id):
    a=[appointment.objects.get(id=id).email]

    send_mail(
        subject = "greetings",
        message = "Sorry your appointment has not  confirmed",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=a,
        
        fail_silently=False

    )
    # a = recipient_list
    # for i in recipient_list:
    #     print(i)

        
    # print(recipient_list)

    return render(request,"actions.html")







# def Doctor_info(request):
#     return render(request,'doctor.html')

def Add_Doctor(request):
    if request.method =="POST":
        form=Add_DoctorForm(request.POST or None,request.FILES or None)

        if form.is_valid():
            form.save()
            messages.success(request,' successfully added doctor!!')
            return redirect(Admin)
    else:
        form=Add_DoctorForm()
    return render(request,'doctor.html',{'form':form})

def Update(request,id):
    upd=Admin_Addinfo.objects.get(id=id)
    update=Add_DoctorForm(request.POST or None ,request.FILES or None,instance=upd)
    if update.is_valid():
        update.save()
        return redirect(Admin)
    return render(request,"updatedoctor.html",{"update":update})  


def Read_doctors(request):
    read = Admin_Addinfo.objects.all()
    return render(request,"read_doctor.html",{"read":read})


def Delete_doctor(request,id):
    del_t=Admin_Addinfo.objects.get(id=id)    
    del_t.delete()

    return redirect("Read_doctors")

#----------------------------------------------------------------
def approve(request, id):
    a = [appointment.objects.get(id=id).email]

    # Copying row from company table to approved table
    approved_row = appointment.objects.all().filter(id=id)
    approved_table_new_row = Approved(
        patient_name=approved_row.first().patient_name,
        phone_number=approved_row.first().phone_number,
        email=approved_row.first().email,
        date=approved_row.first().date,
        gender=approved_row.first().gender,
        department=approved_row.first().department,
        doctor=approved_row.first().doctor,
        message=approved_row.first().message,

    )
    approved_table_new_row.save()

    # sending email when approved
    send_mail(
       subject="greetings",
       message="hello your appoint has been confirmed",
       from_email=settings.EMAIL_HOST_USER,
       recipient_list=a,
       fail_silently=False,
    )

    # deleting approved row from company table
    del_t = appointment.objects.get(id=id)
    del_t.delete()
    return redirect(Admin)


def delete(request, id):
    del_t = appointment.objects.get(id=id)
    del_t.delete()
    return redirect(Admin)


def Ensure(request):
    a = Approved.objects.all()
    return render(request,"ensure.html",{"a":a})



#--------------------------------------------------------
# Add_Nurse  related

def Add_Nurse(request):
    if request.method=="POST":
        form = NurseForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,"New Nurse Added.!")

            return redirect(Admin)
    else:
        form = NurseForm()
    return render(request,"Nurse.html",{"form":form})



def Add_Nurse_Done(request):
    return render(request,"Add_Nurse_Done.html")




def Read_Nurse(request):
    read=Nurse.objects.all()
    return render(request,"Read_Nurse.html",{"read":read})



def Update_Nurse(request,id):
    upd=Nurse.objects.get(id=id)
    update = NurseForm(request.POST or None,request.FILES or None,instance=upd)
    if update.is_valid():
        update.save()
        return redirect("Read_Nurse")
    return render(request,"Update_Nurse.html",{"update":update})


def Nurse_Delate(request, id):
    del_t = Nurse.objects.get(id=id)
    del_t.delete()
    return redirect("Read_Nurse")



def Services(request):
    return render(request,'Services.html')  

def doctorlist(request):
    return render(request,'doctorlist.html')


def About(request):
    return render(request,'About.html')

#Compounder---------------------------------------------

def Add_Compounder(request):
    if request.method=="POST":
        form = CompounderForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,"New Nurse Added.!")

            return redirect(Admin)
    else:
        form = CompounderForm()
    return render(request,"Compounder.html",{"form":form})


def Read_Compounder(request):
    read=Compounder.objects.all()
    return render(request,"Read_Compounder.html",{"read":read})



def Update_Compounder(request,id):
    upd=Compounder.objects.get(id=id)
    update = CompounderForm(request.POST or None,request.FILES or None,instance=upd)
    if update.is_valid():
        update.save()
        return redirect("Read_Compounder")
    return render(request,"Update_Compounder.html",{"update":update})


def Compounder_Delate(request, id):
    del_t = Compounder.objects.get(id=id)
    del_t.delete()
    return redirect("Read_Compounder")

def send_feedback_view(request):
    if request.method=="POST":
        form = FeedbackForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,' Thanks for feedback')
            return redirect("Appointment")

    else:
        form = FeedbackForm(request.FILES)
    return render(request,"send_feedback.html",{"form":form})





def view_feedback_view(request):
    feedbacks=Feedback.objects.all()
    return render(request,'view_feedback.html',{'feedbacks':feedbacks})




