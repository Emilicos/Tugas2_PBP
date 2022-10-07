from datetime import date
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib import messages
from todolist.form import TaskForm
from django.contrib.auth.decorators import login_required
from todolist.models import Task
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    context = {
        "nama": "Alvaro Austin",
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

@login_required(login_url='/todolist/login/')
def todolist_json(request):
    tasks = Task.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", tasks), content_type="application/json")

@login_required(login_url='/todolist/login/')
def add_task(request):
    if(request.method == "POST"):
        form = TaskForm(request.POST)
        if(form.is_valid):
            form.instance.user = request.user
            form_id = form.save()
            return JsonResponse({
                "data": form.data,
                "is_finished": False,
                "date": date.today(),
                "id": form_id.id,
            })

@csrf_exempt
def delete(request, pk):
    if(Task.objects.get(pk=pk).user == request.user):
        Task.objects.filter(pk = pk).delete()
        tasks = Task.objects.filter(user = request.user)
        kirim = []
        for task in tasks:
            data = {
                "id": task.pk,
                "title": task.title,
                "description": task.description,
                "date": str(task.date),
                "is_finished": task.is_finished,
            }
            kirim.append(data)
    
        return JsonResponse(kirim, safe = False)

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