from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm, UserRegistrationForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User  # Importez le modèle User


@login_required
def task_list(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user).order_by('-created_at')
        form = TaskForm()

        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                new_task = form.save(commit=False)
                new_task.user = request.user
                new_task.save()
                return redirect('task_list')

        context = {'tasks': tasks, 'form': form}
        return render(request, 'tasks/task_list.html', context)
    else:
        return render(request, 'tasks/welcome.html')  # Rediriger vers une page d'accueil pour les non-connectés

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@require_POST
def toggle_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})

@require_POST
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    task.delete()
    return redirect('task_list')