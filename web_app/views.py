from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import *

# Create your views here.
def index(request):
    form  = EnquiryForm(request.POST)
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EnquiryForm(request.POST)
    context = {
        'form' : form,
    }
    
    return render(request, "web1/index.html", context)

def blogs(request):
    return render(request, "web1/blogs.html")

def checkout(request):
    return render(request, "web1/checkout.html")

def Register(request):
    return render(request, "web1/dashboard/register.html")

def Login(request):
    return HttpResponse("welcome to login page") 

def clientAreaLogin(request):
    return HttpResponse("welcome to client area login") 

def clientArea(request):
    return HttpResponse("welcome to client area")
