from django.urls import path, include
from . import views

app_name = 'cal'

urlpatterns = [

    path('calculate/', views.show, name='show'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('home/', views.home, name='home'),
    path('', views.home, name='home'),

]