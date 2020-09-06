from django.shortcuts import render,redirect
from .models import Todo
from .forms import Taskform
# Create your views here.

def todos(request):
    form = Taskform()
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    tasks = Todo.objects.all()
    context = {'form':form,'tasks':tasks}


    return render(request, 'index.html',context)


