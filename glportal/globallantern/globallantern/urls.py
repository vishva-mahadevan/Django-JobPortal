"""globallantern URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
<<<<<<< HEAD
from home.views import index,navbar
from jobs.views import addpost,addpost_delete,addpost_edit,addpost_preview,addpost_update
from seeker.views import search_jobs, add_edit_profile,jobsFilterView
=======
from home.views import *
from jobs.views import *
from seeker.views import *
from django.conf import settings
from django.conf.urls.static import static

>>>>>>> ce2194b5be13a1438c60cd717131bea33565e221
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    #home pages 
    path('',index,name='home'),
<<<<<<< HEAD
    path('navbar',navbar),
    path('add_edit_profile',add_edit_profile),
=======
    path('uploadresume',uploadresume,name='uploadresume'),

    #Job Seeker Profile
    path('buildprofile_resume/',buildprofile_resume,name='buildprofiler'),
    
    #adding post 

>>>>>>> ce2194b5be13a1438c60cd717131bea33565e221
    path('addpost',addpost,name='addpost'),
    path('search_jobs', jobsFilterView, name='search_jobs'), #job_search_filter_view
    path('addpost_preview',addpost_preview,name='addpostpreview'),
    path('addpost_edit/<int:id>',addpost_edit,name='addpostedit'),
    path('addposr_update/<int:id>',addpost_update,name='addpostupdate'),
    path('addpost_delete/<int:id>',addpost_delete,name='addpostdelete'),

]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        