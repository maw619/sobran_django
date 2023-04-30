from django.http import JsonResponse
from django.shortcuts import render, redirect
from datetime import date, datetime, time
from .models import SoEmployee, SoOut,SoType
from django.contrib import messages
from .forms import AddSoOutsForm, AddEmployeeForm



def home(request):
    today = date.today() 
    emps = SoEmployee.objects.all()  
    emps.order_by('em_name')
    sout = SoOut.objects.filter(co_date=str(today)) 
    print(today)
    five = time(hour=5, minute=00, second=00)
    six = time(hour=6, minute=15, second=00)
   
    times_yellow = [time(hour=5, minute=00, second=00),time(hour=6, minute=00, second=00),time(hour=7, minute=00, second=00),time(hour=8, minute=00, second=00)]
    times_red = [time(hour=5, minute=00, second=00),time(hour=6, minute=00, second=00),time(hour=7, minute=00, second=00),time(hour=8, minute=00, second=00)]
    time_diff = datetime.combine(datetime.today(),sout[0].co_time_arrived ) - datetime.combine(datetime.today(), five)
    
    default_yellow = five
    default_red = six
    # print(time_diff)
    # print(str(time_diff)[0:4]) 
    if request.method == 'POST':
        today = request.POST.get('date_value') 
        print(today, "if post")
        sout = SoOut.objects.filter(co_date=str(today))  
        context = {'date':today, 'emps': emps, 'sout':sout}
    context = {'date':today, 'emps': emps, 'sout':sout, 'default_yellow':default_yellow, 'default_red':default_red, 'times_yellow':times_yellow,'times_red':times_red}
    return render(request, 'home.html', context)

 
def add_sout(request):
    form = AddSoOutsForm(request.POST or None)
    if request.method == 'POST':
        print("in function")
        if form.is_valid(): 
            form.save()
            messages.success(request, "transaction added")
            return redirect('home')  
    context = {'form':form}
    return render(request, 'add.html', context)

def add_employee(request):
    form = AddEmployeeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Employee Added")
            return redirect('home')
    return render(request, 'add-employee.html', {'form':form})
 
def view_transaction(request, pk):
    if request.user.is_authenticated:
        sout = SoOut.objects.get(co_id_key=pk)
        return render(request, 'transaction.html', {'sout':sout})
    messages.success(request, "You need to be logged in")
    return redirect('home')


def update_so_out(request, pk): 
    if request.user.is_authenticated:
        sout = SoOut.objects.get(co_id_key=pk) 
        form = AddSoOutsForm(instance=sout)
        if request.method == 'POST':
            form = AddSoOutsForm(request.POST, instance=sout)
            print("inside th update")
            form.save()
            messages.success(request, "updated successfully")
            return redirect('home')
        messages.success(request, "updated successfully")
        return render(request, 'update.html', {'form':form})
    else:
        messages.success(request, 'You need to be logged in')
        return redirect('home')


def delete_so_out(request, pk):
    if request.user.is_authenticated:
        sout = SoOut.objects.get(co_id_key=pk)
        sout.delete()
        messages.success(request, "deleted successfully")
    else:
        messages.success(request, "You need to be logged in")
    return redirect('home')

 