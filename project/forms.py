from django import forms
from .models import UserData

class UserTest(forms.ModelForm):
    class Meta:
        model=UserData
        fields = ['first_name','last_name','company_name','age','city','state','zip','email','web']