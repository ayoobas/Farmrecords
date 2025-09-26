from django import forms
from .models import Farminputs
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit

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