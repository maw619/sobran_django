from django.contrib import admin
from .models import SoEmployee,SoOut,SoType 
from django.contrib.auth.models import Group
from django.urls import reverse
from django.utils.html import format_html



 
admin.site.unregister(Group)

@admin.register(SoOut)
class SoOutAdmin(admin.ModelAdmin): 
    list_display = ['co_fk_em_id_key', 'co_fk_type_id_key', 'co_date', 'co_time_arrived', 'co_time_dif']
    list_filter = ('co_fk_em_id_key', 'co_fk_type_id_key', 'co_date', 'co_time_arrived', 'co_time_dif')
    search_fields = ('co_fk_em_id_key', 'co_fk_type_id_key', 'co_date', 'co_time_arrived', 'co_time_dif')
    ordering = ('co_fk_type_id_key', ) 
    list_per_page = 25 
  
    fieldsets = (
        ('Employee', {
            'fields': ('co_fk_em_id_key', 'co_fk_type_id_key', 'co_date','co_time_arrived')
        }),
    )

    def get_ordering(self, request):
        return ['co_fk_em_id_key', 'co_fk_type_id_key', 'co_date', 'co_time_arrived', 'co_time_dif']

    def save_model(self, request, obj, form, change):
        if obj.co_fk_type_id_key.description == 'Vacation':
            obj.co_time_arrived = None
            obj.co_time_dif = None
        else:
            pass

        super().save_model(request, obj, form, change)




# @admin.register(SoType)
# class SoTypeAdmin(admin.ModelAdmin):
#     list_display = ('type_id_key', 'description')
#     list_filter = ('description',)
#     search_fields = ('description',)
#     ordering = ('description',)
#     list_per_page = 25
#     fieldsets = (
#         ('Type', {
#             'fields': ('description',)
#         }),
#     )
#     def get_ordering(self, request):
#         return ['description']




@admin.register(SoEmployee)
class SoEmployeeAdmin(admin.ModelAdmin):
    list_display = ('em_name', 'em_zone')
    list_filter = ('em_zone',)
    search_fields = ('em_name',)
    ordering = ('em_name',)
    list_per_page = 33
    fieldsets = (
        ('Employee', {
            'fields': ('em_name', 'em_zone')
        }),
    )
    def get_ordering(self, request):
        return ['em_name']


