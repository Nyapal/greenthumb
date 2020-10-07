from django.contrib import admin
from .models import Plant
# Register your models here.

class PlantAdmin(admin.ModelAdmin):
  list_display = ('title', 'description')

#Register models here
admin.site.register(Plant, PlantAdmin)