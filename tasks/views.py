from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate
from .models import Task
from django.contrib.auth.decorators import login_required

from django.urls import reverse 

def home(request):
    return render(request, 'home.html')

def task_list(request):
    tasks = Task.objects.order_by('due_date')  
    return render(request, 'task_list.html', {'tasks': tasks})

def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'task_detail.html', {'task': task})

@login_required
def create_task(request):
   
    return render(request, 'create_task.html')


def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
   
    return render(request, 'update_task.html', {'task': task})


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'delete_task.html', {'task': task})

from .forms import TaskForm


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', task_id=task_id)
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    
    return render(request, 'delete_task.html', {'task': task})

from django.shortcuts import render
from .forms import CustomUserCreationForm  

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect(reverse('login'))
            
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                auth_login(request, user)
                return redirect('home') 
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

from django.contrib.auth import logout as auth_logout

def user_logout(request):
    auth_logout(request) 
    return redirect('login') 
