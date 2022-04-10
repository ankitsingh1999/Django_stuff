from django import forms
from django.core import validators


class RegisForm(forms.Form):
    name = forms.CharField(label='UserName', label_suffix=':',initial='Admin',required=True,
                            disabled=True)
    lastname = forms.CharField()
    username  = forms.CharField()
    email = forms.EmailField(error_messages={'required':'Enter your Email Id'})
    password = forms.CharField()
    Repassword = forms.CharField(max_length=10)
    passcode = forms.IntegerField(widget=forms.HiddenInput,required=False)
    date = forms.DateTimeField()

#validatation on complete form in one go
    def clean(self):
        cleaned_data = super().clean()
        pass2 = self.cleaned_data['Repassword']
        pass1 = self.cleaned_data['password']
        if pass1 !=  pass2:
            raise forms.ValidationError("Password did not match")


