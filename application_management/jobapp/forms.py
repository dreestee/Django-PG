from django import forms
from django.core import validators
from .models import *

def validate_name(name):
    if len(name)<2:
        raise forms.ValidationError("Name should have at least 2 character")
        
class ApplicantForm(forms.Form):
        
    field_order = ("app_name","email","phone","password")
    app_name = forms.CharField(validators=[validate_name],widget=forms.TextInput(attrs={"class":"form_control"}),label_suffix=" ", error_messages={'required':'Name is Required'}, max_length=20, label="Applicant's Name")
    phone = forms.CharField(widget=forms.TextInput(attrs={"class":"form_control"}), label_suffix=" ", label="Phone No.")
    email = forms.EmailField(label_suffix=" ", error_messages={'required':'email is Required'}, label="Email Id")
    # to show textarea in django
    description = forms.CharField(label_suffix=" ", max_length=200, required=False, widget=forms.Textarea(attrs={'class':'text-area', "class":"form_control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form_control"})) 


#Modelforms to show fields in a model at frontend
class ApplicationModelForm(forms.ModelForm):
    class Meta:
        model = Application
        # to show all fields
        # fields = "__all__"

        #to show selected fields
        # fields = ('applicant_name', 'phone_no', 'email', 'age', 'is_active')

        #to exclude few and show remaining fields
        exclude = ["is_active"]

        widgets = {
            "applicant_name": forms.TextInput(attrs={"class":"form_control"}),
            "phone_no": forms.TextInput(attrs={"class":"form_control"}),
            
        }
        labels = {
            "applicant_name": "Applicant's Name"
        }
        error_messages = {
            "applicant_name":{'required':"Name is Required"}
        }
        help_texts = {
            "email" : "Please enter a valid mail",
        }