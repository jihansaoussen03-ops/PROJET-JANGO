from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('simulation/', views.simulation, name='simulation'),
    path('exceptions/', views.exceptions, name='exceptions'),
    path('poo/', views.poo, name='poo'),
]