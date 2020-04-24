from django.shortcuts import render
from pyresparser import ResumeParser


# Create your views here.
def buildprofile_resume(request):
    data = ResumeParser('seeker/GL01VishwaMahadevan.pdf').get_extracted_data()
    return render(request,'seeker/rbuildprofile.html',{'resume':data})