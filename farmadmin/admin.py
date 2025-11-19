from django.contrib import admin
from .models import Farm, Field, IrrigationPoint

@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner_name', 'area', 'created_on', 'last_update', 'last_update_by',)
    readonly_fields = ('last_update', 'last_update_by')
    search_fields = ('name', 'owner_name')
    list_filter = ('created_on',)


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('name','farm','crop_type','area','planted_on','last_update','last_update_by',)
    readonly_fields = ('last_update', 'last_update_by')
    list_filter = ('crop_type',)
    search_fields = ('name', 'farm__name')
    raw_id_fields = ('farm',)


@admin.register(IrrigationPoint)
class IrrigationPointAdmin(admin.ModelAdmin):
    list_display = ('point_id','field','water_source','installed_on','last_update','last_update_by',)
    readonly_fields = ('last_update', 'last_update_by')
    search_fields = ('point_id',)
    raw_id_fields = ('field',)
