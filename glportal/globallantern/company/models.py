from django.db import models
from jobs.models import job_location,job_post,job_post_activity,job_post_skill_set,job_type
from seeker.models import education_detail,seeker_profile,seeker_skill_set,skill_set
# Create your models here.
class business_stream(models.Model):
    business_stream_name=models.CharField(max_length=100)

class company(models.Model):
    company_name=models.CharField(max_length=100)
    profile_description=models.CharField(max_length=100)
    business_stream_id=models.ForeignKey(business_stream,on_delete=models.CASCADE)
    establishment_date=models.DateField()
    company_website_url=models.URLField()

    def __str__(self):
        return 'COMPANY ID #{}'.format(self.id)

class company_image(models.Model):
    company_id=models.ForeignKey(company)
    company_image=models.ImageField()