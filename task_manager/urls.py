"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views
urlpatterns = [
    path('', views.register, name='register'),  # Registration page as the initial landing page
    path('home',views.home,name='home'),
    path('tasks/', views.task_list, name='task_list'),  # View all tasks
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),  # Task details
    path('task/create/', views.create_task, name='create_task'),  # Create a task
    path('task/<int:task_id>/update/', views.update_task, name='update_task'),  # Update a task
    path('task/<int:task_id>/delete/', views.delete_task, name='delete_task'),  # Delete a task
    path('task/<int:task_id>/edit/', views.edit_task, name='edit_task'),  # Edit a task
    path('register/', views.register, name='register'),  # Registration page
    path('login/', views.user_login, name='login'),  # Login page
    path('logout/', views.user_logout, name='logout'),  # Logout page
]

