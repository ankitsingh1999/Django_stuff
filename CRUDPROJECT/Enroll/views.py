from django.shortcuts import render
from django.shortcuts import redirect
from Enroll.forms import Registrationform
from .forms import Registrationform
from .models import User
from django.http import HttpResponseRedirect

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        formobj = Registrationform(request.POST)
        if formobj.is_valid():
            nm = formobj.cleaned_data['name']
            em = formobj.cleaned_data['email']
            passcode= formobj.cleaned_data['password']
            user = User(name=nm,email=em,password=passcode)
            user.save()
        formobj = Registrationform()
    else:
        formobj = Registrationform()
    
    db_data = User.objects.all()   
    return render(request, 'Enroll/addshow.html', {'form' : formobj, 'data':db_data})


def delete_data(request, id):
    if request.method == 'POST':
        data_ = User.objects.get(id=id)
        data_.delete()
        return HttpResponseRedirect('/')
    

def update_data(request, id):
    if request.method == 'POST':
        data = User.objects.get(id=id)
        form = Registrationform(request.POST, instance=data)
        if form.is_valid():
            form.save()

    else:
        data = User.objects.get(id=id)
        form = Registrationform(instance=data)
    return render(request, "Enroll/update.html", {'form': form})

