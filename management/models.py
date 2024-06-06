from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100, default='name')
    last_name = models.CharField(max_length=100, default='surname')
    email = models.EmailField()
    position = models.CharField(max_length=100, default='pos')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

class Task(models.Model):
    title = models.CharField(max_length=100, default='Title')
    description = models.TextField()
    status = models.CharField(max_length=50, default='Status')
    start_date = models.DateField()
    due_date = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Project(models.Model):
    name = models.CharField(max_length=200, default='Project')
    description = models.TextField()
    start_date = models.DateField()
    due_date = models.DateField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.name