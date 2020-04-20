from django.contrib import admin
from .models import job_location,job_post,job_post_activity,job_post_skill_set,job_type


# Register your models here.
admin.site.register(job_location)
admin.site.register(job_post)
admin.site.register(job_post_activity)
admin.site.register(job_post_skill_set)
admin.site.register(job_type)