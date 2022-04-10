from django.urls import path
from .views import showdata

urlpatterns = [
    path('show/<int:my_id>/',showdata),
   
]
