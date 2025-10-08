from django.contrib import admin
from . models import Farminputs
from import_export.admin import ImportExportModelAdmin

admin.site.site_header = 'OBAZ FarmInput'

# Register your models here.
@admin.register(Farminputs)
class FarmInputModelAdmin(ImportExportModelAdmin):
    list_display = ('id', 'user','avg_water', 'avg_pesticide', 'avg_temp', 'seed_variety', 'daily_observation', 'created_at')


