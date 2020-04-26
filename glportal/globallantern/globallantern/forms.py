from allauth.account.forms import SignupForm,UserForm,LoginForm
from django import forms



CHOICE= [
    ('job_seeker', 'Job Seeker'),
    ('company', 'Company')
    ]

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name') 
    last_name = forms.CharField(max_length=30, label='Last Name')
    user_type=forms.CharField(label='Job Seeker or Own company', widget=forms.Select(choices=CHOICE))

    def signup(self, request, user):
        user.user_type = self.cleaned_data['user_type']
        user.first_name = self.cleaned_data['first_name'] 
        user.last_name = self.cleaned_data['last_name'] 
        user.save()
        return user
    class Meta:
        fields = ("first_name", "last_name", "email", "username", "password1", "password2")
        fields_order=['first_name','last_name','email','username','password1','password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].label = 'First Name'
        self.fields["first_name"].widget.attrs["placeholder"] = "First Name"
        self.fields["first_name"].widget.attrs["class"] = "form-control"
        self.fields["last_name"].label = 'Last Name'
        self.fields["last_name"].widget.attrs["placeholder"] = "Last Name"
        self.fields["last_name"].widget.attrs["class"] = "form-control"
        self.fields["email"].label = 'Email'
        self.fields["email"].widget.attrs["placeholder"] = "Email"
        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["username"].label = 'Username'
        self.fields["username"].widget.attrs["placeholder"] = "Username"
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password1"].label = 'Password'
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].label = 'Confirm Password'
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"
        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["user_type"].widget.attrs["class"] = "form-control"
