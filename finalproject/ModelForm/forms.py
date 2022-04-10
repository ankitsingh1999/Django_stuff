import email
from .models import User
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']

    #change the labels of the fields
        labels = {'name':'Your Name'}
