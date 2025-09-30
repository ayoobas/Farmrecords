from django import forms
from .models import Farminputs
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class FarminputForm(forms.ModelForm):
    class Meta:
        model = Farminputs
        fields = ['avg_temp','avg_water', 'pesticide_name','avg_pesticide','fertilizer_name', 
                  'avg_fertilizer', 'seed_variety','daily_observation']
    
        widgets = {
            "daily_observation": forms.Textarea(attrs={"rows": 4})  # 👈 make textarea taller
        }

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_method = "post"
    self.helper.layout = Layout(
        Row(
            Column('avg_temp', css_class='col-md-6'),
            Column('avg_water', css_class='col-md-6'),
        ),
        Row(
            Column('pesticide_name', css_class='col-md-6'),
            Column('avg_pesticide', css_class='col-md-6'),
        ),
        Row(
            Column('fertilizer_name', css_class='col-md-6'),
            Column('avg_fertilizer', css_class='col-md-6'),
        ),
        Row(
            Column('seed_variety', css_class='col-md-6'),
        ),
        Row(
            Column('daily_observation', css_class='col-12'),  # 👈 full width now
        ),
        Submit('submit', 'Submit', css_class="btn btn-success mt-3")
    )

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
