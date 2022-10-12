from telnetlib import STATUS
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from todolist.models import Task
from todolist.forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers


@login_required(login_url='/todolist/login/')
def show_todolist(request):
    username = request.user
    # item_list = Task.objects.filter(user=username)

    # for task in item_list:
    #     if (task.is_finished == True):
    #         task.is_finished = "Done"
    #     else:
    #         task.is_finished = "Not Done"

    context = {
        'username': username,
        # 'list_of_tasks': item_list,
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
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
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'The username or password is incorrect!')
    context = {}
    return render(request, 'login.html', context)

@login_required(login_url='/todolist/login/')
def logout_user(request):
    logout(request)
    return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def create_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        form.instance.user = request.user
        form.save()
        if form.is_valid():
            form.save()
            messages.success(request, 'Your task has been successfully added!')
            return redirect('todolist:show_todolist')

    context = {'form':form}
    return render(request, 'create_task.html', context)

@login_required(login_url='/todolist/login/')
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")
        user = request.user

        new_task = Task(user=user, title=title, description=description)
        new_task.save()
        return HttpResponse(b"CREATED")

    return HttpResponseNotFound()

@login_required(login_url='/todolist/login/')
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def edit_task(request, pk):
    task = Task.objects.get(id=pk)
    if task.is_finished == True:
        task.is_finished = False
    else:
        task.is_finished = True
    task.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def get_todolist_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data))
