from django.urls import path
from . import views





urlpatterns = [
    path('', views.homePage, name='homePage'), #default url

    path('logout/', views.logoutUser, name='logout'), #url for logout 

    path('registerPage/', views.registerPage, name='registerPage'), #url for register page

    path('portal_homePage/', views.portal_homePage, name='portal_homePage'), #url for portal home page






]