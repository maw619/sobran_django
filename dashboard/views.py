from django.http import JsonResponse
from django.shortcuts import render, redirect
from datetime import date 
from datetime import date
from .models import SoEmployee, SoOut,SoType
from django.contrib import messages
from .forms import AddSoOutsForm



def home(request):
    today = date.today() 
    emps = SoEmployee.objects.all() 
    sout = SoOut.objects.filter(co_date=str(today)) 
    form = AddSoOutsForm()

    if request.method == 'POST':
        print("in function")
        form = AddSoOutsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "transaction added")
            return redirect('home')  
        
    context = {'date':today, 'emps': emps, 'sout':sout, 'form':form}
    return render(request, 'home.html', context)

def load_so_out(request):
    pass

def update_so_out(request, pk):
    sout = SoOut.objects.get(co_id_key=pk) 
    form = AddSoOutsForm(request.POST, instance=sout)
    if form.is_valid():
        print("inside th update")
        form.save()
        messages.success(request, "updated successfully")
        return redirect('home')
    return render(request, 'home.html', {'form':form})


def delete_so_out(request, pk):
    sout = SoOut.objects.get(co_id_key=pk)
    sout.delete()
    messages.success(request, "deleted successfully")
    return redirect('home')

 