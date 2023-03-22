from django.contrib import admin
from django.urls import path
from hotel import views

urlpatterns = [
    path('hotels/', views.hotels_list),
    path('hotels/<int:id>', views.hotel_detail),
    path('admin/', admin.site.urls)
]
