from django.urls import include, path
from rest_framework import routers
from . import views


urlpatterns = [
    path('hotels/', views.all_hotels),
    path('hotels/<int:hotel_id>/', views.hotel_detail),
    path('hotels/<int:hotel_id>/images/', views.hotel_images)
]
