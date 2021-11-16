from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

def helloWorld(request):
	return HttpResponse("helloWorld in my first app")


def hello(request):
	return render(request, 'index.html', {'name': 'shiva'})

def indexView(request):
    return render(request,'index.html')
@login_required()

def dashboardView(request):
    return render(request,'dashboard.html')

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form':form})