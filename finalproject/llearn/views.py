from faulthandler import disable
from winreg import REG_QWORD
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from .forms import RegisForm
from .models import User

# Create your views here.
def learnDjango(request):
    return render(request, 'test.html', context={"name":"Anksh Singh"})

def homePage(request):
    stu_data = Student.objects.all()
    return render(request, "home.html", {'stu_data' : stu_data})

def basePage(request):
    return render(request, "base.html")


#formView
def regisPage(request):
    if request.method == 'POST':
      form = RegisForm(request.POST)
      if form.is_valid():
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        modelobj = User(name=username, email=email,password=password)
        modelobj.save()
        return render(request, "success.html",{'name':username})
    #     # return HttpResponseRedirect('/regis/success/')
    else:
        form = RegisForm()

        
    # form.order_fields(field_order=['email','name']) use to change the order of form fields
        return render(request, "registration.html",{'form':form})


def success(request):
    return render(request, 'success.html')

