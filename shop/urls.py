from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('index/', views.index,name='index'),
    path('plants/', views.plants,name='plants'),
    path('search', views.search,name='search'),
    path('contact/', views.contact,name='contact'),
    path('items/<int:myid>', views.items,name='items'),
]
