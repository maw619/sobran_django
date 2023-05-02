from django.db import models
from datetime import date,datetime


class SoEmployee(models.Model):
    em_id_key = models.AutoField(primary_key=True)
    em_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Employee', unique=True)
    em_zone = models.IntegerField(blank=True, null=True, verbose_name='Zone')
 
    class Meta:
        managed = True
        db_table = 'so_employees'
    def __str__(self) -> str:
        return self.em_name


class SoOut(models.Model):
    co_id_key = models.AutoField(primary_key=True)
    co_fk_em_id_key = models.ForeignKey('SoEmployee', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Employee', unique=True)
    co_fk_type_id_key = models.ForeignKey('SoType', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Type')
    co_date = models.DateField(blank=True, null=True, default=date.today(), verbose_name='Date')
    co_time_arrived = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name='Time Arrived', default=datetime.now().time())
    co_time_dif = models.CharField(max_length=45, blank=True, null=True, verbose_name='Time Difference') 
  
    class Meta:
        managed = True
        db_table = 'so_outs'
 
    def __str__(self) -> str:
        return str(self.co_fk_em_id_key)


class SoType(models.Model):
    type_id_key = models.AutoField(primary_key=True)
    description = models.CharField(max_length=45, blank=True, null=True, unique=True)

    class Meta:
        managed = True
        db_table = 'so_types'
    def __str__(self) -> str:
        return self.description

