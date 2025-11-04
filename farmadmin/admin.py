from django.contrib import admin
from .models import Farm, Field, IrrigationPoint

@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner_name', 'area', 'created_on')
    search_fields = ('name', 'owner_name')

@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'farm', 'crop_type', 'area', 'planted_on')
    list_filter = ('crop_type',)
    search_fields = ('name',)
    raw_id_fields = ('farm',)  # makes foreign key searchable

@admin.register(IrrigationPoint)
class IrrigationPointAdmin(admin.ModelAdmin):
    list_display = ('point_id', 'field', 'water_source', 'installed_on')
    search_fields = ('point_id',)
    raw_id_fields = ('field',)
