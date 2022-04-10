from http.client import HTTPResponse
import profile
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from UserCreationForm.forms import SignupForm

# Create your views here.

# def signup_view(request):
#     if request.method == 'POST':
#         form  = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = UserCreationForm()
#     return render(request, "UserCreationForm/signup.html", {'form':form})


# adding some additional form fields in inbuilt usercreationform

def signup_view(request):
    if request.method == 'POST':
        form  = SignupForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignupForm()
    return render(request, "UserCreationForm/signup.html", {'form':form})


#Login view function
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user  = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return HTTPResponse('/profile/')
    else:
        form = AuthenticationForm()
    return render(request, "UserCreationForm/userlogin.html",{'form':form})

#after login this view function is being rendered
def profile_view(request):
    if request.user.is_authenticated:
        return render(request, 'UserCreationForm/profile.html')
    else:
        return HTTPResponse('/login/')

# logout view function
def logout_view(request):
    logout(request)
    return HTTPResponse('/login/')