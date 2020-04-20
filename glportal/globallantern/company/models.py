from django.db import models
from jobs import models as m1 
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
    company_id=models.ForeignKey(company,on_delete=models.CASCADE)
    company_image=models.ImageField()