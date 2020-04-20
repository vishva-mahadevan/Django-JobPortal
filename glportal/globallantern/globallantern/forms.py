# from django import forms
# from django.contrib.auth.models import User
# from django.utils.translation import ugettext as _
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Div, Field
# from ajax_select.fields import AutoCompleteSelectField, AutoCompleteField
# from phonenumber_field.formfields  import PhoneNumberField
# from . import models
 
# class SignUpForm(forms.Form):
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=30)
#     phone_number = PhoneNumberField(label=_("Phone (Please state your country code eg. +91)"))
#     organisation = forms.CharField(max_length=50)
 
#     def signup(self, request, user):
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         """
#         profile, created = models.UserProfile.objects.get_or_create(user=user)
#         profile.phone_number = self.cleaned_data['phone_number']
#         profile.organisation = self.cleaned_data['organisation']
#         profile.save()
#         user.save()
#         """
#         up = user.profile
#         up.phone_number = self.cleaned_data['phone_number']
#         up.organisation = self.cleaned_data['organisation']
#         user.save()
#         up.save()
 
# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = models.UserProfile
#         fields = ("company", "job_title", "website", "about_text", "location")
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=30)
#     location = AutoCompleteSelectField("city", required=False)
#     job_title = AutoCompleteField("job_title")
#     company = AutoCompleteField("company")