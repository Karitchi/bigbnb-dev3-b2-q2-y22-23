from django.urls import path

from . import views

urlpatterns = [
    path('cities/', views.all_cities),
    path('cities/<int:city_id>/', views.city_details)
]
