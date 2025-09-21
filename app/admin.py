from django.contrib import admin
from . models import Farminputs

# Register your models here.
@admin.register(Farminputs)
class FarmInputModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'avg_water', 'avg_pesticide', 'avg_temp', 'seed_variety', 'daily_observation', 'created_at')
