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
        fields = [
            'plant_choice','plant_stage','plant_number','plant_age',
            'cocopeat_name','cocopeat_weight',
            'avg_temp','avg_water',
            'seed_variety','seed_variety_other',
            'daily_observation','image','created_at'
        ]

        widgets = {
            "daily_observation": forms.Textarea(attrs={"rows": 4}),
            "created_at": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control"
            }),
            "seed_variety_other": forms.TextInput(attrs={
                "placeholder": "Please specify the seed variety",
                # "style": "display:none;"
            }),
        }

        labels = {
            "plant_age": "Plant age (days)",
            "cocopeat_weight": "Cocopeat weight (kg)",
            "avg_temp": "Average temperature (°C)",
            "avg_water": "Average water (L)",
            # "image":"image(max 500KB allowed)",
            "created_at": "Observation Date",
             "seed_variety_other": "New_seed", 
        }

    def clean(self):   
        cleaned_data = super().clean()
        seed = cleaned_data.get('seed_variety')
        other = cleaned_data.get('seed_variety_other')

    # If "Other (OT)" is selected, require the extra input
        if seed == 'OT' and not other:
            self.add_error(
            'seed_variety_other',
            'Please specify the seed variety.'
        )

    # If NOT "Other", clear the extra field
        if seed != 'OT':
            cleaned_data['seed_variety_other'] = ''

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.instance.pk:
            for field in ['plant_number', 'plant_age', 'cocopeat_weight', 'avg_temp', 'avg_water']:
                self.fields[field].initial = None

        self.fields['seed_variety'].required = False
#For Farminputtwoform

class FarminputtwoForm(forms.ModelForm):
    class Meta:
        model = Farminputtwo
        fields = ['fungicide_name', 'fungicide_other','avg_fungicide','insecticide_name','insecticide_other','avg_insecticide',
                  'herbicide_name','herbicide_other','avg_herbicide', 
                  'micronutrient_name','micronutrient_other', 'avg_micronutrient','fertilizer_name','fertilizer_other',
                  'avg_fertilizer']
        labels = {
              "avg_fungicide":"avg_fungicide (ml)",
              "avg_insecticide":"avg_insecticide (ml)",
              "avg_micronutrient":"avg_micronutrient (ml)",
              "avg_fertilizer":"avg_fertilizer (kg)",
             
              "avg_herbicide":"avg_herbicide (ml)",
              
               "micronutrient_name":"micronutrient_name (ml)",
              "micronutrient_other":"New_micronutrient_name",
              "fungicide_other":"New_fungicide_name",
             "fertilizer_other":"New_fertilizer_name",
             "insecticide_other":"New_insecticide_name",
             "herbicide_other":"New_herbicide_name"

          }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only show placeholder (no starting 0)
    
        self.fields['avg_herbicide'].initial = None
        self.fields['avg_fungicide'].initial = None    
        self.fields['avg_insecticide'].initial = None
        self.fields['avg_micronutrient'].initial = None
        self.fields['avg_fertilizer'].initial = None    
       

        self.fields['herbicide_name'].required  = False
        self.fields['herbicide_other'].required  = False
        self.fields['avg_herbicide'].required  = False
      

        self.fields['fungicide_name'].required = False
        self.fields['fungicide_other'].required = False
        self.fields['avg_fungicide'].required = False

        self.fields['insecticide_name'].required = False
        self.fields['avg_insecticide'].required = False
        self.fields['insecticide_other'].required = False   

        self.fields['micronutrient_name'].required = False
        self.fields['avg_micronutrient'].required = False
        self.fields['micronutrient_other'].required = False
  
        self.fields['fertilizer_name'].required = False
        self.fields['avg_fertilizer'].required = False
        self.fields['fertilizer_other'].required = False
            
        
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
        # labels = {
        #     "image":"image (max 500KB allowed)",
        #         }