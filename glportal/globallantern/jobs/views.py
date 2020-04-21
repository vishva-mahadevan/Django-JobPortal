from django.shortcuts import render

# Create your views here.
def postjob(request):
    return render(request,'jobs/addpost.html')