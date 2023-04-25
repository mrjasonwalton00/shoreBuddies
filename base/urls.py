from django.urls import path
from . import views





urlpatterns = [
    path('', views.homePage, name='homePage'), #default url

    path('logout/', views.logoutUser, name='logout'), #url for logout 

    path('registerPage/', views.registerPage, name='registerPage'), #url for register page

    path('portal_homePage/', views.portal_homePage, name='portal_homePage'), #url for portal home page

    path('portal_profilePage/', views.portal_profilePage, name='portal_profilePage'), #url for portal home page

    path('portal_gamePage/', views.portal_gamePage, name='portal_gamePage'), #url for portal home page

    path('portal_videoPage/', views.portal_videoPage, name='portal_videoPage'), #url for portal home page

]