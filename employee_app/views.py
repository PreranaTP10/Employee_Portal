from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import Employee, Department, Role
from datetime import datetime


# Create your views here.
def index(request):
    return render(request, 'f1.html')


def show_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'all_emp.html', context)


def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, phone=phone, bonus=bonus,
                           dept_id=dept, role_id=role, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('Employee added successfully.')

    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return render('Exception occurred')


def del_emp(request, emp_id=0):
    emps = Employee.objects.all()

    if emp_id:
        try:
            employee_to_be_removed = Employee.objects.get(id=emp_id)
            employee_to_be_removed.delete()
            return HttpResponse('Employee removed successfully')

        except:
            return HttpResponse('Please Enter valid ID')
    context = {
        'emps': emps
    }
    return render(request, 'del_emp.html', context)


def filter_emp(request):
    if request.method=='POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps= emps.filter(Q(first_name__icontains= name) | Q(last_name__icontains= name))
        if dept:
            emps=emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)
        context={
            'emps':emps
        }
        return render(request,'all_emp.html',context)
    elif request.method=='GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse('an exception occurred')

