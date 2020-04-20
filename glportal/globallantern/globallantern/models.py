# from __future__ import unicode_literals
# from django.db import models
# from django.contrib.auth.models import User
# from django.utils.translation import ugettext as _
# from easy_thumbnails.fields import ThumbnailerImageField
# from ciasroot.settings import THUMBNAILER_SIZES, UPLOAD_PATH
# from ciasroot.constants import GENDERS, LANGUAGES
# from ciasroot.util import HashedPk
# import math, decimal, datetime, os
 
 
# class UserProfile(models.Model, HashedPk):
#     user = models.OneToOneField(User, unique=True)
#     company = models.CharField(max_length=128, blank=True, null=True)
#     job_title = models.CharField(max_length=128, blank=True, null=False, default="")
#     gender = models.CharField(max_length=1, choices=GENDERS, null=True, blank=True)
#     website = models.URLField(max_length=255, blank=True, null=True)