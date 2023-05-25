from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_hotels),
    path('<int:hotel_id>/', views.hotel_detail),
    path('filter_hotels/', views.filter_hotels),
    path('<int:hotel_id>/images/', views.hotel_images)
]
