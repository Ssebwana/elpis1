from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('programs/', views.programs, name='programs'),
    path('partnerships/', views.partnerships, name='partnerships'),
    path('donate/', views.donate, name='donate'),
    path('contact/', views.contact, name='contact'),
]