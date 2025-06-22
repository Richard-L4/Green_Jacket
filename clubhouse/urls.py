from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='clubhouse'),
    path('who-we-are/', views.who_we_are, name='who_we_are'),
]