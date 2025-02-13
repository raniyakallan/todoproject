from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Task
from . forms import ToDoForm



# Create your views here.
def add(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority = request.POST.get('priority', '')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()

    return render(request,"home.html",{'task1':task1})
#def details(request):
   # return render(request,"detail.html")

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task=Task.objects.get(id=id)
    f=ToDoForm(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})
