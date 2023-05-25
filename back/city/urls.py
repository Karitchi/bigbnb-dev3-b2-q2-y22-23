from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_cities),
    path('<int:city_id>/', views.city_details)
]
