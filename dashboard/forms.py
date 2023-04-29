from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from.models import SoOut






class AddSoOutsForm(ModelForm):
    class Meta:
        model = SoOut
        fields = ['co_fk_em_id_key','co_fk_type_id_key','co_date','co_time_dif']
        exclude = ['co_time_arrived']
        # labels = {
        #     "rep_fk_pr_key": 'Project',
        #     'rep_fk_emp_key': "Report By:",
        #     'rep_fk_emp_key_sup': "Supervisor", 
        #     'rep_notes': "Scope of Inspection",  
        # }
 
        widgets = { 
            'co_fk_em_id_key': forms.Select(attrs={'class':'form-select'}),
            'co_fk_type_id_key': forms.Select(attrs={'class':'form-select'}),
            'co_date': forms.DateInput(),
            'co_time_dif': forms.TextInput(attrs={'class':'form-control'}), 
        }