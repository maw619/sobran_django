from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from.models import SoOut, SoEmployee



    # co_id_key = models.AutoField(primary_key=True)
    # co_fk_em_id_key = models.ForeignKey('SoEmployee', on_delete=models.CASCADE, null=True, blank=True)
    # co_fk_type_id_key = models.ForeignKey('SoType', on_delete=models.CASCADE, null=True, blank=True)
    # co_date = models.DateField(blank=True, null=True, default=date.today())
    # co_time_arrived = models.TimeField(auto_now=True, auto_now_add=False)
    # co_time_dif = models.CharField(max_length=45, blank=True, null=True)


class AddSoOutsForm(ModelForm):
    class Meta:
        model = SoOut
        fields = ['co_fk_em_id_key','co_fk_type_id_key','co_date','co_time_dif','co_time_arrived']
        #exclude = ['co_time_arrived']
        labels = {
            "co_fk_em_id_key": 'Name',
            'co_fk_type_id_key': "Type", 
            'co_time_arrived': 'Time Arrived'
        }
 
        widgets = { 
            'co_fk_em_id_key': forms.Select(attrs={'class':'form-select'}),
            'co_fk_type_id_key': forms.Select(attrs={'class':'form-select', 'id':'my-dropdown'}), 
            'co_time_arrived': forms.HiddenInput(),
            'co_date': forms.HiddenInput(),
            'co_time_dif': forms.HiddenInput()
        }

class UpdateoOutsForm(ModelForm):
    class Meta:
        model = SoOut
        fields = ['co_fk_em_id_key','co_fk_type_id_key','co_date','co_time_dif','co_time_arrived']
        #exclude = ['co_time_arrived']
        labels = {
            "co_fk_em_id_key": 'Name',
            'co_fk_type_id_key': "Type", 
            'co_time_arrived': 'Time Arrived'
        }
 
        widgets = { 
            'co_fk_em_id_key': forms.Select(attrs={'class':'form-select'}),
            'co_fk_type_id_key': forms.Select(attrs={'class':'form-select', 'id':'my-dropdown'}),
            #'co_time_arrived': forms.widgets.TimeInput(attrs={'class':'form-control', 'id':'my-field'}),
            'co_time_arrived': forms.HiddenInput(),
            #'co_date': forms.DateInput(attrs={'class':'form-control'}),
            'co_date':forms.HiddenInput(),
            'co_time_dif': forms.HiddenInput()
        }

class AddEmployeeForm(ModelForm):
    class Meta:
        model = SoEmployee
        exclude = ['em_id_key']
        labels = {
            'em_name': 'Name',
            'em_zone': 'Zone'
        }

        widgets = {
            'em_name' : forms.widgets.TextInput(attrs={'class':'form-control'}),
            'em_zone' : forms.widgets.TextInput(attrs={'class':'form-control'})
        }
