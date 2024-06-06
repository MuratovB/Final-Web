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