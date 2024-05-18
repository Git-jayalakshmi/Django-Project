from django.shortcuts import render, redirect
from.models import Task
from.forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView

class TaskListView(ListView):
    model=Task
    template_name='Addtask.html'
    context_object_name = 'task1'

class TaskDetailView(DetailView):
    model=Task
    template_name='details.html'
    context_object_name = 'task'


# Create your views here.
def adddetails(request):
    task = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('Task','')
        priority=request.POST.get('Priority','')
        date=request.POST.get('Date','')
        task1=Task(name=name,priority=priority,date=date)
        task1.save()

    return render(request,'Addtask.html',{'task':task})

#def details(request):
#   return render(request,'details.html',)

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method =='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})