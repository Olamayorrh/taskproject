from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from django import forms
def task_List(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_List.html', {'tasks':tasks})

class TaskForm(forms.ModelForm):
 class Meta:
  model = Task
  fields = ['title', 'description', 'completed']

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_List')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})


def task_update(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
       form = TaskForm(request.POST, instance=task)
       if form.is_valid():
          form.save()
          return redirect('task_List')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('task_list')