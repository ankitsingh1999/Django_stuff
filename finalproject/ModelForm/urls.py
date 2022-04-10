from llearn import views


from django.urls import path
from .views import registrationPage

urlpatterns = [
    path('registration/', registrationPage),
   
]
