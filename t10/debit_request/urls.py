from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_request, name='create'),
    path('approve/', views.approve_request, name='approve'),
    path('cancel/', views.approve_request, name='cancel'),
    path('reject/', views.approve_request, name='reject'),
    path('serialize/', views.approve_request, name='serialize')
]