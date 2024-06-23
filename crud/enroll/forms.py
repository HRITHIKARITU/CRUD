from django import forms
from enroll.models import UserProfile

class EmployeeRegistration(forms.ModelForm):
    class Meta:#essential information is placed in Meta
        model = UserProfile
        fields = ['name','email','password']  
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }