from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='homepage'),
    path('applications', views.save_applications, name="applications"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('retrieve/<int:id>', views.retrieve, name="retrieve")
]