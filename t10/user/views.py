from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def create_user(request):
    User.objects.create(name=request.name, email=request.email, password=request.password, is_super=request.is_super, is_enable=request.is_enable)
    return HttpResponse(request)

def login(request):
    result = User.objects.filter(name=request.name, password=request.password)
    if(result):
        return('<h1>Logged')
    else: 
        return('<h1>Error')
    return HttpResponse('<h1>Login')

def logout(request):
    return HttpResponse('<h1>Logout')

def deactivate_user(request, id):
    return HttpResponse('<h1>Deactivate User')