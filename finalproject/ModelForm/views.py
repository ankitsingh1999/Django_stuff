from django.shortcuts import render

from ModelForm.forms import UserForm

# Create your views here.
def registrationPage(request):
    if request.method == 'POST':
      form = UserForm(request.POST)
      if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        print(name,email,password)
        # modelobj = User(name=username, email=email,password=password)
        # modelobj.save()
    else:
        form = UserForm()
        
        
    return render(request, "registration.html",{'form':form})
