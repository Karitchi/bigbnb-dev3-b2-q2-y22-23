from django.urls import include, path
from rest_framework import routers
from hotel_owner import views


urlpatterns = [
    path('', views.all_hotel_owners),
    path('<int:hotel_owner_id>', views.hotel_owner_detail)
]
