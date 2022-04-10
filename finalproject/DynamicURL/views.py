from django.shortcuts import render

# Create your views here.
def showdata(request, my_id):
    return render(request, 'show.html',{})
