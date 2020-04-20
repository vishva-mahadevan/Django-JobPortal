from django.contrib import admin
from .models import company,company_image,business_stream
# Register your models here.
admin.site.register(company)
admin.site.register(company_image)
admin.site.register(business_stream)