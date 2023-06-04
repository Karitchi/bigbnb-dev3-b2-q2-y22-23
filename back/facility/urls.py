from django.urls import  path
from . import  views

urlpatterns = [
    path('<int:hotel_id>/', views.facilities),
]