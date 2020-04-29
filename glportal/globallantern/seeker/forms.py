from django import forms
from .models import seeker_profile


class seekerProfileForm(forms.ModelForm):
    class Meta:
        model = seeker_profile
        fields=['first_name','last_name','current_salary','is_annnually_monthly','currency']
        widgets = { 
          'first_name': forms.TextInput(attrs={'placeholder': 'First Name','class':'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name','class':'form-control'}),            
            'current_salary':forms.TextInput(attrs={'placeholder': 'Current Salary','class':'form-control'}),
            'is_annnually_monthly':forms.CheckboxInput(attrs={'placeholder': '','class':'form-control'}),
            'currency':forms.TextInput(attrs={'placeholder': 'eg. $500','class':'form-control'}),
        }