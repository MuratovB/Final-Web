from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('create_project/', views.create_project, name='create_project'), # URL для создания нового проекта
    path('create_employee/', views.create_employee, name='create_employee'), # URL для создания нового работника
    path('create_task/', views.create_task, name='create_task'), # URL для создания новой задачи
]
