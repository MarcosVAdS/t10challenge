from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def create_request(request):
    return HttpResponse('<h1>New request')

def approve_request(request):
    return HttpResponse('<h1>Approve request')

def cancel_request(request):
    return HttpResponse('<h1>Cancel request')

def reject_request(request):
    return HttpResponse('<h1>Reject request')

def serialize_request(request):
    return HttpResponse('<h1>List request')