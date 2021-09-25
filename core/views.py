from core.models import Todo
from core.forms import Todoform
from django.shortcuts import redirect, render
from core.forms import Todoform


def home(request):
    form = Todoform()
    todos = Todo.objects.all()
    if request.method == 'POST':
        form = Todoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        

    return render(request,'home.html',{'form': form, 'todos': todos})

def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    form = Todoform(instance=todo)
    if request.method == 'POST':
        form = Todoform(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request,'update.html',{'form': form})

def delete(request, todo_id):
    if request.method == 'POST':
        Todo.objects.get(id=todo_id).delete()
        return redirect('home')

