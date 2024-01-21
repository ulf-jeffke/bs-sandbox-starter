"""Defines URL patterns for bau24"""

from django.urls import path    

from  . import views

app_name = 'mini_starter_project'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]