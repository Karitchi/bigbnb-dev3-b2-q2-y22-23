from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from client import views

urlpatterns = [
    path('', views.all_clients),
    path('<int:client_id>/', views.client_details),
]
