from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from django.views.generic import View
from django.views.generic import DetailView
from django.views.generic import UpdateView
from todo.forms import TodoForm
from todo.models import Task


# Create your views here.
def add(request):
    task2 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()

    return render(request,'home.html',{'task1':task2})
# def details(request):
#     task=Task.objects.all()
#     return render(request,'details.html',)
def detail(request,id):
    task = Task.objects.get(id=id)
    return render(request,"details.html",{'task':task})
def delete(request,id):
    if request.method=='POST':
        task=Task.objects.get(id=id)
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task = Task.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})

# class TasklistView(ListView):
#     model=Task
#     template_name='home.html'
#     context_object_name='task1'

# class TaskDetailView(DetailView):
#     task = Task.objects.all()
#     model=task
#     template_name='details.html'
#     context_object_name='task'

def get_success_url(self):
    return reverse_lazy('detail',Kwargs={'id':self.object.id})
# class TaskUpdateView(UpdateView):
#     model=Task
#     template_name='update.html'
#     context_object_name='task'
#     fields=('name','priority','date')
#     success_url = reverse_lazy('cbvhome')
#
# class TaskDeleteView(DeleteView):
#     model=Task
#     template_name='delete.html'
#     success_url = reverse_lazy('cbvhome')