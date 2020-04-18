from django.shortcuts import render

# Create your views here.
def googlelogin(request):
    return render(request,'login.html')