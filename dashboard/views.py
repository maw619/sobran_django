from django.http import JsonResponse
from django.shortcuts import render, redirect
from datetime import date, datetime, time
from .models import SoEmployee, SoOut,SoType,Shift
from django.contrib import messages
from .forms import AddSoOutsForm, AddEmployeeForm, UpdateoOutsForm, AddShiftForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required


     
# five = time(hour=5, minute=00, second=00)
# six = time(hour=6, minute=15, second=00)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password') 
        user = authenticate(request, username=username, password=password) 
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('login')



@login_required(login_url='login')
def home(request):
    
    today = date.today() 
    emps = SoEmployee.objects.all()  
    emps.order_by('em_name')
    sout = SoOut.objects.filter(co_date=str(today)) 
    shift = Shift.objects.all()

    #times_yellow = [time(hour=5, minute=00, second=00),time(hour=6, minute=00, second=00),time(hour=7, minute=00, second=00),time(hour=8, minute=00, second=00)]
    #times_red = [time(hour=5, minute=00, second=00),time(hour=6, minute=00, second=00),time(hour=7, minute=00, second=00),time(hour=8, minute=00, second=00)]
    
    form = AddShiftForm()
 
    shift = Shift.objects.all()
    for x in shift:
        y_start = x.yellow_start
        r_start = x.red_start

    print(request.POST.get('yellow_start'))
    if request.method == 'POST':
        today = request.POST.get('date_value') 
        date_value = datetime.strptime(today, '%Y-%m-%d').date()
        sout = SoOut.objects.filter(co_date=str(today))  
        context = {'date':date_value, 'emps': emps, 'sout':sout, 'yellow_start':str(y_start),'red_start':str(r_start)}
        return render(request, 'home.html', context)
    elif 'form2_submit' in request.POST:
        form = AddShiftForm(request.POST or None)
        form.instance.yellow_start = request.POST.get('yellow_start')
        form.instance.red_start = request.POST.get('red_start')
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'date':today, 'emps': emps, 'sout':sout, 'yellow_start':str(y_start),'red_start':str(r_start)}
    return render(request, 'home.html', context)


  
 
@login_required(login_url='login')
def add_sout(request):

    shift = Shift.objects.all()
    for x in shift:
        y_start = x.yellow_start
        r_start = x.red_start

    form = AddSoOutsForm(request.POST or None, initial={'co_time_arrived': datetime.now().time(), 'co_date': date.today()}) 
    print(datetime.now().time())
    if request.method == 'POST':
        if form.is_valid():  
            #form.instance.co_date = request.POST.get('date')
            zone = form.instance.co_fk_em_id_key.em_zone
            if zone == 1:
                time = y_start
            else:
                time = r_start  

            type_with_name = form.instance.co_fk_type_id_key.description
            if type_with_name == "Vacation" or type_with_name == "Call-out" or type_with_name == "Left early":
                form.instance.co_time_arrived = None
                form.instance.co_time_dif = None 
                form.save()
                messages.success(request, f"Marked as {type_with_name}")
                return redirect('home') 
            else:
                time_arrived = form.instance.co_time_arrived 
                messages.success(request, "transaction added")
                form.save()  
                if time_arrived is not None:
                    time_diff = datetime.combine(datetime.today(), time_arrived ) - datetime.combine(datetime.today(), time) 
                else:
                    time_diff = None
                form.instance.co_time_dif = str(time_diff)[0:4]
                print("time diff: ", form.instance.co_time_dif)
                form.save() 
                return redirect('home')  
            
    context = {'form':form}
    return render(request, 'add.html', context)


@login_required(login_url='login')
def update_so_out(request, pk): 
    shift = Shift.objects.all()
    for x in shift:
        y_start = x.yellow_start
        r_start = x.red_start
    if request.user.is_authenticated:
        sout = SoOut.objects.get(co_id_key=pk) 
        form = UpdateoOutsForm(instance=sout) 
        form.instance.co_date = request.POST.get('date')

        if request.method == 'POST':
            form = UpdateoOutsForm(request.POST, instance=sout)
 
            print("time arrived: ", form.instance.co_time_arrived)
            form.save()
            zone = form.instance.co_fk_em_id_key.em_zone
            if zone == 1:
                time = y_start
            else:
                time = r_start  

            time_value = request.POST.get('time')
            if time_value == "":
                time_obj = None
            else:
                time_obj = datetime.strptime(time_value, '%H:%M').time()
            date_value = request.POST.get('date')
            date_obj = datetime.strptime(date_value, '%Y-%m-%d').date()
            print("date obj: ", date_obj)
            form.instance.co_date = date_obj
            form.instance.co_time_arrived = time_obj
             
            form.save()  
            if time_obj is not None:
                time_diff = datetime.combine(datetime.today(), time_obj) - datetime.combine(datetime.today(), time) 
            else:
                time_diff = None
            form.instance.co_time_dif = str(time_diff)[0:4]
            print("time diff: ", form.instance.co_time_dif)
            form.save()  
            return redirect('home')
         
        return render(request, 'update.html', {'form':form})
    else:
        messages.success(request, 'You need to be logged in')
        return redirect('home')

#not used
def add_so_out(request): 
    
    emps = SoEmployee.objects.all()  
    types = SoType.objects.all()
    if request.method == 'POST':
        name = request.POST.get('single1')
        type = request.POST.get('single2')
        date = request.POST.get('date')
        newSout = SoOut.objects.create(co_fk_em_id_key=name, co_fk_type_id_key=type, co_date=date)
        newSout.save()
        messages.success(request, "transaction added")
        return redirect('home')
    else:
        context = {'emps': emps,'types': types}
        return render(request, 'add.html', context)
    
    
@login_required(login_url='login')
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



@login_required(login_url='login')
def delete_so_out(request, pk):
    if request.user.is_authenticated:
        sout = SoOut.objects.get(co_id_key=pk)
        sout.delete()
        messages.success(request, "deleted successfully")
    else:
        messages.success(request, "You need to be logged in")
    return redirect('home')

 