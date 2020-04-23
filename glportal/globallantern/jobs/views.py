from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import job_post
from .forms import addPostForm
# Create your views here.
def addpost(request):
    if request.method=="POST":
        form=addPostForm(request.POST or None)
        if form.is_valid():
            try:
                form.save()
                return redirect('/addpost_preview')
            except:
                pass
    else:
        form=addPostForm()
    return render(request,'jobs/addpost.html',{'form':form})

def addpost_preview(request):
    showjob=job_post.objects.all()
    return render(request,'jobs/addpost_preview.html',{'job':showjob})

def addpost_edit(request,id):
     showjob=job_post.objects.all(id=id)
     return render(request,'jobs/addpost_edit.html',{'job':showjob})

def addpost_update(request,id):
    showjob=job_post.objects.all(id=id)
    form=addPostForm(request.POST,instance=showjob)
    if form.is_valid():
        form.save()
        return redirect('/addpost_preview')
    return render(request,'jobs/addpost_update.html',{'job':showjob})

def addpost_delete(request,id):
    showjob=job_post.objects.all(id=id)
    showjob.delete()
    return redirect('/addpost_preview')