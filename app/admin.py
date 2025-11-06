from django.contrib import admin
from . models import Farminputs, Farminputtwo, Staff
from import_export.admin import ImportExportModelAdmin

admin.site.site_header = 'OBAZ FarmInput'

# Register your models here.
@admin.register(Farminputs)
class FarmInputModelAdmin(ImportExportModelAdmin):
    list_display = ('id','plant_stage','plant_age','avg_water' ,
                     'avg_temp', 'seed_variety', 'daily_observation',  'user','created_at')

@admin.register(Farminputtwo)
class FarmInputtwoModelAdmin(ImportExportModelAdmin):
    list_display = ('id','FI','fungicide_name','avg_fungicide', 'insecticide_name',
                    'avg_insecticide' ,'micronutrient_name','avg_micronutrient', 
                    'fertilizer_name','avg_fertilizer')

@admin.register(Staff)
class StaffModelAdmin(ImportExportModelAdmin):
    list_display = ('id', 'mobile', 'streetno', 'streetname', 'city', 'state', 'emp_date',
                    'current_salary', 'marital_status','children_no','spouse_no')

