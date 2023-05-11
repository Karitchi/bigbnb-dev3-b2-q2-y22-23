from django.urls import include, path
from rest_framework import routers

from client import views

urlpatterns = [
    path('clients/', views.all_clients),
    path('clients/<int:client_id>/', views.client_details)
]
