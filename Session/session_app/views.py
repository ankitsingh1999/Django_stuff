from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def set_session(request):
    request.session['name1'] = 'Alex'
    request.session['name2'] = 'Onik'
    return render(request, 'session_app/setsession.html')

def get_session(request):
    if 'name1' in request.session:
        name1 = request.session.get('name1') #Guest is by default
        request.session.modified = True
        return render(request, 'session_app/getsession.html', {'name1':name1})
    else:
        return HttpResponse("Session has been expired")


def delete_session(request):
    request.session.flush()
    request.session.clear_expired()  #this is used to clear the expired session so db will not be full
    return render(request, 'session_app/delsession.html')