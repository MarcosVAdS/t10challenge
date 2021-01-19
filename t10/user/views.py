from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
# Create your views here.

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        return HttpResponse("Login!")
    else:
        return HttpResponse("Ops, error")

def logout(request):
    return HttpResponse("Ops, logout")