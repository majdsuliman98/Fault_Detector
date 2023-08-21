from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update_dataset/', views.updateDataset, name='update_dataset'),
    path('add_algorithm/', views.addAlgorithm, name='add_algorithm'),
    path('see_reports/', views.reports, name='see_reports'),
    path('informations/', views.information, name='info'),
    path('loading_screen/', views.information, name='loading'),
]
