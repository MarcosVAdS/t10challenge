from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_partner, name='create'),
    path('<int:id>/deactivate/', views.deactivate_partner, name='deactivate')
]