from django.shortcuts import render, get_object_or_404
from .models import Project, Task, Employee

def index(request):
    projects = Project.objects.all()
    tasks = Task.objects.all()
    employees = Employee.objects.all()
    return render(request, 'index.html', {'projects': projects, 'tasks': tasks, 'employees': employees})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProjectForm()
    return render(request, 'create_project.html', {'form': form})

def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EmployeeForm()
    return render(request, 'create_employee.html', {'form': form})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})
