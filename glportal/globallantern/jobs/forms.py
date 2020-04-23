from django import forms
from .models import job_post as Addpost

JOBTYPE= [
    ('full_time', 'Full Time'),
    ('part_time', 'Part Time'),
    ('freelance','freelance')
    ]

class addPostForm(forms.ModelForm):
    class Meta:
        model=Addpost
        fields='__all__'
        widgets = {
            'job_title': forms.TextInput(attrs={'placeholder': 'eg. Full Stack Developer','class':'form-control'}),
            'company_id': forms.TextInput(attrs={'placeholder': 'eg. Global Lantern','class':'form-control'}),            
            'job_description':forms.Textarea(attrs={'class':'form-control'}),
            'closing_date':forms.DateTimeInput(attrs={'class':'form-control','type':'date'}),
            'minimum_pay':forms.TextInput(attrs={'placeholder': 'eg. $500','class':'form-control'}),
            'maximum_pay':forms.TextInput(attrs={'placeholder': 'eg. $2500','class':'form-control'})
        }