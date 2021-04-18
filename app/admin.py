from django.contrib import admin
from . models import*
# Register your models here.

@admin.register(appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display=['id','patient_name','phone_number']
admin.site.register(Gender)
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Admin_Addinfo)
admin.site.register(Approved)
admin.site.register(Shift)
admin.site.register(Nurse)
admin.site.register(Compounder)
admin.site.register(Feedback)