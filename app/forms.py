from django import forms
from . models import * 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import appointment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class SignUpForm(UserCreationForm):
    class Meta:
        model = User   
        fields =("username",'email',"password1","password2")
    username = forms.CharField(widget=forms.TextInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(widget=forms.TextInput())

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = appointment
        fields="__all__"


class Add_DoctorForm(forms.ModelForm):
    class Meta:
        model = Admin_Addinfo
        fields="__all__"
		
    
	# content=forms.CharField(widget=forms.TextInput({"placeholder":"write content here"}))
	# image=forms.ImageField()
	# date=forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))


class NurseForm(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = "__all__"


class CompounderForm(forms.ModelForm):
    class Meta:
        model = Compounder
        fields = "__all__"


class FeedbackForm(forms.ModelForm):
    class Meta:
        model= Feedback
        fields= "__all__"