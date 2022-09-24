from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from todolist.form import TaskForm
from django.contrib.auth.decorators import login_required
from todolist.models import Task
# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    tasks = Task.objects.filter(user = request.user)
    context = {
        "nama": "Alvaro Austin",
        "tasks": tasks,
        "student_id": 2106752180,
        "user": request.user
    }
    return render(request, 'todolist.html', context)
    
@login_required(login_url='/todolist/login/')
def create_task(request):
    if(request.method == "POST"):
        form = TaskForm(request.POST)
        if(form.is_valid):
            form.instance.user = request.user
            form.save()
           
        return redirect('todolist:show_todolist')
    context = {}
    return render(request, 'create_task.html', context)

@login_required(login_url='/todolist/login/')
def change_task_status(request, pk):
    if(Task.objects.get(pk = pk).is_finished == True and Task.objects.get(pk=pk).user == request.user):
        Task.objects.filter(pk = pk).update(is_finished = False)
    else:
        if(Task.objects.get(pk=pk).user == request.user):
            Task.objects.filter(pk = pk).update(is_finished = True)
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def delete_task(request, pk):
    if(Task.objects.get(pk=pk).user == request.user):
        Task.objects.filter(pk = pk).delete()
    return redirect('todolist:show_todolist')

def register(request):
    form = UserCreationForm()
    if(request.method == "POST"):
        form = UserCreationForm(request.POST)
        if(form.is_valid):
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response 