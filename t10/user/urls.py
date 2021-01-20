from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_user, name='create'),
    path('deactivate/', views.deactivate_user, name='approve'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]