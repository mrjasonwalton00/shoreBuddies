from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout  #used for User Authentication
from django.contrib.auth.decorators import login_required #this is so we can restrict pages if you are not a logged in user
from django.contrib import messages #used to send a flash messages



#View for home Page used for signing into the system
def homePage(request):
    if request.user.is_authenticated: 
        return redirect('portal_homePage') #if the user is authenticated send them to the portal home page
    else:
        if request.method == 'POST': #check if we get a post request
            username = request.POST.get('username') #send username to username varible
            password = request.POST.get('password') #send password to password varible
            user = authenticate(request, username=username, password=password)
            if user is not None: #If we can see if there is a valid user
                login(request, user) #Django login method from import
                return redirect('portal_homePage') #sends user to the portal
            else: #if there is not a valid user
                messages.error(request, 'Username OR password is incorrect') #print flash message
        context = {}
        return render(request, 'base/homePage.html', context) #show the login page again so they can re enter the right credentials


#View for Logout used for logging out of the system
@login_required(login_url='homePage')
def logoutUser(request):
    logout(request) #logout method from Django import
    return redirect('homePage') # redirect user to back to home page when they logout


def registerPage(request):
    return render(request, 'base/registerPage.html')


#Login is required for the following pages

@login_required
def portal_homePage(request):
    return render(request, 'base/portal_homePage.html')

