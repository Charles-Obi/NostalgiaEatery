
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
    path('booking/', views.booking, name='booking'),
    path('order/', views.order, name='order'),
    path('Admin/', views.Admin, name='Admin'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('admindashboard/', views.admindashboard, name='admindashboard'),
    path('delete/<int:id>', views.delete),
    path('deletebooking/<int:id>', views.deletebooking),
    path('deletecontact/<int:id>', views.deletecontact),
    path('deleteregister/<int:id>', views.deleteregister),
    path('edit/<int:id>', views.edit, name='edit'),

    #Mpesa API Urls
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),


]
