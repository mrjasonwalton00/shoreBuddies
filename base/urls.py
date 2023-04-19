from django.urls import path
from . import views

urlpatterns = [

    #base urls
    path('', views.home, name='home'), #this will be the default page
   
  
]