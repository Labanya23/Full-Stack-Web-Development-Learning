
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

tasks = ["foo","bar","baz"]

# Create your views here.

def index(request):
    if "tasks" not in request.sessions:
        request.sessions["task"] = []
    return render(request,"fall/index.html",{
        "tasks": request.session["tasks"]
    })

class NewTaskForm(forms.Form):
    task= forms.CharField(label="New Task")
    pariority = forms.IntegerField(label="Priority",min_value=1,max_value=100)

def add(request):
    if request.method =="POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form.cleanded_data["task"]
            #tasks.append(tasks)
            request.session["tasks"]+=[tasks]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request,"tasks/add.html",{
                "form": form
            })
    
    return render(request, "tasks/add.html",{
        "form": NewTaskForm()
    })

