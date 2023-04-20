from django.shortcuts import render

#userReg Views
def home(request):
    return render(request, 'base/home.html')

