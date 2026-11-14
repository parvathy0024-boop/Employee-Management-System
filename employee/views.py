from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from django.db.models import Q


# View all employees and search
def employee_list(request):
    query = request.GET.get('search')

    employees = Employee.objects.all().order_by('-id')

    if query:
        employees = employees.filter(
            Q(name__icontains=query) |
            Q(employee_id__icontains=query) |
            Q(email__icontains=query) |
            Q(department__icontains=query)
        )

    return render(request, 'employee_list.html', {
        'employees': employees,
        'query': query
    })


# Add employee
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()

    return render(request, 'employee_form.html', {
        'form': form,
        'title': 'Add Employee'
    })


# View employee details
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    return render(request, 'employee_detail.html', {
        'employee': employee
    })


# Edit employee
def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'employee_form.html', {
        'form': form,
        'title': 'Edit Employee'
    })


# Delete employee
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')

    return render(request, 'employee_confirm_delete.html', {
        'employee': employee
    })