from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout  #used for User Authentication
from django.contrib.auth.decorators import login_required #this is so we can restrict pages if you are not a logged in user
from django.contrib import messages #used to send a flash messages
from django.contrib.auth.models import Group #used to access our groups
from .models import Profile  #used to access our profile model
from .models import Buddies #import our characters model
from .forms import CreateUserForm





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


#View to register turtle 
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('portal_homePage') 
    else:
        form1 = CreateUserForm()
        if request.method == 'POST':
            form1 = CreateUserForm(request.POST)
            if form1.is_valid():
                registration_code = request.POST.get('registration_code') # get the value of the registration code from the form
                if registration_code != 'turtle': # check if the registration code is correct
                    messages.error(request, 'Invalid registration code.') # send an error message
                    return redirect('registerPage') # redirect back to the same page
                else:
                    user = form1.save()
                    group = Group.objects.get(name='premium')
                    user.groups.add(group)
                    username = user.username

                    profile = Profile.objects.create(user=user, bio='', firstName='', lastName='', age=None, profile_picture='static/images/profilePictures/default.jpg')
                    profile.save()

                    name = 'turtle'
                    Buddies.objects.create(user=user, name=name, picture='static/images/buddies/turtle.png')

                    messages.success(request, 'Account was created for ' + username )
                    return redirect('homePage')
        context = {'form1':form1,}
        return render(request, 'base/registerPage.html', context)
    

#view to register whale
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('portal_homePage') 
    else:
        form2 = CreateUserForm()
        if request.method == 'POST':
            form2 = CreateUserForm(request.POST)
            if form2.is_valid():
                registration_code = request.POST.get('registration_code') # get the value of the registration code from the form
                if registration_code != 'whale': # check if the registration code is correct
                    messages.error(request, 'Invalid registration code.') # send an error message
                    return redirect('registerPage') # redirect back to the same page
                else:
                    user = form2.save()
                    group = Group.objects.get(name='premium')
                    user.groups.add(group)
                    username = user.username

                    profile = Profile.objects.create(user=user, bio='', firstName='', lastName='', age=None, profile_picture='static/images/profilePictures/default.jpg')
                    profile.save()

                    name = 'whale'
                    Buddies.objects.create(user=user, name=name, picture='static/images/buddies/whale.png')

                    messages.success(request, 'Account was created for ' + username )
                    return redirect('homePage')
        context = {'form2':form2,}
        return render(request, 'base/registerPage.html', context)
    

#view to register seal
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('portal_homePage') 
    else:
        form3 = CreateUserForm()
        if request.method == 'POST':
            form3 = CreateUserForm(request.POST)
            if form3.is_valid():
                registration_code = request.POST.get('registration_code') # get the value of the registration code from the form
                if registration_code != 'seal': # check if the registration code is correct
                    messages.error(request, 'Invalid registration code.') # send an error message
                    return redirect('registerPage') # redirect back to the same page
                else:
                    user = form3.save()
                    group = Group.objects.get(name='premium')
                    user.groups.add(group)
                    username = user.username

                    profile = Profile.objects.create(user=user, bio='', firstName='', lastName='', age=None, profile_picture='static/images/profilePictures/default.jpg')
                    profile.save()

                    name = 'seal'
                    Buddies.objects.create(user=user, name=name, picture='static/images/buddies/seal.png')

                    messages.success(request, 'Account was created for ' + username )
                    return redirect('homePage')
        context = {'form3':form3,}
        return render(request, 'base/registerPage.html', context)
    
#View to register dolphin 
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('portal_homePage') 
    else:
        form4 = CreateUserForm()
        if request.method == 'POST':
            form4 = CreateUserForm(request.POST)
            if form4.is_valid():
                registration_code = request.POST.get('registration_code') # get the value of the registration code from the form
                if registration_code != 'dolphin': # check if the registration code is correct
                    messages.error(request, 'Invalid registration code.') # send an error message
                    return redirect('registerPage') # redirect back to the same page
                else:
                    user = form4.save()
                    group = Group.objects.get(name='premium')
                    user.groups.add(group)
                    username = user.username

                    profile = Profile.objects.create(user=user, bio='', firstName='', lastName='', age=None, profile_picture='static/images/profilePictures/default.jpg')
                    profile.save()

                    name = 'dolphin'
                    Buddies.objects.create(user=user, name=name, picture='static/images/buddies/dolphin.png')

                    messages.success(request, 'Account was created for ' + username )
                    return redirect('homePage')
        context = {'form4':form4,}
        return render(request, 'base/registerPage.html', context)
    
#View to register seagull
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('portal_homePage') 
    else:
        form5 = CreateUserForm()
        if request.method == 'POST':
            form5 = CreateUserForm(request.POST)
            if form5.is_valid():
                registration_code = request.POST.get('registration_code') # get the value of the registration code from the form
                if registration_code != 'seagull': # check if the registration code is correct
                    messages.error(request, 'Invalid registration code.') # send an error message
                    return redirect('registerPage') # redirect back to the same page
                else:
                    user = form5.save()
                    group = Group.objects.get(name='premium')
                    user.groups.add(group)
                    username = user.username

                    profile = Profile.objects.create(user=user, bio='', firstName='', lastName='', age=None, profile_picture='static/images/profilePictures/default.jpg')
                    profile.save()

                    name = 'seagull'
                    Buddies.objects.create(user=user, name=name, picture='static/images/buddies/seagull.png')

                    messages.success(request, 'Account was created for ' + username )
                    return redirect('homePage')
        context = {'form5':form5,}
        return render(request, 'base/registerPage.html', context)
    



    




#View for Logout used for logging out of the system
@login_required(login_url='homePage')
def logoutUser(request):
    logout(request) #logout method from Django import
    return redirect('homePage') # redirect user to back to home page when they logout

#View for portal home page

def portal_homePage(request):
    return render(request, 'base/portal_homePage.html')

#View for portal game page
def portal_gamePage(request):
    return render(request, 'base/portal_gamePage.html')

#View for portal video page
def portal_videoPage(request):
    return render(request, 'base/portal_videoPage.html')

#View for portal profile page
def portal_profilePage(request):
    return render(request, 'base/portal_profilePage.html')


