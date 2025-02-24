from django.urls import path
from . import views

app_name = 'data'

urlpatterns = [
    path('', views.home, name='home-page'),
    path('roles/', views.roles, name='roles'),
    path('candidates/', views.candidates, name='candidates'),
]