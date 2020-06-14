"""
Definition of urls for MyDjangoWebProject/app.
"""

from django.urls import path
from . import forms, views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('setup/', views.setup, name='setup'),
    path('upload/', views.upload, name='upload'),  
    path('host/', views.host, name='host'),
    path('console/', views.console, name='console'),
    path('vs/', views.vs, name='vs'),
    path('vscode/', views.vscode, name='vscode'),
    path('pycharm/', views.pycharm, name='pycharm'),
    path('', views.more, name='more'),
]

