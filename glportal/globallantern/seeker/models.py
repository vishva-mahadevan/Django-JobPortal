from django.db import models
from jobs.models import job_location,job_post,job_post_activity,job_post_skill_set,job_type
from seeker.models import education_detail,seeker_profile,seeker_skill_set,skill_set
from company.models import business_stream,company,company_image

# Create your models here.=
class seeker_profile(models.Model):
    user_account_id=models.IntegerField()
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    current_salary=models.IntegerField()
    is_annnually_monthly=models.CharField(max_length=1)
    currency=models.CharField(max_length=50)
    
    def __str__(self):
        return 'GLUser ID #{}'.format(self.id)

class education_detail(models.Model):
    user_account_id=models.OneToOneField(seeker_profile,on_delete=models.CASCADE)
    certificate_degree_name=models.CharField(unique=True,max_length=50)
    major=models.CharField(max_length=50,unique=True)
    institute_university_name=models.CharField(max_length=50)
    starting_date=models.DateField(auto_now=False)
    completion_date=models.DateField()
    percentage=models.IntegerField()
    CGPA=models.IntegerField()

class experience_details(models.Model):
    user_account_id=models.OneToOneField(seeker_profile,on_delete=models.CASCADE,unique=True)
    is_current_job=models.CharField(max_length=1)
    start_date=models.DateField(unique=True)
    end_date=models.DateField(unique=True)
    job_title=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    job_location_city=models.CharField(max_length=50)
    job_location_state=models.CharField(max_length=50)
    job_location_country=models.CharField(max_length=50)
    description=models.TextField(max_length=4000)
class skill_set(models.Model):
    skill_set_name=models.CharField(max_length=50)

class seeker_skill_set(models.Model):
    user_account_id=models.OneToOneField(seeker_profile,unique=True)
    skill_set_id=models.ManyToManyField(skill_set,unique=True)
    skill_level=models.IntegerField()