from django.contrib import admin
from .models import SoEmployee,SoOut,SoType 
from django.contrib.auth.models import Group
from django.urls import reverse
from django.utils.html import format_html
from datetime import date, datetime, time


 
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
            zone = form.instance.co_fk_em_id_key.em_zone 
            obj.co_time_dif = None 
            return super().save_model(request, obj, form, change) 
        else:
            obj.co_time_arrived = form.cleaned_data['co_time_arrived'] 
            type_with_name = form.cleaned_data['co_fk_type_id_key'].description
            zone = form.instance.co_fk_em_id_key.em_zone

            time_arrival = obj.co_time_arrived = form.cleaned_data['co_time_arrived']
            print(time_arrival)
            five = time(hour=5, minute=00, second=00)
            six = time(hour=6, minute=15, second=00)
            if zone == 1:
                time2 = five
            else:
                time2 = six  
                 
            timedelta_obj = datetime.combine(datetime.today(), time_arrival) - datetime.combine(datetime.today(), time2)
            seconds = timedelta_obj.total_seconds()
            hours = int(seconds // 3600)
            minutes = int((seconds // 60) % 60)
            seconds = int(seconds % 60)
            formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"
            obj.co_time_dif = formatted_time
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


