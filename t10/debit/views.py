from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def new_request():
    return HttpResponse("New Request")

def cancel_request():
    return HttpResponse("Cancel Request")

def approve_request():
    return HttpResponse("Aproved request")

def reject_request():
    return HttpResponse("Rejected Request")

def list_request():
    return HttpResponse("All Requests")