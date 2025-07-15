from django.contrib import admin
from django.urls import path
from . import views

"""
URL configuration for the 'clubhouse' app.

Defines URL patterns that map to the views handling
the homepage and the 'who we are' page.
"""

urlpatterns = [
    path('', views.index, name='clubhouse'),
    path('who-we-are/', views.who_we_are, name='who_we_are'),
]
