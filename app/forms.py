from django import forms
from .models import Farminputs, Farminputtwo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#Form to enter farm records
class FarminputForm(forms.ModelForm):
    class Meta:
        model = Farminputs
        fields = ['plant_stage','plant_number','plant_age','cocopeat_name','cocopeat_weight',
                  'avg_temp','avg_water', 'seed_variety',
                  'daily_observation']
    
        widgets = {
            "daily_observation": forms.Textarea(attrs={"rows": 4})  # 👈 make textarea taller
        }

class FarminputtwoForm(forms.ModelForm):
    class Meta:
        model = Farminputtwo
        fields = ['fungicide_name','avg_fungicide','insecticide_name','avg_insecticide', 
                  'micronutrient_name', 'avg_micronutrient','fertilizer_name', 
                  'avg_fertilizer']



    # class LoginForm(AuthenticationForm):
    # username = UsernameField(widget=forms.TextInput(attrs={'autofocus ':'True', 'class':'form-control'}))
    # password = forms.CharField( widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control'}))



#for registration form 
class StaffRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus ':'True', 'class':'form-control'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

    password1 = forms.CharField(label = 'Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    password2 = forms.CharField(label = 'Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
