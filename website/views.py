from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record
# Create your views here.


def home(request):
    records = Record.objects.all()




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
        return render(request, 'website/home.html', {'home':'home', 'records':records})




# def login(request):
#     return render(request,'webiste/login.html',{})





def user_logout(request):
    logout(request)
    messages.success(request,'You Have Been Logged Out!...')
    return redirect('website:home')





def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,'You Have Been Successfuly Registered ')
            return redirect('website:home')
    else:
        form = SignUpForm()

        return render(request,'website/register.html',{'form':form,})
    return render(request,'website/register.html',{'form':form,})



 


