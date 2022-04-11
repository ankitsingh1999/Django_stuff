from django.shortcuts import render
import random, json

# Create your views here.
def set_cookie(request):
    response = render(request, 'cookies_app/setcookie.html')
    response.set_cookie('name','Anksh', max_age=60*60*24*2)
    return response


def get_cookie(request):
    # name = request.COOKIES['name']
    name = request.COOKIES.get("name")

    return render(request, 'cookies_app/getcookie.html', {'name' : name})


def del_cookie(request):
    response = render(request, 'cookies_app/delcookie.html')
    response.delete_cookie('name')
    return response