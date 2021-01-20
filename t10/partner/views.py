from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def create_partner(request):
    return HttpResponse('<h1>Partner created')

def deactivate_partner(request):
    return HttpResponse('<h1>Partner deactvate')