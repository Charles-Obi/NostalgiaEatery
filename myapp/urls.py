
from django.contrib import admin
from django.urls import path
from myapp import  views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('specials/', views.specials, name='specials'),
    path('events/', views.events, name='events'),
    path('chefs/', views.chefs, name='chefs'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
]
