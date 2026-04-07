from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('programs/', views.programs, name='programs'),
    path('partnerships/', views.partnerships, name='partnerships'),
    path('donate/', views.donate, name='donate'),
    path('contact/', views.contact, name='contact'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('programs/<slug:slug>/', views.program_detail, name='program_detail'),
    path('news/', views.news_list, name='news_list'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('stories/', views.stories_list, name='stories_list'),
    path('stories/<int:pk>/', views.story_detail, name='story_detail'),
    path('gallery/', views.gallery, name='gallery'),
    
]