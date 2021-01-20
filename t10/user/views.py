from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def create_user(request):
    return HttpResponse('<h1>Create User')

def login(request):
    return HttpResponse('<h1>Login')

def logout(request):
    return HttpResponse('<h1>Logout')

def deactivate_user(request):
    return HttpResponse('<h1>Deactivate User')