from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_user, name='create'),
    path('<int:id>/deactivate/', views.deactivate_user, name='deactivate'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]