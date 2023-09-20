from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def home(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('website:home')
        else:
            messages.success(request, "Incorrect username or password")
            return redirect('website:home')
    else:
        return render(request,'website/home.html',{'home':'home'})




# def login(request):
#     return render(request,'webiste/login.html',{})





def user_logout(request):
    logout(request)
    messages.success(request,'You Have Been Logged Out!...')
    return redirect('website:home')





def register(request):
    
    return render(request,'website/register.html',{})