from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('hotel_owner.urls')),
    path('', include('city.urls')),
    path('', include('client.urls')),
    path('', include('hotel.urls')),
    path('', include('booking.urls')),
    path('admin/', admin.site.urls)
]
