from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
from .filehandler import handle_uploaded_file
# Create your views here.
def index(request):
    return render(request,'index.html')

def uploadresume(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('File Uploaded Successfully')
    else:
        form = UploadFileForm()
    return render(request, 'home/upload_resume.html', {'form': form})