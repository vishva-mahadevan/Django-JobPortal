from django.shortcuts import render
<<<<<<< HEAD
from .forms import seekerProfileForm
from jobs.models import job_post
from django.db.models import Q
# Create your views here.
def search_jobs(request):
    return render(request,'seeker/search_jobs.html')

def jobsFilterView(request):
    qs=""
    jobs_query=request.GET.get('jobs')
    jobs_location=request.GET.get('location')
    if jobs_query!= '' and jobs_query is not None:
        qs=job_post.objects.all()
        qs=qs.filter((Q(job_title__icontains=jobs_query) & Q(job_location_id__city__icontains=jobs_location))) #filters jobs based on the given location
    context = {
        'query_set' : qs,
        'job' : jobs_query
    }
    return render(request,'seeker/search_jobs.html',context)

def add_edit_profile(request):
    if request.method=="POST":
        form=seekerProfileForm(request.POST or None)
        if form.is_valid():
            print("Form is saved")
            try:
                form.save()
                return redirect('')
            except:
                print("Not working")
        else:
            print("form is not working")
    else:
        form=seekerProfileForm()
    return render(request,'seeker/add_edit_profile.html',{'form':form})
=======
from pyresparser import ResumeParser


# Create your views here.
def buildprofile_resume(request):
    data = ResumeParser('seeker/GL01VishwaMahadevan.pdf').get_extracted_data()
    return render(request,'seeker/rbuildprofile.html',{'resume':data})
>>>>>>> ce2194b5be13a1438c60cd717131bea33565e221
