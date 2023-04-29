from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('delete_so_out/<pk>', views.delete_so_out, name='delete_so_out'),
    path('update_so_out/<pk>', views.update_so_out, name='update_so_out'),
    path('load_so_out/<pk>', views.load_so_out, name='load_so_out'),
 ]
