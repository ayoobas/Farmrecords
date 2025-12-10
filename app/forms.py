from django import forms
from .models import Farminputs, Farminputtwo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Staff

#Form to enter farm records
class FarminputForm(forms.ModelForm):
    class Meta:
        model = Farminputs
        fields = ['plant_stage','plant_number','plant_age','cocopeat_name','cocopeat_weight',
                  'avg_temp','avg_water', 'seed_variety',
                  'daily_observation']
    
        widgets = {
            "daily_observation": forms.Textarea(attrs={"rows": 4}),  # 👈 make textarea taller
       
        }
        labels = {
            "plant_age":"plant_age (days)",
            "cocopeat_weight": "Cocopeat weight (kg)",  # 👈 adds (kg) to the field label
             "avg_temp": "avg_temp (°C)",
             "avg_water":"avg_water (L)",
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only show placeholder (no starting 0)
        if not self.instance or not self.instance.pk:
            self.fields['plant_number'].initial = None
            self.fields['plant_age'].initial = None
            self.fields['cocopeat_weight'].initial = None
            self.fields['avg_temp'].initial = None
            self.fields['avg_water'].initial = None
         


class FarminputtwoForm(forms.ModelForm):
    class Meta:
        model = Farminputtwo
        fields = ['fungicide_name','avg_fungicide','insecticide_name','avg_insecticide','herbicide_name','avg_herbicide', 
                  'micronutrient_name', 'avg_micronutrient','fertilizer_name', 
                  'avg_fertilizer']
        labels = {
              "avg_fungicide":"avg_fungicide (L)",
              "avg_insecticide":"avg_insecticide (L)",
              "avg_micronutrient":"avg_micronutrient (L)",
              "avg_fertilizer":"avg_fertilizer (kg)",
              "avg_herbicide":"avg_herbicide (L)"
          }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only show placeholder (no starting 0)
        if not self.instance or not self.instance.pk:
            self.fields['avg_herbicide'].initial = None
            self.fields['avg_fungicide'].initial = None    
            self.fields['avg_insecticide'].initial = None
            self.fields['avg_micronutrient'].initial = None
            self.fields['avg_fertilizer'].initial = None
            self.fields['avg_herbicide'].required  = False
            self.fields['fungicide_name'].required = False
            self.fields['avg_herbicide'].required = False
            self.fields['herbicide_name'].required = False
            self.fields['avg_fungicide'].required = False
            self.fields['fungicide_name'].required = False
            self.fields['insecticide_name'].required = False
            self.fields['avg_insecticide'].required = False
            self.fields['micronutrient_name'].required = False
            self.fields['avg_micronutrient'].required = False
            self.fields['fertilizer_name'].required = False
            self.fields['avg_fertilizer'].required = False
            
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


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'last_name' ]
class StaffUpdateForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['mobile', 'streetno', 'streetname','city','state','current_salary',
                  'gender','marital_status', 'emp_role','image']