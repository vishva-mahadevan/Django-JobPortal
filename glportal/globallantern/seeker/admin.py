from django.contrib import admin
from seeker.models import education_detail,seeker_profile,seeker_skill_set,skill_set
# Register your models here.

admin.site.register(education_detail)
admin.site.register(seeker_profile)
admin.site.register(skill_set)