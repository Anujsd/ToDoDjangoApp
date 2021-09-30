from django.shortcuts import render,HttpResponseRedirect
from .forms import add_tasks
from .models import User

# Thos function will add tasks and show them
def add_show(request):
    if request.method=="POST":
        fm=add_tasks(request.POST)
        if fm.is_valid():
            tnm=fm.cleaned_data['task_name']
            tdesc=fm.cleaned_data['task_desc']
            reg=User(task_name=tnm,task_desc=tdesc)
            reg.save()
            # or fm.save()
            fm=add_tasks()
            return HttpResponseRedirect('/')
    else:
        fm=add_tasks()
    task_data=User.objects.all()
    return render(request,"enroll/addandshow.html",{'form':fm,'stu':task_data})

# this function will update and delete
def update_data(request,id):
    if request.method=="POST":
        pi = User.objects.get(pk=id)
        fm = add_tasks(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = add_tasks(instance=pi)
    return render(request,'enroll/updateData.html',{'form':fm})

# this will delete 
def delete_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')