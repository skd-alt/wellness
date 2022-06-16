from django import forms
from django.forms import fields
from .models import Consult

class SkinCareForm(forms.ModelForm):
    
    class Meta:
        model = Consult
        fields = ['name_of_consult', 'prescription',]

class BackPainForm(forms.ModelForm):
    
    class Meta:
        model = Consult
        fields = ['name_of_consult', 'prescription',]

   


            