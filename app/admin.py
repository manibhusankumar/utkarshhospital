from django.contrib import admin
from . models import*
from .models import Doctor,Doctorlist

# Register your models here.

@admin.register(appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display=['id','patient_name','mobile','email','address','date','gender','department','doctor', 'select','message']
admin.site.register(Gender)
admin.site.register(Department)

admin.site.register(Admin_Addinfo)
admin.site.register(Approved)
admin.site.register(Shift)
admin.site.register(Nurse)
admin.site.register(Compounder)
admin.site.register(Feedback)
admin.site.register(Doctor)
admin.site.register(Select)
admin.site.register(Approve_Doctor)
admin.site.register(Staff)



@admin.register(Room_Service)
class RoomServiceAdmin(admin.ModelAdmin):
    list_display=['room_number','bed_number','patient_name','patient_age','patient_gender','staff']


class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctorlist, DoctorAdmin)

    