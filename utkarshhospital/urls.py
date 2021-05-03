"""utkarshhospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from app import views
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.conf import settings
from app.views import Send_Email




urlpatterns = [
    path('admin/', admin.site.urls),
	path("",views.Home,name="Home"),
	path('Appointment/',views.Appointment,name="Appointment"),
	path('Admin/',views.Admin,name="Admin"),
	path('login/',views.Admin_login,name="login"),
	path('user_login/',views.User_Login,name="user_login"),
	# path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
	path("SignUp/",views.doctor_signup_view,name="SignUp"),
	# path('logout_user',views.Logout_user,name="logout_user"),
	path('User_Logout1/',views.User_Logout1,name='User_Logout1'),
	path('Admin_logout/',views.Logout,name="Admin_logout"),
	path('Admin_base/',views.Admin_base,name="Admin_base"),
	path("Read_Appointment/",views.Read_Appointment,name="Read_Appointment"),
	path("Actions_Appointment/",views.Actions_Appointment,name="Actions_Appointment"),
    path("delete/<int:id>",views.Delete,name="delete"),
    path("Delete_doctor/<int:id>",views.Delete_doctor,name="Delete_doctor"),
	# path('send/<int:id>',views.Send_Email,name='email'),
	path('send/',views.Send_Email,name='email'),
	# path('DoctorApprovaldone/<int:id>',views.Send_Email2,name='DoctorApprovaldone'),
	path('reject/<int:id>',views.Reject_Email,name='reject'),
	# path('Doctor_info/',views.Doctor_info,name="Doctor_info"),
	path("Add_Doctor/",views.Add_Doctor,name="Add_Doctor"),
	path("update/<int:id>",views.Update,name="update"),
	path('Read_doctors/',views.Read_doctors,name="Read_doctors"),
	path("delete/<int:id>", views.delete, name="delete"),
    path("approve/<int:id>", views.approve, name="approve"),
    path("Approve_Doctorlist/<int:id>", views.Approve_Doctorlist, name="Approve_Doctorlist"),
	path('Ensure/',views.Ensure,name='Ensure'),
	path('DoctorApproval/',views.DoctorApproval,name='DoctorApproval'),
	# Nurse add
	path("Add_Nurse/",views.Add_Nurse,name="Add_Nurse"),
    path("Add_Nurse_Done/",views.Add_Nurse_Done,name="Add_Nurse_Done"),
    path("Read_Nurse/",views.Read_Nurse,name="Read_Nurse"),
    path("Update_Nurse/<int:id>",views.Update_Nurse,name="Update_Nurse"),
    path("Nurse_Delate/<int:id>",views.Nurse_Delate,name="Nurse_Delate"),
	path("Services/",views.Services,name="Services"),
	path("doctorlist/",views.doctorlist,name="doctorlist"),
	path("About/",views.About,name="About"),
	# compounder
	path("Add_Compounder/",views.Add_Compounder,name="Add_Compounder"),
	path("Read_Compounder/",views.Read_Compounder,name="Read_Compounder"),
    path("Update_Compounder/<int:id>",views.Update_Compounder,name="Update_Compounder"),
    path("Compounder_Delate/<int:id>",views.Compounder_Delate,name="Compounder_Delate"),
	path('send-feedback', views.send_feedback_view,name='send-feedback'),
    path('view-feedback', views.view_feedback_view,name='view-feedback'),

	# Room Services
	path("Add_Room_Service/",views.Add_Room_Service,name="Add_Room_Service"),
    path("Add_Room_Service_Done/",views.Add_Room_Service_Done,name="Add_Room_Service_Done"),
    path("Read_Room_Service/",views.Read_Room_Service,name="Read_Room_Service"),
    path("edit/<int:id>",views.Update_Room_Service,name="edit"),
	### Doctor Dashboard
	path("DashboardDoctor/",views.DashboardDoctor,name="DashboardDoctor"),
	path("Read_ApplyDoctor/",views.Read_ApplyDoctor,name="Read_ApplyDoctor"),
	path("Delete_ApplyDoctor/<int:id>",views.Delete_ApplyDoctor,name="Delete_ApplyDoctor"),
	### confirm doctor name
	path("Confirm_Doctor/",views.Confirm_Doctor,name="Confirm_Doctor"),
	path("Doctor_Wait/",views.Doctor_Wait,name="Doctor_Wait"),
	path('update-doctor/<int:pk>', views.update_doctor_view,name='update-doctor'),

	
	
	



]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

