from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority =forms.IntegerField(label="Priority", min_value=1, max_value=10)

# tasks =["foo","bar","baz"]
# tasks=[]
# Create your views here.
def index(request):
    if "tasks" not in request.session:  #it will have session so every user can see different values it store in tables
        request.session["tasks"]=[]
    return render(request,"tasks/index.html",{
        "tasks":request.session["tasks"]
    })

def add(request):
    if request.method == "POST": 
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            # tasks.append(task)
            request.session["tasks"]+=[task]
            return HttpResponseRedirect(reverse("tasks:index")) #it come back to task page
        else:
            return render(request,"tasks/add.html",{
                "form":form
            })
    return render(request,"tasks/add.html",{
        "form":NewTaskForm()
    })