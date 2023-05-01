from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('delete_so_out/<pk>', views.delete_so_out, name='delete_so_out'),
    path('update_so_out/<pk>', views.update_so_out, name='update_so_outs'), 
    path('view_transaction/<pk>', views.view_transaction, name='view_transaction'),
    path('add', views.add_sout, name='add'),
    path('add_employee', views.add_employee, name='add_employee'),
    path('add_so_out', views.add_so_out, name='add_so_out'),
 ]
